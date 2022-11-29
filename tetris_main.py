import pygame

FPS = 60

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
GAME_COLORS = [RED, BLUE, YELLOW, GREEN]

WIDTH = 1920
HEIGHT = 1080

class tetromino:
    ''''
    Фигуры, состоящие из 4-х квадратиков.
    '''
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.x = x
        self.y = y

        self.color = choice(GAME_COLORS)
        self.live = 30
        self.t = 0



    def move(self):


class row:
    '''
    Ряды поля, заполненные квадратиками. Должен хранить данные о том, какие поля заполнены.
    '''
    def selfDestruction(self):
        '''
        Очищает ряд, когда он он полностью заполнен квадратиками.
        '''
