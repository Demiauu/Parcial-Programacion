import pygame
pygame.mixer.init()

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

TAMAÑO_BOTON = (200,50)

#Agrege el temaño de lo botones de opciones 🌹
TAMAÑO_PREGUNTA = (350,150)
TAMAÑO_RESPUESTA = (250,60)
TAMAÑO_BOTON_VOLUMEN = (80,40)
TAMAÑO_BOTON_VOLVER = (80,40)
#Agregue los audios para los clicks y las respuestas erroneas 🌹
SONIDO_CLICK = pygame.mixer.Sound("sonidos/click.mp3")
SONIDO_ERROR = pygame.mixer.Sound("sonidos/error.mp3")

#nuevos audios click 👻
CLICK_SOUND = pygame.mixer.Sound("sonidos/click_boton1.wav")
CLICK_SOUND_OUT = pygame.mixer.Sound("sonidos/click_boton2.0.wav")
#audio click encima 👻
CLICK_ON_SOUND = pygame.mixer.Sound("sonidos/click_on.wav")

CANTIDAD_VIDAS = 3
PUNTUACION_ACIERTO = 100
PUNTUACION_ERROR = 25
