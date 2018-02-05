import pygame
from pygame.locals import *
from random import randint

from Classes.resources import oldWidth, oldHeight
from Classes.resources import width, height



def moveDown(object):
	y = object.positionY
	y += object.speed

	if y >= height - object.heightChar : 
		y -= object.speed

	return y

def moveUp(object):
	y = object.positionY
	y -= object.speed

	if y <= 0:
		y += object.speed

	return y

def moveRight(object):
	x = object.positionX
	x += object.speed

	if x >= width - object.widthChar:
		x -= object.speed

	return x	

def moveLeft(object):
	x = object.positionX
	x -= object.speed
	if x <= 0: 
		x += object.speed

	return x

def update(x, y, object):
	''' Le da movimiento al objeto  que se le pasa con las flechas de direccion ''' 

	keys = pygame.key.get_pressed() 
	if keys[K_DOWN]: 
		y = moveDown(object)

	if keys[K_UP]:
		y = moveUp(object) 

	if keys[K_RIGHT]: 
		x = moveRight(object)

	if keys[K_LEFT]:
		x = moveLeft(object)

	return x, y


def attracted(objectAttracted, attractor, range = 15):
	''' acerca un objeto a otro '''
	x = objectAttracted.positionX
	y = objectAttracted.positionY

	if (objectAttracted.positionX >= attractor.positionX and \
		objectAttracted.positionX + range <= attractor.positionX) or \
		(objectAttracted.positionX <= attractor.positionX and \
		objectAttracted.positionX + range >= attractor.positionX) or\
		(objectAttracted.positionY <= attractor.positionX and \
		objectAttracted.positionX + range >= attractor.positionY) or\
		(objectAttracted.positionY >= attractor.positionY and \
		objectAttracted.positionY + range <= attractor.positionY):	


		if objectAttracted.positionX < attractor.positionX:
			x = moveRight(objectAttracted)
		
		if objectAttracted.positionX > attractor.positionX:
			x = moveLeft(objectAttracted)

		if objectAttracted.positionY < attractor.positionY:
			y = moveDown(objectAttracted)

		if objectAttracted.positionY > attractor.positionY:
			y = moveUp(objectAttracted)# ricardo!, ahora solo te falta dibujar con las variables de posicion al enemigo

	return x, y



def createObjects(surface, limit1, limit2, object, widthObj = 50, heightObj = 50):
	''' Crea objetos  en un lugar random dentro de dos limites '''

	listObjects = []
	quantityObjects = randint(limit1, limit2)

	for obj in range(quantityObjects):
		posX = randint(0, oldWidth - widthObj)
		posY = randint(0, oldHeight - heightObj)

		newObject = object(surface, posX, posY)
		listObjects.append(newObject)
	
	return listObjects

def randomPos(object, farFromObj, range = 20):
		object.positionX = randint(object.widthChar , width)
		object.positionY = randint(object.heightChar, height)

		while (object.positionX >= farFromObj.positionX and \
			object.positionX + range <= farFromObj.positionX) or \
			(object.positionX <= farFromObj.positionX and \
			object.positionX + range >= farFromObj.positionX) or\
			(object.positionY <= farFromObj.positionX and \
			object.positionX + range >= farFromObj.positionY) or \
			(object.positionY >= farFromObj.positionY and \
			object.positionY + range <= farFromObj.positionY):
			
			object.positionX = randint(object.widthChar , oldWidth)
			object.positionY = randint(object.widthChar , oldHeight)

		return object.positionX, object.positionY