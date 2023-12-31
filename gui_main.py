import pygame
from pygame.locals import *
import sys
from constantes import *
from auxiliar import *
from gui_form import Form
from gui_form_menu_A import FormMenuA
from gui_form_menu_B import*
from gui_form_menu_C import FormMenuC
from gui_form_menu_game_l1 import FormGameLevel1 
from gui_form_menu_pause import FormMenuPausa



'''
Instalar biblioteca pygame:
En una terminal escribir (o copiar y pegar) este comando:
pip install -U pygame
Probar pygame:
Una vez que termine la instalación ingresar el siguiente comando:
python -m pygame.examples.aliens

'''

flags = DOUBLEBUF 
screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA), flags, 16)
pygame.display.set_caption("Mi Juego")
pygame.init()
clock = pygame.time.Clock()

start_time = pygame.time.get_ticks()
    
score_aux=0

cronometro=TIEMPO_DE_JUEGO



form_menu_A = FormMenuA(name="form_menu_A",master_surface = screen,x=300,y=200,w=500,h=400,color_background=(53,57,69),color_border=(255,0,255),active=True)
form_menu_B = FormMenuB(name="form_menu_B",master_surface = screen,x=300,y=200,w=500,h=400,color_background=(53,57,69),color_border=(255,0,255),active=False)
form_menu_C = FormMenuC(name="form_menu_C",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=(53,57,69),color_border=(255,0,255),active=False)
form_pausa = FormMenuPausa(name="form_menu_pause" ,master_surface = screen,x=300,y=200,w=500,h=400,color_background=(53,57,69),color_border=(0,0,0),active=False)
form_game_L1 = FormGameLevel1(name="form_game_L1",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA_IMAGEN,h=ALTO_VENTANA,color_background=(53,57,69),color_border=(255,0,255),active=False)
form_mostrar = FormMostrarDatos("mostrar_datos", master_surface= screen,x=300,y=200, w=500,h=400, color_background=(53,57,69),color_border=(255,0,255), active=False)
while True:     
    lista_eventos = pygame.event.get()
    for event in lista_eventos:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
            
    keys = pygame.key.get_pressed()
    delta_ms = clock.tick(FPS)
    tiempo_actual = pygame.time.get_ticks()
    elapsed_time = (tiempo_actual - start_time) // 1000
    tiempo_restante_juego=cronometro-elapsed_time
    
    aux_form_active = Form.get_active()
    if(aux_form_active != None and aux_form_active.active):
        if aux_form_active.name =="form_game_L1":
            score_aux = aux_form_active.score
           
           
            
        if aux_form_active.name =="form_menu_B":
            aux_form_active.score = score_aux
              
        aux_form_active.update(lista_eventos,keys,delta_ms, tiempo_actual, tiempo_restante_juego)
        aux_form_active.draw()
        '''if  form_game_L1.restart==True:
            form_game_L1.restart_pending = True
            aux_form_active.restart = False
        if form_game_L1.restart_pending:    
            form_game_L1 = form_game_aux
            form_game_L1.restart_pending = False 
            print("llefgue pero no hice nada :v")'''
        if aux_form_active.quit:
            pygame.quit()
            sys.exit()  
    pygame.display.flip()




    


  



