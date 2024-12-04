import pygame
from configuracion import (
    audio,
    fin,
    menu,
    jugar,
    auxiliar,
    pausa,
    constantes,
    comodines,
    controles,
    opciones,
    modificaciones,
    ranking,
    funciones
)

pygame.init()
pygame.display.set_caption("League of Quiz")
icono = pygame.image.load("imagenes/icono.png")
pygame.display.set_icon(icono)

pantalla = pygame.display.set_mode(constantes.VENTANA)
corriendo = True

configuracion = funciones.leer_csv("configuracion\config.csv")

datos_juego =  {"puntuacion":0,
                "vidas":configuracion["vidas"],
                "nombre":"",
                "volumen_juego":100,"volumen_clicks":100}    

Reloj = pygame.time.Clock()

ventana_actual = "menu"

while corriendo:
    Reloj.tick(constantes.FPS)
    cola_eventos = pygame.event.get()
    #eventos 
    pantalla.fill(constantes.COLOR_BLANCO)
    #se agrega el menu principal 👻
    if ventana_actual == "menu":
        ventana_actual = menu.mostrar_menu(pantalla,cola_eventos)
        #se escuche otra musica adentro de menú.🌹
        audio.reproducir_musica(ventana_actual,datos_juego)
    #se agrega la ventana jugar 👻
    elif ventana_actual == "jugar":
    #Con esto muestra las opciones para configurar el sonido.🌹
        ventana_actual = auxiliar.mostrar_jugar(pantalla,cola_eventos)
        audio.reproducir_musica(ventana_actual,datos_juego)
    elif ventana_actual == "pausa":
        ventana_actual = pausa.mostrar_pausa(pantalla,cola_eventos)
    #Con esto muestra las opciones para configurar el sonido 🌹
    elif ventana_actual == "opciones":
        ventana_actual = opciones.mostrar_opciones(pantalla,cola_eventos,datos_juego)
        #se escuche otra musica adentro de opciones.🌹
        audio.reproducir_musica(ventana_actual,datos_juego)
    elif ventana_actual == "modificaciones":
        ventana_actual = modificaciones.mostrar_mod_menu(pantalla,cola_eventos,datos_juego)
        #se escuche otra musica adentro de opciones.🌹
        audio.reproducir_musica(ventana_actual,datos_juego)
    #se agrega el ranking 👻
    elif ventana_actual == "ranking":
        ventana_actual = ranking.mostrar_ranking(pantalla,cola_eventos)
        audio.reproducir_musica(ventana_actual,datos_juego)
    #Se agrego la pantalla de controles.🌹
    elif ventana_actual == "controles":
        ventana_actual = controles.mostrar_controles(pantalla,cola_eventos)
        audio.reproducir_musica(ventana_actual,datos_juego)
    elif ventana_actual == "comodines":
        ventana_actual = comodines.mostrar_comodines(pantalla,cola_eventos)
        audio.reproducir_musica(ventana_actual,datos_juego)
    elif ventana_actual == "fin_juego":
        ventana_actual = fin.mostrar_fin_juego(pantalla,cola_eventos)
        audio.reproducir_musica(ventana_actual,datos_juego)
    elif ventana_actual == "salir":
        corriendo = False

    pygame.display.flip()
pygame.quit()