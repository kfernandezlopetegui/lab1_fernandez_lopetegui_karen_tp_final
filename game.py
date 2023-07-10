import pygame
from constantes import * 
from auxiliar import *

pygame.mixer.init()

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

        self.volume = 1.0
        self.sound_volume = 1.0
        
        self.is_muted = False
        
        
        self.is_sound_muted = False
        # se cargan los sonidos predeterminados
        self.corte_sound = pygame.mixer.Sound("music/corte.mp3")
        self.disparo_sound = pygame.mixer.Sound("music/SHOOT.mp3")
        self.muerte_sound = pygame.mixer.Sound("music/muerte.mp3")


    def play_music(self, file_path):
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.set_volume(self.volume)
        pygame.mixer.music.play(-1)
   
        
    def set_volume(self, volume):
        self.volume = volume
        pygame.mixer.music.set_volume(self.volume)
   
        
    def set_sound_volume(self, volume):
        self.sound_volume = volume
        self.corte_sound.set_volume(self.sound_volume)
        self.disparo_sound.set_volume(self.sound_volume)
        self.muerte_sound.set_volume(self.sound_volume)
   
        
    def mute(self):
        self.is_muted = not self.is_muted
        if self.is_muted:
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
   
            
    def mute_sound(self):
        self.is_sound_muted = not self.is_sound_muted
        if self.is_sound_muted:
            self.corte_sound.set_volume(0)
            self.disparo_sound.set_volume(0)
            self.muerte_sound.set_volume(0)
        else:
            self.corte_sound.set_volume(self.sound_volume)
            self.disparo_sound.set_volume(self.sound_volume)
            self.muerte_sound.set_volume(self.sound_volume)
   
            
    def reproducir_corte(self):
        if not self.is_sound_muted:
            self.corte_sound.play()


    def reproducir_disparo(self):
        if not self.is_sound_muted:
            self.disparo_sound.play()


    def reproducir_muerte(self):
        if not self.is_sound_muted:
            self.muerte_sound.play()        

                
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
