# -*- coding: utf-8 -*-

from Caballero import Caballero
from Orco import Orco
from Choza import Choza
from Funciones import *
import random
import textwrap

class Juego:
    def __init__(self):
        self.chozas = [] #Inicializamos el número de chozas que tendremos dentro de nuestro juego
        self.jugador = None #En primer lugar el jugador no tendrá una instancia definida

    def get_ocupantes(self):
        return [x.Tipo_de_ocupante() for x in self.chozas]

    def Mostrar_mision(self):
        print_bold("Ataca a los Orcos V1.0.0")

        msg = ("La guerra entre los humanos y sus arqueros enemigos, los Orcos, estaba en el aire."
              "Un enorme ejército de orcos se dirigía hacia los territos de los humanos. Destruían"
              "prácticamente todo en su camino. Los grandes reyes de la raza humana, se unieron para"
              " derrotar a su peor enemigo, era la gran batalla de su tiempo. Sir Gandorel, uno de los "
              "valientes caballeros que guardan las llanuras meridionales, inició un largo viaje hacia el este"
              ", a través de un desconocido bosque espeso. Durante dos días y dos noches, se movió con cautela "
              "a través del grueso bosque. En su camino, vio un pequeño asentamiento aislado. Cansado y con "
              "la esperanza de reponer su stock de alimentos, decidió tomar un desvío. Cuando se acercó al pueblo,"
              "vio cinco chozas. No había nadie alrededor. En ese instante, decidió entrar en un choza...")
        print(textwrap.fill(msg, width = 72))
        print_bold("Misión:")
        print("  1. Lucha contra el enemigo.")
        print("  2. Conquista cada una de las chozas hasta que estén bajo tu control")
        print("-"*72)

    def _procesar_decision(self):
        verifying_choice = True
        idx = 0
        print("Ocupantes actuales: %s" % self.get_ocupantes())
        while verifying_choice:
            user_choice = input("Elige un número de choza para entrar (1-5): ")
            try:
                idx = int(user_choice)
            except ValueError as e:
                print("Entrada no válida: %s \n" %e.args)
                continue
            try:
                if self.chozas[idx-1].conquistada:
                    print("Esta choza ya está conquistada")
                    print_bold("<INFO: No puedes curarte en las choza que hayas conquistado.>")
                else:
                    verifying_choice = False
            except IndexError:
                print("Entrada no aceptada: ", idx)
                print("El número debe estar entre 1 y 5.Inténtalo de nuevo")
                continue
        return idx

    def _ocupar_chozas(self):
        for i in range(5):
            ocupantes = ['enemigo','amigo',None]
            eleccion_aleatoria = random.choice(ocupantes)

            if eleccion_aleatoria == 'enemigo':
                nombre = 'Enemigo-'+ str(i+1) #Colocamos el numero del enemigo como identificador
                self.chozas.append(Choza(i+1, Orco(nombre)))
            elif eleccion_aleatoria == 'amigo':
                nombre = 'Caballero-'+ str(i+1)
                self.chozas.append(Choza(i+1, Caballero(nombre)))
            else:
                self.chozas.append(Choza(i+1, eleccion_aleatoria))

    def play(self):
        self.jugador = Caballero()
        self._ocupar_chozas()
        Contador_chozas_conquistadas = 0

        self.Mostrar_mision()
        self.jugador.mostrar_salud(bold=True)

        while Contador_chozas_conquistadas < 5:
            idx = self._procesar_decision()
            self.jugador.Conquistar_choza(self.chozas[idx-1])

            if self.jugador.Medidor_salud <=0:
                print_bold("Sir Gandorel, esperamos que la próxima vez tenga más suerte")
                break

            if self.chozas[idx-1].conquistada:
                Contador_chozas_conquistadas +=1

        if Contador_chozas_conquistadas == 5:
            print_bold("¡Enhorabuena! Sir Gandorel ha conquistado la aldea")
