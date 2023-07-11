import pygame
from pygame.locals import *
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar
from constantes import *
from auxiliar import *
from gui_label import Label



class FormMenuGameOver(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)
       
        self.label1= Label(master=self, x=120, y=15, w=300, h=50, color_background=(53,57,69), color_border=None,
                            image_background=None, text="GAME OVER", font="Times New Roman", font_size=40, font_color=C_BLACK)

        self.boton2 = Button(master=self,x=150,y=330,w=200,h=40,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_XL_08.png",on_click=self.on_click_boton1,on_click_param="form_menu_A",text="HOME",font="Verdana",font_size=22,font_color=C_BLACK)
        self.boton3 = Button(master=self,x=150,y=270,w=200,h=40,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_XL_08.png",on_click=self.on_click_boton1,on_click_param="form_menu_B",text="SAVE SCORE",font="Verdana",font_size=22,font_color=C_BLACK)
        self.boton4 = Button(master=self,x=250,y=90,w=80,h=80,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Pixel_Border/Buttons/repeat.png",on_click=self.on_click_boton1,on_click_param="form_game_L1",text="",font="Verdana",font_size=22,font_color=C_BLACK)
        self.boton1 = Button(master=self,x=150,y=210,w=200,h=40,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_XL_08.png",on_click=self.on_click_boton1,on_click_param="form_game_L1",text="RATING",font="Verdana",font_size=22,font_color=C_BLACK)
        
        
        self.lista_widget = [self.boton1, self.boton2, self.boton3, self.boton4, self.label1]

    def on_click_boton1(self, parametro):
        self.set_active(parametro)

        
    def update(self, lista_eventos,keys,delta_ms,tiempo_actual, tiempo_restante):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self): 
        super().draw()
        self.surface.fill(self.color_background)
        for aux_widget in self.lista_widget:    
            aux_widget.draw()