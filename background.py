import pygame
from constantes import *
from auxiliar import Auxiliar


class Background:
    def __init__(self, x, y,width, height,  path):

        self.image = pygame.image.load(path).convert()
        self.image = pygame.transform.scale(self.image,(width,height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(x+self.rect.width/3,y,self.rect.width/3,self.rect.height)


    def draw(self,screen, offset):
        y = self.rect.y 
        x = self.rect.x
        if offset is not None :
            x = offset
            
        
           
            
        screen.blit(self.image, (x, y))
        #screen.blit(self.image,self.rect)
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)        
        