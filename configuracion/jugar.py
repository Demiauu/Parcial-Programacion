import pygame 
from .constantes import *
from .funciones import mostrar_texto, crear_boton, cambiar_boton, leer_csv
from .estado import *
from .estado import estado_guardar_config
from .comodines import *
import json
from .puntos import puntos

pygame.init()

#todo# ACCESO AL ARCHIVO .JSON -> PREGUNTAS, RESPUESTAS Y RESPUESTA_CORRECTA
with open("configuracion/quiz.json", "r") as archivo:
    preguntas = json.load(archivo)

#guarde la imagen en una variable para despues cambiarle el tamaño con .transform.scale 👻
fondo_original = pygame.image.load("imagenes/jugar.png")
fondo = pygame.transform.scale(fondo_original, (702,502))

fuente_menu = pygame.font.SysFont("Pixel Operator 8",30)

#leo el csv 👻
configuraciones = leer_csv("configuracion\config.csv")
#agrego el tiempo restante 👻
tiempo_restante = configuraciones["temporizador"]
tiempo_restante_aux = tiempo_restante
vidas = configuraciones["vidas"]
vidas_aux = vidas
primera_iteracion = False

#//////////////
#todo# VARIABLES AUXILARES
pregunta_actual = 0
opcion_colores = [COLOR_AZUL] * 4
respuesta_seleccionada = None
mensaje_resultado = ""  # Inicialmente, todas las opciones tienen el mismo color; color de las opciones
mostrar_respuesta = False
temporizador = 0
nombre = ""

#todo# FUNCIONES PARA ADAPTAR EL TEXTO SEGUN EL TAMANO DE LA PANTALLA
# def mostrar_texto(texto, x, y, color=COLOR_NEGRO):
#     superficie = fuente_menu.render(texto, True, color)
#     pantalla.blit(superficie, (x, y))

def dividir_texto(texto, fuente, ancho_maximo):
    """
    Divide el texto en múltiples líneas que no excedan el ancho máximo.
    """
    palabras = str(texto).split()
    lineas = []
    linea_actual = ""
    
    for palabra in palabras:
        if fuente.size(linea_actual + palabra)[0] <= ancho_maximo:
            linea_actual += palabra + " "
        else:
            lineas.append(linea_actual.strip())
            linea_actual = palabra + " "
    lineas.append(linea_actual.strip())
    return lineas

