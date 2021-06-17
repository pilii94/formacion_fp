#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Source:  http://razonartificial.com/2010/02/pygame-8-inteligencia/

#importamos pygame y los módulos que hacen falta
import sys, pygame
from funcionespy import *
from bolapy import *
from palapy import *
from pygame.locals import *
 


def main():
    #creamos la ventana del juego
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pruebas Pygame")
    
    #cargamos imagen del fondo
    background_image = load_image('images/fondo_pong.png')

    #cargamos la bola 
    bola = Bola()

    #cargamos las palas:
    pala_jug = Pala(30) #30 px del borde derecho de la ventana
    pala_cpu = Pala(WIDTH - 30)

    #creamos un reloj que controle el tiempo del juego, para situar la bola en el espacio
    clock = pygame.time.Clock()
    puntos = [0, 0]

    # bucle infinito, que será el bucle del juego
    while True:

        #cuanto tiempo pasa cada vez que se ejecuta una iteración del bucle
        #framerate=60, con él nos aseguramos de que el juego corre igual en todos los ordenadores
        time = clock.tick(60)
        # keys tiene qué teclas se pulsan
        keys = pygame.key.get_pressed()
        #si queremos cerrar la ventana  eja de ejecutarse el bucle infinito
        #pygame.event.get() es una lista interna de Pygame con los eventos que se están ejecutando
        for eventos in pygame.event.get():
            #comprobamos si el tipo de evento es igual a QUIT
            if eventos.type == QUIT:
                #cerramos ventana
                sys.exit(0)


        #debemos actualizar la posición de bola y palas antes de actualizarlas en la ventana
        puntos = bola.actualizar(time, pala_jug, pala_cpu, puntos)
        pala_jug.mover(time, keys)
        pala_cpu.ia(time, bola)


        #recogemos la puntuación
        p_jug, p_jug_rect = texto(str(puntos[0]), WIDTH/4, 40)
        p_cpu, p_cpu_rect = texto(str(puntos[1]), WIDTH-WIDTH/4, 40)


        #definimos que imagen poner de fondo y en que posición 
        screen.blit(background_image, (0, 0))
        #actualizamos puntos en la ventana
        screen.blit(p_jug, p_jug_rect)
        screen.blit(p_cpu, p_cpu_rect)
        #posicionamos la bola en nuestra ventana
        screen.blit(bola.image, bola.rect)
        # actualizamos la pala
        screen.blit(pala_jug.image, pala_jug.rect)
        screen.blit(pala_cpu.image, pala_cpu.rect)

        # actualizar toda la ventana para que se muestren los cambios que han sucedido
        pygame.display.flip()
    return 0
 
if __name__ == '__main__':
    #inicializamos pygame
    pygame.init()
    main()
