# -*- coding: utf-8 -*-
from Unidad_de_juego import Unidad_de_juego
from Funciones import *


class Orco(Unidad_de_juego):
    def __init__(self, Nombre=''):
        Unidad_de_juego.__init__(self,Nombre)
        self.max_salud = 30
        self.Medidor_salud = self.max_salud
        self.tipo_unidad = 'enemigo'
        self.numero_choza = 0

    def info(self):
        print("Grrrr..Soy un Orco montador de huargos. Creo que esta noche serás mi cena")
