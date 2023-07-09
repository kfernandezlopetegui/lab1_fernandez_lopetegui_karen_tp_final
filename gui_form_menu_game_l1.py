import pygame
import random
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar
from player import Player
from enemigo import Enemy
from plataforma import Plataform
from background import Background
from bullet import Bullet
from game import Game
from nivel import Level


class FormGameLevel1(Form):
    def __init__(self, name, master_surface, x, y, w, h, color_background, color_border, active):
        super().__init__(name, master_surface, x, y, w,
                         h, color_background, color_border, active)

        self.game = Game()
        self.end_game = False
        self.contador= 0
        self.current_position = 0
 
        # --- GUI WIDGET ---
        self.boton1 = Button(master=self, x=0, y=0, w=140, h=50, color_background=None, color_border=None, image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",
                             on_click=self.on_click_boton1, on_click_param="form_menu_B", text="BACK", font="Verdana", font_size=30, font_color=C_WHITE)
        self.boton2 = Button(master=self, x=200, y=0, w=140, h=50, color_background=None, color_border=None, image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",
                             on_click=self.on_click_boton1, on_click_param="form_menu_B", text="PAUSE", font="Verdana", font_size=30, font_color=C_WHITE)
        self.boton_shoot = Button(master=self, x=400, y=0, w=140, h=50, color_background=None, color_border=None, image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",
                                  on_click=self.on_click_shoot, on_click_param="form_menu_B", text="SHOOT", font="Verdana", font_size=30, font_color=C_WHITE)

        self.pb_lives = ProgressBar(master=self, x=500, y=50, w=240, h=50, color_background=None, color_border=None,
                                    image_background="images/gui/set_gui_01/Glitch_Border/Bars/Bar_Background04.png", image_progress="images/gui/set_gui_01/Comic/Elements/heart.png", value=5, value_max=5)
        self.widget_list = [self.boton1, self.boton2,
                            self.pb_lives, self.boton_shoot]

        # --- GAME ok ELEMNTS ---
        self.static_background = Background(
            x=0, y=0, width=w, height=h, path="images\locations\set_bg_01\prueba1.png")

        self.player_1 = Player(x=0, y=400, speed_walk=9, speed_run=12, gravity=17, jump_power=30,
                               frame_rate_ms=100, move_rate_ms=50, jump_height=140, p_scale=0.2, interval_time_jump=300)

        self.enemy_list = []
        self.enemy_generation_condition = False
        self.enemy_list.append(Enemy(x=450, y=400, speed_walk=6, speed_run=5, gravity=14, jump_power=30,
                               frame_rate_ms=150, move_rate_ms=50, jump_height=140, p_scale=0.08, interval_time_jump=300))
        self.enemy_list.append(Enemy(x=900, y=400, speed_walk=6, speed_run=5, gravity=14, jump_power=30,
                               frame_rate_ms=150, move_rate_ms=50, jump_height=140, p_scale=0.08, interval_time_jump=300))
        self.enemy_list.append(Enemy(x=1000, y=400, speed_walk=6, speed_run=5, gravity=14, jump_power=30,
                               frame_rate_ms=150, move_rate_ms=50, jump_height=140, p_scale=0.08, interval_time_jump=300))
        self.enemy_list.append(Enemy(x=4000, y=400, speed_walk=6, speed_run=5, gravity=14, jump_power=30,
                               frame_rate_ms=150, move_rate_ms=50, jump_height=140, p_scale=0.08, interval_time_jump=300))

        self.plataform_list = []
        self.plataform_list.append(Plataform(
            x=410, y=500, width=50, height=50, frame_rate_ms=150, move_rate_ms=50, move=True, type=24))
        self.plataform_list.append(Plataform(
            x=460, y=500, width=50, height=50, frame_rate_ms=150, move_rate_ms=50, move=True, type=24))
        self.plataform_list.append(Plataform(
            x=510, y=500, width=50, height=50, frame_rate_ms=150, move_rate_ms=50, move=True, type=24))
        self.plataform_list.append(Plataform(
            x=600, y=430, width=50, height=50, frame_rate_ms=150, move_rate_ms=50, move=False, type=25))
        self.plataform_list.append(Plataform(
            x=650, y=430, width=50, height=50, frame_rate_ms=150, move_rate_ms=50, move=False, type=25))
        self.plataform_list.append(Plataform(
            x=750, y=360, width=50, height=50, frame_rate_ms=150, move_rate_ms=50, move=False, type=25))
        self.plataform_list.append(Plataform(
            x=800, y=360, width=50, height=50, frame_rate_ms=150, move_rate_ms=50, move=False, type=26))
        self.plataform_list.append(Plataform(
            x=850, y=360, width=50, height=50, frame_rate_ms=150, move_rate_ms=50, move=False, type=26))
        self.plataform_list.append(Plataform(
            x=900, y=360, width=50, height=50, frame_rate_ms=150, move_rate_ms=50, move=False, type=26))
        self.plataform_list.append(Plataform(
            x=950, y=360, width=50, height=50, frame_rate_ms=150, move_rate_ms=50, move=False, type=26))
        self.plataform_list.append(Plataform(
            x=950, y=260, width=50, height=50, frame_rate_ms=150, move_rate_ms=50, move=False, type=26))
        self.plataform_list.append(Plataform(
            x=1000, y=260, width=50, height=50, frame_rate_ms=150, move_rate_ms=50, move=False, type=26))
        self.plataform_list.append(Plataform(
            x=1050, y=260, width=50, height=50, frame_rate_ms=150, move_rate_ms=50, move=False, type=26))
        self.plataform_list.append(Plataform(
            x=550, y=430, width=50, height=50, frame_rate_ms=150, move_rate_ms=50, move=False, type=26))

        self.level_1 = Level(self.player_1, self.plataform_list,
                             self.enemy_list, self.static_background)

    def on_click_boton1(self, parametro):
        self.set_active(parametro)

    def generate_enemies(self, num_enemies):
        min_x = 10  # Coordenada mínima en X donde pueden aparecer
        max_x = ANCHO_VENTANA-10  # Coordenada máxima en X donde pueden aparecer los enemigos
        min_y = 10  # Coordenada mínima en Y donde pueden aparecer los enemigos
        max_y = GROUND_LEVEL   # Coordenada máxima en Y donde pueden aparecer los enemigos

        for _ in range(num_enemies):
            x = random.randint(min_x, max_x)
            y = GROUND_LEVEL-400
            self.enemy_list.append(Enemy(x=x, y=y, speed_walk=6, speed_run=5, gravity=14,
                                         jump_power=30, frame_rate_ms=150, move_rate_ms=50,
                                         jump_height=140,
                                         nombre_imagen_walk="images/caracters/enemies/Troll1/Walk_00{0}.png",
                                         cant_imag_walk_inicio=0, cant_imag_walk_fin=9,
                                         nombre_imagen_idle="images/caracters/enemies/Troll1/Idle_00{0}.png",
                                         cant_imag_idle_inicio=0, cant_imag_idle_fin=9,
                                         nombre_imagen_die="images/caracters/enemies/Troll1/Dead_00{0}.png",
                                         cant_imag_die_inicio=0, cant_imag_die_fin=9,
                                         nombre_imagen_hurt="images/caracters/enemies/Troll1/Hurt_00{0}.png",
                                         cant_imag_hurt_inicio=0, cant_imag_hurt_fin=9, p_scale=0.40, interval_time_jump=300))

    def on_click_shoot(self, parametro):
        for enemy_element in self.enemy_list:
            self.bullet_list.append(Bullet("enemy", enemy_element.rect.centerx, enemy_element.rect.centery, self.player_1.rect.centerx,
                                    self.player_1.rect.centery, 20, type=False, frame_rate_ms=100, move_rate_ms=20, width=5, height=5))

    def update(self, lista_eventos, keys, delta_ms, tiempo_actual, tiempo_restante):

        for aux_widget in self.widget_list:
            aux_widget.update(lista_eventos)
        self.level_1.update(keys, tiempo_actual, delta_ms)
        self.game.update(tiempo_restante)
        self.game.is_game_over = self.player_1.is_death
        
        if self.current_position <= -4900:
            self.level_1.shift_world(0)
            
        else: 
                
            if self.player_1.rect.right >= 500:
                diff = self.player_1.rect.right - 500
                self.player_1.rect.right = 500
                self.level_1.shift_world(-diff)
            
            # If the player gets near the left side, shift the world right (+x)
            if self.player_1.rect.left <= 1:
                diff = 1 -self.player_1.rect.left
                self.player_1.rect.left = 1
                self.level_1.shift_world(diff)  
                
            self.current_position = self.player_1.rect.x + self.level_1.world_shift
        
        
        '''if current_position < self.level_1.level_limit:
           self.player_1.rect.x = 1 
'''            
        if self.player_1.is_death:
            self.contador+=1
        if self.player_1.is_death and self.contador == 60:
            
            self.end_game = self.game.is_game_over
            
        self.game.score = self.player_1.score
        self.pb_lives.value = self.player_1.lives

    def draw(self):
        super().draw()
        self.level_1.draw(self.surface)
        self.game.draw(self.surface)
        

        for aux_widget in self.widget_list:
            aux_widget.draw()
