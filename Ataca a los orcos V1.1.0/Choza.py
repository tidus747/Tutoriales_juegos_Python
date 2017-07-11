# -*- coding: utf-8 -*-
from Funciones import *

class Choza:
    def __init__(self, numero, ocupantes):
        self.ocupantes = ocupantes
        self.numero = numero
        self.conquistada = False

    def conquistar(self, nuevo_ocupante):
        self.ocupantes = nuevo_ocupante
        self.conquistada = True
        print_bold("¡Buena trabajo! La choza %d ha sido conquistada"% self.numero)

    def Tipo_de_ocupante(self):
        if self.conquistada:
            tipo_ocupante = 'Conquistada'
        elif self.ocupantes is None:
            tipo_ocupante = 'No ocupada'
        else:
            tipo_ocupante = self.ocupantes.tipo_unidad

        return tipo_ocupante
