import pygame
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar


class FormMenuA(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)

        self.boton1 = Button(master=self,x=150,y=90,w=200,h=40,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_XL_08.png",on_click=self.on_click_boton3,on_click_param="form_game_L1",text="PLAY",font="Verdana",font_size=30,font_color=C_BLACK)
        self.boton2 = Button(master=self,x=150,y=150,w=200,h=40,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_XL_08.png",on_click=self.on_click_boton3,on_click_param="form_menu_settings",text="SETTINGS",font="Verdana",font_size=30,font_color=C_BLACK)
        self.boton3 = Button(master=self,x=150,y=210,w=200,h=40,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_XL_08.png",on_click=self.on_quit,on_click_param="form_menu_C",text="QUIT",font="Verdana",font_size=30,font_color=C_BLACK)
                                
       
        self.lista_widget = [self.boton1,self.boton2,self.boton3]

    def on_click_boton1(self, parametro):
        self.pb1.value += 1
 
    def on_click_boton2(self, parametro):
        self.pb1.value -= 1
    
    def on_click_boton3(self, parametro):
        
        self.set_active(parametro)
    def on_quit(self,parametro):
        self.quit=True    

    def update(self, lista_eventos,keys,delta_ms, tiempo_actual, tiempo_restante):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self): 
        super().draw()
        for aux_widget in self.lista_widget:    
            aux_widget.draw()