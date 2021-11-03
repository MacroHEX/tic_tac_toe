import pygame
import pygame_menu

pygame.init()
surface = pygame.display.set_mode((600,600))
pygame.display.set_caption("Ta-Te-Ti Menu")

def start_server():
    import server

def start_client():
    import client

tema = pygame_menu.themes.THEME_DARK.copy()
bg = pygame_menu.baseimage.BaseImage(image_path='res/bg.png', drawing_mode=pygame_menu.baseimage.IMAGE_MODE_CENTER)
tema.background_color= bg
tema.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_NONE

menu = pygame_menu.Menu('', 600, 600,
                       theme=tema)

menu.add.button('Iniciar Servidor', start_server)
menu.add.button('Unirse a Partida', start_client)
menu.add.button('Salir', pygame_menu.events.EXIT)

menu.mainloop(surface)