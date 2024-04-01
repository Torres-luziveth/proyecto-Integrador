import pygame
import sys, time
import threading
import json

# funcion fuente pixel
def get_font(size): 
    return pygame.font.Font("fuentes/font.ttf", size)

#colorcito
brow = (140, 70, 40) 
brow_claro = (229, 170, 122)
borde_activo = 3
borde_pasivo = 0
borde = borde_pasivo

# funcion para texto
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# configurarion de la ventana
pygame.init()
mainClock = pygame.time.Clock() # controla los intervalos del juego
pygame.display.set_caption('ADE Saving')
screen = pygame.display.set_mode((360, 639),0,32) # configuracion de la ventana

# Carga de imagenes
fondo = pygame.image.load('recursos/fondo.png').convert()

loading = pygame.image.load('recursos/loading.png')
loading_RECT = loading.get_rect(center=(180, 300))

barra = pygame.image.load('recursos/barra.png').convert_alpha()

boy1 = pygame.image.load('recursos/boy1.png').convert_alpha()
boy1 = pygame.transform.scale(boy1, (80, 80))

bot = pygame.image.load('recursos/bot.png').convert_alpha()
bot = pygame.transform.scale(bot, (90, 80))

txt = pygame.image.load('recursos/text.png').convert_alpha()


button_font = pygame.font.Font('fuentes/FjallaOne-Regular.ttf', 30)
main_font = pygame.font.Font('fuentes/FjallaOne-Regular.ttf', 40)
alert_font = pygame.font.Font('fuentes/FjallaOne-Regular.ttf', 20)


# Función para iniciar juego
def start_game():

    # variables login
   
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    entry_button = pygame.Rect(100,570,155,57)

    while True:
        
        screen.blit(fondo, [0,0]) # definicion de la imagen del fondo

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if entry_button.collidepoint(x, y):
                  return False

        screen.blit(bot, (90, 100))

        draw_text('¡Bienvenido!', main_font, (0,0,0), screen, 10, 10)
        
        pygame.draw.rect(screen, (128, 128, 128), entry_button, 5)
        draw_text('Regresar', button_font, (0, 0, 0), screen, 130, 580)

        pygame.display.flip()
        mainClock.tick(60)
