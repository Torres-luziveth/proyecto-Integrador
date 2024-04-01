import pygame

active_level = pygame.image.load('recursos/level.png')
inactive_level = pygame.image.load('recursos/nivel1.png')

class Button:
    def __init__(self, image, pos):
        self.image = image
        self.rect = self.image.get_rect(topleft=pos)
 
    # Define la función para el primer nivel activo
    def active(self):
        self.image = active_level.convert_alpha()
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

    def pressed(self):
        self.image = active_level
 
    # Define la función para el primer nivel inactivo
    def inactive(self):
        self.image = inactive_level.convert_alpha()
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
 