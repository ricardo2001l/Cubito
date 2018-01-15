import pygame
from pygame.locals import *
from random import randint

BLANCO = (255, 255, 255)
VERDE = (76, 201, 34)
AMARILLO = (217, 232, 53)
GRIS = (185, 186, 176)
NEGRO = (0, 0, 0)

ancho = 1080
alto = 480

def moverAbajo(objeto, alto):
	y = objeto.posicionY
	y += objeto.velocidad
	if y >= alto: 
		y -= objeto.velocidad

	return y

def moverArriba(objeto, alto):
	y = objeto.posicionY
	y -= objeto.velocidad
	if y <= 0 + objeto.tamano:
		y += objeto.velocidad

	return y

def moverDerecha(objeto, ancho):
	x = objeto.posicionX
	x += objeto.velocidad 
	if x >= ancho: 
		x -= objeto.velocidad

	return x	

def moverIzquierda(objeto, ancho):
	x = objeto.posicionX
	x -= objeto.velocidad
	if x <= 0 + objeto.tamano: 
		x += objeto.velocidad

	return x

def update(x, y, objeto):
	''' Le da movimiento al objeto  que se le pasa con las flechas de direccion ''' 

	keys = pygame.key.get_pressed() 
	if keys[K_DOWN]: 
		y = moverAbajo(objeto, alto)

	if keys[K_UP]: 
		y = moverArriba(objeto, alto)

	if keys[K_RIGHT]: 
		x = moverDerecha(objeto, ancho)

	if keys[K_LEFT]:
		x = moverIzquierda(objeto, ancho)

	return x, y


def atraido(objetoAtraido, atraedor, rango):
	''' acerca un objeto a otro '''
	x = objetoAtraido.posicionX
	y = objetoAtraido.posicionY
	if (objetoAtraido.posicionX >= atraedor.posicionX and \
		objetoAtraido.posicionX + rango <= atraedor.posicionX) or \
		(objetoAtraido.posicionX <= atraedor.posicionX and \
		objetoAtraido.posicionX + rango >= atraedor.posicionX) or\
		(objetoAtraido.posicionY <= atraedor.posicionX and \
		objetoAtraido.posicionX + rango >= atraedor.posicionY) or\
		(objetoAtraido.posicionY >= atraedor.posicionY and \
		objetoAtraido.posicionY + rango <= atraedor.posicionY):	


		if objetoAtraido.posicionX < atraedor.posicionX:
			x = moverDerecha(objetoAtraido, ancho)
		
		if objetoAtraido.posicionX > atraedor.posicionX:
			x = moverIzquierda(objetoAtraido, ancho)

		if objetoAtraido.posicionY < atraedor.posicionY:
			y = moverAbajo(objetoAtraido, alto)

		if objetoAtraido.posicionY > atraedor.posicionY:
			y = moverArriba(objetoAtraido, alto)# ricardo!, ahora solo te falta dibujar con las variables de posicion al enemigo

	return x, y



def crearObjetos(superficie, limite1, limite2, objeto, tamano = 50):
	''' Crea objetos  en un lugar random dentro de dos limites '''

	listaObjetos = []
	cantidadObjetos = randint(limite1, limite2)

	for obj in range(cantidadObjetos):
		posX = randint(0, ancho - tamano)
		posY = randint(0, alto - tamano)

		nuevoObjeto = objeto(superficie, posX, posY)
		listaObjetos.append(nuevoObjeto)
	
	return listaObjetos

def randomPos(objeto, alejarObj, rango):
		objeto.posicionX = randint(15 , ancho)
		objeto.posicionY = randint(15 , alto)

		while (objeto.posicionX >= alejarObj.posicionX and \
			objeto.posicionX + rango <= alejarObj.posicionX) or \
			(objeto.posicionX <= alejarObj.posicionX and \
			objeto.posicionX + rango >= alejarObj.posicionX) or\
			(objeto.posicionY <= alejarObj.posicionX and \
			objeto.posicionX + rango >= alejarObj.posicionY) or \
			(objeto.posicionY >= alejarObj.posicionY and \
			objeto.posicionY + rango <= alejarObj.posicionY):
			
			objeto.posicionX = randint(15 , ancho)
			objeto.posicionY = randint(15 , alto)

		return objeto.posicionX, objeto.posicionY
