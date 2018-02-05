#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Un juego simple, en el que tienes que recoger todos los puntos para ganar.
Pero cuidado! Que no te toquen los enemigos :)'''

import pygame, sys
from pygame.locals import *
from random import randint

from Classes import *
from Classes.resources import *

def principal():
	''' - algunas sentencis necesarias para que funcione el juego 

	- creacion de objetos (personajes, puntos y otros de pygame)

	- El bucle principal de este juego, se encarga de revisar los eventos, la logica del juego
	, actualizar cada dibujo e imprimirlos
	'''
	
	from Classes.resources import oldWidth, oldHeight



	pygame.init()
	window = pygame.display.set_mode((width, height), HWSURFACE|DOUBLEBUF|RESIZABLE)
	pygame.display.set_caption('Cubito - Un simple juego')

	icon = pygame.image.load('images/icon.png')
	pygame.display.set_icon(icon)

	clock = pygame.time.Clock()
	pygame.key.set_repeat(True)

	player = characters.Cubito(width/2, height/2)
	enemy = characters.Enemy(0, 0)
	pointsList = movement.createObjects(window, 10, 20, points.Point)

	enemy.positionX, enemy.positionY = movement.randomPos(enemy, player)
	
	font = pygame.font.SysFont('Arial', 20)
	bigFont = pygame.font.SysFont('Arial', 30)


	lost = False


	while True:
		#EVENTOS
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

			if event.type == VIDEORESIZE:#ERROR TALVEZ
				# ACTUALIZANDO LOS GRAFICOS CUANDO SE REDIMENCIONA
				
				if event.dict["w"] != oldWidth:
					proportion = event.dict["w"] / float(oldWidth)

					event.dict["h"] *= proportion

					oldWidth = event.dict["w"]

				if event.dict["h"] != oldHeight:
					proportion = event.dict["h"] / float(oldHeight)

					event.dict["w"] *= proportion

					oldHeight = event.dict["h"]





				window = pygame.display.set_mode((int(event.dict["w"]), int(event.dict["h"])),  HWSURFACE|DOUBLEBUF|RESIZABLE)
				pygame.display.flip()
				
			if event.type == KEYDOWN:
				if event.key == K_r:
					pygame.key.set_repeat(False)

					enemy.positionX, enemy.positionY = movement.randomPos(enemy, player)
					pointsList = movement.createObjects(window, 10, 20, points.Point)

					lost = False
					player.points = 0

					pygame.key.set_repeat(True)
			

		#LOGICA
		player.positionX, player.positionY = movement.update(player.positionX, player.positionY, player)

		enemy.positionX, enemy.positionY = movement.attracted(enemy, player)

		


		#DIBUJO
		window.fill(GRAY)
		if not lost and len(pointsList) > 0:
			player.draw(window, player.positionX, player.positionY)
			enemy.draw(window, enemy.positionX, enemy.positionY)
			
			textPoints = font.render('Puntos: ', 0, YELLOW)
			window.blit(textPoints, (10, 10))

			textQuantity = font.render(str(player.points), 0, BLACK)
			window.blit(textQuantity, (10, 35))


		elif lost:
			desing.centeredText('Has Perdido!', window, bigFont, True)
			desing.centeredText('Si quieres volver a jugar, presiona R', window, font, True, 0, 35)

			desing.centeredText('Puntos:', window, font, False, 0, 70)
			desing.centeredText(player.points, window, font, False, 0, 85)


		

		if len(pointsList) > 0:
			for point in pointsList:
				
				if player.rectangle.colliderect(point.rectangle):
					player.points += point.quantity

					pointsList.remove(point)
				else:
					point.draw()
		else:
			desing.centeredText('Has Ganado!', window, bigFont, True)
			desing.centeredText('Si quieres volver a jugar, presiona R', window, font, True, 0, 35)

			desing.centeredText('Puntos:', window, font, False, 0, 70)
			desing.centeredText(player.points, window, font, False, 0, 85)

			
		if not lost:
			if enemy.rectangle.colliderect(player.rectangle):
				lost = True
				
		pygame.display.update()


		#ACTUALIZACIONES
		clock.tick(60)


principal()
