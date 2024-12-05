import random
from .constantes import *
#from .jugar import configuraciones
import pygame
import csv
import os
import json

def agregar_pregunta(json_path, nueva_pregunta, respuestas):
    """
    Esta función agrega una nueva pregunta con 4 respuestas a un archivo JSON.
    Recibe como parámetros la ruta del archivo JSON, el texto de la nueva pregunta,
    la respuesta correcta y tres respuestas incorrectas. 👻
    """
    
    # Crear la nueva entrada
    nueva_entrada = {
        "pregunta": nueva_pregunta,
        "respuesta_1": respuestas[0],
        "respuesta_2": respuestas[1],
        "respuesta_3": respuestas[2],
        "respuesta_4": respuestas[3],
        "respuesta_correcta": respuestas[0]
    }

    try:
        # Leer el archivo JSON 👻
        with open(json_path, 'r') as file:

        #lee y convierte el archivo en una estructura de datos nativa de python 👻

            datos = json.load(file)

        # Agregar la nueva entrada
        datos.append(nueva_entrada)

        # Escribir los datos modificados en el archivo 👻
        with open(json_path, 'w') as file:

            #con vierte la estructura de datos nativa de python en texto json 👻
            
            json.dump(datos, file, indent=4)

        print("Pregunta agregada exitosamente.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

def modificar_json(nombre_archivo, clave, nuevo_valor):
    """
    Esta función recibe la ruta de un archivo JSON, una clave y un nuevo valor,
    y actualiza el archivo con el dato modificado o agrega la clave si no existe, sin romper nada 👻.
    """
    try:
        # Leer el archivo JSON 👻
        with open(nombre_archivo, mode="r") as archivo:

            #lee y convierte el archivo en una estructura de datos nativa de python 👻

            datos = json.load(archivo)
        
        # Verificar si la clave existe en los datos 👻
        if clave in datos:
            # Actualizar el valor de la clave existente 👻
            datos[clave] = nuevo_valor
        else:
            # Si la clave no existe, agregarla 👻
            datos[clave] = nuevo_valor

        # Escribir los datos modificados en el archivo 👻
        with open(nombre_archivo, mode="w") as archivo:

            #con vierte la estructura de datos nativa de python en texto json 👻

            json.dump(datos, archivo, indent=4)

        print(f"Archivo JSON modificado exitosamente: {clave} = {nuevo_valor} 👻")

    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe. 👻")
    except json.JSONDecodeError:
        print("El archivo no es un JSON válido. 👻")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e} 👻")

def leer_csv(ruta_csv):
    """esta funcion recibe como parametro la ruta del csv y lo convierte en un diccionario 👻"""
    opciones = {}
    #abro el archivo en modo 'r' para solo lectura 👻
    
    if os.path.exists(ruta_csv):
        #cuando termina el with el interprete de python se encarga de cerrarlo solo 👻
        with open(ruta_csv, mode='r') as archivo:
            #el lector de csv interpreta cada fila como un diccionario y la columna como clave 👻
            lector_csv = csv.DictReader(archivo)
            #recorremos la lista con un for y agregamos los elementos a un diccionario 👻
            for fila in lector_csv:
            # Usa el valor de la columna "opcion" como clave y convierte "valor" a entero antes de asignarlo. 👻
                opciones[fila["opcion"]] = int(fila["valor"])
        #print(opciones)
        return opciones
    else:
        print("ERROR, EL ARCHIVO NO EXISTE")
        return

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

def modificar_csv(nombre_archivo, clave, nuevo_valor):
    """esta funcion recibe la ruta del CSV, una clave y un nuevo valor, 
    y actualiza el archivo con el dato modificado sin romper nada 👻"""
    datos = []

    existe_clave = False

    with open(nombre_archivo, mode="r") as archivo:
        #el lector de csv interpreta cada fila como un diccionario y la columna como clave 👻
        lector = csv.DictReader(archivo)
        #recorremos la lista con un for y agregamos los elementos a un diccionario 👻
        for fila in lector:
            if fila["opcion"] == clave:
                #convierto el valor en cadena 👻
                fila["valor"] = str(nuevo_valor)
                existe_clave = True
            datos.append(fila)
    
    #si la clave no existe se agrega al diccionario 👻
    if not existe_clave:
        datos.append({"opcion": clave, "valor": str(nuevo_valor)})

    # Sobrescribir el archivo con los datos modificados 👻
    with open(nombre_archivo, mode="w", newline='') as archivo:
        #definimos la cabecera 👻
        cabecera = ["opcion", "valor"]
        escritor = csv.DictWriter(archivo, fieldnames=cabecera)
        escritor.writeheader()
        escritor.writerows(datos)

def guardar_puntaje(nombre_archivo, nombre_jugador, puntuacion):
    """
    Guarda un puntaje y el nombre del jugador en un archivo CSV.

    :param nombre_archivo: Nombre del archivo CSV donde se guardará el puntaje.
    :param nombre_jugador: Nombre del jugador.
    :param puntuacion: Puntuación del jugador.
    """
    try:
        with open(nombre_archivo, 'a', newline='', encoding='utf-8') as archivo:
            archivo.write(f'{nombre_jugador},{puntuacion}\n')
        print(f"Puntuación guardada: {nombre_jugador} - {puntuacion}")
    except Exception as e:
        print(f"Ocurrió un error al guardar la puntuación: {e}")

def leer_csv_sin_cabecera(ruta_csv):
    """
    Esta función recibe como parámetro la ruta de un archivo CSV **sin cabecera** 
    y lo convierte en un diccionario. Cada fila debe tener al menos dos columnas: 
    la primera será la clave y la segunda, el valor. 👻
    """
    opciones = {}  # Diccionario donde se almacenarán las claves y valores del CSV.

    # Verificamos si el archivo existe antes de intentar abrirlo 👻
    if os.path.exists(ruta_csv):
        with open(ruta_csv, mode='r') as archivo:  
            lector_csv = csv.reader(archivo)
            
            # Iteramos sobre cada fila del archivo CSV 👻
            for fila in lector_csv:
                if len(fila) >= 2:  # Verificamos que la fila tenga al menos 2 columnas.
                    opciones[fila[0]] = int(fila[1])  # La primera columna es la clave, la segunda el valor.
                else:
                    # Advertimos si encontramos filas incompletas que no tienen 2 columnas. 👻
                    print(f"Advertencia: Fila incompleta ignorada: {fila}")
        
        return opciones  # Devolvemos el diccionario con las opciones procesadas. 👻
    else:
        # Si el archivo no existe, mostramos un mensaje de error y devolvemos un diccionario vacío. 👻
        print("ERROR, EL ARCHIVO NO EXISTE")
        return {}

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
        datos_juego["puntuacion"] += configuraciones["puntos_acierto"]
        retorno = True
    else:
        datos_juego["puntuacion"] += configuraciones["puntos_error"]
        
        datos_juego["vidas"] -= 1
        retorno = False

    return retorno

def reiniciar_estadisticas(datos_juego:dict):
    datos_juego["puntuacion"] = 0
    datos_juego["vidas"] = configuraciones["vidas"]