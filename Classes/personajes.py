import pygame
from pygame.locals import *


BLANCO = (255, 255, 255)
VERDE = (76, 201, 34)
AMARILLO = (217, 232, 53)
GRIS = (185, 186, 176)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)

ancho = 1080
alto = 480


class Cubito(pygame.sprite.Sprite ):
	''' Clase del personaje principal '''

	def __init__(self, posicionX, posicionY, color = VERDE, velocidad = 7, tamano = 50):
		pygame.sprite.Sprite.__init__(self)
		self.velocidad = velocidad
		self.posicionX = posicionX
		self.posicionY = posicionY

		self.color = color
		self.tamano = tamano
		self.puntos = 0

		self.rectangulo = pygame.Rect(self.posicionX, self.posicionY, tamano, tamano)




	def dibujar(self, superficie, posicionX, posicionY):

		self.rectangulo.centerx = posicionX
		self.rectangulo.centery = posicionY  

		centro = self.tamano / 2
		self.rectangulo.centerx -= centro
		self.rectangulo.centery -= centro



		pygame.draw.rect(superficie, self.color, self.rectangulo)


class Enemigo(Cubito):
	''' Clase del personaje enemigo '''
	def __init__(self, posicionX, posicionY, velocidad = 5, tamano = 30, color = ROJO):
		
		Cubito.__init__(self, posicionX, posicionY, color, velocidad, tamano)
