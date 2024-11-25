import pygame
from configuracion import (
    audio,
    menu,
    jugar,
    pausa,
    constantes,
    preguntas,
    funciones,
    opciones,
    ranking
)

pygame.init()
pygame.display.set_caption("League of Quiz")
icono = pygame.image.load("imagenes/icono.png")
pygame.display.set_icon(icono)

pantalla = pygame.display.set_mode(constantes.VENTANA)
corriendo = True

datos_juego = {"puntuacion":0,
               "vidas":constantes.CANTIDAD_VIDAS,
               "nombre":"",
               "volumen_juego":100,"volumen_clicks":100}

Reloj = pygame.time.Clock()

ventana_actual = "menu"

while corriendo:
    Reloj.tick(constantes.FPS)  
    cola_eventos = pygame.event.get()
    pantalla.fill(constantes.COLOR_BLANCO)
    #se agrega el menu principal 👻
    if ventana_actual == "menu":
        ventana_actual = menu.mostrar_menu(pantalla,cola_eventos)
        audio.reproducir_musica(ventana_actual,datos_juego)
    #se agrega la ventana jugar 👻
    elif ventana_actual == "jugar":
        ventana_actual = jugar.mostrar_jugar(pantalla,cola_eventos)
        audio.reproducir_musica(ventana_actual,datos_juego)
    elif ventana_actual == "pausa":
        ventana_actual = pausa.mostrar_pausa(pantalla,cola_eventos)
    #Con esto muestra las opciones para configurar el sonido 🌹
    elif ventana_actual == "opciones":
        ventana_actual = opciones.mostrar_opciones(pantalla,cola_eventos,datos_juego)
        #se escuche otra musica adentro de opciones 🌹
        audio.reproducir_musica(ventana_actual,datos_juego)
    #se agrega el ranking 👻
    elif ventana_actual == "ranking":
        ventana_actual = ranking.mostrar_ranking(pantalla,cola_eventos)
    elif ventana_actual == "salir":
        corriendo = False

    pygame.display.flip()
pygame.quit()