#creo los botones llamando a la funcion de crear botones👻
def mostrar_jugar(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event]) -> str:
    """esta funcion dibuja el menu jugar al llamarla, recibe como primer parametro las dimensiones de la pantalla, 
    como segundo parametro la cola de eventos, devuelve un string. 👻"""

    #todo# ACCESO A VARIABLES
    global pregunta_actual
    global opcion_colores
    global respuesta_seleccionada
    global mensaje_resultado 
    global mostrar_respuesta
    global temporizador

    global tiempo_restante,tiempo_restante_aux,primera_iteracion,estado_guardar_config,configuraciones
    global vidas, vidas_aux

    global GAME_OVER
    global PUNTOS,puntos
    global VIDAS
    global SCORES
    global nombre
    #configuraciones = leer_csv("configuracion/config.csv")

    #si detecta una modificación vuelve a leer el archivo csv 👻
    if estado_guardar_config["bandera_configuracion"]:
        configuraciones = leer_csv("configuracion\config.csv")

        tiempo_restante = configuraciones["temporizador"]
        tiempo_restante_aux = tiempo_restante

        vidas = configuraciones["vidas"]
        vidas_aux = vidas

        estado_guardar_config["bandera_configuracion"] = False


    x_texto = ANCHO // 2
    y_texto = ALTO // 10  # Margen superior
    margen_lateral = 50
    ancho_opcion = ANCHO - 2 * margen_lateral  # Ancho del rectángulo
    alto_opcion = 50  # Altura fija
    espacio_entre_opciones = 20  # Espacio vertical entre opciones

    # Coordenadas iniciales para las opciones
    x_opcion = margen_lateral
    y_opcion_inicial = ALTO // 3

    retorno = "jugar"
    #manejo de eventos 👻
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                retorno = "pausa"
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
            #si se preciona escape entra a la pestaña comodines 👻
            if evento.key == pygame.K_SPACE:
                retorno = "comodines"
                SONIDO_MENU_COMODINES_OUT.play()
        if evento.type == pygame.MOUSEMOTION:
            #se actualizan las imagenes dependiendo si el mouse está encima del botón o no 👻
            pass

        #todo# ACCESO A LAS PREGUNTAS Y RESPUESTAS
        elif evento.type == pygame.MOUSEBUTTONDOWN and not mostrar_respuesta:
            x, y = pygame.mouse.get_pos()
            claves_opciones = ["respuesta_1", "respuesta_2", "respuesta_3", "respuesta_4"]

            for i, clave_opcion in enumerate(claves_opciones):
                if (x_opcion <= x <= x_opcion + ancho_opcion and y_opcion_inicial + i * (alto_opcion + espacio_entre_opciones) <= y <= y_opcion_inicial + i * (alto_opcion + espacio_entre_opciones) + alto_opcion):
                    respuesta_seleccionada = preguntas[pregunta_actual][clave_opcion]
                    respuesta_correcta = preguntas[pregunta_actual]["respuesta_correcta"]
                    # Cambiar color según respuesta
                    if respuesta_seleccionada == respuesta_correcta:
                        opcion_colores[i] = COLOR_VERDE
                        mensaje_resultado = "¡Correcto!"
                        if estado_comodin_doble_puntuacion["bandera_doble_puntuacion"] == False:
                            PUNTOS += puntos_configuraciones
                            puntos["puntaje"] += puntos_configuraciones
                        else:
                            # puntos_comodin = 20
                            PUNTOS += puntos_doble_puntuacion(configuraciones)
                            estado_comodin_doble_puntuacion["bandera_doble_puntuacion"] = False
                            puntos["puntaje"] += puntos_configuraciones
                        print(PUNTOS)
                    else:
                        opcion_colores[i] = COLOR_ROJO
                        mensaje_resultado = "Incorrecto"
                        PUNTOS = max(0, PUNTOS - configuraciones["puntos_error"])
                        puntos["puntaje"] = max(0, PUNTOS - configuraciones["puntos_error"])
                        vidas -= 1

                    mostrar_respuesta = True
                    temporizador = pygame.time.get_ticks()

    
    #dibujar fondo 👻
    mostrar_texto(pantalla, "Prueba", (100, 100), fuente_menu, COLOR_NEGRO)
    pantalla.blit(fondo, (0,0))
    
    #Verifica el uso del comodin de saltar pregunta.🌹
    if estado_comodin_saltar["bandera_saltar"] == True:
        pregunta_actual = (pregunta_actual + 1) % len(preguntas)  # Salta a la siguiente pregunta
        estado_comodin_saltar["bandera_saltar"] = False

    #todo# Mostrar la pregunta actual
    pregunta = preguntas[pregunta_actual]["pregunta"]
    lineas_pregunta = dividir_texto(pregunta, fuente_menu, ANCHO - 100)  # Ajusta el ancho máximo según el diseño

    for i, linea in enumerate(lineas_pregunta):
        x_texto = ANCHO // 2 - fuente_menu.size(linea)[0] // 2  # Centramos el texto horizontalmente
        y_texto = ALTO // 8 + i * 40  # Ajustamos el margen superior y espaciado
        mostrar_texto(pantalla, linea, (x_texto, y_texto), fuente_menu, COLOR_NEGRO)
        #mostrar_texto(pantalla, linea, (50, 50 + i * 40), fuente_menu, COLOR_NEGRO)  #todo# Ajusta el espaciado entre líneas


    #todo# Mostrar opciones con colores
    claves_opciones = ["respuesta_1", "respuesta_2", "respuesta_3", "respuesta_4"]
    #Verifica el uso del comodin bomba.🌹
    for i, clave_opcion in enumerate(claves_opciones):
        if estado_comodin_bomba["bandera_bomba"] == False:
            texto_opcion = preguntas[pregunta_actual][clave_opcion]
            x_opcion = margen_lateral
            y_opcion = y_opcion_inicial + i * (alto_opcion + espacio_entre_opciones)
            texto_x = x_opcion + 10  # Margen interno para el texto
            texto_y = y_opcion + 10  # Margen interno
            pygame.draw.rect(pantalla, opcion_colores[i], (50, 200 + i * 60, 700, 50))
            mostrar_texto(pantalla, texto_opcion, (texto_x, texto_y), fuente_menu, COLOR_NEGRO)
        else:
            desactivar_dos_respuestas(pregunta_actual, preguntas)
            texto_opcion = preguntas[pregunta_actual][clave_opcion]
            x_opcion = margen_lateral
            y_opcion = y_opcion_inicial + i * (alto_opcion + espacio_entre_opciones)
            texto_x = x_opcion + 10  # Margen interno para el texto
            texto_y = y_opcion + 10  # Margen interno
            pygame.draw.rect(pantalla, opcion_colores[i], (50, 200 + i * 60, 700, 50))
            mostrar_texto(pantalla, texto_opcion, (texto_x, texto_y), fuente_menu, COLOR_NEGRO)
            estado_comodin_bomba["bandera_bomba"] = False
        #mostrar_texto(pantalla, texto_opcion, (60, 210 + i * 60), fuente_menu, COLOR_NEGRO)

    #todo# Mostrar resultado
    if mensaje_resultado:
        x_mensaje = ANCHO // 2 - fuente_menu.size(mensaje_resultado)[0] // 2
        y_mensaje = ALTO - 60
        mostrar_texto(pantalla, mensaje_resultado, (x_mensaje, y_mensaje), fuente_menu, COLOR_NEGRO)
        #mostrar_texto(pantalla, mensaje_resultado, (50, 500), fuente_menu, COLOR_NEGRO)

    #todo# Cambiar a la siguiente pregunta después de 2 segundos
    if mostrar_respuesta and pygame.time.get_ticks() - temporizador > 1000:
        pregunta_actual = (pregunta_actual + 1) % len(preguntas)
        opcion_colores = [COLOR_AZUL] * 4  # Reiniciar colores
        mensaje_resultado = ""
        mostrar_respuesta = False          
        #////////////////////////////////////

    if tiempo_restante > 0:
        tiempo_restante -= 1 / 60  
    else:
        vidas -= 1
        tiempo_restante = tiempo_restante_aux
    
    if vidas == 0:
        retorno = "fin_juego"
        if pygame.mixer.music.get_busy():
                    pygame.mixer.music.stop()
        vidas = vidas_aux
    
    #le damos formato al temporizador 👻
    minutos = int(tiempo_restante // 60)
    segundos = int(tiempo_restante % 60)
    tiempo_formateado = f"{minutos:02}:{segundos:02}"

    #mostramos las vidas y el reloj 👻
    mostrar_texto(pantalla,tiempo_formateado,(ANCHO-160,20),fuente,COLOR_BLANCO)
    mostrar_texto(pantalla,f"vidas: {vidas}",(60,20),fuente,COLOR_BLANCO)
    #se agregar las vidas 👻
    pygame.display.flip()
    
    return retorno