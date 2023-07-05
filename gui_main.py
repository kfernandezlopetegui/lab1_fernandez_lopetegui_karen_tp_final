import pygame
from pygame.locals import *
import sys
from constantes import *
from auxiliar import *
from gui_form import Form
from gui_form_menu_A import FormMenuA
from gui_form_menu_B import FormMenuB
from gui_form_menu_C import FormMenuC
from gui_form_menu_game_l1 import FormGameLevel1 

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
pygame.init()
clock = pygame.time.Clock()

start_time = pygame.time.get_ticks()
    


cronometro=TIEMPO_DE_JUEGO



form_menu_A = FormMenuA(name="form_menu_A",master_surface = screen,x=300,y=200,w=500,h=400,color_background=(255,255,0),color_border=(255,0,255),active=True)
form_menu_B = FormMenuB(name="form_menu_B",master_surface = screen,x=300,y=200,w=500,h=400,color_background=(0,255,255),color_border=(255,0,255),active=False)
form_menu_C = FormMenuC(name="form_menu_C",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=(0,255,255),color_border=(255,0,255),active=False)

form_game_L1 = FormGameLevel1(name="form_game_L1",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA_IMAGEN,h=ALTO_VENTANA,color_background=(0,255,255),color_border=(255,0,255),active=False)

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
    texto_cronometro = Auxiliar.generar_texto(
        "Arial", TAMANIO_TEXTO, "Tiempo:{0}".format(tiempo_restante_juego), C_BLACK)
    aux_form_active = Form.get_active()
    if(aux_form_active != None and aux_form_active.active):
           
        aux_form_active.update(lista_eventos,keys,delta_ms, tiempo_actual)
        aux_form_active.draw()
    screen.blit(texto_cronometro, (500, 100))
    if tiempo_restante_juego== 0:
        pygame.quit()
        sys.exit()  
    pygame.display.flip()




    


  



