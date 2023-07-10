import pygame
from pygame.locals import *
from gui_form_menu_A import FormMenuA
from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar
from constantes import *
from auxiliar import *
from gui_label import Label


class FormMenuSettings(FormMenuA):
    def __init__(self, name, master_surface, x, y, w, h, color_background, color_border, active):
        super().__init__(name, master_surface, x, y, w,
                         h, color_background, color_border, active)
        
        self.label2 = Label(master=self, x=150, y=10, w=200, h=90, color_background=(53,57,69), color_border=None,
                            image_background=None, text="SETTINGS", font="Times New Roman", font_size=40, font_color=C_BLACK)

        self.label1 = Label(master=self, x=360, y=30, w=50, h=50, color_background=None, color_border=None,
                            image_background="images/gui/set_gui_01/Pixel_Border/Buttons/settings.png", text="", font="Arial", font_size=30, font_color=C_WHITE)
        self.label3 = Label(master=self, x=20, y=130, w=105, h=90, color_background=(53,57,69), color_border=None,
                            image_background=None, text="MUSIC", font="Times New Roman", font_size=26, font_color=C_BLACK)

        self.label4 = Label(master=self, x=20, y=230, w=105, h=90, color_background=(53,57,69), color_border=None,
                            image_background=None, text="SOUNDS", font="Times New Roman", font_size=26, font_color=C_BLACK)

        self.boton1 = Button(master=self, x=450, y=150, w=50, h=50, color_background=None, color_border=None, image_background="images/gui/set_gui_01/Pixel_Border/Buttons/audioPlus.png",
                             on_click=self.on_click_boton1, on_click_param="", text="", font="Verdana", font_size=30, font_color=C_WHITE)
        self.boton2 = Button(master=self, x=140, y=150, w=50, h=50, color_background=None, color_border=None, image_background="images/gui/set_gui_01/Pixel_Border/Buttons/audioMute.png",
                             on_click=self.on_click_boton2, on_click_param="", text="", font="Verdana", font_size=30, font_color=C_WHITE)
        self.boton3 = Button(master=self, x=30, y=350, w=200, h=40, color_background=None, color_border=None, image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_XL_08.png",
                             on_click=self.on_click_boton3, on_click_param="form_menu_pause", text="BACK", font="Verdana", font_size=22, font_color=C_BLACK)
        self.boton4 = Button(master=self, x=450, y=250, w=50, h=50, color_background=None, color_border=None, image_background="images/gui/set_gui_01/Pixel_Border/Buttons/audioPlus.png",
                             on_click=self.on_click_boton4, on_click_param="", text="", font="Verdana", font_size=30, font_color=C_WHITE)
        self.boton5 = Button(master=self, x=140, y=250, w=50, h=50, color_background=None, color_border=None, image_background="images/gui/set_gui_01/Pixel_Border/Buttons/audioMute.png",
                             on_click=self.on_click_boton5, on_click_param="", text="", font="Verdana", font_size=30, font_color=C_WHITE)

        self.pb1 = ProgressBar(master=self, x=200, y=150, w=240, h=50, color_background=None, color_border=None, image_background="images/gui/set_gui_01/Comic_Border/Bars/Bar_Background01.png",
                               image_progress="images/gui/set_gui_01/Comic_Border/Bars/Bar_Segment05.png", value=8, value_max=8)
        self.pb2 = ProgressBar(master=self, x=200, y=250, w=240, h=50, color_background=None, color_border=None, image_background="images/gui/set_gui_01/Comic_Border/Bars/Bar_Background01.png",
                               image_progress="images/gui/set_gui_01/Comic_Border/Bars/Bar_Segment05.png", value=8, value_max=8)

        self.lista_widget = [self.boton1, self.boton2, self.label1,
                             self.pb1, self.boton3, self.boton4,
                             self.boton5, self.pb2,self.label2, self.label3,
                            self.label4]

    def on_click_boton4(self, parametro):
        self.pb2.value += 1

    def on_click_boton5(self, parametro):
    
        self.pb2.value -= 1

    def get_volume(self):
        
        volume = self.volume_slider.get_value()  # Obtiene el  de volumen musica
        return volume
    
    def get_volume_sounds(self):
        
        volume = self.volume_slider.get_value()  # Obtiene el  de volumen musica
        return volume
    
    
    def update(self, lista_eventos, keys, delta_ms, tiempo_actual, tiempo_restante):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self):
        super().draw()
        
        for aux_widget in self.lista_widget:
            aux_widget.draw()
