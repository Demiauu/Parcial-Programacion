import pygame
import configuracion.audio as audio
from configuracion.menu import *
from configuracion.constantes import *
from configuracion.preguntas import *
from configuracion.funciones import *

pygame.init()
pygame.display.set_caption("League of Quiz")
icono = pygame.image.load("imagenes/icono.png")
pygame.display.set_icon(icono)
pantalla = pygame.display.set_mode(VENTANA)
corriendo = True

sonido_click = pygame.mixer.Sound("sonidos/click.mp3")
sonido_clicks = pygame.mixer.Sound.set_volume(sonido_click,0.3)
sonido_error = pygame.mixer.Sound("sonidos/error.mp3")
sonido_errores = pygame.mixer.Sound.set_volume(sonido_error,0.06)

datos_juego = {"puntuacion":0,"vidas":CANTIDAD_VIDAS,"nombre":"","volumen_juego":25}

Reloj = pygame.time.Clock()

ventana_actual = "menu"

#musica del juego. 👻
audio.musica(ventana_actual,datos_juego)

while corriendo:
    Reloj.tick(FPS)  
    cola_eventos = pygame.event.get()

    #eventos 
    if ventana_actual == "menu":
        ventana_actual = mostrar_menu(pantalla,cola_eventos)
    elif ventana_actual == "juego":
        pass
    elif ventana_actual == "opciones":
        pass
    elif ventana_actual == "ranking":
        pass
    elif ventana_actual == "salir":
        corriendo = False
        
    pygame.display.flip()
pygame.quit()
