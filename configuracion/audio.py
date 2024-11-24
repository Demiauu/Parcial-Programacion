import pygame

pygame.mixer.init()

def musica(ventana_actual,datos_juego):
    """esta funcion recibe en que ventana estamos, los datos del juego y reproduce musica dependiendo en que ventana estamos ahora. 👻"""
    if ventana_actual == "menu" or ventana_actual:
        #carga la musica al menu 👻
        pygame.mixer.init()
        pygame.mixer.music.load("sonidos/League of Legends - Warriors.WAV")
        pygame.mixer.music.set_volume(datos_juego["volumen_juego"]/100)
        #
        pygame.mixer.music.set_volume(datos_juego["volumen_clicks"]/100)
        #/////////////////////////
        pygame.mixer.music.play()
        pygame.mixer.music.play(-1)
    elif ventana_actual == "jugar":
        pass
    #Este elif es para que se escuche la musica adentro de opciones 🌹
    elif ventana_actual == "opciones":
        pygame.mixer.init()
        pygame.mixer.music.load("sonidos/League of Legends - Warriors.WAV")
        pygame.mixer.music.set_volume(datos_juego["volumen_juego"]/100)
        pygame.mixer.music.set_volume(datos_juego["volumen_clicks"]/100)
        pygame.mixer.music.play()
        pygame.mixer.music.play(-1)