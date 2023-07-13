import pygame
from constantes import *
from auxiliar import Auxiliar


class Plataform:
    def __init__(self, x, y,width, height, frame_rate_ms, move_rate_ms,move=False, type=1):

        self.image_list= Auxiliar.getSurfaceFromSeparateFiles("images/tileset/forest/Tiles/{0}.png",1,28,flip=False,w=width,h=height)
        
        self.image = self.image_list[type]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #self.collition_rect = pygame.Rect(self.rect)
        self.collition_rect = pygame.Rect(x+self.rect.width/3,y,self.rect.width/3,self.rect.height)
        self.ground_collition_rect = pygame.Rect(self.rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H
        self.speed_move=5
        self.move_x = 0
        self.move = move
        self.frame_rate_ms = frame_rate_ms 
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms
        self.contador=0
        self.width=width 
        self.height=height
        self.type= type
        

    def draw(self,screen):
        
         
        x = self.rect.x
        y = self.rect.y

        screen.blit(self.image, (x, y))    
        
        
       
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
            pygame.draw.rect(screen,color=(255,255,0),rect=self.ground_collition_rect)
    
    def change_x(self,delta_x):
        self.rect.x += delta_x
        self.collition_rect.x += delta_x
        self.ground_collition_rect.x += delta_x

    def change_y(self,delta_y):
        self.rect.y += delta_y
        self.collition_rect.y += delta_y
        self.ground_collition_rect.y += delta_y
        
    def do_movement(self,delta_ms):
        
            self.tiempo_transcurrido_move += delta_ms
            if(self.tiempo_transcurrido_move >= self.move_rate_ms):
                self.tiempo_transcurrido_move = 0

                self.change_x(self.move_x)
                if self.contador <= 70:
                            self.move_x = -self.speed_move
                            
                            self.contador += 1 
                elif self.contador <= 140:
                            self.move_x = self.speed_move
                        
                            self.contador += 1    
                else:
                            self.contador = 0
                            
    def update(self,delta_ms):
        if self.move:
            self.do_movement(delta_ms)
        self.collition_rect = pygame.Rect(self.rect.x+self.rect.width/3, self.rect.y,self.rect.width/3,self.rect.height)
        self.ground_collition_rect = pygame.Rect(self.rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H    
                     
    def copy(self):
        # Crear una nueva instancia de Enemy con los mismos valores de atributos
        nueva_instancia = Plataform(self.rect.x, self.rect.y, self.width,
                                    self.height, self.frame_rate_ms, self.move_rate_ms,
                                    self.move, self.type)
        # Copiar otros atributos y componentes de la clase Enemy según sea necesario

        # Retorna la nueva instancia copiada
        return nueva_instancia
             
        