import pygame
import copy
from .constantes import *
from .funciones import mostrar_texto,crear_boton,cambiar_boton,leer_csv,modificar_csv
from .estado import estado_guardar_config

fondo_opciones = pygame.image.load("imagenes/mod_menu.png")
fondo = pygame.transform.scale(fondo_opciones, (702,502))

pygame.init()

fuente_boton = pygame.font.SysFont("Pixel Operator 8",11)
fuente_controles = pygame.font.SysFont("Pixel Operator 8",9)
fuente_volumen = pygame.font.SysFont("Pixel Operator 8",20)
fuente_desactivar = pygame.font.SysFont("Pixel Operator 9", 20)

#///////////////////////////////////////////////////////
    
#creamos el boton atras👻
boton_volver = crear_boton((70,30),"imagenes/boton_atras.png")

#creamos los botones para subir y bajar volumen👻
boton_suma_vidas = crear_boton((40,40),"imagenes/boton_plus.png")
boton_resta_vidas = crear_boton((40,40),"imagenes/boton_minus.png")
boton_suma_temporizador = crear_boton((40,40),"imagenes/boton_plus.png")
boton_resta_temporizador = crear_boton((40,40),"imagenes/boton_minus.png")
boton_suma_puntos_acierto = crear_boton((40,40),"imagenes/boton_plus.png")
boton_resta_puntos_acierto = crear_boton((40,40),"imagenes/boton_minus.png")
boton_suma_puntos_error = crear_boton((40,40),"imagenes/boton_plus.png")
boton_resta_puntos_error = crear_boton((40,40),"imagenes/boton_minus.png")
boton_suma_comodines = crear_boton((40,40),"imagenes/boton_plus.png")
boton_resta_comodines = crear_boton((40,40),"imagenes/boton_minus.png")

configuracion = leer_csv("configuracion\config.csv")
configuracion_aux = copy.deepcopy(configuracion)

