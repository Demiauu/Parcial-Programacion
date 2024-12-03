import pygame
from .funciones import mostrar_texto
from .constantes import *


pygame.init()

fondo_original = pygame.image.load("imagenes/pausa_raw.png")
fondo = pygame.transform.scale(fondo_original, (702,502))

fuente = pygame.font.SysFont("Pixel Operator 8",30)
fuente_gameover = pygame.font.SysFont("Pixel Operator 8",60)
fuente_puntuacion = pygame.font.SysFont("Pixel Operator 8",20)
fuente_auxiliar = pygame.font.SysFont("Pixel Operator 8",15)

cuadro = {}
imagen_original = pygame.image.load("imagenes/cuadro.png")
cuadro["superficie"] = pygame.transform.scale(imagen_original, (400,40))
#cuadro["superficie"] = pygame.Surface((300,150))
cuadro["rectangulo"] = cuadro["superficie"].get_rect()
nombre = ""

def mostrar_fin_juego(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event]) -> str:
    global nombre
    retorno = "fin_juego"

    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"

        elif evento.type == pygame.KEYDOWN:
            # bloc_mayus = pygame.key.get_mods() and pygame.KMOD_SHIFT
            # print(bloc_mayus)
            tecla = pygame.key.name(evento.key) 

            if tecla == "enter" and len(nombre) > 0:
                pass
            elif tecla == "space":
                nombre += " "

            elif tecla == "backspace" and len(tecla) > 0:
                nombre = nombre[0:-1] #divide el nombre del 0 hasta el ultimo pero como el ultimo no lo incluye lo elimina 👻
                cuadro["superficie"] = pygame.transform.scale(imagen_original, (400,40))

            if len(tecla) == 1:
                if pygame.key.get_mods() & pygame.KMOD_SHIFT:  
                    nombre += tecla.upper()
                else:
                    nombre += tecla.lower() 
                #print(f"Tecla presionada: {tecla}, Nombre actual: {nombre}")
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            #rint(evento.pos)
            pass
        


    pantalla.blit(fondo, (0,0))
    mostrar_texto(cuadro["superficie"],nombre,(5,5),fuente,COLOR_BLANCO)
    mostrar_texto(pantalla,"ingrese su nombre",(151,180),fuente_auxiliar,COLOR_BLANCO)
    cuadro["rectangulo"]=pantalla.blit(cuadro["superficie"],(151,200))
    mostrar_texto(pantalla,f"Puntuación: ",(151,300),fuente_puntuacion,COLOR_BLANCO)
    mostrar_texto(pantalla,"GAMEOVER",(107,20),fuente_gameover,COLOR_BLANCO)
    mostrar_texto(pantalla,"presiona ENTER para guardar",(161, 410),fuente_auxiliar,COLOR_BLANCO)
    return retorno