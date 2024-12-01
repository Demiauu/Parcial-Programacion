import pygame
from .constantes import *
from .funciones import mostrar_texto,crear_boton,cambiar_boton
import random

#Todo este codigo es para que la ventana de opciones funcione bien.🌹

fondo_opciones = pygame.image.load("imagenes/pausa_raw.png")
fondo = pygame.transform.scale(fondo_opciones, (702,502))

pygame.init()

fuente_boton = pygame.font.SysFont("Pixel Operator 8",11)

comodin_segunda_oportunidad = {}
comodin_segunda_oportunidad["superficie"] = pygame.Surface(TAMAÑO_BOTON_VOLUMEN)
comodin_segunda_oportunidad["rectangulo"] = comodin_segunda_oportunidad["superficie"].get_rect()
comodin_segunda_oportunidad["superficie"].fill(COLOR_ROJO)
comodin_eliminar_dos = {}
comodin_eliminar_dos["superficie"] = pygame.Surface(TAMAÑO_BOTON_VOLUMEN)
comodin_eliminar_dos["rectangulo"] = comodin_eliminar_dos["superficie"].get_rect()
comodin_eliminar_dos["superficie"].fill(COLOR_ROJO)
comodin_doble_puntuacion = {}
comodin_doble_puntuacion["superficie"] = pygame.Surface(TAMAÑO_BOTON_VOLUMEN)
comodin_doble_puntuacion["rectangulo"] = comodin_doble_puntuacion["superficie"].get_rect()
comodin_doble_puntuacion["superficie"].fill(COLOR_ROJO)
comodin_saltar_pregunta = {}
comodin_saltar_pregunta["superficie"] = pygame.Surface(TAMAÑO_BOTON_VOLUMEN)
comodin_saltar_pregunta["rectangulo"] = comodin_saltar_pregunta["superficie"].get_rect()
comodin_saltar_pregunta["superficie"].fill(COLOR_ROJO)

boton_volver = crear_boton((70,30),"imagenes/boton_atras.png")

# la funcion detecta cada click de los botones para ajustar el volumen de los audios.🌹
def mostrar_comodines(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event]) -> str:
    retorno = "comodines"

    for evento in cola_eventos:

        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if comodin_segunda_oportunidad["rectangulo"].collidepoint(evento.pos):
                print(f"hola")
                CLICK_SOUND.play()
            elif comodin_eliminar_dos["rectangulo"].collidepoint(evento.pos):
                print(f"niggers")
                CLICK_SOUND.play()
            elif comodin_doble_puntuacion["rectangulo"].collidepoint(evento.pos):
                print(f"jaja")
                CLICK_SOUND.play()
            elif comodin_saltar_pregunta["rectangulo"].collidepoint(evento.pos):
                print(f"falopero")
                CLICK_SOUND.play()
            elif boton_volver["rectangulo"].collidepoint(evento.pos):
                retorno = "jugar"
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.stop()
                CLICK_SOUND_OUT.play()

    #dibuja el fondo.🌹
    pantalla.blit(fondo, (0,0))

    #dibujo el boton atras 👻
    boton_volver["rectangulo"] = pantalla.blit(boton_volver["superficie"],(10,10))

    comodin_segunda_oportunidad["rectangulo"] = pantalla.blit(comodin_segunda_oportunidad["superficie"],(583,150))
    comodin_eliminar_dos["rectangulo"] = pantalla.blit(comodin_eliminar_dos["superficie"],(20,150))
    comodin_doble_puntuacion["rectangulo"] = pantalla.blit(comodin_doble_puntuacion["superficie"],(583,240))
    comodin_saltar_pregunta["rectangulo"] = pantalla.blit(comodin_saltar_pregunta["superficie"],(20,240))

    mostrar_texto(comodin_segunda_oportunidad["superficie"],"Volumen +",(4,15),fuente_boton,COLOR_NEGRO)
    mostrar_texto(comodin_eliminar_dos["superficie"],"Volumen -",(4,15),fuente_boton,COLOR_NEGRO)
    mostrar_texto(comodin_doble_puntuacion["superficie"],"Volumen +",(4,15),fuente_boton,COLOR_NEGRO)
    mostrar_texto(comodin_saltar_pregunta["superficie"],"Volumen -",(4,15),fuente_boton,COLOR_NEGRO)

    return retorno