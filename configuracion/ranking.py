import pygame
from .constantes import *
from .funciones import mostrar_texto,crear_boton,cambiar_boton

pygame.init()
#guarde la imagen en una variable para despues cambiarle el tamaño con .transform.scale 👻
fondo_original = pygame.image.load("imagenes/menu_raw.png")
fondo = pygame.transform.scale(fondo_original, (702,502))

fuente_menu = pygame.font.SysFont("Pixel Operator 8",30)

#creo los botones llamando a la funcion de crear botones👻
boton_atras = crear_boton((70,30),"imagenes/boton_atras.png")

def mostrar_ranking(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event]) -> str:
    """esta funcion dibuja el menu ranking al llamarla, recibe como primer parametro las dimensiones de la pantalla, 
    como segundo parametro la cola de eventos, devuelve un string. 👻"""
    
    retorno = "ranking"
    #manejo de eventos 👻
    for evento in cola_eventos:
        if evento.type == pygame.MOUSEMOTION:
            #se actualizan las imagenes dependiendo si el mouse está encima del botón o no 👻
            if boton_atras["rectangulo"].collidepoint(evento.pos):
                CLICK_ON_SOUND.play()
                cambiar_boton(boton_atras,"imagenes/boton_atras_on.png",(70,30),True)
            else:
                cambiar_boton(boton_atras,"imagenes/boton_atras_on.png",(70,30),False)
        #agrego la interacción de boton de atras 👻
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_atras["rectangulo"].collidepoint(evento.pos):
                retorno = "menu"
                #detiene la musica para reproducir nueva 👻.
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.stop()
                #se agrega el sonido de la constante 👻
                CLICK_SOUND_OUT.play()
        
    #////////////////////////////////////
        #evento quit
        if evento.type == pygame.QUIT:
            retorno = "salir"
    #actualizar el juego

    #dibujar fondo 
    pantalla.blit(fondo, (0,0))
    #dibujo el boton atras 👻
    boton_atras["rectangulo"] = pantalla.blit(boton_atras["superficie"],(10,10))

    return retorno
