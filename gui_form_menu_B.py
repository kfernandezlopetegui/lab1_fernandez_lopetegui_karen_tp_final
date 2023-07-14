import pygame
from pygame.locals import *
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar
from constantes import *
from gui_label import Label

import sqlite3

class FormMostrarDatos(Form):
    def __init__(self, name, master_surface, x, y, w, h, color_background, color_border, active):
        super().__init__(name, master_surface, x, y, w, h, color_background, color_border, active)
        #self.tablero = TextBox(master=self, x=0, y=0, w=w/2, h=h/2, color_background=color_background, color_border=None, text=text, font="Arial", font_size=14, font_color=C_BLACK)
        self.lista_widget  = []
        self.boton = Button(master=self, x=40, y=300, w=90, h=80, color_background=None, color_border=None, image_background="images/gui/set_gui_01/Pixel_Border/Buttons/arrowLeft.png",
                             on_click=self.on_click_boton_active, on_click_param="form_menu_A", text="", font="Verdana", font_size=22, font_color=C_BLACK)
        self.label_score = Label(master=self, x=150, y=10, w=200, h=50, color_background=(53,57,69), color_border=None, text="Rating", font="Arial", font_size=20, font_color=C_BLACK)
        self.lista_widget.append(self.label_score)
        self.lista_widget.append(self.boton)
        
        
    def update(self, lista_eventos,keys,delta_ms,tiempo_actual, tiempo_restante):
          for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def on_show(self, datos):
        lineas = datos.splitlines()
       
        for i, linea in enumerate(lineas):
            label = Label(master=self, x=150, y=70*i, w=250, h=50, color_background=(53,57,69), color_border=C_BLACK, text=linea, font="Arial", font_size=16, font_color=C_BLACK)
            self.lista_widget.append(label) 
    
    def on_click_boton_active(self, parametro):
        print("Hola")
        self.set_active(parametro)        
    
    def draw(self):
        super().draw()
        for aux_widget in self.lista_widget:    
            aux_widget.draw()

class FormMenuB(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)
        self.text_score=""
        self.boton1 = Button(master=self,x=150,y=150,w=200,h=40,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_XL_08.png",on_click=self.on_click_boton1,on_click_param="form_game_L1",text="BACK",font="Verdana",font_size=30,font_color=C_BLACK)
        self.boton2 = Button(master=self,x=150,y=200,w=200,h=40,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_XL_08.png",on_click=self.on_click_boton2,on_click_param="",text="AGREGAR",font="Verdana",font_size=30,font_color=C_BLACK)
        self.boton3 = Button(master=self,x=150,y=250,w=200,h=40,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_XL_08.png",on_click=self.on_click_boton3,on_click_param="",text="CREAR",font="Verdana",font_size=30,font_color=C_BLACK)
        self.boton4 = Button(master=self,x=150,y=300,w=200,h=40,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_XL_08.png",on_click=self.on_click_boton4,on_click_param="",text="MOSTRAR",font="Verdana",font_size=30,font_color=C_BLACK)
        self.boton5 = Button(master=self,x=150,y=350,w=200,h=40,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_XL_08.png",on_click=self.on_click_boton5,on_click_param="",text="Borrar datos",font="Verdana",font_size=30,font_color=C_BLACK)
       
        self.txt1 = TextBox(master=self,x=130,y=50,w=240,h=40,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_XL_08.png",text="Ingrese su nombre",font="Verdana",font_size=20,font_color=C_BLACK)
        #self.label = Label(master=self, x=0, y=100, w=250, h=40, color_background=(53,57,69), color_border=C_BLACK, text="Score: {0}".format(self.text_score), font="Arial", font_size=20, font_color=C_BLACK)
        
        self.lista_widget = [self.boton1,self.boton2,self.boton3,self.boton4,self.txt1, self.boton5]

    def on_click_boton1(self, parametro):
        self.set_active(parametro)

    def on_click_boton2(self, parametro):
        import sqlite3
        with sqlite3.connect("db/db_score.db") as conexion:
            try:
                conexion.execute("insert into score (nombre,value) values (?,?)", (self.txt1._text, self.text_score))
                conexion.commit()# Actualiza los datos realmente en la tabla
            except:
                print("Error")
    
    def on_click_boton3(self, parametro):
        
        with sqlite3.connect("db/db_score.db") as conexion:
            try:
                sentencia = ''' create  table score
                                (
                                        id integer primary key autoincrement,
                                        nombre text,
                                        value real
                                )
                            '''
                conexion.execute(sentencia)
                print("Se creo la tabla personajes")                       
            except sqlite3.OperationalError:
                print("La tabla ya existe")

    def on_click_boton4(self, parametro):
        with sqlite3.connect("db/db_score.db") as conexion:
            cursor=conexion.execute("SELECT * FROM score")
            datos=""
            lista_datos=[]
            for fila in cursor:
                datos += f"Nombre: {fila[1]}, Score: {fila[2]}\n"
                lista_datos.append(fila)
                
            form_mostrar = FormMostrarDatos("MostrarDatos", self.master_surface,300,200, self.w, self.h, (53,57,69), (53,57,69), False)
            form_mostrar.on_show(datos)  # Configurar los datos en la etiqueta del formulario mostrado
            self.set_active("MostrarDatos")  # Mostrar el formulario FormMostrarDatos
   
    def on_click_boton5(self, parametro):
        with sqlite3.connect("db/db_score.db") as conexion:
            cursor = conexion.cursor()
            cursor.execute("DROP TABLE IF EXISTS score;") 
            conexion.commit()   
   
    def update(self, lista_eventos,keys,delta_ms,tiempo_actual, tiempo_restante):
        self.text_score = str(self.score)    
        label = Label(master=self, x=130, y=100, w=250, h=40, color_background=(53,57,69), color_border=C_BLACK, text="Score: {0}".format(self.text_score), font="Arial", font_size=30, font_color=C_BLACK)
        self.lista_widget.append(label)
        
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)
        

    def draw(self): 
        super().draw()
        for aux_widget in self.lista_widget:    
            aux_widget.draw()