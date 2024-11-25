import pygame 
from .constantes import *
from .funciones import mostrar_texto, crear_boton, cambiar_boton

pygame.init()
#guarde la imagen en una variable para despues cambiarle el tamaño con .transform.scale 👻
fondo_original = pygame.image.load("imagenes/jugar_raw.png")
fondo = pygame.transform.scale(fondo_original, (702,502))

fuente_menu = pygame.font.SysFont("Arial Narrow",30)

#creo los botones llamando a la funcion de crear botones👻

def mostrar_jugar(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event]) -> str:
    """esta funcion dibuja el menu jugar al llamarla, recibe como primer parametro las dimensiones de la pantalla, 
    como segundo parametro la cola de eventos, devuelve un string. 👻"""

    retorno = "jugar"
    #manejo de eventos 👻
    for evento in cola_eventos:
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                retorno = "pausa"
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
        if evento.type == pygame.MOUSEMOTION:
            #se actualizan las imagenes dependiendo si el mouse está encima del botón o no 👻
            pass

        #////////////////////////////////////
        #evento quit
        if evento.type == pygame.QUIT:
            retorno = "salir"
    #actualizar el juego

    #dibujar fondo 👻
    pantalla.blit(fondo, (0,0))
    return retorno