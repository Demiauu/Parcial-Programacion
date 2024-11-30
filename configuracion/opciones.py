import pygame
from .constantes import *
from .funciones import mostrar_texto,crear_boton,cambiar_boton
from .estado import estado_pausa
#Todo este codigo es para que la ventana de opciones funcione bien.🌹

fondo_opciones = pygame.image.load("imagenes/opciones.png")
fondo = pygame.transform.scale(fondo_opciones, (702,502))

pygame.init()

bandera_musica = False
bandera_general = False
general_aux = 0
musica_aux = 0
musica_aux2 = 0

fuente_boton = pygame.font.SysFont("Pixel Operator 8",11)
fuente_controles = pygame.font.SysFont("Pixel Operator 8",9)
fuente_volumen = pygame.font.SysFont("Pixel Operator 8",20)
fuente_desactivar = pygame.font.SysFont("Pixel Operator 9", 20)

#///////////////////////////////////////////////////////
    
#creamos el boton atras👻
boton_volver = crear_boton((70,30),"imagenes/boton_atras.png")
#creamos el boton desactivar musica y sonidos👻
boton_desactivar_musica = crear_boton(TAMAÑO_BOTON_VOLUMEN,"imagenes/boton_musica.png")
boton_desactivar_audio = crear_boton(TAMAÑO_BOTON_VOLUMEN,"imagenes/boton_audio.png")
#creamos los botones para subir y bajar volumen👻
boton_suma = crear_boton(TAMAÑO_BOTON_VOLUMEN,"imagenes/boton_plus.png")
boton_resta = crear_boton(TAMAÑO_BOTON_VOLUMEN,"imagenes/boton_minus.png")
boton_suma_efectos = crear_boton(TAMAÑO_BOTON_VOLUMEN,"imagenes/boton_plus.png")
boton_resta_efectos = crear_boton(TAMAÑO_BOTON_VOLUMEN,"imagenes/boton_minus.png")
#creamos el boton controles 👻
boton_controles = crear_boton(TAMAÑO_BOTON_VOLUMEN,"imagenes/boton_controles.png")

