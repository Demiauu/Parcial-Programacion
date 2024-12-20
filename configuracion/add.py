import pygame
from .funciones import mostrar_texto,guardar_puntaje,agregar_pregunta
from .constantes import *
from .puntos import puntos

pygame.init()

fondo_original = pygame.image.load("imagenes/pausa_raw.png")
fondo = pygame.transform.scale(fondo_original, (702,502))

fuente = pygame.font.SysFont("Pixel Operator 8",30)
fuente_gameover = pygame.font.SysFont("Pixel Operator 8",60)
fuente_puntuacion = pygame.font.SysFont("Pixel Operator 8",20)
fuente_auxiliar = pygame.font.SysFont("Pixel Operator 8",15)

cuadro = {}
imagen_original = pygame.image.load("imagenes/cuadro.png")
cuadro["superficie"] = pygame.transform.scale(imagen_original, (600,40))
#cuadro["superficie"] = pygame.Surface((300,150))
cuadro["rectangulo"] = cuadro["superficie"].get_rect()
nuevo = ["","","","","","",""]
i = 0
textos = ["","","","","","",""]

nueva_entrada = {
        "pregunta": "",
        "respuesta_1": "",
        "respuesta_2": "",
        "respuesta_3": "",
        "respuesta_4": "",
        "respuesta_correcta": ""
    }

def agregar_pregunta(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event]) -> str:
    global textos, nuevo, i, nueva_entrada

    pregunta = nuevo[0]
    respuestas = nuevo[1:5]

    retorno = "agregar_pregunta"

    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"

        elif evento.type == pygame.KEYDOWN:
            # bloc_mayus = pygame.key.get_mods() and pygame.KMOD_SHIFT
            # print(bloc_mayus)
            tecla = pygame.key.name(evento.key) 
            
            if tecla == "return" and len(nuevo[i]) > 0:
                # i+=1
                # if i == len(nuevo)-1:
                #     agregar_pregunta("configuracion/quiz.json",pregunta,respuestas)
                #     retorno = "menu"
                if i == 0:
                    nueva_entrada["pregunta"] = nuevo[i]
                    
                elif i == 1:
                    nueva_entrada["respuesta_1"] = nuevo[i]
                    nueva_entrada["respuesta_correcta"] = nueva_entrada["respuesta_1"]
                    
                elif i == 2:
                    nueva_entrada["respuesta_2"] = nuevo[i]
                    
                elif i == 3:
                    nueva_entrada["respuesta_3"] = nuevo[i]
                    
                elif i == 4:
                    nueva_entrada["respuesta_4"] = nuevo[i]
                    
                    agregar_pregunta("configuracion/quiz.json",pregunta,respuestas)
                i+=1
                

            elif tecla == "space":
                nuevo[i] += " "

            elif tecla == "backspace" and len(tecla) > 0:
                nuevo[i] = nuevo[i][0:-1] #divide el nombre del 0 hasta el ultimo pero como el ultimo no lo incluye lo elimina 👻
                cuadro["superficie"] = pygame.transform.scale(imagen_original, (700,40))

            if len(tecla) == 1:
                if pygame.key.get_mods() & pygame.KMOD_SHIFT:  
                    nuevo[i] += tecla.upper()
                else:
                    nuevo[i] += tecla.lower() 
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            pass
     

    pantalla.blit(fondo, (0,0))
    mostrar_texto(cuadro["superficie"],nuevo[i],(5,5),fuente,COLOR_BLANCO)
    mostrar_texto(pantalla,textos[i],(151,180),fuente_auxiliar,COLOR_BLANCO)
    cuadro["rectangulo"]=pantalla.blit(cuadro["superficie"],(50,200))
    # mostrar_texto(pantalla,"GAMEOVER",(107,20),fuente_gameover,COLOR_BLANCO)
    mostrar_texto(pantalla,"presiona ENTER para continuar",(161, 410),fuente_auxiliar,COLOR_BLANCO)
    return retorno