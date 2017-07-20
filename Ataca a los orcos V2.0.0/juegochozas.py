# -*- coding: utf-8 -*-

import sys
import random

if sys.version_info < (3, 0):
    from Tkinter import Tk, Label, Radiobutton, PhotoImage, IntVar
    import tkMessageBox as messagebox
else:
    from tkinter import Tk, Label, Radiobutton, PhotoImage, IntVar
    from tkinter import messagebox


class JuegoChozas:
    def __init__(self, parent):
        self.imagen_fondo = PhotoImage(file="Jungle_small_2.gif")
        self.imagen_choza = PhotoImage(file="Hut_small_2.gif")

        self.ancho_choza = 60
        self.alto_choza = 140
        self.container = parent

        self.Chozas = []
        self.result = ""

        self.ocupar_chozas()

        self.setup()

    def ocupar_chozas(self):
        ocupantes = ['enemigo', 'amigo', 'vacia']
        while len(self.Chozas) < 5:
            computer_choice = random.choice(ocupantes)
            self.Chozas.append(computer_choice)
        print("Los ocupantes de las chozas son:", self.Chozas)

    def entrar_choza(self, numero_choza):
        print("Entrando en la choza #:", numero_choza)
        ocupante_choza = self.Chozas[numero_choza-1]
        print("El ocupante de la choza es: ", ocupante_choza)

        if ocupante_choza == 'enemigo':
            self.result = "Enemigo visto en la choza # %d \n\n" % numero_choza
            self.result += "Has perdido :( Mucha suerte la próxima vez!"
        elif ocupante_choza == 'vacia':
            self.result = "La Choza # %d está vacia\n\n" % numero_choza
            self.result += "Enhorabuena! Has ganado!!!"
        else:
            self.result = "Amigo visto en la choza # %d \n\n" % numero_choza
            self.result += "Enhorabuena! Has ganado!!!"

        self.anunciar_ganador(self.result)

    def crear_widgets(self):

        self.var = IntVar()
        self.background_label = Label(self.container,
                                      image=self.imagen_fondo)
        txt = "Selecciona una choza en la que entrar. Ganarás si:\n"
        txt += "La choza está vacia o si su ocupante es tu aliado, de lo contrario morirás"
        self.info_label = Label(self.container, text=txt, bg='white')
        # Creamos un dicionario con las opciones para las imagenes de las chozas
        r_btn_config = {'variable': self.var,
                        'bg': '#8AA54C',
                        'activebackground': 'green',
                        'image': self.imagen_choza,
                        'height': self.alto_choza,
                        'width': self.ancho_choza,
                        'command': self.radio_btn_pressed}

        self.r1 = Radiobutton(self.container, r_btn_config, value=1)
        self.r2 = Radiobutton(self.container, r_btn_config, value=2)
        self.r3 = Radiobutton(self.container, r_btn_config, value=3)
        self.r4 = Radiobutton(self.container, r_btn_config, value=4)
        self.r5 = Radiobutton(self.container, r_btn_config, value=5)

    def setup(self):
        self.crear_widgets()
        self.setup_layout()

    def setup_layout(self):
        self.container.grid_rowconfigure(1, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        self.container.grid_columnconfigure(4, weight=1)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.info_label.grid(row=0, column=0, columnspan=5, sticky='nsew')
        self.r1.grid(row=1, column=0)
        self.r2.grid(row=1, column=2)
        self.r3.grid(row=1, column=4)
        self.r4.grid(row=4, column=2)
        self.r5.grid(row=4, column=0)

    def anunciar_ganador(self, data):
        messagebox.showinfo("¡Atención!", message=data)

    # Handle Events
    def radio_btn_pressed(self):
        self.entrar_choza(self.var.get())

if __name__ == "__main__":

    mainwin = Tk()
    WIDTH = 1280
    HEIGHT = 700
    mainwin.geometry("%sx%s" % (WIDTH, HEIGHT))
    mainwin.resizable(0, 0)
    mainwin.title("Ataca a los orcos V 2.0.0 - El Videojuego")
    game_app = JuegoChozas(mainwin)
    mainwin.mainloop()