# la funcion detecta cada click de los botones para ajustar el volumen de los audios.🌹
def mostrar_opciones(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego:dict) -> str:
    retorno = "opciones"
    
    global bandera_general, bandera_musica, musica_aux, general_aux, musica_aux2

    for evento in cola_eventos:
        #///////////////////////////////////////////

        #metemos la interacción sobre el botón atrás 👻
        if evento.type == pygame.MOUSEMOTION:
            if boton_volver["rectangulo"].collidepoint(evento.pos):
                cambiar_boton(boton_volver,"imagenes/boton_atras_on.png",(70,30),True)
            else:
                cambiar_boton(boton_volver,"imagenes/boton_atras_on.png",(70,30),False)

            if boton_desactivar_musica["rectangulo"].collidepoint(evento.pos):
                cambiar_boton(boton_desactivar_musica,"imagenes/boton_musica_on.png",TAMAÑO_BOTON_VOLUMEN,True)
            else:
                cambiar_boton(boton_desactivar_musica,"imagenes/boton_musica_on.png",TAMAÑO_BOTON_VOLUMEN,False)

            if boton_desactivar_audio["rectangulo"].collidepoint(evento.pos):
                cambiar_boton(boton_desactivar_audio,"imagenes/boton_audio_on.png",TAMAÑO_BOTON_VOLUMEN,True)
            else:
                cambiar_boton(boton_desactivar_audio,"imagenes/boton_audio_on.png",TAMAÑO_BOTON_VOLUMEN,False)
            
            if boton_suma["rectangulo"].collidepoint(evento.pos):
                cambiar_boton(boton_suma,"imagenes/boton_plus_on.png",TAMAÑO_BOTON_VOLUMEN,True)
            else: 
                cambiar_boton(boton_suma,"imagenes/boton_plus_on.png",TAMAÑO_BOTON_VOLUMEN,False)
            
            if boton_resta["rectangulo"].collidepoint(evento.pos):
                cambiar_boton(boton_resta,"imagenes/boton_minus_on.png",TAMAÑO_BOTON_VOLUMEN,True)
            else:
                cambiar_boton(boton_resta,"imagenes/boton_minus_on.png",TAMAÑO_BOTON_VOLUMEN,False)
            
            if boton_suma_efectos["rectangulo"].collidepoint(evento.pos):
                cambiar_boton(boton_suma_efectos,"imagenes/boton_plus_on.png",TAMAÑO_BOTON_VOLUMEN,True)
            else: 
                cambiar_boton(boton_suma_efectos,"imagenes/boton_plus_on.png",TAMAÑO_BOTON_VOLUMEN,False)

            if boton_resta_efectos["rectangulo"].collidepoint(evento.pos):
                cambiar_boton(boton_resta_efectos,"imagenes/boton_minus_on.png",TAMAÑO_BOTON_VOLUMEN,True)
            else:
                cambiar_boton(boton_resta_efectos,"imagenes/boton_minus_on.png",TAMAÑO_BOTON_VOLUMEN,False)

            if boton_controles["rectangulo"].collidepoint(evento.pos):
                cambiar_boton(boton_controles,"imagenes/boton_controles_on.png",TAMAÑO_BOTON_VOLUMEN,True)
            else:
                cambiar_boton(boton_controles,"imagenes/boton_controles_on.png",TAMAÑO_BOTON_VOLUMEN,False)
            

        #///////////////////////////////////////////
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
            elif boton_suma_efectos["rectangulo"].collidepoint(evento.pos):
                if datos_juego["volumen_clicks"] < 100:
                    datos_juego["volumen_clicks"] += 5
                CLICK_SOUND.play()
            elif boton_resta_efectos["rectangulo"].collidepoint(evento.pos):
                if datos_juego["volumen_clicks"] > 0:
                    datos_juego["volumen_clicks"] -= 5
                CLICK_SOUND.play()
            elif boton_volver["rectangulo"].collidepoint(evento.pos):
                #detiene la musica para reproducir nueva 👻.
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.stop()
                CLICK_SOUND_OUT.play()
                #lo que hace esto es que al cambiar de ventana al menu de opciones desde juego, 
                # cuando das al boton atras vuelve a juego en vez de salir al menu 👻
                if estado_pausa["bandera"] == False:
                    retorno = "menu"
                else:
                    retorno = "pausa"
                    estado_pausa["bandera"] = False
            elif boton_controles["rectangulo"].collidepoint(evento.pos):
                CLICK_SOUND.play()
                retorno = "controles"
            #Se agrego la funcion del boton mute musica y que guarde el valor que tenia antes.🌹
            elif boton_desactivar_musica["rectangulo"].collidepoint(evento.pos):
                if bandera_musica == False:
                    musica_aux = datos_juego["volumen_juego"]
                    datos_juego["volumen_juego"] = 0
                    bandera_musica = True
                else:
                    datos_juego["volumen_juego"] = musica_aux
                    bandera_musica = False
                CLICK_SOUND.play()
            #Se agrego la funcion del boton mute general y que guarde el valor que tenia antes.🌹
            elif boton_desactivar_audio["rectangulo"].collidepoint(evento.pos):
                if bandera_general == False:
                    general_aux = datos_juego["volumen_clicks"]
                    musica_aux2 = datos_juego["volumen_juego"]
                    datos_juego["volumen_clicks"] = 0
                    datos_juego["volumen_juego"] = 0
                    bandera_general = True
                else:
                    datos_juego["volumen_clicks"] = general_aux
                    datos_juego["volumen_juego"] = musica_aux2
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

    #///////////////////////////////////

    #dibujo el boton atras 👻
    boton_volver["rectangulo"] = pantalla.blit(boton_volver["superficie"],(10,10))
    #dibujo los botones desactivar musica y audio 👻
    boton_desactivar_musica["rectangulo"] = pantalla.blit(boton_desactivar_musica["superficie"],(420,380))
    boton_desactivar_audio["rectangulo"] = pantalla.blit(boton_desactivar_audio["superficie"],(220,380))
    #///////////////////////////////////

    boton_suma["rectangulo"] = pantalla.blit(boton_suma["superficie"],(543,150))
    boton_resta["rectangulo"] = pantalla.blit(boton_resta["superficie"],(60,150))
    boton_suma_efectos["rectangulo"] = pantalla.blit(boton_suma_efectos["superficie"],(543,240))
    boton_resta_efectos["rectangulo"] = pantalla.blit(boton_resta_efectos["superficie"],(60,240))
    boton_volver["rectangulo"] = pantalla.blit(boton_volver["superficie"],(10,10))
    boton_controles["rectangulo"] = pantalla.blit(boton_controles["superficie"],(610,10))

    mostrar_texto(pantalla,f"{datos_juego["volumen_juego"]}%",(310,160),fuente_volumen,COLOR_BLANCO)
    mostrar_texto(pantalla,f"{datos_juego["volumen_clicks"]}%",(310,250),fuente_volumen,COLOR_BLANCO)

    return retorno