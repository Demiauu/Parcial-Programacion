import pygame 
from .constantes import *
from .funciones import mostrar_texto, crear_boton, cambiar_boton, leer_csv, mezclar_lista
from .estado import *
from .comodines import *
from .puntos import puntos
import json

pygame.init()

#todo# ACCESO AL ARCHIVO .JSON -> PREGUNTAS, RESPUESTAS Y RESPUESTA_CORRECTA
with open("configuracion/quiz.json", "r") as archivo:
    preguntas = json.load(archivo)

mezclar_lista(preguntas)

fondo_original = pygame.image.load("imagenes/jugar_raw.png")
fondo = pygame.transform.scale(fondo_original, (702,502))

fuente_menu = pygame.font.SysFont("Pixel Operator 8", 15)
fuente_respuestas = pygame.font.SysFont("Pixel Operator 8", 12)
fuente_respuestas_evento = pygame.font.SysFont("Pixel Operator 8", 15)
configuraciones = leer_csv("configuracion\config.csv")  # Inicializa el temporizador global
tiempo_restante = configuraciones["temporizador"]
vidas = configuraciones["vidas"]
aciertos = 0

pregunta_actual = 0
opcion_colores = [COLOR_BOTON_AZUL] * 4 #! QUITAR
respuesta_seleccionada = None
mensaje_resultado = ""
temporizador = 0
nombre = ""
tiempo_restante_aux = tiempo_restante
color_botones = [COLOR_BLANCO, COLOR_NEGRO]
mostrar_respuesta = False
#C:\Users\ebiqu\OneDrive\Escritorio\programacion I\Parcial-Programacion
clock = pygame.time.Clock()

#//////////////////////////////////////////////////////////////////////////

#leo el csv 馃懟
configuraciones = leer_csv("configuracion\config.csv")
#agrego el tiempo restante 馃懟
tiempo_restante = configuraciones["temporizador"]
tiempo_restante_aux = tiempo_restante
vidas = configuraciones["vidas"]
vidas_aux = vidas
primera_iteracion = False

#//////////////////////////////////////////////////////////////////////////

def dividir_texto(texto, fuente, ancho_maximo):

    """
    Divide el texto en m煤ltiples l铆neas que no excedan el ancho m谩ximo.
    """
    palabras = str(texto).split()
    lineas = []
    linea_actual = ""
    
    for palabra in palabras:
        if len(palabra) <= ancho_maximo:
            linea_actual += palabra + " "
        else:
            lineas.append(linea_actual.strip())
            linea_actual = palabra + " "
    lineas.append(linea_actual.strip())
    return lineas

def linea_de_pregunta(pantalla: pygame.Surface) -> str:

    #todo# Mostrar la pregunta actual
    pregunta = preguntas[pregunta_actual]["pregunta"]
    linea_de_pregunta = dividir_texto(pregunta, fuente_menu, ANCHO)

    for i, linea in enumerate(linea_de_pregunta):
        x_texto = ANCHO // 9 - len(linea) // 2  # Centramos el texto horizontalmente
        y_texto = ALTO // 10 + i  # Ajustamos el margen superior y espaciado
        mostrar_texto(pantalla, linea, (x_texto, y_texto), fuente_menu, COLOR_NEGRO)



