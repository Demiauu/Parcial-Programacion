import pygame
from .constantes import *
from .funciones import mostrar_texto

#Todo este codigo es para que la ventana de opciones funcione bien 🌹

pygame.init()

fuente_boton = pygame.font.SysFont("Arial Narrow",20)
fuente_volumen = pygame.font.SysFont("Arial Narrow",50)

boton_suma = {}
boton_suma["superficie"] = pygame.Surface(TAMAÑO_BOTON_VOLUMEN)
boton_suma["rectangulo"] = boton_suma["superficie"].get_rect()
boton_suma["superficie"].fill(COLOR_ROJO)
boton_resta = {}
boton_resta["superficie"] = pygame.Surface(TAMAÑO_BOTON_VOLUMEN)
boton_resta["rectangulo"] = boton_resta["superficie"].get_rect()
boton_resta["superficie"].fill(COLOR_ROJO)
boton_suma_click = {}
boton_suma_click["superficie"] = pygame.Surface(TAMAÑO_BOTON_VOLUMEN)
boton_suma_click["rectangulo"] = boton_suma_click["superficie"].get_rect()
boton_suma_click["superficie"].fill(COLOR_ROJO)
boton_resta_click = {}
boton_resta_click["superficie"] = pygame.Surface(TAMAÑO_BOTON_VOLUMEN)
boton_resta_click["rectangulo"] = boton_resta_click["superficie"].get_rect()
boton_resta_click["superficie"].fill(COLOR_ROJO)
boton_volver = {}
boton_volver["superficie"] = pygame.Surface(TAMAÑO_BOTON_VOLVER)
boton_volver["rectangulo"] = boton_volver["superficie"].get_rect()
boton_volver["superficie"].fill(COLOR_AZUL)

# la funcion detecta cada click de los botones para ajustar el volumen de los audios 🌹
def mostrar_opciones(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego:dict) -> str:
    retorno = "opciones"
    
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_suma["rectangulo"].collidepoint(evento.pos):
                if datos_juego['volumen_juego'] < 100:
                    print("Sube el Volumen")
                    datos_juego['volumen_juego'] += 5
                CLICK_SOUND.play()
            elif boton_resta["rectangulo"].collidepoint(evento.pos):
                if datos_juego['volumen_juego'] > 0:
                    print("Baja el Volumen")                    
                    datos_juego['volumen_juego'] -= 5
                CLICK_SOUND.play()
            elif boton_suma_click["rectangulo"].collidepoint(evento.pos):
                if datos_juego['volumen_clicks'] < 100:
                    print("Sube el Volumen")
                    datos_juego['volumen_clicks'] += 5
                CLICK_SOUND.play()
            elif boton_resta_click["rectangulo"].collidepoint(evento.pos):
                if datos_juego['volumen_clicks'] > 0:
                    print("Baja el Volumen")
                    datos_juego['volumen_clicks'] -= 5
                CLICK_SOUND.play()
            elif boton_volver["rectangulo"].collidepoint(evento.pos):
                #detiene la musica para reproducir nueva 👻.
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.stop()
                print("Vuelve al menú")
                CLICK_SOUND.play()
                retorno = "menu"

    boton_suma["rectangulo"] = pantalla.blit(boton_suma["superficie"],(600,250))
    boton_resta["rectangulo"] = pantalla.blit(boton_resta["superficie"],(20,250))
    boton_suma_click["rectangulo"] = pantalla.blit(boton_suma_click["superficie"],(600,340))
    boton_resta_click["rectangulo"] = pantalla.blit(boton_resta_click["superficie"],(20,340))
    boton_volver["rectangulo"] = pantalla.blit(boton_volver["superficie"],(10,10))

    mostrar_texto(boton_suma["superficie"],"Volumen +",(5,15),fuente_boton,COLOR_NEGRO)
    mostrar_texto(boton_resta["superficie"],"Volumen -",(5,15),fuente_boton,COLOR_NEGRO)
    mostrar_texto(boton_suma_click["superficie"],"Volumen +",(5,15),fuente_boton,COLOR_NEGRO)
    mostrar_texto(boton_resta_click["superficie"],"Volumen -",(5,15),fuente_boton,COLOR_NEGRO)
    mostrar_texto(boton_volver["superficie"],"Volver",(15,15),fuente_boton,COLOR_BLANCO)
    mostrar_texto(pantalla,f"{datos_juego['volumen_juego']}%",(310,250),fuente_volumen,COLOR_NEGRO)
    mostrar_texto(pantalla,f"{datos_juego['volumen_clicks']}%",(310,340),fuente_volumen,COLOR_NEGRO)
    return retorno