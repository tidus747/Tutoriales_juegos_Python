from __future__ import print_function
from Caballero import Caballero
from ErrorUnidadJuego import GameUnitError

if __name__ == '__main__':
    print("Creando a un caballero..")
    knight = Caballero("Sir Bar")
    knight.Medidor_salud = 10
    knight.mostrar_salud()
    try:
        knight.curar(curado_por=100, curacion_completa=False)
    except GameUnitError as e:
        print(e)
        print(e.error_message)

    knight.mostrar_salud()
