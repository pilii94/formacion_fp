import sys, pygame
#cargamos las constantes
from pygame.locals import *
from funcionespy import *
# Constantes
#definimos las constantes de ancho y alto de la ventana
WIDTH = 640
HEIGHT = 480
 
#la clase Bola y Pala heredan los métodos de la clase pygame.sprite.Sprite
class Bola(pygame.sprite.Sprite):

    #inicializamos la clase
    def __init__(self):
        #un Sprite es más que una imagen, es una superficie que puede interactuar, moverse y demás
        pygame.sprite.Sprite.__init__(self)
        #imagen de la pelota
        self.image = load_image("images/ball.png", True)
        #obtenemos un rectangulo con las dimensiones y posición de la imagen y se lo asignamos a self.rect
        #get_rect() tiene parámetros para posicionar y redimensionar nuestra imagen
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2
        self.speed = [0.5, -0.5]
    #controlamos el movimiento de la pelota con el método actualizar. Recibe el tiempo transcurrido
    def actualizar(self, time, pala_jug, pala_cpu,puntos):
        '''e=v*t establecemos que el centro de nuestro rectangulo en x 
        es el valor que tenía (self.rect.centerx) más (+=) la valocidad 
        a la que se mueve en el eje x (self.speed[0]) por (*) el tiempo t
        ranscurrido (time)'''
        self.rect.centerx += self.speed[0] * time
        self.rect.centery += self.speed[1] * time

        #PUNTOS: puntos[0] los puntos del jugador y en el puntos[1] los puntos de la cpu.
        if self.rect.left <= 0:
            puntos[1] += 1
        if self.rect.right >= WIDTH:
            puntos[0] += 1

        ''' establecemos que si la parte izquierda del rectángulo de la 
        bola es menor o igual a 0 o mayor o igual a el ancho de la pantalla (WIDTH), 
        es decir,  que este en el extremo izquierdo o derecho, la velocidad de x 
        (self.speed[0]) cambie de signo (-self.speed[0]) con esto conseguiremos 
        que vaya hacia el otro lado. Lo mismo con el eje y'''
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.speed[0] = -self.speed[0]
            self.rect.centerx += self.speed[0] * time
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed[1] = -self.speed[1]
            self.rect.centery += self.speed[1] * time
 
        #Saber si un Sprite colisiona con otro 
        if pygame.sprite.collide_rect(self, pala_jug):
            #en caso afirmativo cambiamos la dirección de la bola 
            self.speed[0] = -self.speed[0]
            self.rect.centerx += self.speed[0] * time
 
        if pygame.sprite.collide_rect(self, pala_cpu):
            self.speed[0] = -self.speed[0]
            self.rect.centerx += self.speed[0] * time
        return(puntos)

