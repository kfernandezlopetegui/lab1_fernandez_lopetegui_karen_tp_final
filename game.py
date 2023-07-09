import pygame
from constantes import * 
from auxiliar import *


class Game():
    def __init__(self) -> None:

        self.game_over_image = Auxiliar.escalar_imagen(
            "images/gui/set_gui_01/Sand/Text/GAME_OVER.png",1)

        self.digit_images_score = {
           
            "0": Auxiliar.escalar_imagen("images/gui/set_gui_01/Glitch_Border/Text/0.png",0.25),
            "1": Auxiliar.escalar_imagen("images/gui/set_gui_01/Glitch_Border/Text/1.png",0.25),
            "2": Auxiliar.escalar_imagen("images/gui/set_gui_01/Glitch_Border/Text/2.png",0.25),
            "3": Auxiliar.escalar_imagen("images/gui/set_gui_01/Glitch_Border/Text/3.png",0.25),
            "4": Auxiliar.escalar_imagen("images/gui/set_gui_01/Glitch_Border/Text/4.png",0.25),
            "5": Auxiliar.escalar_imagen("images/gui/set_gui_01/Glitch_Border/Text/5.png",0.25),
            "6": Auxiliar.escalar_imagen("images/gui/set_gui_01/Glitch_Border/Text/6.png",0.25),
            "7": Auxiliar.escalar_imagen("images/gui/set_gui_01/Glitch_Border/Text/7.png",0.25),
            "8": Auxiliar.escalar_imagen("images/gui/set_gui_01/Glitch_Border/Text/8.png",0.25),
            "9": Auxiliar.escalar_imagen("images/gui/set_gui_01/Glitch_Border/Text/9.png",0.25)
        }
        self.digit_images = {
            "0": Auxiliar.escalar_imagen("images/gui/set_gui_01/Pixel_Border/Text/0.png",0.4),
            "1": Auxiliar.escalar_imagen("images/gui/set_gui_01/Pixel_Border/Text/1.png",0.4),
            "2": Auxiliar.escalar_imagen("images/gui/set_gui_01/Pixel_Border/Text/2.png",0.4),
            "3": Auxiliar.escalar_imagen("images/gui/set_gui_01/Pixel_Border/Text/3.png",0.4),
            "4": Auxiliar.escalar_imagen("images/gui/set_gui_01/Pixel_Border/Text/4.png",0.4),
            "5": Auxiliar.escalar_imagen("images/gui/set_gui_01/Pixel_Border/Text/5.png",0.4),
            "6": Auxiliar.escalar_imagen("images/gui/set_gui_01/Pixel_Border/Text/6.png",0.4),
            "7": Auxiliar.escalar_imagen("images/gui/set_gui_01/Pixel_Border/Text/7.png",0.4),
            "8": Auxiliar.escalar_imagen("images/gui/set_gui_01/Pixel_Border/Text/8.png",0.4),
            "9": Auxiliar.escalar_imagen("images/gui/set_gui_01/Pixel_Border/Text/9.png",0.4)
        }
        
        self.timer = 0  # Tiempo transcurrido en el juego
        self.start_time = pygame.time.get_ticks()
        self.is_game_over = False  # Estado de "Game Over"
        self.score = 0  # Puntaje del juego

    def draw_timer(self, screen):
        # Convierte el valor del cronómetro a una cadena de texto
        timer_str = str(self.timer)
        # Calcula la posición x inicial para dibujar los dígitos
        x = (800 - len(timer_str) * 50) // 2

        # Dibuja cada dígito del cronómetro utilizando las imágenes correspondientes
        for digit in timer_str:
            if digit in self.digit_images:
                digit_image = self.digit_images[digit]
                screen.blit(digit_image, (x+200, 120))
                x += digit_image.get_width()

    def draw_score(self, screen):
        # Convierte el valor del cronómetro a una cadena de texto
        score_str = str(self.score)
       
        # Calcula la posición x inicial para dibujar los dígitos
        x = (800 - len(score_str) * 50) // 2

        # Dibuja cada dígito del cronómetro utilizando las imágenes correspondientes
        for digit in score_str:
            if digit in self.digit_images_score:
                digit_image = self.digit_images_score[digit]
                screen.blit(digit_image, (x+700, 10))
                x += digit_image.get_width()

    def draw_game_over(self, screen, x=100, y=350):

        screen.blit(self.game_over_image, (x, y))

    def update(self, tiempo_restante):
        # Lógica de actualización del juego
        if self.timer >= TIEMPO_DE_JUEGO:
            self.is_game_over= True
            
        if not self.is_game_over:

            self.timer = tiempo_restante  # Actualiza el cronómetro

    def draw(self, screen):

        # Dibuja el cronómetro
        self.draw_timer(screen)

        # Dibuja el puntaje
        self.draw_score(screen)
        
        
        if self.is_game_over:
            # Dibuja el estado de "Game Over"
            self.draw_game_over(screen)
