import pygame
from .constantes import *
from .funciones import mostrar_texto,crear_boton

pygame.init()
#guarde la imagen en una variable para despues cambiarle el tamaño con .transform.scale 👻
fondo_original = pygame.image.load("imagenes/menu.jpg")
fondo = pygame.transform.scale(fondo_original, (702,502))

fuente_menu = pygame.font.SysFont("Arial Narrow",30)

boton_jugar = crear_boton(TAMAÑO_BOTON,"imagenes/boton_jugar.png")
boton_ranking = crear_boton(TAMAÑO_BOTON,"imagenes/boton_ranking.png")
boton_opciones = crear_boton(TAMAÑO_BOTON,"imagenes/boton_opciones.png")
boton_salir = crear_boton((70,30),"imagenes/boton_salir.png")

def mostrar_menu(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event]) -> str:
    """esta funcion dibuja el menu al llamarla, recibe como primer parametro las dimensiones de la pantalla, como segundo parametro la cola de eventos, devuelve un string. 👻"""

    retorno = "menu"

    #manejo de eventos
    for evento in cola_eventos:
        # if evento.type == pygame.MOUSEMOTION:
        #     print(evento.pos)
        if evento.type == pygame.QUIT:
            retorno = "salir"
        #Agrege el boton opciones para que funcione 🌹
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_opciones["rectangulo"].collidepoint(evento.pos):
                retorno = "opciones"

    #dibujar fondo 
    pantalla.blit(fondo, (0,0))
    #botones 
    boton_jugar["rectangulo"] = pantalla.blit(boton_jugar["superficie"],(250, 282))
    boton_ranking["rectangulo"] = pantalla.blit(boton_ranking["superficie"],(15,350))
    boton_opciones["rectangulo"] = pantalla.blit(boton_opciones["superficie"],(486,350))
    boton_salir["rectangulo"] = pantalla.blit(boton_salir["superficie"],(318, 400))
    #texto botones
    #mostrar_texto(boton_jugar["superficie"],"JUGAR",(0,-40),fuente_menu,COLOR_BLANCO)
    #mostrar_texto(boton_ranking["superficie"],"PUNTUACIONES",(0,-40),fuente_menu,COLOR_BLANCO)
    #mostrar_texto(boton_opciones["superficie"],"OPCIONES",(0,-40),fuente_menu,COLOR_BLANCO)

    return retorno