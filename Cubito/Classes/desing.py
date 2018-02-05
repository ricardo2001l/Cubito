import pygame
from pygame.locals import *
from Classes.resources import BLACK


def centeredText(string, surface, font, Antialias = False, distanceX = 0, distanceY = 0, color = BLACK):
	'''Escribe un texto en el centro  de la pantalla (con una distancia de este, por defecto 0) '''

	text = font.render(str(string), True, color)

	textRectangle = text.get_rect()

	textRectangle.centerx = surface.get_rect().centerx + distanceX
	textRectangle.centery = surface.get_rect().centery + distanceY
	surface.blit(text, textRectangle)
