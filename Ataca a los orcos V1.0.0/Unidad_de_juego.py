# -*- coding: utf-8 -*-

from Funciones import *

class Unidad_de_juego:
    def __init__(self, Nombre_unidad = ''):
        self.max_salud = 0
        self.Medidor_salud = 0
        self.nombre = Nombre_unidad
        self.enemigo = None
        self.tipo_unidad = None

    def info(self):
        pass

    def atacar(self, enemigo):
        Unidad_herida = eleccion_aleatoria_ataque(self, enemigo) #Funcion que implementamos en el archivo de funciones de juego
        herida = random.randint(10, 15)
        Unidad_herida.Medidor_salud = max(Unidad_herida.Medidor_salud - herida, 0)
        print("¡Ataque! ")
        self.mostrar_salud()
        enemigo.mostrar_salud()

    def curar(self, curado_por=2, curacion_completa=True):
        if self.Medidor_salud == self.max_salud: #Caso en el que la salud sea completa
            return

        if curacion_completa:
            self.Medidor_salud = self.max_salud
        else:
            self.Medidor_salud += curado_por #Puede ocurrir que se sobre pase la salud máxima

        print_bold("¡Has sido curado!")
        self.mostrar_salud(bold=True)

    def reset_medidor_salud(self):
        self.Medidor_salud = self.max_salud

    def mostrar_salud(self, bold=False):
        #Se presenta un problema si no tenemos ningun enemigo
        msg = "Salud: %s: %d" % (self.nombre, self.Medidor_salud)
        if bold:
            print_bold(msg)
        else:
            print(msg)
