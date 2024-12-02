import pygame
# from funciones import leer_csv
pygame.mixer.init()

# configuraciones = leer_csv("configuracion/config.csv")

COLOR_BLANCO = (255,255,255)
COLOR_NEGRO = (0,0,0)
COLOR_VERDE = (0,255,0)
COLOR_ROJO = (255,0,0)
COLOR_AZUL = (0,0,255)
COLOR_VIOLETA = (134,23,219)
ANCHO = 700
ALTO = 500
VENTANA = (ANCHO,ALTO)
FPS = 60

#todo# VARIABLE PARA ACCEDER A LA VENTANA
PANTALLA = pygame.display.set_mode(VENTANA)

TAMAÑO_BOTON = (200,50)

#Agrege el temaño de lo botones de opciones.🌹
#Agrego tamaño de botones en la ventana pausa 👻
TAMAÑO_BOTON_PAUSA = (180,115)
#Agrege el temaño de lo botones de opciones 🌹
TAMAÑO_PREGUNTA = (350,150)
TAMAÑO_RESPUESTA = (250,60)
TAMAÑO_BOTON_VOLUMEN = (60,60)
TAMAÑO_BOTON_DESACTIVAR_VOLUMEN = (150,40)
TAMAÑO_BOTON_VOLVER = (80,40)
TAMAÑO_COMODINES = (119,119)

#Agregue los audios para los clicks y las respuestas erroneas.🌹
SONIDO_CLICK = pygame.mixer.Sound("sonidos/click.mp3")
SONIDO_ERROR = pygame.mixer.Sound("sonidos/error.mp3")

#nuevos audios click 👻
CLICK_SOUND = pygame.mixer.Sound("sonidos/click_boton1.wav")
CLICK_SOUND_OUT = pygame.mixer.Sound("sonidos/click_boton2.0.wav")
#audio click por encima del boton 👻
CLICK_ON_SOUND = pygame.mixer.Sound("sonidos/click_on.wav")
SONIDO_MENU_COMODINES = pygame.mixer.Sound("sonidos/flash.wav")
SONIDO_MENU_COMODINES_OUT = pygame.mixer.Sound("sonidos/flash_reverb.wav")
#sonido comodines 👻
SONIDO_BOMBA = pygame.mixer.Sound("sonidos/bomba.wav")
DOBLE_CHANCE = pygame.mixer.Sound("sonidos/doble_chance.wav")

#todo# PUNTUACION
GAME_OVER = False 
SCORES = []
PUNTOS = 0
VIDAS = 3 

