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

def check_data(data_dict):

    result = False
    
    for key in data_dict:
        if data_dict[key] in ['', ' ', None]:
            result = True
            break

    return result


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

first_name_rect = pygame.Rect(50, 95, 265, 33)
last_name_rect = pygame.Rect(50, 200, 265, 33)
age_rect = pygame.Rect(50, 300, 265, 33)
username_rect = pygame.Rect(50, 400, 265, 33)
password_rect = pygame.Rect(50, 500, 265, 33)

button_font = pygame.font.Font('fuentes/FjallaOne-Regular.ttf', 30)
main_font = pygame.font.Font('fuentes/FjallaOne-Regular.ttf', 40)
alert_font = pygame.font.Font('fuentes/FjallaOne-Regular.ttf', 20)


# Menu principal
def save_user():

    # variables login
    base_font = get_font(15)
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    first_name_active = False
    last_name_active = False
    age_active = False
    username_active = False
    password_active = False

    save_error = False

    # Diccionario de datos
    data = {
        'first_name': '',
        'last_name': '',
        'age': '',
        'username': '',
        'password': '',
        'show_password': ''
    }

    entry_button = pygame.Rect(100,570,155,57)
    return_button = pygame.Rect(210,10,140,40)

    while True:
        
        screen.blit(fondo, [0,0]) # definicion de la imagen del fondo

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                x, y = event.pos

                first_name_active = first_name_rect.collidepoint(event.pos)
                last_name_active = last_name_rect.collidepoint(event.pos)
                age_active = age_rect.collidepoint(event.pos)
                username_active = username_rect.collidepoint(event.pos)
                password_active = password_rect.collidepoint(event.pos)

                if entry_button.collidepoint(x, y):

                    if check_data(data):
                        save_error = True
                    else:
                        with open(f"./users/{data['username']}.txt", 'w') as store_file: 
                            json.dump(data, store_file)
                    
                        return False
                
                if return_button.collidepoint(x, y):
                    return False

            if event.type == pygame.KEYDOWN:

                save_error = False

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                if first_name_active:
                    if event.key == pygame.K_BACKSPACE:
                       data['first_name'] = data['first_name'][0:-1]
                    else:
                       data['first_name'] += event.unicode
                
                if last_name_active:
                    if event.key == pygame.K_BACKSPACE:
                       data['last_name'] = data['last_name'][0:-1]
                    else:
                       data['last_name'] += event.unicode
                
                if age_active:
                    if event.key == pygame.K_BACKSPACE:
                       data['age'] = data['age'][0:-1]
                    else:
                       data['age'] += event.unicode
                
                if username_active:
                    if event.key == pygame.K_BACKSPACE:
                       data['username'] = data['username'][0:-1]
                    else:
                       data['username'] += event.unicode

                if password_active:
                    if event.key == pygame.K_BACKSPACE:
                       data['password'] = data['password'][0:-1]
                       data['show_password'] = data['show_password'][0:-1]
                    else:
                       data['password'] += event.unicode
                       data['show_password'] += '*'
        
        first_name_border = borde_activo if first_name_active else borde_pasivo
        last_name_border = borde_activo if last_name_active else borde_pasivo
        age_border = borde_activo if age_active else borde_pasivo
        username_border = borde_activo if username_active else borde_pasivo
        password_border = borde_activo if password_active else borde_pasivo
            

        time.sleep(0.1)
        # screen.blit(bot, (90, 100))

        draw_text('Registro', main_font, (0,0,0), screen, 10, 10)

        pygame.draw.rect(screen, (128, 128, 128), return_button, 5)
        draw_text('Volver', button_font, (0, 0, 0), screen, 245, 12)
        
        draw_text('Nombres', get_font(23), brow, screen, 95, 70)
        first_name_input = base_font.render(data['first_name'], True, 'black')
        pygame.draw.rect(screen, brow_claro, first_name_rect, first_name_border)
        screen.blit(first_name_input,(first_name_rect.x + 5, first_name_rect.y + 9))

        draw_text('Apellidos', get_font(23), brow, screen, 80, 177)
        last_name_input = base_font.render(data['last_name'], True, 'black')
        pygame.draw.rect(screen, brow_claro, last_name_rect, last_name_border)
        screen.blit(last_name_input,(last_name_rect.x + 5, last_name_rect.y + 9))

        draw_text('Edad', get_font(23), brow, screen, 130, 278)
        age_input = base_font.render(data['age'], True, 'black')
        pygame.draw.rect(screen, brow_claro, age_rect, age_border)
        screen.blit(age_input,(age_rect.x + 5, age_rect.y + 9))

        draw_text('Usuario', get_font(23), brow, screen, 100, 378)
        username_input = base_font.render(data['username'], True, 'black')
        pygame.draw.rect(screen, brow_claro, username_rect, username_border)
        screen.blit(username_input,(username_rect.x + 5, username_rect.y + 9))

        draw_text('Contraseña', get_font(23), brow, screen, 70, 478)
        password_input = base_font.render(data['show_password'], True, 'black')
        pygame.draw.rect(screen, brow_claro, password_rect, password_border)
        screen.blit(password_input,(password_rect.x + 5, password_rect.y + 9))

        if save_error:
            draw_text('Ingresar toda la información solicitada', alert_font, (0, 0, 0), screen, 30, 545)

        pygame.draw.rect(screen, (128, 128, 128), entry_button, 5)
        draw_text('Guardar', button_font, (0, 0, 0), screen, 130, 580)

        pygame.display.flip()
        mainClock.tick(60)
