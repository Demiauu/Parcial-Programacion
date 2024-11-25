import pygame 
from .constantes import *
from .funciones import mostrar_texto, crear_boton, cambiar_boton

pygame.init()
#guarde la imagen en una variable para despues cambiarle el tamaño con .transform.scale 👻
fondo_original = pygame.image.load("imagenes/pausa_raw.png")
fondo = pygame.transform.scale(fondo_original, (702,502))

fuente_menu = pygame.font.SysFont("Pixel Operator 8",30)

#creo los botones llamando a la funcion de crear botones👻
boton_resumen = crear_boton(TAMAÑO_BOTON_PAUSA,"imagenes/boton_resumen_pausa.png")
boton_opciones = crear_boton(TAMAÑO_BOTON_PAUSA,"imagenes/boton_opciones_pausa.png")
boton_salir = crear_boton(TAMAÑO_BOTON_PAUSA,"imagenes/boton_salir_pausa.png")

def mostrar_pausa(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event]) -> str:
    """esta funcion dibuja el menu pausa al llamarla, recibe como primer parametro las dimensiones de la pantalla, 
    como segundo parametro la cola de eventos, devuelve un string. 👻"""

    retorno = "pausa"
    #manejo de eventos 👻
    for evento in cola_eventos:
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                retorno = "jugar"
                if not pygame.mixer.music.get_busy():
                    pygame.mixer.music.unpause()
        if evento.type == pygame.MOUSEMOTION:
            #se actualizan las imagenes dependiendo si el mouse está encima del botón o no 👻
            if boton_resumen["rectangulo"].collidepoint(evento.pos):
                cambiar_boton(boton_resumen,"imagenes/boton_resumen_pausa_on.png",TAMAÑO_BOTON_PAUSA,True)
            else:
                cambiar_boton(boton_resumen,"imagenes/boton_resumen_pausa_on.png",TAMAÑO_BOTON_PAUSA,False)
            if boton_opciones["rectangulo"].collidepoint(evento.pos):
                cambiar_boton(boton_opciones,"imagenes/boton_opciones_pausa_on.png",TAMAÑO_BOTON_PAUSA,True)
            else:
                cambiar_boton(boton_opciones,"imagenes/boton_opciones_pausa_on.png",TAMAÑO_BOTON_PAUSA,False)
            if boton_salir["rectangulo"].collidepoint(evento.pos):
                #CLICK_ON_SOUND.play()
                cambiar_boton(boton_salir,"imagenes/boton_salir_pausa_on.png",TAMAÑO_BOTON_PAUSA,True)
            else:
                cambiar_boton(boton_salir,"imagenes/boton_salir_pausa_on.png",TAMAÑO_BOTON_PAUSA,False)
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_resumen["rectangulo"].collidepoint(evento.pos):
                retorno = "jugar"
                #reproduce el sonido de click 👻
                CLICK_SOUND.play()
            elif boton_opciones["rectangulo"].collidepoint(evento.pos):
                retorno = "opciones"
                #si se está reproduciendo musica se detiene 👻
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.stop()
                #reproduce el sonido de click 👻
                CLICK_SOUND.play()
            elif boton_salir["rectangulo"].collidepoint(evento.pos):
                retorno = "menu"
                #si se está reproduciendo musica se detiene 👻
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.stop()
                #reproduce el sonido de click 👻
                CLICK_SOUND.play()
        
        #////////////////////////////////////
        #evento quit
        if evento.type == pygame.QUIT:
            retorno = "salir"
    #actualizar el juego

    #dibujar fondo 👻
    pantalla.blit(fondo, (0,0))
    #dibujo los botones 👻
    boton_resumen["rectangulo"] = pantalla.blit(boton_resumen["superficie"],(260, 40))
    boton_opciones["rectangulo"] = pantalla.blit(boton_opciones["superficie"],(260, 190))
    boton_salir["rectangulo"] = pantalla.blit(boton_salir["superficie"],(260, 340))

    return retorno