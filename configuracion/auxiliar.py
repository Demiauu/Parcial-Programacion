import pygame 
from .constantes import *
from .funciones import mostrar_texto, crear_boton, cambiar_boton, leer_csv, mezclar_lista
from .estado import *
from .comodines import *
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

#leo el csv 👻
configuraciones = leer_csv("configuracion\config.csv")
#agrego el tiempo restante 👻
tiempo_restante = configuraciones["temporizador"]
tiempo_restante_aux = tiempo_restante
vidas = configuraciones["vidas"]
vidas_aux = vidas
primera_iteracion = False

#//////////////////////////////////////////////////////////////////////////

def dividir_texto(texto, fuente, ancho_maximo):

    """
    Divide el texto en múltiples líneas que no excedan el ancho máximo.
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

    global tiempo_restante,tiempo_restante_aux,primera_iteracion,estado_guardar_config
    global vidas, vidas_aux

    #si detecta una modificación vuelve a leer el archivo csv 👻
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
            # x = mouse[0] #posicion x
            # y = mouse[1]
            print(x, y)
            validacion_pregunta(claves_opciones, x, y, pantalla)
            
        #! AGREGAR LOOPS DE PREGUNTAS Y RESPUESTAS; CONFIRMAR
        #!FINALMENTE AJUSTAR
    
    pantalla.blit(fondo, (0,0))

        
        # elif event.type == pygame.MOUSEMOTION:
        #     mouse = pygame.mouse.get_pos()
            #x = mouse[0] #posicion x
            #y = mouse[1]
            #print(mouse)

    #tiempo_restante_aux = tiempo_restante
    preguntas_respuestas(pantalla)
    #validacion_pregunta(claves_opciones, pantalla)
    #mostar_mensaje_resultado(pantalla)
    #comodin(pantalla, claves_opciones, margen_lateral, y_opcion_inicial, alto_opcion, espacio_entre_opciones)
    #game_over(pantalla)
    

    if tiempo_restante > 0:
        tiempo_restante -= 1 / 60  # Reducir el tiempo restante por fotograma (asume 60 FPS)
    else:
        vidas -= 1
        tiempo_restante = tiempo_restante_aux
        siguiente_pregunta()
    
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

def preguntas_respuestas(pantalla):
    linea_de_pregunta(pantalla)

    #dibujos
    boton_pregunta_1 = pygame.draw.rect(pantalla, COLOR_BOTON_AZUL, (50, 100, 610, 90))
    boton_pregunta_2 = pygame.draw.rect(pantalla, COLOR_BOTON_AZUL, (50, 200, 610, 90))
    boton_pregunta_3 = pygame.draw.rect(pantalla, COLOR_BOTON_AZUL, (50, 300, 610, 90))
    boton_pregunta_4 = pygame.draw.rect(pantalla, COLOR_BOTON_AZUL, (50, 400, 610, 90))
    
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
    global PUNTOS, VIDAS, mostrar_respuesta

    for i, clave_opcion in enumerate(opciones):
        boton_y = y_boton + i * (alto_boton + espacio_entre_opciones)
        if (x_boton <= x <= x_boton + ancho_boton and boton_y <= y <= boton_y + alto_boton):
            #for clave_opcion in opciones:
            print(clave_opcion)
            respuesta_seleccionada = preguntas[pregunta_actual][clave_opcion]
            respuesta_correcta = preguntas[pregunta_actual]["respuesta_correcta"]
                # # Cambiar color según respuesta
            if respuesta_seleccionada == respuesta_correcta:
                opcion_colores[i] = COLOR_VERDE
                mensaje_resultado = "¡Correcto!" #*VER EN DONDE UTLIIZAR ESTE MENSAJE
                if estado_comodin_doble_puntuacion["bandera_doble_puntuacion"] == False:
                    PUNTOS += puntos_configuraciones
                else:
                    #             # puntos_comodin = 20
                    PUNTOS += puntos_doble_puntuacion(configuraciones)
                    estado_comodin_doble_puntuacion["bandera_doble_puntuacion"] = False
                print(PUNTOS)
            if not respuesta_seleccionada == respuesta_correcta:
                opcion_colores[i] = COLOR_ROJO 
                mensaje_resultado = "Incorrecto"
                PUNTOS = max(0, PUNTOS - configuraciones["puntos_error"])
                VIDAS -= 1
            
            mostrar_respuesta = True
            temporizador = pygame.time.get_ticks()
        mostar_mensaje_resultado(pantalla)
        siguiente_pregunta()
    
    #mostrar_respuesta = True

def comodin(pantalla, opciones, margen_lateral, y_opcion_inicial, alto_opcion, espacio_entre_opciones): #! FALTA ACOPLAR
    #Verifica el uso del comodin de saltar pregunta.🌹
    if estado_comodin_saltar["bandera_saltar"] == True:
        pregunta_actual = (pregunta_actual + 1) % len(preguntas)  # Salta a la siguiente pregunta
        estado_comodin_saltar["bandera_saltar"] = False
    
    #Verifica el uso del comodin bomba.🌹
    for i, clave_opcion in enumerate(opciones):
        if estado_comodin_bomba["bandera_bomba"] == False:
            texto_opcion = preguntas[pregunta_actual][clave_opcion]
            x_opcion = margen_lateral
            y_opcion = y_opcion_inicial + i * (alto_opcion + espacio_entre_opciones)
            texto_x = x_opcion + 10  # Margen interno para el texto
            texto_y = y_opcion + 10  # Margen interno
            pygame.draw.rect(pantalla, opcion_colores[i], (50, 200 + i * 60, 700, 50))
            mostrar_texto(pantalla, texto_opcion, (texto_x, texto_y), fuente_menu, COLOR_BLANCO)
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

def mostar_mensaje_resultado(pantalla):
    if mensaje_resultado:
        x_mensaje = ANCHO // 2 - fuente_menu.size(mensaje_resultado)[0] // 2
        y_mensaje = ALTO - 60
        mostrar_texto(pantalla, mensaje_resultado, (x_mensaje, y_mensaje), fuente_menu, COLOR_NEGRO)
        #mostrar_texto(pantalla, mensaje_resultado, (50, 500), fuente_menu, COLOR_NEGRO)

def reloj(pantalla): #! FALTA ACOPLAR
    #* Actualizar el tiempo restante
    if tiempo_restante > 0:
        tiempo_restante -= 1 / 60  # Reducir el tiempo restante por fotograma (asume 60 FPS)
    else:
        tiempo_restante = tiempo_restante_aux
        vidas -= 1
        
        print(vidas)

    #* Mostrar el temporizador global
    minutos = int(tiempo_restante // 60)
    segundos = int(tiempo_restante % 60)
    tiempo_formateado = f"{minutos:02}:{segundos:02}"
    texto_temporizador = fuente_menu.render(tiempo_formateado, True, COLOR_BLANCO)
    pantalla.blit(texto_temporizador, (ANCHO - 150, 10))  # Posición del temporizador en pantalla

def siguiente_pregunta():
    global mostrar_respuesta, pregunta_actual
    #todo# Cambiar a la siguiente pregunta después de 2 segundos
    if mostrar_respuesta and pygame.time.get_ticks() - temporizador > 1000:
        pregunta_actual = (pregunta_actual + 1) % len(preguntas)
        opcion_colores = [COLOR_AZUL] * 4  # Reiniciar colores
        mensaje_resultado = ""
        mostrar_respuesta = False 