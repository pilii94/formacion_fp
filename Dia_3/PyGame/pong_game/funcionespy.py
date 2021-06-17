import sys, pygame
#cargamos las constantes
from pygame.locals import *


# Funciones
# ---------------------------------------------------------------------
#el método load image recibe  el nombre/ruta del archivo y si tiene parte transparente
def load_image(filename, transparent=False):

        image = pygame.image.load(filename)
        
        #convertimos la imagen al tipo interno de Pygame que hace que sea mucho más eficiente
        image = image.convert()
        if transparent:
                #obtenemos el color del pixel (0, 0) de la imagen (esquina superior izquierda)
                color = image.get_at((0,0))
                #lo definimos como color transparente de la imagen
                image.set_colorkey(color, RLEACCEL)
        return image

def texto(texto, posx, posy, color=(255, 255, 255)):
    # tipografía
    fuente = pygame.font.Font("images/DroidSans.ttf", 25)
    #pygame trata a todos los textos como Sprites
    salida = pygame.font.Font.render(fuente, texto, 1, color)
    salida_rect = salida.get_rect() #como con el resto de Sprites
    salida_rect.centerx = posx
    salida_rect.centery = posy
    return salida, salida_rect