import pygame
from .constantes import *

pygame.mixer.init()

def musica(ventana_actual,datos_juego):
    """esta funcion recibe en que ventana estamos, los datos del juego y reproduce musica dependiendo en que ventana estamos ahora. 👻"""
    
    if ventana_actual == "menu":
        pygame.mixer.music.load("sonidos/League of Legends - Warriors.WAV")
    #Este elif es para que se escuche la musica adentro de opciones 🌹
    elif ventana_actual == "opciones":
        pygame.mixer.music.load("sonidos/musica.mp3")

    pygame.mixer.music.set_volume(datos_juego["volumen_juego"]/100)
    pygame.mixer.Sound.set_volume(SONIDO_CLICK,datos_juego["volumen_clicks"]/100)
    pygame.mixer.music.play(-1)
