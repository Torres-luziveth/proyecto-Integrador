import pygame
import sys, time
import threading
from sign_up import save_user
from game import start_game
from os.path import exists
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

# funcion para perder el tiempo con el loading
def doWork():
    global loading_finished, loading_progress

    for i in range(work):
        math_question = 523687 / 789456 * 89456
        loading_progress = i
    loading_finished = True

# funcion para texto
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def check_user(user, password):

    user_path = f'./users/{user}.txt'

    if not exists(user_path):
        return 'No existe el usuario'
    
    with open(user_path, 'r') as load_file: 
        data = json.load(load_file)

    if user == data['username'] and password == data['password']:
        return 'ok'
    else:
        return 'Usuario o contraseña incorrecta'


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


# variables necesaria loading
loading_finished = False
loading_progress = 0
barra_width = 0
work = 100000000
threading.Thread(target=doWork).start() # para que la funcion funciones al mismo tiempor que el if en el main

input_RECT = pygame.Rect(50, 230, 265, 33)
password_input = pygame.Rect(50, 320, 265, 33)

button_font = pygame.font.Font('fuentes/FjallaOne-Regular.ttf', 30)
alert_font = pygame.font.Font('fuentes/FjallaOne-Regular.ttf', 20)

# Menu principal
def main_menu():

    # variables login
    base_font = get_font(15)
    user_text = ''
    password = ''
    show_password = ''
    active = False
    second_active = False

    entry_button = pygame.Rect(100,390,155,57)
    register_button = pygame.Rect(100,460,155,57)

    error_message = ''

    while True:
        
        screen.blit(fondo, [0,0]) # definicion de la imagen del fondo

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_RECT.collidepoint(event.pos):
                    active = True
                else:
                    active = False

                if password_input.collidepoint(event.pos):
                    second_active = True
                else:
                    second_active = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if register_button.collidepoint(x, y):
                    save_user()
                
                if entry_button.collidepoint(x, y):
                    if user_text == '' or password == '':
                        error_message = 'Falta información de ingreso'
                    else:
                        error_message = check_user(user_text, password)
                        if error_message == 'ok':
                            user_text = ''
                            password = ''
                            show_password = ''
                            error_message = ''
                            start_game()

            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                if register_button.collidepoint(x, y) or entry_button.collidepoint(x, y):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                else:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                if active == True:
                    if event.key == pygame.K_BACKSPACE:
                       user_text = user_text[0:-1]
                    else:
                       user_text += event.unicode

                if second_active == True:
                    if event.key == pygame.K_BACKSPACE:
                       password = password[0:-1]
                       show_password = show_password[0:-1]
                    else:
                       password += event.unicode
                       show_password += '*'
        
        # validacion para el loading
        if not loading_finished:

            barra_width = loading_progress / work * 210
            num_blocks = int(barra_width / 17.4)  # Ancho de cada cuadrito

            # Dibuja los cuadritos de la barra de carga
            for i in range(num_blocks):
                screen.blit(barra, (74 + i * 18, 285.6))
                
            draw_text('Loading', get_font(35), brow, screen, 90, 220)
            screen.blit(boy1,(10,180))
            screen.blit(loading, loading_RECT) 

        else:
            if active:
                borde = borde_activo
            else: 
                borde = borde_pasivo

            second_border = borde_activo if second_active else borde_pasivo
               

            time.sleep(0.1)
            screen.blit(bot, (90, 100))
           
            draw_text('Usuario', get_font(23), brow, screen, 95, 200)
            text_surface = base_font.render(user_text, True, 'black')
            pygame.draw.rect(screen, brow_claro, input_RECT,borde)
            screen.blit(text_surface,(input_RECT.x + 5, input_RECT.y + 9))

            draw_text('Contraseña', get_font(23), brow, screen, 65, 290)
            pass_input = base_font.render(show_password, True, 'black')
            pygame.draw.rect(screen, brow_claro, password_input, second_border)
            screen.blit(pass_input,(password_input.x + 5, password_input.y + 9))

            draw_text(error_message, alert_font, (0, 0, 0), screen, 30, 545)

            pygame.draw.rect(screen, (128, 128, 128), entry_button, 5)
            draw_text('Ingresar', button_font, (0, 0, 0), screen, 130, 400)
            pygame.draw.rect(screen, (128, 128, 128), register_button, 5)
            draw_text('Registrarse', button_font, (0, 0, 0), screen, 115, 470)

        pygame.display.flip()
        mainClock.tick(60)


main_menu()
