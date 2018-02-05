import pygame
from pygame.locals import *

from Classes.resources import YELLOW

class Point(pygame.sprite.Sprite):
	''' Puntos que hacen que el jugador gane ''' 
	def __init__(self, surface, posX, posY, widthPoint = 10, heightPoint = 10, color = YELLOW, quantity = 10):
		pygame.sprite.Sprite.__init__(self)
		self.widthPoint = widthPoint
		self.heightPoint = heightPoint
		self.quantity = quantity
		self.color = color

		self.posX = posX
		self.posY = posY

		self.rectangle = pygame.Rect(posX, posY, widthPoint, heightPoint)

		self.surface = surface 

	def draw(self):
		pygame.draw.rect(self.surface, self.color,  self.rectangle)

