import pygame
from pygame.locals import *

BLANCO = (255, 255, 255)
VERDE = (76, 201, 34)
AMARILLO = (217, 232, 53)
GRIS = (185, 186, 176)
NEGRO = (0, 0, 0)

ancho = 1080
alto = 480

class Puntos(pygame.sprite.Sprite):
	''' Puntos que hacen que el jugador gane ''' 
	def __init__(self, superficie, x, y, tamano = 10, color = AMARILLO, cantidad = 10):
		pygame.sprite.Sprite.__init__(self)
		self.tamano = tamano
		self.cantidad = cantidad
		self.color = color

		self.x = x
		self.y = y

		self.rectangulo = pygame.Rect(x, y, tamano, tamano)

		self.superficie = superficie 

	def dibujar(self):
		pygame.draw.rect(self.superficie, self.color,  self.rectangulo)

