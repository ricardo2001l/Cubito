import pygame
from pygame.locals import *

from Classes.resources import GREEN, RED


class Cubito(pygame.sprite.Sprite ):
	''' Clase del personaje principal '''

	def __init__(self, positionX, positionY, widthChar = 50, heightChar = 50, color = GREEN, speed = 7):
		pygame.sprite.Sprite.__init__(self)
		self.speed = speed
		self.positionX = positionX
		self.positionY = positionY

		self.color = color
		self.widthChar = widthChar
		self.heightChar = heightChar
		self.points = 0


		self.rectangle = pygame.Rect(self.positionX, self.positionY, self.widthChar, self.heightChar)



	def draw(self, surface, positionX, positionY):

		self.rectangle.centerx = positionX
		self.rectangle.centery = positionY

		centerX = self.widthChar / 2
		centerY = self.heightChar / 2
		self.rectangle.centerx -= centerX
		self.rectangle.centery -= centerY



		pygame.draw.rect(surface, self.color, self.rectangle)


class Enemy(Cubito):
	''' Clase del personaje enemigo '''
	def __init__(self, positionX, positionY, widthChar = 30, heightChar = 30, speed = 5, color = RED):
		
		Cubito.__init__(self, positionX, positionY, widthChar, heightChar, color, speed)
