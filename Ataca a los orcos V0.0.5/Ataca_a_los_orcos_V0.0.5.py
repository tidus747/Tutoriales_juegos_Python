# -*- coding: utf-8 -*-

import random
import textwrap

def print_bold(msg):
    #Funcion para mostrar por pantalla un string en negrita
    print("\033[1m"+msg+"\033[0m")

def print_linea_punteada(width=72):
    print('-'*width)

def ocupar_chozas():
    ocupantes = ['enemigo','amigo','no ocupada']
    chozas = []
    while len(chozas) < 5: #Definimos un número de asentamiento para establecerlo como amigo o enemigo
        eleccion_aleatoria = random.choice(ocupantes)
        chozas.append(eleccion_aleatoria)
    return chozas

def mostrar_mision():
    print("\033[1m"+ "Ataca a los Orcos V0.0.5" + "\033[0m")

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
    print("\033[1m"+"Misión:"+"\033[0m")
    print("Elige una choza donde poder descansar...")
    print("\033[1m"+"NOTA:"+"\033[0m")
    print("¡Cuidado! Hay enemigos rondando la zona")
    print_linea_punteada()

def mostrar_salud(medidor_salud, bold):
    if bold:
        print_bold("Salud Sir Gandorel:")
        print_bold("%d"%(medidor_salud['jugador']))
        print_bold("Salud Enemigo:")
        print_bold("%d"%(medidor_salud['enemigo']))
    else:
        print("Salud Sir Gandorel:")
        print("%d"%(medidor_salud['jugador']))
        print("Salud Enemigo:")
        print("%d"%(medidor_salud['enemigo']))


def procesar_decision_usuario():
    msg = "\033[1m" + "Elige una choza, introduce un número entre 1 y 5: " + "\033[0m"
    decision_usuario = input("\n"+msg)
    idx = int(decision_usuario)
    return idx

def reset_medidor_salud(medidor_salud):
    medidor_salud['jugador']=40
    medidor_salud['enemigo']=30

def atacar(medidor_salud):
    lista_golpes = 4*['jugador']+6*['enemigo']
    unidad_herida = random.choice(lista_golpes)
    puntos_vida = medidor_salud[unidad_herida]
    herida = random.randint(10,15)
    medidor_salud[unidad_herida] = max(puntos_vida- herida,0)
    print("¡Ataque!")
    mostrar_salud(medidor_salud,bold=False)

def revelar_ocupantes(idx, chozas):
    msg=""
    print("Revelando los ocupantes...")
    for i in range(len(chozas)):
        ocupantes_info = "<%d:%s>"%(i+1, chozas[i])
        if i+1 == idx:
            ocupantes_info = "\033[1m" + ocupantes_info + "\033[0m"
        msg += ocupantes_info + " "
    print("\t" + msg)
    print_linea_punteada()

#En la siguiente función se establece un sistema de combate iterativo
def play_game(medidor_salud):
    chozas = ocupar_chozas()
    idx = procesar_decision_usuario()
    revelar_ocupantes(idx, chozas)

    if chozas[idx-1] != 'enemigo':
        print_bold("¡Enhorabuena! ¡Has GANADO!")
    else:
        print_bold('¡Enemigo encontrado!')
        mostrar_salud(medidor_salud, bold=True)
        continuar_ataque = True

        while continuar_ataque:
            continuar_ataque = input("...continuar con el ataque? Si(1)/No(0)")
            if continuar_ataque == 0:
                print_bold("Huyendo con el siguiente estado de salud...")
                mostrar_salud(medidor_salud, bold=True)
                print_bold("¡Game Over!")
                break

            atacar(medidor_salud)

            if medidor_salud['enemigo'] <=0:
                print_bold("¡Sir Gandorel ha derrotado a su enemigo!")
                break
            if medidor_salud['jugador'] <=0:
                print_bold("Sir Gandorel ha muerto ...")
                break

#Funcion para hacer funcionar el programa principal que queremos ejecutar
def run_application():
    seguir_jugando = 1
    medidor_salud = {}
    reset_medidor_salud(medidor_salud)
    mostrar_mision()

    while seguir_jugando == 1:
        reset_medidor_salud(medidor_salud)
        play_game(medidor_salud)
        seguir_jugando = input("¿Quieres jugar de nuevo? Si(1)/No(0):")

if __name__ == '__main__':
    run_application()
