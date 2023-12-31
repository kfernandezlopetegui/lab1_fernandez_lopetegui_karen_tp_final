import pygame
from pygame.locals import *
from gui_widget import Widget
from gui_button import Button
from game import Game
class Form():
    forms_dict = {}
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        self.name= name
        self.forms_dict[name] = self
        self.master_surface = master_surface
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color_background = color_background
        self.color_border = color_border
        self.score=0

        self.surface = pygame.Surface((w,h))
        self.slave_rect = self.surface.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y
        self.active = active
        self.x = x
        self.y = y
        self.volumen_music = 1.0
        self.volumen_sounds = 1.0
        self.restart=False
        self.quit=False
        if(self.color_background != None):
            self.surface.fill(self.color_background)
        self.end_game= False    
            
    @staticmethod
    def set_active(name):
        for aux_form in Form.forms_dict.values():
            aux_form.active = False
        Form.forms_dict[name].active = True
    
    @staticmethod
    def get_active():
        for aux_form in Form.forms_dict.values():
            if(aux_form.active):
                return aux_form
        return None
    
    @staticmethod
    def set_game_volume(volume):
        Game.set_volume(volume)
    
    @staticmethod
    def set_game_volume(volume):
       Game.set_sound_volume(volume)
       
    def on_click_boton_active(self, parametro):
        self.set_active(parametro)
    
    def reset(self):
        pass    
    
    def render(self):
        pass

    def update(self,lista_eventos):
        pass

    def draw(self):
        
        self.master_surface.blit(self.surface,self.slave_rect)


class FormMenu(Form):
    def __init__(self,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(master_surface,x,y,w,h,color_background,color_border,active)

        self.boton1 = Button(master=self,x=100,y=50,w=200,h=50,color_background=(255,0,0),color_border=(255,0,255),on_click=self.on_click_boton1,on_click_param="1234",text="MENU",font="Verdana",font_size=30,font_color=(0,255,0))
        self.boton2 = Button(master=self,x=200,y=50,w=200,h=50,color_background=(255,0,0),color_border=(255,0,255),on_click=self.on_click_boton1,on_click_param="8",text="MENU 2",font="Verdana",font_size=30,font_color=(0,255,0))
        self.lista_widget = [self.boton1,self.boton2]

    def on_click_boton1(self, parametro):
        print("CLICK",parametro)

    def update(self, lista_eventos):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self): 
        super().draw()
        for aux_widget in self.lista_widget:    
            aux_widget.draw()