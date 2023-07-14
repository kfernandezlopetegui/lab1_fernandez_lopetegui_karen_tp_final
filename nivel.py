import pygame
 
from constantes import *
from auxiliar import * 

import copy

from bullet import Bullet
 
class Level():
    """
    Clase generica padre  nivel
    
    """
   
    def __init__(self, player, platform_list, enemy_list, item_list, background, game, level,otros_enemigos, otras_plataformas ):
        
        #copias para reestablecer el nivel
        self.enemy_list_copia = otros_enemigos
        self.plataformas_copia=otras_plataformas
        
            
        self.plataform_list = platform_list
        self.enemy_list = enemy_list
        self.bullet_list = []
        self.items_list = item_list
        
        self.background = background
      
        
 
        # que tanto es recorrido el mundo
        self.world_shift = 0
        self.level_limit = -4900
        '''self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()'''
        self.player_1 = player
        
        
        
        self.shoot_delay = 500  # Retraso en milisegundos entre disparos
        self.last_shoot_time = 0

        self.game= game
    
    def on_fire_shoot(self, el_que_dispara): 
            '''
            Funcion que crea los proyectiles del nivel
            
            '''
            if el_que_dispara.direction==DIRECTION_L:
                x_final = 0
                x_inicio=-50
            else:
                x_final = ANCHO_VENTANA
                x_inicio=25      
                   
            self.bullet_list.append(Bullet(el_que_dispara.nombre,el_que_dispara.rect.centerx+x_inicio,el_que_dispara.rect.centery-25,x_final,el_que_dispara.rect.centery-25,35,type=True,frame_rate_ms=100,move_rate_ms=20,width=5,height=5))
            self.game.reproducir_disparo()
            el_que_dispara.can_shoot = False
            
    # Se actualiza todo el nivel
    def update(self, keys, tiempo_actual, delta_ms):
        
                
        for bullet_element in self.bullet_list:
            bullet_element.update(delta_ms,self.plataform_list,self.enemy_list,self.player_1)
            
                
            if not bullet_element.is_active:
                self.bullet_list.remove(bullet_element)
                
        # se actualiza cada plataforma en la lista        
        for plataform_element in self.plataform_list:
            plataform_element.update(delta_ms)
            
        for item in self.items_list:
            if self.player_1.rect.colliderect(item.rect):
                self.player_1.increment_item(item.name)
                self.player_1.score+=20
                item.pickup()
                self.items_list.remove(item)    
                        
        #Se actualiza cada enemigo en la lista
        for enemy_element in self.enemy_list:
            enemy_element.update(delta_ms,self.plataform_list, self.player_1, tiempo_actual, self.game)
            if enemy_element.is_death:
                
                self.enemy_list.remove(enemy_element)
                self.player_1.score += 20
            if enemy_element.can_shoot and enemy_element.is_shooter:
                self.on_fire_shoot(enemy_element)
                enemy_element.last_shoot_time = tiempo_actual
                     
            if enemy_element.is_shooter and not enemy_element.can_shoot and tiempo_actual - enemy_element.last_shoot_time >= enemy_element.shoot_delay :
                enemy_element.can_shoot = True
                  
        #Actualiza comportamientos del player
        if(keys[pygame.K_s] and not keys[pygame.K_a] and self.player_1.can_shoot):
            
            if tiempo_actual - self.last_shoot_time >= self.shoot_delay:
                self.on_fire_shoot(self.player_1)       
                self.player_1.last_shoot_time = tiempo_actual
                        
        self.player_1.events(delta_ms,keys)
        self.player_1.update(delta_ms,self.plataform_list)
           
        if not self.player_1.can_shoot and tiempo_actual - self.player_1.last_shoot_time >=self.player_1.shoot_delay:
            self.player_1.can_shoot = True    
       
    
       
        
    def reiniciar_nivel(self, nivel, player,plataform_list,enemy_list, background):
        player.reset()
        plataform_list = self.plataformas_copia
        enemy_list = self.enemy_list_copia
        
        background.update(0,0)
       
        self.world_shift = 0
        return player,plataform_list, enemy_list, background
        
 
    def draw(self, screen):
      
        self.background.draw(screen, offset=self.world_shift // 3)

        for plataforma in self.plataform_list:
            plataforma.draw(screen)
            
        for item in self.items_list:
            item.draw(screen)
            
        for enemy_element in self.enemy_list:
            enemy_element.draw(screen)
            
        self.player_1.draw(screen)
        
        for bullet_element in self.bullet_list:
            bullet_element.draw(screen)
             
             
    def shift_world(self, shift_x):
        """ 
        Realiza el movimiento de todo el mundo cuando el player se mueve
        """

         
        self.world_shift += shift_x
 
       
        for platform in self.plataform_list:
            platform.rect.x += shift_x
 
        for enemy in self.enemy_list:
            enemy.rect.x += shift_x
            
        for item in self.items_list:
            item.rect.x += shift_x
                
 

