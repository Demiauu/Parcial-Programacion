import pygame
from .constantes import *
from .funciones import mostrar_texto,crear_boton,cambiar_boton
from .estado import estado_boton
from .puntos import puntos

pygame.init()
#guarde la imagen en una variable para despues cambiarle el tamaño con .transform.scale 👻
fondo_original = pygame.image.load("imagenes/menu.jpg")
fondo = pygame.transform.scale(fondo_original, (702,502))

fuente_menu = pygame.font.SysFont("Pixel Operator 8",30)

#creo los botones llamando a la funcion de crear botones👻

boton_jugar = crear_boton(TAMAÑO_BOTON,"imagenes/boton_jugar.png")
boton_ranking = crear_boton(TAMAÑO_BOTON,"imagenes/boton_ranking.png")
boton_opciones = crear_boton(TAMAÑO_BOTON,"imagenes/boton_opciones.png")
boton_salir = crear_boton((70,30),"imagenes/boton_salir.png")
boton_mod = crear_boton((48,30),"imagenes/boton_mod.png")
boton_add = crear_boton((48,48),"imagenes/boton_add.jpg")

def mostrar_menu(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event]) -> str:
    """esta funcion dibuja el menu al llamarla, recibe como primer parametro las dimensiones de la pantalla, 
    como segundo parametro la cola de eventos, devuelve un string. 👻"""
    retorno = "menu"

    global estado_boton,PUNTOS,puntos

    #manejo de eventos 👻
    for evento in cola_eventos:
        if evento.type == pygame.MOUSEMOTION:
            #se actualizan las imagenes dependiendo si el mouse está encima del botón o no 👻
            if boton_jugar["rectangulo"].collidepoint(evento.pos):
                if estado_boton["bandera_boton"] == False:
                    CLICK_ON_SOUND.play()
                cambiar_boton(boton_jugar,"imagenes/boton_jugar_on.png",TAMAÑO_BOTON,True)
                estado_boton["bandera_boton"] = True
                puntos["puntaje"] = 0
                
            else:
                cambiar_boton(boton_jugar,"imagenes/boton_jugar_on.png",TAMAÑO_BOTON,False)
            
            if boton_opciones["rectangulo"].collidepoint(evento.pos):
                if estado_boton["bandera_boton"] == False:
                    CLICK_ON_SOUND.play()
                cambiar_boton(boton_opciones,"imagenes/boton_opciones_on.png",TAMAÑO_BOTON,True)
                estado_boton["bandera_boton"] = True
            else:
                cambiar_boton(boton_opciones,"imagenes/boton_opciones_on.png",TAMAÑO_BOTON,False)
                
            if boton_ranking["rectangulo"].collidepoint(evento.pos):
                if estado_boton["bandera_boton"] == False:
                    CLICK_ON_SOUND.play()
                cambiar_boton(boton_ranking,"imagenes/boton_ranking_on.png",TAMAÑO_BOTON,True)
                estado_boton["bandera_boton"] = True
            else:
                cambiar_boton(boton_ranking,"imagenes/boton_ranking_on.png",TAMAÑO_BOTON,False)
                
            if boton_mod["rectangulo"].collidepoint(evento.pos):
                cambiar_boton(boton_mod,"imagenes/boton_mod_on.png",(48,30),True)
            else:
                cambiar_boton(boton_mod,"imagenes/boton_mod_on.png",(48,30),False)
            if boton_salir["rectangulo"].collidepoint(evento.pos):
                cambiar_boton(boton_salir,"imagenes/boton_salir_on.png",(70,30),True)
                if estado_boton["bandera_boton"] == False:
                    CLICK_ON_SOUND.play()
                estado_boton["bandera_boton"] = True
            else:
                cambiar_boton(boton_salir,"imagenes/boton_salir_on.png",(70,30),False)
                estado_boton["bandera_boton"] = False

            
        #agrego la interacción de boton puntuaciones 👻
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_ranking["rectangulo"].collidepoint(evento.pos):
                retorno = "ranking"
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.stop()
                CLICK_SOUND.play()
        #agrego la interacción de boton de salir 👻
            elif boton_salir["rectangulo"].collidepoint(evento.pos):
                retorno = "salir"
        #agrego la interacción de boton de jugar 👻
            elif boton_jugar["rectangulo"].collidepoint(evento.pos):
                retorno = "jugar"
                #detiene la musica para reproducir nueva 👻.
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.stop()
                CLICK_SOUND.play()
            elif boton_mod["rectangulo"].collidepoint(evento.pos):
                retorno = "modificaciones"
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.stop()
                CLICK_SOUND.play()
            elif boton_add["rectangulo"].collidepoint(evento.pos):
                retorno = "agregar_pregunta"
                CLICK_SOUND.play()
        #Agrege el boton opciones para que funcione 🌹
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_opciones["rectangulo"].collidepoint(evento.pos):
                #detiene la musica para reproducir nueva 👻.
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.stop()
                retorno = "opciones"
                CLICK_SOUND.play()
    #////////////////////////////////////
        if evento.type == pygame.QUIT:
            retorno = "salir"
    #actualizar el juego

    #dibujo el fondo 👻
    pantalla.blit(fondo, (0,0))
    #dibujo los botones 👻
    boton_jugar["rectangulo"] = pantalla.blit(boton_jugar["superficie"],(250, 282))
    boton_ranking["rectangulo"] = pantalla.blit(boton_ranking["superficie"],(15,350))
    boton_opciones["rectangulo"] = pantalla.blit(boton_opciones["superficie"],(486,350))
    boton_salir["rectangulo"] = pantalla.blit(boton_salir["superficie"],(318, 400))
    boton_mod["rectangulo"] = pantalla.blit(boton_mod["superficie"],(634,20))
    boton_add["rectangulo"] = pantalla.blit(boton_add["superficie"],(20,20))

    return retorno