def mostrar_mod_menu(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego:dict) -> str:
    retorno = "modificaciones"

    global configuracion,configuracion_aux,estado_guardar_config
    
    for evento in cola_eventos:
        #///////////////////////////////////////////

        #metemos la interacción sobre el botón atrás 👻
        if evento.type == pygame.MOUSEMOTION:
            if boton_volver["rectangulo"].collidepoint(evento.pos):
                cambiar_boton(boton_volver,"imagenes/boton_atras_on.png",(70,30),True)
            else:
                cambiar_boton(boton_volver,"imagenes/boton_atras_on.png",(70,30),False)
        #region
            if boton_suma_vidas["rectangulo"].collidepoint(evento.pos):
                cambiar_boton(boton_suma_vidas, "imagenes/boton_plus_on.png", (40, 40), True)
            else:
                cambiar_boton(boton_suma_vidas, "imagenes/boton_plus_on.png", (40, 40), False)

            if boton_resta_vidas["rectangulo"].collidepoint(evento.pos):
                cambiar_boton(boton_resta_vidas, "imagenes/boton_minus_on.png", (40, 40), True)
            else:
                cambiar_boton(boton_resta_vidas, "imagenes/boton_minus_on.png", (40, 40), False)

            if boton_suma_temporizador["rectangulo"].collidepoint(evento.pos):
                cambiar_boton(boton_suma_temporizador, "imagenes/boton_plus_on.png", (40, 40), True)
            else:
                cambiar_boton(boton_suma_temporizador, "imagenes/boton_plus_on.png", (40, 40), False)

            if boton_resta_temporizador["rectangulo"].collidepoint(evento.pos):
                cambiar_boton(boton_resta_temporizador, "imagenes/boton_minus_on.png", (40, 40), True)
            else:
                cambiar_boton(boton_resta_temporizador, "imagenes/boton_minus_on.png", (40, 40), False)

            if boton_suma_puntos_acierto["rectangulo"].collidepoint(evento.pos):
                cambiar_boton(boton_suma_puntos_acierto, "imagenes/boton_plus_on.png", (40, 40), True)
            else:
                cambiar_boton(boton_suma_puntos_acierto, "imagenes/boton_plus_on.png", (40, 40), False)

            if boton_resta_puntos_acierto["rectangulo"].collidepoint(evento.pos):
                cambiar_boton(boton_resta_puntos_acierto, "imagenes/boton_minus_on.png", (40, 40), True)
            else:
                cambiar_boton(boton_resta_puntos_acierto, "imagenes/boton_minus_on.png", (40, 40), False)

            if boton_suma_puntos_error["rectangulo"].collidepoint(evento.pos):
                cambiar_boton(boton_suma_puntos_error, "imagenes/boton_plus_on.png", (40, 40), True)
            else:
                cambiar_boton(boton_suma_puntos_error, "imagenes/boton_plus_on.png", (40, 40), False)

            if boton_resta_puntos_error["rectangulo"].collidepoint(evento.pos):
                cambiar_boton(boton_resta_puntos_error, "imagenes/boton_minus_on.png", (40, 40), True)
            else:
                cambiar_boton(boton_resta_puntos_error, "imagenes/boton_minus_on.png", (40, 40), False)

            if boton_suma_comodines["rectangulo"].collidepoint(evento.pos):
                cambiar_boton(boton_suma_comodines, "imagenes/boton_plus_on.png", (40, 40), True)
            else:
                cambiar_boton(boton_suma_comodines, "imagenes/boton_plus_on.png", (40, 40), False)

            if boton_resta_comodines["rectangulo"].collidepoint(evento.pos):
                cambiar_boton(boton_resta_comodines, "imagenes/boton_minus_on.png", (40, 40), True)
            else:
                cambiar_boton(boton_resta_comodines, "imagenes/boton_minus_on.png", (40, 40), False)
        #endregion

        #///////////////////////////////////////////
        if evento.type == pygame.QUIT:
            retorno = "salir"

        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_volver["rectangulo"].collidepoint(evento.pos):
                CLICK_SOUND_OUT.play()
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.stop()
                for clave,valor in configuracion.items():
                    modificar_csv("configuracion\config.csv",clave,valor)
                estado_guardar_config["bandera_configuracion"] = True
                
                retorno = "menu"
            if boton_suma_vidas["rectangulo"].collidepoint(evento.pos):
                configuracion["vidas"] += 1
            elif boton_resta_vidas["rectangulo"].collidepoint(evento.pos):
                if configuracion["vidas"] > 1:
                    configuracion["vidas"] -= 1
            elif boton_suma_temporizador["rectangulo"].collidepoint(evento.pos):
                configuracion["temporizador"] += 5
            elif boton_resta_temporizador["rectangulo"].collidepoint(evento.pos):
                if configuracion["temporizador"] > 5:
                    configuracion["temporizador"] -= 5
            elif boton_suma_puntos_acierto["rectangulo"].collidepoint(evento.pos):
                configuracion["puntos_acierto"] += 5
            elif boton_resta_puntos_acierto["rectangulo"].collidepoint(evento.pos):
                configuracion["puntos_acierto"] -= 5
            elif boton_suma_puntos_error["rectangulo"].collidepoint(evento.pos):
                configuracion["puntos_error"] += 5
            elif boton_resta_puntos_error["rectangulo"].collidepoint(evento.pos):
                configuracion["puntos_error"] -= 5
            elif boton_suma_comodines["rectangulo"].collidepoint(evento.pos):
                configuracion["comodines"] += 1
            elif boton_resta_comodines["rectangulo"].collidepoint(evento.pos):
                if configuracion["comodines"] > 0:
                    configuracion["comodines"] -= 1
        
                
    #dibuja el fondo.👻
    pantalla.blit(fondo, (0,0))

    #///////////////////////////////////

    #dibujo el boton atras 👻
    boton_volver["rectangulo"] = pantalla.blit(boton_volver["superficie"],(622,10))
    #///////////////////////////////////

    boton_suma_vidas["rectangulo"] = pantalla.blit(boton_suma_vidas["superficie"], (543, 85))
    boton_resta_vidas["rectangulo"] = pantalla.blit(boton_resta_vidas["superficie"], (403, 85))
    boton_suma_temporizador["rectangulo"] = pantalla.blit(boton_suma_temporizador["superficie"], (543, 160))
    boton_resta_temporizador["rectangulo"] = pantalla.blit(boton_resta_temporizador["superficie"], (403, 160))
    boton_suma_puntos_acierto["rectangulo"] = pantalla.blit(boton_suma_puntos_acierto["superficie"], (543, 235))
    boton_resta_puntos_acierto["rectangulo"] = pantalla.blit(boton_resta_puntos_acierto["superficie"], (403, 235))
    boton_suma_puntos_error["rectangulo"] = pantalla.blit(boton_suma_puntos_error["superficie"], (543, 310))
    boton_resta_puntos_error["rectangulo"] = pantalla.blit(boton_resta_puntos_error["superficie"], (403, 310))
    boton_suma_comodines["rectangulo"] = pantalla.blit(boton_suma_comodines["superficie"], (543, 385))
    boton_resta_comodines["rectangulo"] = pantalla.blit(boton_resta_comodines["superficie"], (403, 385))

    minutos = int(configuracion["temporizador"] // 60)
    segundos = int(configuracion["temporizador"] % 60)
    tiempo_formateado = f"{minutos:02}:{segundos:02}"

    mostrar_texto(pantalla, f"{configuracion['vidas']}", (490, 95), fuente_volumen, COLOR_BLANCO)  # Vida
    mostrar_texto(pantalla, f"{tiempo_formateado}", (445, 170), fuente_volumen, COLOR_BLANCO)  # Temporizador
    mostrar_texto(pantalla, f"{configuracion['puntos_acierto']}", (470, 245), fuente_volumen, COLOR_BLANCO)  # Puntos de acierto
    mostrar_texto(pantalla, f"{configuracion['puntos_error']}", (475, 320), fuente_volumen, COLOR_BLANCO)  # Puntos de error
    mostrar_texto(pantalla, f"{configuracion['comodines']}", (490, 395), fuente_volumen, COLOR_BLANCO)  # Comodines
    return retorno