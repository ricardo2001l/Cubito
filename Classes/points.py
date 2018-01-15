import pygame
from pygame.locals import *

WHITE = (255, 255, 255)
GREEN = (76, 201, 34)
YELLOW = (217, 232, 53)
GRAY = (185, 186, 176)
BLACK = (0, 0, 0)

width = 1080
height = 720

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

