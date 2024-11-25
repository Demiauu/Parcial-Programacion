import pygame
from .constantes import *

def reproducir_musica(ventana_actual, datos_juego):
    """esta funcion recibe en que ventana estamos, los datos del juego y reproduce musica dependiendo en que ventana estamos ahora. 👻"""
    # si no está iniciado el mixer lo inicia 👻
    if not pygame.mixer.get_init():
        pygame.mixer.init()
    # selecciona la musica dependiendo de la ventana 👻
    if ventana_actual == "menu":
        ruta_musica = "sonidos/Warsongs_ Piercing Light (Mako Remix) wip.WAV"
        #utiliza el volumen designado para la musica y el sonido de los clicks 🌹
        pygame.mixer.Sound.set_volume(CLICK_SOUND,datos_juego['volumen_clicks'] / 100)
        pygame.mixer.Sound.set_volume(CLICK_ON_SOUND,datos_juego['volumen_clicks'] / 100)
        pygame.mixer.music.set_volume(datos_juego['volumen_juego'] / 100)
    elif ventana_actual == "opciones":
        ruta_musica = "sonidos/rift_base_sound.WAV"
        #utiliza el volumen designado para la musica y el sonido de los clicks 🌹
        pygame.mixer.Sound.set_volume(CLICK_SOUND,datos_juego['volumen_clicks'] / 100)
        pygame.mixer.Sound.set_volume(CLICK_ON_SOUND,datos_juego['volumen_clicks'] / 100)
        pygame.mixer.music.set_volume(datos_juego['volumen_juego'] / 100)
    elif ventana_actual == "jugar":
        ruta_musica = "sonidos/Ignite - Zedd.WAV"
        #utiliza el volumen designado para la musica y el sonido de los clicks 🌹
        pygame.mixer.Sound.set_volume(CLICK_SOUND,datos_juego['volumen_clicks'] / 100)
        pygame.mixer.Sound.set_volume(CLICK_ON_SOUND,datos_juego['volumen_clicks'] / 100)
        pygame.mixer.music.set_volume(datos_juego['volumen_juego'] / 100)
    elif ventana_actual == "ranking":
        ruta_musica = "sonidos/League of Legends - Warriors.WAV"
        #utiliza el volumen designado para la musica y el sonido de los clicks 🌹
        pygame.mixer.Sound.set_volume(CLICK_SOUND,datos_juego['volumen_clicks'] / 100)
        pygame.mixer.Sound.set_volume(CLICK_ON_SOUND,datos_juego['volumen_clicks'] / 100)
        pygame.mixer.music.set_volume(datos_juego['volumen_juego'] / 100)
    else:
        return  #si no hay musica sale
    #si la musica ya está encendida no hace nda 👻
    if pygame.mixer.music.get_busy():
        return
    #se carga la musica 👻
    pygame.mixer.music.stop()
    pygame.mixer.music.load(ruta_musica)
    pygame.mixer.music.play(-1)  # Reproduce en bucle