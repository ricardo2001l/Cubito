'''Un juego simple, en el que tienes que recoger todos los puntos para ganar.
Pero cuidado! Que no te toquen los enemigos :)'''

import pygame, sys
from pygame.locals import *
from random import randint

from Classes import *

BLANCO = (255, 255, 255)
VERDE = (76, 201, 34)
AMARILLO = (217, 232, 53)
GRIS = (185, 186, 176)
NEGRO = (0, 0, 0)

ancho = 1080
alto = 480


def principal():
	''' - algunas sentencis necesarias para que funcione el juego 

	- creacion de objetos (personajes, puntos y otros de pygame)

	- El bucle principal de este juego, se encarga de revisar los eventos, la logica del juego
	, actualizar cada dibujo e imprimirlos
	'''

	pygame.init()
	ventana = pygame.display.set_mode((ancho, alto))
	pygame.display.set_caption('Cubito - Un simple juego')

	icono = pygame.image.load('imagenes/icono.png')
	pygame.display.set_icon(icono)

	reloj = pygame.time.Clock()
	pygame.key.set_repeat(True)

	jugador = personajes.Cubito(ancho/2, alto/2)
	enemigo = personajes.Enemigo(0, 0)
	listaPuntos = movimiento.crearObjetos(ventana, 10, 20, puntos.Puntos)

	enemigo.posicionX, enemigo.posicionY = movimiento.randomPos(enemigo, jugador, 20)
	
	fuente = pygame.font.SysFont('Arial', 20)
	fuenteGrande = pygame.font.SysFont('Arial', 30)

	lost = False

	while True:
		#EVENTOS
		for evento in pygame.event.get():
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()
			if evento.type == KEYDOWN:
				if evento.key == K_r:
					pygame.key.set_repeat(False)

					enemigo.posicionX, enemigo.posicionY = movimiento.randomPos(enemigo, jugador, 20)
					listaPuntos = movimiento.crearObjetos(ventana, 10, 20, puntos.Puntos)

					lost = False
					jugador.puntos = 0

					pygame.key.set_repeat(True)
			

		#LOGICA
		jugador.posicionX, jugador.posicionY = movimiento.update(jugador.posicionX, jugador.posicionY, jugador)

		enemigo.posicionX, enemigo.posicionY = movimiento.atraido(enemigo, jugador, 15)

		


		#DIBUJO
		ventana.fill(GRIS)
		if not lost and len(listaPuntos) > 0:
			jugador.dibujar(ventana, jugador.posicionX, jugador.posicionY)
			enemigo.dibujar(ventana, enemigo.posicionX, enemigo.posicionY)
			
			textoPuntos = fuente.render('Puntos: ', 0, AMARILLO)
			ventana.blit(textoPuntos, (10, 10))

			textoCantidad = fuente.render(str(jugador.puntos), 0, NEGRO)
			ventana.blit(textoCantidad, (10, 35))


		elif lost:
			diseno.textoCentrado('Has Perdido!', ventana, fuenteGrande, True)
			diseno.textoCentrado('Si quieres volver a jugar, presiona R', ventana, fuente, True, 0, 35)

			diseno.textoCentrado('Puntos:', ventana, fuente, False, 0, 70)
			diseno.textoCentrado(jugador.puntos, ventana, fuente, False, 0, 85)


		

		if len(listaPuntos) > 0:
			for punto in listaPuntos:
				
				if jugador.rectangulo.colliderect(punto.rectangulo):
					jugador.puntos += punto.cantidad

					listaPuntos.remove(punto)
				else:
					punto.dibujar()
		else:
			diseno.textoCentrado('Has Ganado!', ventana, fuenteGrande, True)
			diseno.textoCentrado('Si quieres volver a jugar, presiona R', ventana, fuente, True, 0, 35)

			diseno.textoCentrado('Puntos:', ventana, fuente, False, 0, 70)
			diseno.textoCentrado(jugador.puntos, ventana, fuente, False, 0, 85)

			
		if not lost:
			if enemigo.rectangulo.colliderect(jugador.rectangulo):
				lost = True
				
		pygame.display.update()


		#ACTUALIZACIONES
		reloj.tick(60)


principal()
