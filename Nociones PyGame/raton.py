# -*- coding: utf-8 -*-

import pygame, sys
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS

# Variables de juego
pygame.init()
clock = pygame.time.Clock()

windowWidth = 800
windowHeight = 800

surface = pygame.display.set_mode((windowWidth, windowHeight))

pygame.display.set_caption('Pruebas de ratón en PyGame')

# Variables referentes al ratón
mousePosition = None
mousePressed = False

# Variables para el cuadrado que será el actor de la escena
squareSize = 40
squareColor = (0, 255, 0)
squareX = windowWidth / 2
squareY = windowHeight - squareSize
draggingSquare = False
gravity = 9.81

def checkBounds():

	global squareColor, squareX, squareY, draggingSquare

	if mousePressed == True:
		# Comprobamos que el ratón está colocado sobre el cuadrado que hemos definido
		if mousePosition[0] > squareX and mousePosition[0] < squareX + squareSize:

			if mousePosition[1] > squareY and mousePosition[1] < squareY + squareSize:

				draggingSquare = True
				pygame.mouse.set_visible(0)

	else :
		squareColor = (255,0,0)
		pygame.mouse.set_visible(1)
		draggingSquare = False

def checkGravity():

	global gravity, squareY, squareSize, windowHeight

	# Comprobamos la posición de nuestro cuadrado
	if squareY < windowHeight - squareSize and mousePressed == False:
		squareY += gravity
		gravity = gravity * 1.1
	else :
		squareY = windowHeight - squareSize
		gravity = 9.81

def drawSquare():

	global squareColor, squareX, squareY, draggingSquare

	if draggingSquare == True:

		squareColor = (0, 0, 255)
		squareX = mousePosition[0] - squareSize / 2
		squareY = mousePosition[1] - squareSize / 2

	pygame.draw.rect(surface, squareColor, (squareX, squareY, squareSize, squareSize))

# How to quit our program
def quitGame():
	pygame.quit()
	sys.exit()

while True:

	mousePosition = pygame.mouse.get_pos()

	surface.fill((190,190,190))

	# Comprobamos si estamos pulsando el ratón
	if pygame.mouse.get_pressed()[0] == True:
		mousePressed = True
	else :
		mousePressed = False

	checkBounds() #Si el ratón está pulsado comprobamos que esté sobre el cuadrado para levantarlo
	checkGravity() # Comprobamos si el cuadrado está en el aire para hacerlo caer
	drawSquare() # Dibujamos el cuadrado donde esté nuestro ratón

	clock.tick(60) # Limitamos el programa a 60 fps
	pygame.display.update()

	for event in GAME_EVENTS.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				quitGame()
		if event.type == GAME_GLOBALS.QUIT:
			quitGame()
