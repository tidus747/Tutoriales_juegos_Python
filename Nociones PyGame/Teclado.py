# -*- coding: utf-8 -*-

import pygame, sys
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS

# Variables de PyGame
pygame.init()
clock = pygame.time.Clock()

windowWidth = 800
windowHeight = 800

surface = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Pruebas de teclado en PyGame')

# Variables para el cuadrado
playerSize = 20;
playerX = (windowWidth / 2) - (playerSize / 2)
playerY = windowHeight - playerSize
playerVX = 1.0
playerVY = 0.0
jumpHeight = 25.0
moveSpeed = 1.0
maxSpeed = 10.0
gravity = 1.0

# Variables de teclado que vamos a utilizar
leftDown = False
rightDown = False
haveJumped = False

def move():

	global playerX, playerY, playerVX, playerVY, haveJumped, gravity

	# Movimiento izquierda
	if leftDown:
		#Si nos estamos moviendo a la derecha tenemos que invertir la dirección
		if playerVX > 0.0:
			playerVX = moveSpeed
			playerVX = -playerVX
		# Comprobamos que no nos salimos de la ventana
		if playerX > 0:
			playerX += playerVX

	# Movimento derecha
	if rightDown:
		# Si nos estamos movimento a la izquierda tenemos que invertir la dirección
		if playerVX < 0.0:
			playerVX = moveSpeed
		# Nos aseguramos de que no nos salimos de la ventana por la derecha
		if playerX + playerSize < windowWidth:
			playerX += playerVX

	if playerVY > 1.0:
		playerVY = playerVY * 0.9
	else :
		playerVY = 0.0
		haveJumped = False

	# Comprobamos si el cubo está en el aire
	if playerY < windowHeight - playerSize:
		playerY += gravity
		gravity = gravity * 1.1
	else :
		playerY = windowHeight - playerSize
		gravity = 1.0

	playerY -= playerVY

	# Sentencia para que nuestro personaje vaya acelerando 
	if playerVX > 0.0 and playerVX < maxSpeed or playerVX < 0.0 and playerVX > -maxSpeed:
		if haveJumped == False:
			playerVX = playerVX * 1.1

# Funcion para salir del juego
def quitGame():
	pygame.quit()
	sys.exit()

while True:

	surface.fill((190,190,190))

	pygame.draw.rect(surface, (255,0,0), (playerX, playerY, playerSize, playerSize))

	# Miramos los eventos que han ocurrido
	for event in GAME_EVENTS.get():

		if event.type == pygame.KEYDOWN:

			if event.key == pygame.K_LEFT:
				leftDown = True
			if event.key == pygame.K_RIGHT:
				rightDown = True
			if event.key == pygame.K_UP:
				if not haveJumped:
					haveJumped = True
					playerVY += jumpHeight
			if event.key == pygame.K_ESCAPE:
				quitGame()

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				leftDown = False
				playerVX = moveSpeed
			if event.key == pygame.K_RIGHT:
				rightDown = False
				playerVX = moveSpeed

		if event.type == GAME_GLOBALS.QUIT:
			quitGame()

	move()

	clock.tick(60)
	pygame.display.update()
