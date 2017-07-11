# -*- coding: utf-8 -*-
from Unidad_de_juego import Unidad_de_juego
from Funciones import *


class Caballero(Unidad_de_juego):
    def __init__(self,Nombre='Sir Gandorel'):
        Unidad_de_juego.__init__(self, Nombre)
        self.max_salud = 40
        self.Medidor_salud = self.max_salud
        self.tipo_unidad = 'amigo'

    def info(self):
        print("¡Mi nombre es Sir Gandorel. Soy un caballero de las llanuras meridionales!")

    def Conquistar_choza(self, Choza):
        print_bold("Entrando en la choza %d..."%Choza.numero)
        es_enemigo = (isinstance(Choza.ocupantes, Unidad_de_juego) and Choza.ocupantes.tipo_unidad == 'enemigo')
        continuar_ataque = 1

        if es_enemigo:
            print_bold("¡Enemigo sitiado!")
            self.mostrar_salud(bold=True)
            Choza.ocupantes.mostrar_salud(bold=True)
            while continuar_ataque:
                continuar_ataque = input("...continuar ataque? Si(1)/No(0)")
                if continuar_ataque == 0:
                    self.huir()
                    break

                self.atacar(Choza.ocupantes)

                if Choza.ocupantes.Medidor_salud <= 0:
                    print("")
                    Choza.conquistar(self)
                    break
                if self.Medidor_salud <= 0:
                    print("")
                    break
        else:
            if Choza.Tipo_de_ocupante() == 'No ocupada':
                print_bold("La choza está vacía")
            else:
                print_bold("¡Amigo avistado!")
            Choza.conquistar(self)
            self.curar()

    def huir(self):
        print_bold("Escapando del enemigo...")
        self.enemigo = None
