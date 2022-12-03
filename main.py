import pygame
from objects import figure
from objects import game_field
FPS = 3
screenWidth = 1920
screenHeight = 1080
gameFieldHeight = 20
gameFieldWidth = 10
BLACK = 0x000000

pygame.init()
screen = pygame.display.set_mode((screenWidth, screenHeight))


clock = pygame.time.Clock()

finished = False


while not finished:
    '''
    Основной цикл программы.
    '''
pygame.quit()