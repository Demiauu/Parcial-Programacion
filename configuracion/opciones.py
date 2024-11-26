import pygame
from .constantes import *
from .funciones import mostrar_texto

#Todo este codigo es para que la ventana de opciones funcione bien.🌹

fondo_opciones = pygame.image.load("imagenes/pausa_raw.png")
fondo = pygame.transform.scale(fondo_opciones, (702,502))

pygame.init()

fuente_boton = pygame.font.SysFont("Pixel Operator 8",11)
fuente_controles = pygame.font.SysFont("Pixel Operator 8",9)
fuente_volumen = pygame.font.SysFont("Pixel Operator 8",20)
fuente_desactivar = pygame.font.SysFont("Pixel Operator 9", 20)

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
#Se agregaron los botones de desactivar la musica y los sonidos.🌹
boton_desactivar_musica = {}
boton_desactivar_musica["superficie"] = pygame.Surface(TAMAÑO_BOTON_VOLVER)
boton_desactivar_musica["rectangulo"] = boton_desactivar_musica["superficie"].get_rect()
boton_desactivar_musica["superficie"].fill(COLOR_ROJO)
boton_desactivar_general = {}
boton_desactivar_general["superficie"] = pygame.Surface(TAMAÑO_BOTON_VOLVER)
boton_desactivar_general["rectangulo"] = boton_desactivar_general["superficie"].get_rect()
boton_desactivar_general["superficie"].fill(COLOR_ROJO)
#Se agrego el boton para acceder a los controles.🌹
boton_controles = {}
boton_controles["superficie"] = pygame.Surface(TAMAÑO_BOTON_VOLVER)
boton_controles["rectangulo"] = boton_controles["superficie"].get_rect()
boton_controles["superficie"].fill(COLOR_AZUL)

# la funcion detecta cada click de los botones para ajustar el volumen de los audios.🌹
def mostrar_opciones(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego:dict) -> str:
    retorno = "opciones"
    
    bandera_musica = False
    bandera_general = False
    general_aux = 0
    musica_aux = 0

    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_suma["rectangulo"].collidepoint(evento.pos):
                if datos_juego["volumen_juego"] < 100:
                    datos_juego["volumen_juego"] += 5
                CLICK_SOUND.play()
            elif boton_resta["rectangulo"].collidepoint(evento.pos):
                if datos_juego["volumen_juego"] > 0:    
                    datos_juego["volumen_juego"] -= 5
                CLICK_SOUND.play()
            elif boton_suma_click["rectangulo"].collidepoint(evento.pos):
                if datos_juego["volumen_clicks"] < 100:
                    datos_juego["volumen_clicks"] += 5
                CLICK_SOUND.play()
            elif boton_resta_click["rectangulo"].collidepoint(evento.pos):
                if datos_juego["volumen_clicks"] > 0:
                    datos_juego["volumen_clicks"] -= 5
                CLICK_SOUND.play()
            elif boton_volver["rectangulo"].collidepoint(evento.pos):
                #detiene la musica para reproducir nueva 👻.
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.stop()
                CLICK_SOUND.play()
                retorno = "menu"
            elif boton_controles["rectangulo"].collidepoint(evento.pos):
                CLICK_SOUND.play()
                retorno = "controles"
            elif boton_desactivar_musica["rectangulo"].collidepoint(evento.pos):
                if bandera_musica == False:
                    musica_aux = datos_juego["volumen_juego"]
                    datos_juego["volumen_juego"] = 0
                    bandera_musica = True
                else:
                    datos_juego["volumen_juego"] = musica_aux
                    bandera_musica = False
                CLICK_SOUND.play()
            elif boton_desactivar_general["rectangulo"].collidepoint(evento.pos):
                if bandera_general == False:
                    general_aux = datos_juego["volumen_clicks"]
                    datos_juego["volumen_clicks"] = 0
                    bandera_general = True
                else:
                    datos_juego["volumen_clicks"] = general_aux
                    bandera_general = False
        # Se agrego la funcion de subir y bajar el volumen con las flechas del teclado.🌹
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RIGHT:
                if datos_juego["volumen_juego"] < 100:
                    datos_juego["volumen_juego"] += 5
                    CLICK_SOUND.play()
            elif evento.key == pygame.K_LEFT:
                if datos_juego["volumen_juego"] > 0:
                    datos_juego["volumen_juego"] -= 5
                    CLICK_SOUND.play()
            elif evento.key == pygame.K_UP:
                if datos_juego["volumen_clicks"] < 100:
                    datos_juego["volumen_clicks"] += 5
                    CLICK_SOUND.play()
            elif evento.key == pygame.K_DOWN:
                if datos_juego["volumen_clicks"] > 0:
                    datos_juego["volumen_clicks"] -= 5
                    CLICK_SOUND.play()

    #dibuja el fondo.🌹
    pantalla.blit(fondo, (0,0))

    boton_suma["rectangulo"] = pantalla.blit(boton_suma["superficie"],(583,150))
    boton_resta["rectangulo"] = pantalla.blit(boton_resta["superficie"],(20,150))
    boton_suma_click["rectangulo"] = pantalla.blit(boton_suma_click["superficie"],(583,240))
    boton_resta_click["rectangulo"] = pantalla.blit(boton_resta_click["superficie"],(20,240))
    boton_volver["rectangulo"] = pantalla.blit(boton_volver["superficie"],(10,10))
    boton_controles["rectangulo"] = pantalla.blit(boton_controles["superficie"],(610,10))
    boton_desactivar_general["rectangulo"] = pantalla.blit(boton_desactivar_general["superficie"],(220,380))
    boton_desactivar_musica["rectangulo"] = pantalla.blit(boton_desactivar_musica["superficie"],(420,380))

    mostrar_texto(boton_suma["superficie"],"Volumen +",(4,15),fuente_boton,COLOR_NEGRO)
    mostrar_texto(boton_resta["superficie"],"Volumen -",(4,15),fuente_boton,COLOR_NEGRO)
    mostrar_texto(boton_suma_click["superficie"],"Volumen +",(4,15),fuente_boton,COLOR_NEGRO)
    mostrar_texto(boton_resta_click["superficie"],"Volumen -",(4,15),fuente_boton,COLOR_NEGRO)
    mostrar_texto(boton_volver["superficie"],"Volver",(15,15),fuente_boton,COLOR_BLANCO)
    mostrar_texto(boton_controles["superficie"],"Controles",(4,9),fuente_controles,COLOR_BLANCO)
    mostrar_texto(boton_desactivar_musica["superficie"],"Desactivar musica",(5,10),fuente_desactivar,COLOR_BLANCO)
    mostrar_texto(boton_desactivar_general["superficie"],"Desactivar sonidos",(5,10),fuente_desactivar,COLOR_BLANCO)
    mostrar_texto(pantalla,f"{datos_juego["volumen_juego"]}%",(310,160),fuente_volumen,COLOR_BLANCO)
    mostrar_texto(pantalla,f"{datos_juego["volumen_clicks"]}%",(310,250),fuente_volumen,COLOR_BLANCO)

    return retorno