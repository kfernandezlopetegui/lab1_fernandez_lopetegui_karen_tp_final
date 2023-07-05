from player import *
from constantes import *
from auxiliar import Auxiliar
import math

class Bullet():
    
    def __init__(self,owner,x_init,y_init,x_end,y_end,speed,type,frame_rate_ms,move_rate_ms,width=5,height=5) -> None:
        self.tiempo_transcurrido_move = 0
        self.tiempo_transcurrido_animation = 0
        self.image = pygame.image.load("images/gui/set_gui_01/Comic_Border/Bars/Bar_Segment05.png").convert()
        self.image = pygame.transform.scale(self.image,(width,height))
        if type:
            if x_end< x_init:
                
                self.animation=Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/robot/Objects/Bullet_00{0}.png",0,4,flip=True,scale=0.2)
            else:
                self.animation=Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/robot/Objects/Bullet_00{0}.png",0,4,flip=False,scale=0.2)    
                    
        else:
            if x_end< x_init:
                
                self.animation=Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/robot/Objects/Bullet_00{0}.png",0,4,flip=True,scale=0.2)
            else:
                self.animation=Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/robot/Objects/Bullet_00{0}.png",0,4,flip=False,scale=0.2)    
                     
        self.rect = self.image.get_rect()
        self.x = x_init
        self.y = y_init
        self.owner = owner
        self.rect.x = x_init
        self.rect.y = y_init
        self.frame=0
        self.frame_rate_ms = frame_rate_ms
        self.imagen = self.animation[self.frame]
        self.rect_imagen = self.imagen.get_rect()
        self.rect_imagen.x=x_init
        self.rect_imagen.y=y_init
        self.move_rate_ms = move_rate_ms
        self.collition_rect = pygame.Rect(self.rect)
        self.collition_rect_imagen = pygame.Rect(self.rect_imagen)
        angle = math.atan2(y_end - y_init, x_end - x_init) #Obtengo el angulo en radianes
        

        self.move_x = math.cos(angle)*speed
        self.move_y = math.sin(angle)*speed
        
        
        
        self.is_active = True 
   
    def change_x(self,delta_x):
        self.x = self.x + delta_x
        self.rect.x = int(self.x)
        self.rect_imagen.x = int(self.x)

    def change_y(self,delta_y):
        self.y = self.y + delta_y
        self.rect.y = int(self.y)
        self.rect_imagen.y = int(self.y)

    def do_movement(self,delta_ms,plataform_list,enemy_list,player):
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0
            self.change_x(self.move_x)
            self.change_y(self.move_y)
            self.check_impact(plataform_list,enemy_list,player)

    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
                #print(self.frame)
            else: 
                self.frame = 0
    
    def check_impact(self,plataform_list,enemy_list,player):
        
        if(self.is_active and self.owner != "player" and self.rect.colliderect(player.rect)):
            
            
            player.receive_shoot()
            self.is_active = False
            
        for aux_enemy in enemy_list:
            if(self.is_active and self.owner != "enemy" and self.rect.colliderect(aux_enemy.rect)):
                
                
                aux_enemy.receive_shoot()
                aux_enemy.take_damage()
                self.is_active = False
                
        for aux_plataform in plataform_list:
                    
            if self.is_active and self.rect.colliderect(aux_plataform.rect) or self.rect.left < 0 or self.rect.right > ANCHO_VENTANA or self.rect.top < 0 or self.rect.bottom > ALTO_VENTANA:
                self.is_active=False   
                 

    def update(self,delta_ms,plataform_list,enemy_list,player):
        self.do_movement(delta_ms,plataform_list,enemy_list,player)
        
        self.do_animation(delta_ms) 

    def draw(self,screen):
        if(self.is_active):
            if(DEBUG):
                pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
                
            
            self.imagen = self.animation[self.frame]
    
            screen.blit(self.imagen,self.rect_imagen)
            
            
    def on_fire_shoot(self,delta_ms):
        retorno = True
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0
            retorno = False
        
        return retorno            
            
            
