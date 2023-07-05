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


class FormGameLevel1(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)
      
        self.camera_offset = 0  # Inicializa el desplazamiento de la cámara a (0, 0)
      
        
        # --- GUI WIDGET --- 
        self.boton1 = Button(master=self,x=0,y=0,w=140,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",on_click=self.on_click_boton1,on_click_param="form_menu_B",text="BACK",font="Verdana",font_size=30,font_color=C_WHITE)
        self.boton2 = Button(master=self,x=200,y=0,w=140,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",on_click=self.on_click_boton1,on_click_param="form_menu_B",text="PAUSE",font="Verdana",font_size=30,font_color=C_WHITE)
        self.boton_shoot = Button(master=self,x=400,y=0,w=140,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",on_click=self.on_click_shoot,on_click_param="form_menu_B",text="SHOOT",font="Verdana",font_size=30,font_color=C_WHITE)
       
        self.pb_lives = ProgressBar(master=self,x=500,y=50,w=240,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Glitch_Border/Bars/Bar_Background04.png",image_progress="images/gui/set_gui_01/Comic/Elements/heart.png",value = 5, value_max=5)
        self.widget_list = [self.boton1,self.boton2,self.pb_lives,self.boton_shoot]

        # --- GAME ok ELEMNTS --- 
        self.static_background = Background(x=0,y=0,width=w,height=h,path="images\locations\set_bg_01\prueba1.png")

        self.player_1 = Player(x=0,y=400,speed_walk=6,speed_run=12,gravity=17,jump_power=30,frame_rate_ms=100,move_rate_ms=50,jump_height=140,p_scale=0.2,interval_time_jump=300)
        
        self.enemy_list = []
        self.enemy_generation_condition = False
        self.enemy_list.append (Enemy(x=450,y=400,speed_walk=6,speed_run=5,gravity=14,jump_power=30,frame_rate_ms=150,move_rate_ms=50,jump_height=140,p_scale=0.08,interval_time_jump=300))
        self.enemy_list.append (Enemy(x=900,y=400,speed_walk=6,speed_run=5,gravity=14,jump_power=30,frame_rate_ms=150,move_rate_ms=50,jump_height=140,p_scale=0.08,interval_time_jump=300))
       
        self.plataform_list = []
        self.plataform_list.append(Plataform(x=410,y=500,width=50,height=50,frame_rate_ms=150,move_rate_ms=50,move=True,type=24))
        self.plataform_list.append(Plataform(x=460,y=500,width=50,height=50,frame_rate_ms=150,move_rate_ms=50,move=True,type=24))
        self.plataform_list.append(Plataform(x=510,y=500,width=50,height=50,frame_rate_ms=150,move_rate_ms=50,move=True,type=24))   
        self.plataform_list.append(Plataform(x=600,y=430,width=50,height=50,frame_rate_ms=150,move_rate_ms=50,move=False,type=25))
        self.plataform_list.append(Plataform(x=650,y=430,width=50,height=50,frame_rate_ms=150,move_rate_ms=50,move=False,type=25))
        self.plataform_list.append(Plataform(x=750,y=360,width=50,height=50,frame_rate_ms=150,move_rate_ms=50,move=False,type=25))
        self.plataform_list.append(Plataform(x=800,y=360,width=50,height=50,frame_rate_ms=150,move_rate_ms=50,move=False,type=26))
        self.plataform_list.append(Plataform(x=850,y=360,width=50,height=50,frame_rate_ms=150,move_rate_ms=50,move=False,type=26))
        self.plataform_list.append(Plataform(x=900,y=360,width=50,height=50,frame_rate_ms=150,move_rate_ms=50,move=False,type=26))
        self.plataform_list.append(Plataform(x=950,y=360,width=50,height=50,frame_rate_ms=150,move_rate_ms=50,move=False,type=26))
        self.plataform_list.append(Plataform(x=950,y=260,width=50,height=50,frame_rate_ms=150,move_rate_ms=50,move=False,type=26))
        self.plataform_list.append(Plataform(x=1000,y=260,width=50,height=50,frame_rate_ms=150,move_rate_ms=50,move=False,type=26))
        self.plataform_list.append(Plataform(x=1050,y=260,width=50,height=50,frame_rate_ms=150,move_rate_ms=50,move=False,type=26))
        self.plataform_list.append(Plataform(x=550,y=430,width=50,height=50,frame_rate_ms=150,move_rate_ms=50,move=False,type=26))
        

        self.bullet_list = []
        self.can_shoot = True
        self.shoot_delay = 500  # Retraso en milisegundos entre disparos
        self.last_shoot_time = 0
        


    def on_click_boton1(self, parametro):
        self.set_active(parametro)
        
    def generate_enemies(self, num_enemies):
        min_x = 10  # Coordenada mínima en X donde pueden aparecer los enemigos
        max_x = ANCHO_VENTANA-10 # Coordenada máxima en X donde pueden aparecer los enemigos
        min_y = 10  # Coordenada mínima en Y donde pueden aparecer los enemigos
        max_y = GROUND_LEVEL   # Coordenada máxima en Y donde pueden aparecer los enemigos

        for _ in range(num_enemies):
            x = random.randint(min_x, max_x)
            y = GROUND_LEVEL-400
            self.enemy_list.append (Enemy(x=x,y=y,speed_walk=6,speed_run=5,gravity=14,
                                          jump_power=30,frame_rate_ms=150,move_rate_ms=50,
                                          jump_height=140,
                                          nombre_imagen_walk="images/caracters/enemies/Troll1/Walk_00{0}.png",
                 cant_imag_walk_inicio=0,cant_imag_walk_fin=9,
                 nombre_imagen_idle="images/caracters/enemies/Troll1/Idle_00{0}.png",
                 cant_imag_idle_inicio=0,cant_imag_idle_fin=9,
                 nombre_imagen_die="images/caracters/enemies/Troll1/Dead_00{0}.png",
                 cant_imag_die_inicio=0,cant_imag_die_fin=9,
                 nombre_imagen_hurt="images/caracters/enemies/Troll1/Hurt_00{0}.png",
                 cant_imag_hurt_inicio=0,cant_imag_hurt_fin=9,p_scale=0.40,interval_time_jump=300))   

    def on_click_shoot(self, parametro):
        for enemy_element in self.enemy_list:
            self.bullet_list.append(Bullet("enemy",enemy_element.rect.centerx,enemy_element.rect.centery,self.player_1.rect.centerx,self.player_1.rect.centery,20,type=False,frame_rate_ms=100,move_rate_ms=20,width=5,height=5))

        
    def on_fire_shoot(self, el_que_dispara): 
            if el_que_dispara.direction==DIRECTION_L:
                x_final = 0
                x_inicio=-50
            else:
                x_final = ANCHO_VENTANA
                x_inicio=25      
                   
            self.bullet_list.append(Bullet(el_que_dispara.nombre,el_que_dispara.rect.centerx+x_inicio,el_que_dispara.rect.centery-25,x_final,el_que_dispara.rect.centery-25,35,type=True,frame_rate_ms=100,move_rate_ms=20,width=5,height=5))
            el_que_dispara.can_shoot = False
            
    def update(self, lista_eventos,keys,delta_ms, tiempo_actual):
        if len(self.enemy_list) <1:
            self.enemy_generation_condition= True
            
       
        if(keys[pygame.K_s] and not keys[pygame.K_a] and self.player_1.can_shoot):
            
            if tiempo_actual - self.last_shoot_time >= self.shoot_delay:
                self.on_fire_shoot(self.player_1)       
                self.player_1.last_shoot_time = tiempo_actual
                
               
        for aux_widget in self.widget_list:
            aux_widget.update(lista_eventos)

        for bullet_element in self.bullet_list:
            bullet_element.update(delta_ms,self.plataform_list,self.enemy_list,self.player_1)
            
                
            if not bullet_element.is_active:
                self.bullet_list.remove(bullet_element)
        
        for enemy_element in self.enemy_list:
            enemy_element.update(delta_ms,self.plataform_list)
            if enemy_element.can_shoot:
                self.on_fire_shoot(enemy_element)
                enemy_element.last_shoot_time = tiempo_actual
                 
            if enemy_element.is_death:
                
                self.enemy_list.remove(enemy_element)
            if not enemy_element.can_shoot and tiempo_actual - enemy_element.last_shoot_time >= enemy_element.shoot_delay:
                enemy_element.can_shoot = True  
               
        for plataform_element in self.plataform_list:
            plataform_element.update(delta_ms)       
                
        self.player_1.events(delta_ms,keys)
        self.player_1.update(delta_ms,self.plataform_list)
        
            
        self.pb_lives.value = self.player_1.lives 
        
        if not self.player_1.can_shoot and tiempo_actual - self.player_1.last_shoot_time >=self.player_1.shoot_delay:
            self.player_1.can_shoot = True
            
        if self.enemy_generation_condition:
            self.generate_enemies(1)
            self.enemy_generation_condition=False
            
         # Actualiza la posición de la cámara en función del jugador
        self.camera_offset = self.player_1.rect.x
        if self.camera_offset<1:
             self.camera_offset = 0
        elif self.camera_offset==1116:
            self.camera_offset = 1115     
           
            

    def draw(self): 
        super().draw()
        self.static_background.draw(self.surface, offset=self.camera_offset)

        for aux_widget in self.widget_list:    
            aux_widget.draw()

        for plataforma in self.plataform_list:
            plataforma.draw(self.surface)

        for enemy_element in self.enemy_list:
            enemy_element.draw(self.surface)
        
        self.player_1.draw(self.surface,offset=self.camera_offset)
        

        for bullet_element in self.bullet_list:
            bullet_element.draw(self.surface)