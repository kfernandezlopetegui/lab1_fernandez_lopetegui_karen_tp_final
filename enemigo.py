from player import *
from constantes import *
from auxiliar import Auxiliar

class Enemy():
    
    def __init__(self,x,y,speed_walk,speed_run,gravity,jump_power,frame_rate_ms,
                 move_rate_ms,jump_height,nombre_imagen_walk="images/caracters/enemies/ork_sword/WALK/WALK_00{0}.png",
                 cant_imag_walk_inicio=0,cant_imag_walk_fin=7,
                 nombre_imagen_idle="images/caracters/enemies/ork_sword/IDLE/IDLE_00{0}.png",
                 cant_imag_idle_inicio=0,cant_imag_idle_fin=7,
                 nombre_imagen_die="images/caracters/enemies/ork_sword/DIE/DIE_00{0}.png",
                 cant_imag_die_inicio=0,cant_imag_die_fin=9,
                 nombre_imagen_hurt="images/caracters/enemies/ork_sword/HURT/HURT_00{0}.png",
                 cant_imag_hurt_inicio=0,cant_imag_hurt_fin=6,
                 nombre_imagen_attak="images/caracters/enemies/ork_sword/ATTAK/ATTAK_00{0}.png",
                 cant_imag_attak_inicio=0,cant_imag_attak_fin=6,p_scale=0.9,interval_time_jump=100,
                 is_shooter=False
                 ) -> None:
        self.nombre= "enemy"
        self.walk_r = Auxiliar.getSurfaceFromSeparateFiles(nombre_imagen_walk,cant_imag_walk_inicio,cant_imag_walk_fin,scale=p_scale)
        self.walk_l = Auxiliar.getSurfaceFromSeparateFiles(nombre_imagen_walk,cant_imag_walk_inicio,cant_imag_walk_fin,flip=True,scale=p_scale)
        self.stay_r = Auxiliar.getSurfaceFromSeparateFiles(nombre_imagen_idle,cant_imag_idle_inicio,cant_imag_idle_fin,scale=p_scale)
        self.stay_l = Auxiliar.getSurfaceFromSeparateFiles(nombre_imagen_idle,cant_imag_idle_inicio,cant_imag_idle_fin,flip=True,scale=p_scale)
        self.death_r = Auxiliar.getSurfaceFromSeparateFiles(nombre_imagen_die,cant_imag_die_inicio,cant_imag_die_fin,scale=p_scale)
        self.death_l = Auxiliar.getSurfaceFromSeparateFiles(nombre_imagen_die,cant_imag_die_inicio,cant_imag_die_fin,flip=True,scale=p_scale)
        self.hurt_r= Auxiliar.getSurfaceFromSeparateFiles(nombre_imagen_hurt,cant_imag_hurt_inicio,cant_imag_hurt_fin,scale=p_scale)
        self.hurt_l= Auxiliar.getSurfaceFromSeparateFiles(nombre_imagen_hurt,cant_imag_hurt_inicio,cant_imag_hurt_fin,flip=True,scale=p_scale)
        self.attack_r=Auxiliar.getSurfaceFromSeparateFiles(nombre_imagen_attak,cant_imag_attak_inicio,cant_imag_attak_fin,scale=p_scale)
        self.attack_l=Auxiliar.getSurfaceFromSeparateFiles(nombre_imagen_attak,cant_imag_attak_inicio,cant_imag_attak_fin,flip=True,scale=p_scale)
        self.contador = 0
        self.frame = 0
        self.lives = 5
        self.score = 0
        self.move_x = 0
        self.move_y = 0
        self.speed_walk =  speed_walk
        self.speed_run =  speed_run
        self.gravity = gravity
        self.jump_power = jump_power
        self.animation = self.stay_r
        self.direction = DIRECTION_R
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(x+self.rect.width/3,y,self.rect.width/3,self.rect.height)
        self.ground_collition_rect = pygame.Rect(self.collition_rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H
        self.ground_collition_rect.y = y + self.rect.height - GROUND_COLLIDE_H

        self.is_jump = False
        self.is_fall = False
        self.is_shoot = False
        self.is_knife = False
        self.is_death=False

        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms
        self.y_start_jump = 0
        self.jump_height = jump_height

        self.tiempo_transcurrido = 0
        self.tiempo_last_jump = 0 # en base al tiempo transcurrido general
        self.interval_time_jump = interval_time_jump
        
        self.shoot_delay=1500
        self.can_shoot = False
        self.last_shoot_time=None
        self.contador_daño=0
        self.damaged = False
        self.damaged_timer = 0
       
        self.weapon_rect = pygame.Rect(0, 0, 20, 30)
        self.attack_range = 80  # Distancia máxima de ataque del enemigo
        self.is_attacking = False  # Estado de ataque del enemigo
        self.last_attack_time = 0 
        self.attack_delay = 700
        self.attack_timer = 0
        self.is_shooter = is_shooter  
    
    def change_x(self,delta_x):
        self.rect.x += delta_x
        self.collition_rect.x += delta_x
        self.ground_collition_rect.x += delta_x

    def change_y(self,delta_y):
        self.rect.y += delta_y
        self.collition_rect.y += delta_y
        self.ground_collition_rect.y += delta_y
    
    def update_weapon_rect(self):
        # Actualiza la posición del rectángulo del arma con respecto al enemigo
        if DIRECTION_L == self.direction:
            
            self.weapon_rect.centerx = self.rect.centerx-45
            # Posición x centrada
        else: 
             self.weapon_rect.centerx = self.rect.centerx+45
                   
        self.weapon_rect.top = self.rect.top + 40  # Posición y ligeramente por encima del enemigo
        
    def is_player_in_range(self, player):
        # Verifica si el jugador está dentro del rango de ataque del enemigo
        distance_x = abs(self.rect.centerx - player.rect.centerx)
        distance_y = abs(self.rect.centery - player.rect.centery)
        distance = (distance_x ** 2 + distance_y ** 2) ** 0.5  # Fórmula de la distancia euclidiana
        return distance <= self.attack_range
        
    def attack(self, player, tiempo_actual, game):
        # Verifica la colisión entre el rectángulo del arma y el jugador
        
            
            if self.weapon_rect.colliderect(player.rect) and self.is_player_in_range(player) :
                
                if not self.is_attacking or tiempo_actual - self.last_attack_time >= self.attack_delay:
                    self.is_attacking=True
                  
                    self.last_attack_time = tiempo_actual
                    self.attack_timer = tiempo_actual
                    game.reproducir_corte()
                    player.receive_damage(5)  # Aplica el daño al jugador
                    
                
    def do_movement(self,delta_ms,plataform_list, game):
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0
            if self.lives>0:
                
                if self.damaged:
                    self.do_hurt()
                else:
                    if self.is_attacking :
                        self.do_attack()
                        
                        
                    elif(not self.is_on_plataform(plataform_list)):
                        if(self.move_y == 0):
                            self.is_fall = True
                            self.change_y(self.gravity)
                    else:
                        
                            
                            self.is_fall = False
                            self.change_x(self.move_x)
                            
                                
                            if self.contador <= 50:
                                self.move_x = -self.speed_walk
                                self.animation = self.walk_l
                                self.direction = DIRECTION_L
                                self.contador += 1 
                            elif self.contador <= 100:
                                self.move_x = self.speed_walk
                                self.animation = self.walk_r
                                self.direction = DIRECTION_R
                                self.contador += 1    
                            else:
                                self.contador = 0
            else:
                game.reproducir_muerte()
                self.do_death()
                
                                    
    def do_death(self):
        if self.direction == DIRECTION_R:
            self.animation = self.death_r
        else:
            self.animation = self.death_l
    
    def take_damage(self):
        self.damaged = True
        self.damaged_timer = pygame.time.get_ticks()  # Obtener el tiempo actual en milisegundos

    def do_hurt(self):
        if self.direction == DIRECTION_R:
            self.animation = self.hurt_r
        else:
            self.animation = self.hurt_l
   
    def do_attack(self):
        if self.direction == DIRECTION_R:
            self.animation = self.attack_r
        else:
            self.animation = self.attack_l
                          
    def is_on_plataform(self,plataform_list):
        retorno = False
        
        if(self.ground_collition_rect.bottom >= GROUND_LEVEL):
            retorno = True     
        else:
            for plataforma in  plataform_list:
                if(self.ground_collition_rect.colliderect(plataforma.ground_collition_rect)):
                    retorno = True
                    break       
        return retorno          

    def do_animation(self,delta_ms):
        
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
                
                self.image = self.animation[self.frame]
            else:
                if self.lives<1:
                    
                    self.is_death=True
                     
                self.frame = 0

    def update(self,delta_ms,plataform_list, player, tiempo_actual, game):
        if self.damaged and tiempo_actual - self.damaged_timer > 350:  
            self.damaged = False
        if  self.is_attacking and tiempo_actual - self.attack_timer > 700 :
            self.is_attacking= False
            
            
        else:
            self.attack(player, tiempo_actual, game)
         
                
        self.update_weapon_rect()
           
        self.do_movement(delta_ms,plataform_list,game)
        self.do_animation(delta_ms) 
        

    def draw(self,screen):
        
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
            pygame.draw.rect(screen,color=(255,255,0),rect=self.ground_collition_rect)
            pygame.draw.rect(screen,color=(255,255,0),rect=self.weapon_rect)
            
        
        #self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)
        
    def receive_shoot(self):
        self.contador_daño +=1
        
        if(self.lives>0 and self.contador_daño == 1):
            
            self.lives -= 1
            self.contador_daño = 0
        
