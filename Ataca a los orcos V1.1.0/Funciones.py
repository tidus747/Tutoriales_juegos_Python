# -*- coding: utf-8 -*-
import random

def print_bold(msg):
    #Funcion para mostrar por pantalla un string en negrita
    print("\033[1m"+msg+"\033[0m")

def print_linea_punteada(width=72):
    print('-'*width)

def eleccion_aleatoria_ataque(obj1, obj2):
    weighted_list = 5 * [id(obj1)] + 5 * [id(obj2)]
    selection = random.choice(weighted_list)

    if selection == id(obj1):
        return obj1

    return obj2
