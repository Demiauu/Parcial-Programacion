import pygame
import configuracion.audio as audio
from configuracion.menu import *
from configuracion.constantes import *
from configuracion.preguntas import *
from configuracion.funciones import *
from configuracion.opciones import *

pygame.init()
pygame.display.set_caption("League of Quiz")
icono = pygame.image.load("imagenes/icono.png")
pygame.display.set_icon(icono)
pantalla = pygame.display.set_mode(VENTANA)
corriendo = True

datos_juego = {"puntuacion":0,"vidas":CANTIDAD_VIDAS,"nombre":"","volumen_juego":100,"volumen_clicks":100}

Reloj = pygame.time.Clock()

ventana_actual = "menu"

#musica del juego. 👻
audio.musica(ventana_actual,datos_juego)

while corriendo:
    Reloj.tick(FPS)  
    cola_eventos = pygame.event.get()
    pantalla.fill(COLOR_BLANCO)
    #eventos 
    if ventana_actual == "menu":
        ventana_actual = mostrar_menu(pantalla,cola_eventos)
    elif ventana_actual == "jugar":
        pass
    #Con esto muestro las opciones para configurar el sonido 🌹
    elif ventana_actual == "opciones":
        ventana_actual = mostrar_opciones(pantalla,cola_eventos,datos_juego)
    elif ventana_actual == "ranking":
        pass
    elif ventana_actual == "salir":
        corriendo = False

    pygame.display.flip()
pygame.quit()
