# -*- coding: utf-8 -*-

import random
import textwrap

if __name__ == '__main__':
    seguir_jugando = 1
    ocupantes = ['enemigo','amigo','no ocupada']
    ancho_linea = 72
    linea_punteada = ancho_linea * '-'
    print(linea_punteada)
    print("\033[1m"+ "Ataca a los Orcos V0.0.1" + "\033[0m")

    msg = ("La guerra entre los humanos y sus arqueros enemigos, los Orcos, estaba en el aire."
          "Un enorme ejército de orcos se dirigía hacia los territos de los humanos. Destruían"
          "prácticamente todo en su camino. Los grandes reyes de la raza humana, se unieron para"
          " derrotar a su peor enemigo, era la gran batalla de su tiempo. Sir Gandorel, uno de los "
          "valientes caballeros que guardan las llanuras meridionales, inició un largo viaje hacia el este"
          ", a través de un desconocido bosque espeso. Durante dos días y dos noches, se movió con cautela "
          "a través del grueso bosque. En su camino, vio un pequeño asentamiento aislado. Cansado y con "
          "la esperanza de reponer su stock de alimentos, decidió tomar un desvío. Cuando se acercó al pueblo,"
          "vio cinco chozas. No había nadie alrededor. En ese instante, decidió entrar en un choza...")

    print(textwrap.fill(msg, width = ancho_linea))
    print("\033[1m"+"Misión:"+"\033[0m")
    print("Elige una choza donde poder descansar...")
    print("\033[1m"+"NOTA:"+"\033[0m")
    print("¡Cuidado! Hay enemigos rondando la zona")
    print(linea_punteada)

    while seguir_jugando == 1:
        chozas = []
        while len(chozas) < 5: #Definimos un número de asentamiento para establecerlo como amigo o enemigo
            eleccion_aleatoria = random.choice(ocupantes)
            chozas.append(eleccion_aleatoria)

        msg = "\033[1m" + "Elige una choza, introduce un número entre 1 y 5: " + "\033[0m"
        decision_usuario = input("\n"+msg)
        idx = int(decision_usuario)

        #Pasamos a descubrir cuales son los ocupantes del emplazamiento

        print("Descubriendo los ocupantes...")
        msg=""
        for i in range(len(chozas)):
            ocupantes_info = "<%d:%s>"%(i+1, chozas[i])
            if i+1 == idx:
                ocupantes_info = "\033[1m" + ocupantes_info + "\033[0m"
            msg += ocupantes_info + " "
        print("\t" + msg)
        print(linea_punteada)
        print("\033[1m" + "Entrando en la choza %d..." %idx + "\033[0m")

        if chozas[idx-1] == 'enemigo':
            print("\033[1m" + "Sir Gandorel ha muerto asesinado por una manada de orcos (Mucha suerte la próxima vez)" + "\033[0m")
        else:
            print("\033[1m" + "¡Felicidades! Sir Gandorel ha podido descansar con éxito" + "\033[0m")
        print(linea_punteada)
        seguir_jugando = input("¿Quieres jugar de nuevo? Si(1)/No(0):")
