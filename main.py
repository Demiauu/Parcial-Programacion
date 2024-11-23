import pygame
from constantes import *
from preguntas import *
from funciones import *

pygame.init()
pygame.display.set_caption("League of Quiz")
icono = pygame.image.load("icono.png")
pygame.display.set_icon(icono)
pantalla = pygame.display.set_mode(VENTANA)
corriendo = True

sonido_click = pygame.mixer.Sound("click.mp3")
sonido_clicks = pygame.mixer.Sound.set_volume(sonido_click,0.3)
sonido_error = pygame.mixer.Sound("error.mp3")
sonido_errores = pygame.mixer.Sound.set_volume(sonido_error,0.06)

pygame.mixer.init()
pygame.mixer.music.load("musica.mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play()
pygame.mixer.music.play(-1)

datos_juego = {"puntuacion":0,"vidas":CANTIDAD_VIDAS,"nombre":"","volumen juego":100}

Reloj = pygame.time.Clock()

ventana_actual = "menu"
while corriendo:
    Reloj.tick(FPS)  
    cola_eventos = pygame.event.get()

    if ventana_actual == "menu":
        pass
    elif ventana_actual == "juego":
        pass
    elif ventana_actual == "opciones":
        pass
    elif ventana_actual == "ranking":
        pass
    elif ventana_actual == "salir":
        corriendo = False
pygame.quit()
