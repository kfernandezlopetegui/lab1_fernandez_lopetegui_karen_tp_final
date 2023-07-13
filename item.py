import pygame
from constantes import *
from auxiliar import Auxiliar

class Item:
    def __init__(self, name, x,y,width,height, type=1):
        self.name = name
        self.collected = False
        self.image_list= Auxiliar.getSurfaceFromSeparateFiles("items/item({0}).png",0,4,flip=False,w=width,h=height)
        self.image = self.image_list[type]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x_initial= x
        self.y_initial= y
        self.collition_rect = pygame.Rect(self.rect.x+self.rect.width,self.rect.y,self.rect.width,self.rect.height)

    def draw(self,screen):
        if self.collected == False:
            
            x = self.rect.x
            y = self.rect.y

            screen.blit(self.image, (x, y))    
        
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
            
            
    

    def pickup(self):
        self.collected = True
        
    
    def reset(self):
        self.collected = False
        self.rect.x = self.x_initial
        self.rect.y = self.y_initial
             
       