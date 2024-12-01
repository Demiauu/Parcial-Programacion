import pygame
from .constantes import *
from .funciones import crear_boton, cambiar_boton

pygame.init()

fondo_original = pygame.image.load("imagenes/comodines.png")
fondo = pygame.transform.scale(fondo_original, (702,502))

fuente = pygame.font.SysFont("Pixel Operator 8",30)

#creo los botones llamando a la funcion de crear botones👻
boton_bomba = crear_boton(TAMAÑO_COMODINES,"imagenes/bomba.png")
boton_doble_chance = crear_boton((121,122),"imagenes/doble_chance.png")
boton_x2 = crear_boton((135,46),"imagenes/x2.png")
boton_pasar = crear_boton((144,46),"imagenes/next.png")

def mostrar_comodines(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event]) -> str:
    """esta funcion dibuja el menu de comodines al llamarla, recibe como primer parametro las dimensiones de la pantalla, 
    como segundo parametro la cola de eventos, devuelve un string. 👻"""
    
    retorno = "comodines"

    for evento in cola_eventos:
        if evento.type == pygame.KEYDOWN:
        #con esto al darle espacio vuelve a juego 👻
            if evento.key == pygame.K_SPACE:
                print("gag")
                retorno = "jugar"
                SONIDO_MENU_COMODINES_OUT.play()
        #metemos la logica de los botones 👻
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_bomba["rectangulo"].collidepoint(evento.pos):
                retorno = "jugar"
                SONIDO_BOMBA.play()
            elif boton_doble_chance["rectangulo"].collidepoint(evento.pos):
                retorno = "jugar"
                DOBLE_CHANCE.play()
            elif boton_x2["rectangulo"].collidepoint(evento.pos):
                retorno = "jugar"
            elif boton_pasar["rectangulo"].collidepoint(evento.pos):
                retorno = "jugar"

        #evento quit 👻
        if evento.type == pygame.QUIT:
            retorno = "salir"
    
    #dibuja el fondo.👻
    pantalla.blit(fondo, (0,0))

    #dibujo los comodines 👻
    boton_bomba["rectangulo"] = pantalla.blit(boton_bomba["superficie"],(55,125))
    boton_doble_chance["rectangulo"] = pantalla.blit(boton_doble_chance["superficie"],(200,125))
    boton_x2["rectangulo"] = pantalla.blit(boton_x2["superficie"],(340,160))
    boton_pasar["rectangulo"] = pantalla.blit(boton_pasar["superficie"],(40,300))

    return retorno