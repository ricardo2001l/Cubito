import pygame
from pygame.locals import *
from Classes import *

BLANCO = (255, 255, 255)
VERDE = (76, 201, 34)
AMARILLO = (217, 232, 53)
GRIS = (185, 186, 176)
NEGRO = (0, 0, 0)

ancho = 1080
alto = 480


def textoCentrado(string, superficie, fuente, Antialias = False, distanciaX = 0, distanciaY = 0, color = NEGRO):
	'''Escribe un texto en el centro  de la pantalla (con una distancia de este, por defecto 0) '''

	texto = fuente.render(str(string), True, color)

	rectanguloTexto = texto.get_rect()

	rectanguloTexto.centerx = superficie.get_rect().centerx + distanciaX
	rectanguloTexto.centery = superficie.get_rect().centery + distanciaY
	superficie.blit(texto, rectanguloTexto)
