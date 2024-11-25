import pygame
from .constantes import *
from .funciones import *

# Se agrego el boton de controles en opciones.🌹

pygame.init()

fondo_original4 = pygame.image.load("imagenes/GaTstotW8AAlBrF.png")
fondo = pygame.transform.scale(fondo_original4, (702,502))

fuente_boton = pygame.font.SysFont("Pixel Operator 8",20)
fuente_volumen = pygame.font.SysFont("Pixel Operator 8",50)

boton_volver = {}
boton_volver["superficie"] = pygame.Surface(TAMAÑO_BOTON_VOLVER)
boton_volver["rectangulo"] = boton_volver["superficie"].get_rect()
boton_volver["superficie"].fill(COLOR_AZUL)

def mostrar_controles(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event]) -> str:
    retorno = "controles"

    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_volver["rectangulo"].collidepoint(evento.pos):
                CLICK_SOUND.play()
                retorno = "opciones"

    pantalla.blit(fondo, (0,0))

    boton_volver["rectangulo"] = pantalla.blit(boton_volver["superficie"],(10,10))
    mostrar_texto(boton_volver["superficie"],"Volver",(15,15),fuente_boton,COLOR_BLANCO)
    mostrar_texto(pantalla,f"CONTROLES",(310,150),fuente_volumen,COLOR_BLANCO)
    mostrar_texto(pantalla,f"Escape = Pausa",(310,260),fuente_volumen,COLOR_BLANCO)
    mostrar_texto(pantalla,f"B = Comodines",(310,300),fuente_volumen,COLOR_BLANCO)
    mostrar_texto(pantalla,f"Flechas = Ajustar volumen (en opciones)",(310,340),fuente_volumen,COLOR_BLANCO)

    return retorno