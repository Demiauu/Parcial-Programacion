import pygame
from .constantes import *
from .funciones import *

# Se agrego el boton de controles en opciones.🌹

pygame.init()

fondo_original4 = pygame.image.load("imagenes/controles.png")
fondo = pygame.transform.scale(fondo_original4, (702,502))

fuente_boton = pygame.font.SysFont("Pixel Operator 8",11)
fuente_volumen = pygame.font.SysFont("Pixel Operator 8",20)

#creamos el boton volver👻
boton_volver = crear_boton((70,30),"imagenes/boton_atras.png")

def mostrar_controles(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event]) -> str:
    retorno = "controles"

    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_volver["rectangulo"].collidepoint(evento.pos):
                CLICK_SOUND.play()
                retorno = "opciones"
        #agregamos la interaccion de mouse on en el boton atras👻
        elif evento.type == pygame.MOUSEMOTION:
            if boton_volver["rectangulo"].collidepoint(evento.pos):
                cambiar_boton(boton_volver,"imagenes/boton_atras_on.png",(70,30),True)
            else:
                cambiar_boton(boton_volver,"imagenes/boton_atras_on.png",(70,30),False)

    pantalla.blit(fondo, (0,0))

    boton_volver["rectangulo"] = pantalla.blit(boton_volver["superficie"],(10,10))

    return retorno