def mostrar_jugar(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event]) -> str:
    retorno = "jugar"
    claves_opciones = ["respuesta_1", "respuesta_2", "respuesta_3", "respuesta_4"]

    global tiempo_restante,tiempo_restante_aux,primera_iteracion,estado_guardar_config, configuraciones
    global preguntas, pregunta_actual
    global vidas, vidas_aux, aciertos

    #si detecta una modificaci贸n vuelve a leer el archivo csv 馃懟
    if estado_guardar_config["bandera_configuracion"]:
        configuraciones = leer_csv("configuracion\config.csv")

        tiempo_restante = configuraciones["temporizador"]
        tiempo_restante_aux = tiempo_restante

        vidas = configuraciones["vidas"]
        vidas_aux = vidas

        estado_guardar_config["bandera_configuracion"] = False
    
    for event in cola_eventos:
        if event.type == pygame.QUIT:
            retorno = "salir"

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                retorno = "pausa"
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                retorno = "comodines"
                SONIDO_MENU_COMODINES_OUT.play()
        
        
        elif event.type == pygame.MOUSEBUTTONDOWN and not mostrar_respuesta:
            x, y = pygame.mouse.get_pos()
            validacion_pregunta(claves_opciones, x, y)
        if event.type == pygame.MOUSEMOTION:
            pass
            
    
    pantalla.blit(fondo, (0,0))

    preguntas_respuestas(pantalla)
    mostar_mensaje_resultado(pantalla)  # Mostrar resultado de la respuesta
    siguiente_pregunta()
    reloj(pantalla)

    #logica de las vidas con el tiempo 馃懟.

    if tiempo_restante > 0:
        tiempo_restante -= 1 / 60  
    else:
        pregunta_actual = (pregunta_actual + 1) % len(preguntas)
        vidas -= 1
        puntos["puntaje"] += configuraciones["puntos_error"]
        tiempo_restante = tiempo_restante_aux
    
    if vidas == 0:
        retorno = "fin_juego"
        if pygame.mixer.music.get_busy():
                    pygame.mixer.music.stop()
        vidas = vidas_aux
    
    if vidas == 0:
        retorno = "fin_juego"
        if pygame.mixer.music.get_busy():
                    pygame.mixer.music.stop()
        vidas = vidas_aux
    #mostramos el puntaje en pantalla 馃懟
    mostrar_texto(pantalla,f"puntaje: {puntos["puntaje"]}",(260,15),fuente,COLOR_BLANCO)

    pygame.display.flip()
    return retorno

def preguntas_respuestas(pantalla):
    linea_de_pregunta(pantalla)

    if estado_comodin_bomba["bandera_bomba"] == True:
        desactivar_dos_respuestas(pregunta_actual, preguntas)
        estado_comodin_bomba["bandera_bomba"] = False

    #dibujos
    boton_pregunta_1 = pygame.draw.rect(pantalla, opcion_colores[0], (50, 100, 610, 90))
    boton_pregunta_2 = pygame.draw.rect(pantalla, opcion_colores[1], (50, 200, 610, 90))
    boton_pregunta_3 = pygame.draw.rect(pantalla, opcion_colores[2], (50, 300, 610, 90))
    boton_pregunta_4 = pygame.draw.rect(pantalla, opcion_colores[3], (50, 400, 610, 90))
    
    #renderizacion
    respuesta_uno = fuente_respuestas.render(preguntas[pregunta_actual]["respuesta_1"], 0, COLOR_BLANCO)
    respuesta_dos = fuente_respuestas.render(preguntas[pregunta_actual]["respuesta_2"], 0, COLOR_BLANCO)
    respuesta_tres = fuente_respuestas.render(preguntas[pregunta_actual]["respuesta_3"], 0, COLOR_BLANCO)
    respuesta_cuatro = fuente_respuestas.render(preguntas[pregunta_actual]["respuesta_4"], 0, COLOR_BLANCO)

    pantalla.blit(respuesta_uno, (55, 120))
    pantalla.blit(respuesta_dos, (55, 220))
    pantalla.blit(respuesta_tres, (55, 320))
    pantalla.blit(respuesta_cuatro, (55, 420))

