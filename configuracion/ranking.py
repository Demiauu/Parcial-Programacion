import pygame
from .constantes import *
from .funciones import mostrar_texto,crear_boton,cambiar_boton,leer_csv_sin_cabecera
from .estado import estado_ranking

pygame.init()
#guarde la imagen en una variable para despues cambiarle el tamaño con .transform.scale 👻
fondo_original = pygame.image.load("imagenes/ranking.png")
fondo = pygame.transform.scale(fondo_original, (702,502))
fuente_top = pygame.font.SysFont("Pixel Operator 8",60)
fuente_menu = pygame.font.SysFont("Pixel Operator 8",20)
#creo los botones llamando a la funcion de crear botones👻
boton_atras = crear_boton((70,30),"imagenes/boton_atras.png")

def mostrar_ranking(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event]) -> str:
    """esta funcion dibuja el menu ranking al llamarla, recibe como primer parametro las dimensiones de la pantalla, 
    como segundo parametro la cola de eventos, devuelve un string. 👻"""
    
    retorno = "ranking"

    puntajes = leer_csv_sin_cabecera("configuracion\puntuaciones.csv")

    #manejo de eventos 👻
    for evento in cola_eventos:
        if evento.type == pygame.MOUSEMOTION:
            #se actualizan las imagenes dependiendo si el mouse está encima del botón o no 👻
            if boton_atras["rectangulo"].collidepoint(evento.pos):
                #CLICK_ON_SOUND.play()
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
    mostrar_texto(pantalla,"TOP 10",(180,20),fuente_top,COLOR_BLANCO)

    acumulador_a = 150
    acumulador_b = 150

    #ultimos 10 puntajes 👻
    #convierto el los ultimos elementos de mi diccionario en una lista de tuplas
    #ultimos_10 = list(puntajes.items())[-10:]
    # Ordeno el diccionario por los valores en orden descendente y convierto en una lista de tuplas
    ultimos_10 = sorted(puntajes.items(), key=lambda x: x[1], reverse=True)[:10]

    #muestro los primeros 5 👻
    for clave, valor in ultimos_10[:5]:
        mostrar_texto(pantalla, f"{clave}: {valor}", (80, acumulador_a), fuente_menu, COLOR_BLANCO)
        acumulador_a += 50

    #muestro los otros 5 👻
    for clave, valor in ultimos_10[5:]:
        mostrar_texto(pantalla, f"{clave}: {valor}", (423, acumulador_b), fuente_menu, COLOR_BLANCO)
        acumulador_b += 50

    return retorno
