import pygame
import random
import json
import csv
from .constantes import *
from .funciones import crear_boton, cambiar_boton, leer_csv
from .jugar import *
from .estado import *

pygame.init()

fondo_original = pygame.image.load("imagenes/comodines.png")
fondo = pygame.transform.scale(fondo_original, (702,502))

fuente = pygame.font.SysFont("Pixel Operator 8",20)

#creo los botones llamando a la funcion de crear botones👻
boton_bomba = crear_boton(TAMAÑO_COMODINES,"imagenes/bomba.png")
boton_doble_chance = crear_boton((121,122),"imagenes/doble_chance.png")
boton_x2 = crear_boton((135,46),"imagenes/x2.png")
boton_pasar = crear_boton((144,46),"imagenes/next.png")

with open("configuracion/quiz.json", "r") as archivo:
    preguntas = json.load(archivo)

configuraciones = leer_csv("configuracion\config.csv")

puntos_configuraciones = configuraciones["puntos_acierto"]

#Funcion para el comodin de doble puntuacion.🌹
def puntos_doble_puntuacion(configuraciones):
    if estado_comodin_doble_puntuacion["bandera_doble_puntuacion"] == True:
        configuraciones["puntos_acierto"] = puntos_configuraciones * 2
    
    return configuraciones["puntos_acierto"]

#Funcion para el comodin de eliminar 2 respuestas incorrectas.🌹
def desactivar_dos_respuestas(pregunta_actual,preguntas):
    respuestas = ["respuesta_1", "respuesta_2", "respuesta_3", "respuesta_4"]
    respuesta_correcta = preguntas[pregunta_actual]["respuesta_correcta"]
    incorrectas = []
    pregunta = preguntas[pregunta_actual]

    for respuesta in respuestas:
        if pregunta[respuesta] != respuesta_correcta:
            incorrectas.append(respuesta)

    desactivar_distintas = random.sample(incorrectas, 2)

    for respuesta in desactivar_distintas:
        pregunta[respuesta] = ""

def segunda_chance(pregunta_actual,preguntas):
    respuestas = ["respuesta_1", "respuesta_2", "respuesta_3", "respuesta_4"]
    respuesta_correcta = preguntas[pregunta_actual]["respuesta_correcta"]
    pregunta = preguntas[pregunta_actual]

    if pregunta[respuesta] != respuesta_correcta and estado_uso_comodin_segunda_chance["bandera_uso_segunda_chance"] == True:
            for respuesta in respuestas:
                incorrecta = respuesta_seleccionada
                sacar_respuesta = incorrecta
                pregunta[sacar_respuesta] = ""


#Funcion para abrir la ventana de los comodines.🌹
def mostrar_comodines(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event]) -> str:
    """esta funcion dibuja el menu de comodines al llamarla, recibe como primer parametro las dimensiones de la pantalla, 
    como segundo parametro la cola de eventos, devuelve un string. 👻"""
    
    retorno = "comodines"
    global puntos_configuraciones

    for evento in cola_eventos:
        if evento.type == pygame.KEYDOWN:
        #con esto al darle espacio vuelve a juego 👻
            if evento.key == pygame.K_SPACE:
                retorno = "jugar"
                SONIDO_MENU_COMODINES_OUT.play()
        #metemos la logica de los botones 👻
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_bomba["rectangulo"].collidepoint(evento.pos):
                if configuraciones["comodines"] > 0:
                    configuraciones["comodines"] -= 1
                if estado_uso_comodin_bomba["bandera_uso_bomba"] == True or configuraciones["comodines"] == 0:
                    retorno = "jugar"    
                elif estado_uso_comodin_bomba["bandera_uso_bomba"] == False:
                    estado_comodin_bomba["bandera_bomba"] = True
                    estado_uso_comodin_bomba["bandera_uso_bomba"] = True
                retorno = "jugar"
            elif boton_doble_chance["rectangulo"].collidepoint(evento.pos):
                retorno = "jugar"
                DOBLE_CHANCE.play()
            elif boton_x2["rectangulo"].collidepoint(evento.pos):
                if configuraciones["comodines"] > 0:
                    configuraciones["comodines"] -= 1
                if estado_uso_comodin_doble_puntuacion["bandera_uso_doble_puntuacion"] == True or configuraciones["comodines"] == 0:
                    retorno = "jugar"                    
                elif estado_uso_comodin_doble_puntuacion["bandera_uso_doble_puntuacion"] == False:
                    estado_comodin_doble_puntuacion["bandera_doble_puntuacion"] = True
                    estado_uso_comodin_doble_puntuacion["bandera_uso_doble_puntuacion"] = True
                retorno = "jugar"
            elif boton_pasar["rectangulo"].collidepoint(evento.pos):
                if configuraciones["comodines"] > 0:
                    configuraciones["comodines"] -= 1
                if estado_uso_comodin_saltar["bandera_uso_saltar"] == True and configuraciones["comodines"] == 0:
                    retorno = "jugar"    
                elif estado_uso_comodin_saltar["bandera_uso_saltar"] == False:
                    estado_comodin_saltar["bandera_saltar"] = True
                    estado_uso_comodin_saltar["bandera_uso_saltar"] = True
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