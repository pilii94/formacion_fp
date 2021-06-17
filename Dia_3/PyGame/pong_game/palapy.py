import sys, pygame
#cargamos las constantes
from pygame.locals import *
from funcionespy import *

# Constantes
#definimos las constantes de ancho y alto de la ventana
WIDTH = 640
HEIGHT = 480
 

#la clase Pala es casi idéntica a la clase Bola
class Pala(pygame.sprite.Sprite):
    '''le pasamos el parámetro x para usarlo en self.rect.centerx, 
    esto es debido a que necesitamos dos palas una en la parte izquierda y
     otra en la derecha, con el parámetro x definimos a que altura del eje x
      queremos colocar el Sprite. solo se mueve en el eje y, no definimos velocidad para el eje x'''
    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("images/pala.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = HEIGHT / 2
        self.speed = 0.5

    '''mover recibe self y time como el método actualizar de la bola y además recibe 
    el parámetro keys que es una lista con el valor 
    booleano de las teclas pulsadas'''
    def mover(self, time, keys):
        
        if self.rect.top >= 0: # comprobamos que la pala no se sale de la ventana.
            if keys[K_UP]: #tenemos presionada la tecla de la flecha hacia arriba
                self.rect.centery -= self.speed * time #disminuye el valor de centery haciendo que la pala se mueva hacia arriba
        if self.rect.bottom <= HEIGHT: # comprobamos que la pala no se sale de la ventana.
            if keys[K_DOWN]: #tenemos presionada la tecla de la flecha hacia abajo
                self.rect.centery += self.speed * time #aumenta el valor de centery haciendo que la pala se mueva hacia abajo
    

    #lograr que la pala se mueva para golpear la bola
    def ia(self, time, ball):
        #comprobamos que la pelota se este moviendo hacia la pala de la cpu
        if ball.speed[0] >= 0 and ball.rect.centerx >= WIDTH/2:
            if self.rect.centery < ball.rect.centery: #si la pala está más arriba que que la pelota
                self.rect.centery += self.speed * time #mueve la pala de la cpu hacia abajo.
            if self.rect.centery > ball.rect.centery:
                self.rect.centery -= self.speed * time
 