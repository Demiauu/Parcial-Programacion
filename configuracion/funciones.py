import random
from .constantes import *
import pygame
import csv

def leer_csv(ruta_csv):
    """esta funcion recibe como parametro la ruta del csv y lo convierte en un diccionario 👻"""
    opciones = {}
    #abro el archivo en modo 'r' para solo lectura 👻
    with open(ruta_csv, mode='r') as archivo:
        lector_csv = csv.DictReader(archivo)
        for fila in lector_csv:
            opciones[fila["opcion"]] = int(fila["valor"])
    return opciones

def crear_boton(tamanio:tuple,imagen:str)->dict:
    """esta funcion crea botones, recibe el tamaño de la imagen como primer parametro y 
    como segundo parametro recibe la imagen, devuelve un diccionario con la información del botón. 👻"""
    boton = {}
    imagen_original = pygame.image.load(imagen)
    boton["superficie"] = pygame.transform.scale(imagen_original, tamanio)
    boton["rectangulo"] = boton["superficie"].get_rect()

    #guardo la misma imagen pero con otra key para usarla más tarde 👻
    boton["imagen_vieja"] = boton["superficie"]
    return boton

def cambiar_boton(boton:dict,imagen:str,tamanio:tuple,evento:bool):
    """esta función recibe la info del botón que vamos a modificar, imagen nueva, tamaño y un booleano. 
    devuelve el botón modificado. 👻"""
    if "imagen_nueva" not in boton:  # Si la imagen no ha sido cargada aún
        imagen_nueva_original = pygame.image.load(imagen)
        boton["imagen_nueva"] = pygame.transform.scale(imagen_nueva_original, tamanio)
    # Cambiar la imagen dependiendo del evento 👻
    if evento:
        boton["superficie"] = boton["imagen_nueva"]
    else:
        boton["superficie"] = boton["imagen_vieja"]

    # Actualizar el rectángulo del botón 👻
    boton["rectangulo"] = boton["superficie"].get_rect()
    return boton

def mostrar_texto(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, False, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

def mezclar_lista(lista_preguntas:list) -> None:
    random.shuffle(lista_preguntas)

def verificar_respuesta(datos_juego:dict,pregunta_actual:dict,respuesta:int) -> bool:
    if respuesta == pregunta_actual["respuesta_correcta"]:
        datos_juego["puntuacion"] += PUNTUACION_ACIERTO
        retorno = True
    else:
        #SIN PUNTOS NEGATIVOS
        if datos_juego["puntuacion"] > PUNTUACION_ERROR:
            datos_juego["puntuacion"] -= PUNTUACION_ERROR
            
        #CON PUNTOS NEGATIVOS
        #datos_juego["puntuacion"] -= PUNTUACION_ERROR
        
        datos_juego["vidas"] -= 1
        retorno = False

    return retorno

def reiniciar_estadisticas(datos_juego:dict):
    datos_juego["puntuacion"] = 0
    datos_juego["vidas"] = CANTIDAD_VIDAS