def validacion_pregunta(opciones: list, x, y, pantalla):
    global puntos, vidas, mostrar_respuesta, tiempo_restante, configuraciones, aciertos

    botones = [
        pygame.Rect(50, 100, 610, 90),  # Bot贸n 1
        pygame.Rect(50, 200, 610, 90),  # Bot贸n 2
        pygame.Rect(50, 300, 610, 90),  # Bot贸n 3
        pygame.Rect(50, 400, 610, 90)   # Bot贸n 4
    ]

    for i, boton in enumerate(botones):
        if boton.collidepoint(x, y):
            respuesta_seleccionada = preguntas[pregunta_actual][opciones[i]]
            respuesta_correcta = preguntas[pregunta_actual]["respuesta_correcta"]
            # Cambiar color seg煤n respuesta
            if respuesta_seleccionada == respuesta_correcta:
                opcion_colores[i] = COLOR_VERDE
                mensaje_resultado = "隆Correcto!"
                PUNTOS += configuraciones["puntos_acierto"]  # Sumar puntos
                # if estado_comodin_doble_puntuacion["bandera_doble_puntuacion"] == False:
                #     #PUNTOS += puntos_configuraciones
                #     puntos["puntaje"] += configuraciones["puntos_acierto"]
                # else:
                #     # puntos_comodin = 20
                #     #PUNTOS += puntos_doble_puntuacion(configuraciones)
                #     puntos["puntaje"] += configuraciones["puntos_acierto"] * 2
                #     estado_comodin_doble_puntuacion["bandera_doble_puntuacion"] = False

                #logica de cada 5 respuestas correctas se gana una vida 馃懟
                
                if aciertos == 4 and vidas < vidas_aux:
                    vidas += 1
                    aciertos = 0
                else:
                    aciertos += 1
                    print(aciertos)

                tiempo_restante = tiempo_restante_aux

            else:
                opcion_colores[i] = COLOR_ROJO
                mensaje_resultado = "Incorrecto"
                PUNTOS = max(0, PUNTOS - configuraciones["puntos_error"])  # Restar puntos, no menos de 0
                VIDAS -= 1  # Restar una vida
                
                tiempo_restante = tiempo_restante_aux

            mostrar_respuesta = True
            temporizador = pygame.time.get_ticks()
            return
        # mostar_mensaje_resultado(pantalla)
        # siguiente_pregunta()
    
    #mostrar_respuesta = True

def mostar_mensaje_resultado(pantalla):
    if mensaje_resultado:
        x_mensaje = ANCHO // 2 - fuente_menu.size(mensaje_resultado)[0] // 2
        y_mensaje = ALTO - 60
        mostrar_texto(pantalla, mensaje_resultado, (x_mensaje, y_mensaje), fuente_menu, COLOR_NEGRO)
        #mostrar_texto(pantalla, mensaje_resultado, (50, 500), fuente_menu, COLOR_NEGRO)

def reloj(pantalla): 

    global vidas, retorno, tiempo_restante, puntos, pregunta_actual, preguntas

    # if tiempo_restante > 0:
    #     tiempo_restante -= 1 / 60  
    # else:
    #     pregunta_actual = (pregunta_actual + 1) % len(preguntas)
    #     vidas -= 1
    #     puntos["puntaje"] += configuraciones["puntos_error"]
    #     tiempo_restante = tiempo_restante_aux
    
    # if vidas == 0:
    #     retorno = "fin_juego"
    #     if pygame.mixer.music.get_busy():
    #                 pygame.mixer.music.stop()
    #     vidas = vidas_aux
    
    #le damos formato al temporizador 馃懟
    minutos = int(tiempo_restante // 60)
    segundos = int(tiempo_restante % 60)
    tiempo_formateado = f"{minutos:02}:{segundos:02}"

    #mostramos las vidas y el reloj 馃懟
    mostrar_texto(pantalla,tiempo_formateado,(ANCHO-160,20),fuente,COLOR_BLANCO)
    mostrar_texto(pantalla,f"vidas: {vidas}",(60,20),fuente,COLOR_BLANCO)


def siguiente_pregunta():
    global mostrar_respuesta, pregunta_actual, opcion_colores, mensaje_resultado
    if mostrar_respuesta and pygame.time.get_ticks() - temporizador > 1000:  # Esperar 2 segundos
        pregunta_actual = (pregunta_actual + 1) % len(preguntas)  # Cambiar a la siguiente pregunta
        opcion_colores = [COLOR_BOTON_AZUL] * 4  # Reiniciar colores de los botones
        mensaje_resultado = ""  # Limpiar mensaje
        mostrar_respuesta = False 