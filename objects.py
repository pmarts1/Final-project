from random import choice
import random
import copy
import pygame
#from pygame import font

screen_width = 1920
screen_height = 1080
game_field_height = 20
game_field_width = 10

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
BLACK = 0x000000
GREY = 0xc0c0c0
GAME_COLORS = [BLACK, RED, BLUE, YELLOW, GREEN]

screenWidth = 1800
screenHeight = 1000
screen = pygame.display.set_mode((screenWidth, screenHeight))

top_score = 0
'''
Цвета, случайно выбирающиеся при появлении новой фигуры
'''
tT = [[0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 1, 1, 1, 0],
      [0, 0, 1, 0, 0],
      [0, 0, 0, 0, 0]]

jT = [[0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 1, 1, 1, 0],
      [0, 0, 0, 1, 0],
      [0, 0, 0, 0, 0]]

lT = [[0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 1, 1, 1, 0],
      [0, 1, 0, 0, 0],
      [0, 0, 0, 0, 0]]

sT = [[0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 1, 1, 0],
      [0, 1, 1, 0, 0],
      [0, 0, 0, 0, 0]]

zT = [[0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 1, 1, 0, 0],
      [0, 0, 1, 1, 0],
      [0, 0, 0, 0, 0]]

iT = [[0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [1, 1, 1, 1, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0]]

oT = [[0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 1, 1, 0],
      [0, 0, 1, 1, 0],
      [0, 0, 0, 0, 0]]

tetromino_list = [tT, jT, lT, sT, zT, iT, oT]
'''
Создание всех типов фигур.
'''


class figure:
    '''
    Фигуры, состоящие из 4-х квадратиков.
    '''

    def __init__(self):
        self.x = 0
        self.y = 5
        self.moving_left_start = 0
        self.moving_left = 0
        self.moving_right_start = 0
        self.moving_right = 0
        self.moving_down_start = 0
        self.moving_down = 0
        '''
        Координаты цетра вращения фигуры...
        '''
        self.color = 1
        self.coordinates = [[0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0]]
        self.supporting_coordinates = [[0, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0]]
        '''
        Список, описывающий текущий поворот фигуры. 0 - пустая клетка, 1 - заполненная
        '''

    def new_figure(self):
        self.x = 5
        self.y = 0
        self.coordinates = choice(tetromino_list)
        self.color = random.randint(1, 4)
        self.moving_left_start = 0
        self.moving_left = 0
        self.moving_right_start = 0
        self.moving_right = 0
        self.moving_down_start = 0
        self.moving_down = 0
        '''
        Создает новый тетрамино сверху экрана со случайным выбором новой формы и цвета
        '''

    def check_movement_possibility(self, field):
        for i in range(5):
            for j in range(5):
                if self.supporting_coordinates[i][j] == 1 and (
                        self.x + j - 2 > 9 or self.x + j - 2 < 0 or self.y + i - 2 > 19 or
                        field.static_field[self.y + i - 2][self.x + j - 2] != 0):
                    return False
        return True

    def move_down(self, field):
        '''
        Движение вниз на одну клетку.
        '''
        self.supporting_coordinates = self.coordinates
        self.y += 1
        if self.check_movement_possibility(field) == False:
            self.y -= 1
        self.supporting_coordinates = [[0, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0]]

    def move_left(self, field):
        """
        Движение влево на одну клетку.
        """
        self.supporting_coordinates = self.coordinates
        self.x -= 1
        if self.check_movement_possibility(field) == False:
            self.x += 1
        self.supporting_coordinates = [[0, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0]]

    def move_right(self, field):
        self.supporting_coordinates = self.coordinates
        self.x += 1
        if self.check_movement_possibility(field) == False:
            self.x -= 1
        self.supporting_coordinates = [[0, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0]]

    def rotate_clockwise(self, field):
        """
        Обновляет список, отвечающий за форму тетрамино (без привязки к координате) в соотвествии с поворотом по часовой стрелке.
        """
        for i in range(5):
            for j in range(5):
                if self.coordinates[i][j] == 1:
                    self.supporting_coordinates[j][4 - i] = 1
        if self.check_movement_possibility(field) == True:
            self.coordinates = self.supporting_coordinates
            self.supporting_coordinates = [[0, 0, 0, 0, 0],
                                           [0, 0, 0, 0, 0],
                                           [0, 0, 0, 0, 0],
                                           [0, 0, 0, 0, 0],
                                           [0, 0, 0, 0, 0]]

    def rotate_counterclockwise(self, field):
        """
        Обновляет список, отвечающий за форму тетрамино (без привязки к координате) в соотвествии с поворотом против часовой стрелки.
        """
        for i in range(5):
            for j in range(5):
                if self.coordinates[i][j] == 1:
                    self.supporting_coordinates[4 - j][i] = 1
        if self.check_movement_possibility(field) == True:
            self.coordinates = self.supporting_coordinates
            self.supporting_coordinates = [[0, 0, 0, 0, 0],
                                           [0, 0, 0, 0, 0],
                                           [0, 0, 0, 0, 0],
                                           [0, 0, 0, 0, 0],
                                           [0, 0, 0, 0, 0]]


class game_field():
    '''
    Игровое поле + поле с информацией (очки, уровень, следующая фигура)
    '''

    def __init__(self, x0, y0, game_field_width):
        """
        x0, y0 - координаты левого верхнего угла игрового поля.
        game_field_width, game_field_height - ширина и высота игрового поля.
        info_field_width, info_field_height

        """
        self.x0 = x0
        self.y0 = y0
        self.game_field_width = copy.deepcopy(game_field_width)
        self.game_field_height = copy.deepcopy(game_field_width) * 2
        self.lines = 0
        self.level = 5

        self.score = 0

        self.field = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for i in range(20)]
        self.static_field = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for i in range(20)]

        """
        Cписок клеток. 0 - пустая клетка. Другая цифра (в зависимости от цвета) - заполненная клетка.
        """

    def update_field_for_drawing(self, moving_figure):
        self.field = copy.deepcopy(self.static_field)
        for i in range(5):
            for j in range(5):
                if moving_figure.y + i - 2 < 20 and moving_figure.x + j - 2 < 10 and moving_figure.y + i - 2 >= 0 and moving_figure.coordinates[i][j] != 0:
                    self.field[moving_figure.y + i - 2][moving_figure.x + j - 2] = moving_figure.coordinates[i][j] * moving_figure.color

    def draw(self):
        for i in range(20):
            for j in range(10):
                pygame.draw.rect(screen, GAME_COLORS[self.field[i][j]],
                                 pygame.Rect(self.x0 + self.game_field_width / 10 * j,
                                             self.y0 + self.game_field_height / 20 * i, self.game_field_width / 10,
                                             self.game_field_height / 20))
                pygame.draw.rect(screen, GREY,
                                 pygame.Rect(self.x0 + self.game_field_width / 10 * j,
                                             self.y0 + self.game_field_height / 20 * i, self.game_field_width / 10,
                                             self.game_field_height / 20), 1)
        f1 = pygame.font.Font(None, 72)
        follow0 = f1.render("TOP", 1, (255, 255, 255))
        screen.blit(follow0, (540, 50))
        resultat = f1.render(str(top_score), 1, (255, 255, 255))
        screen.blit(resultat, (575, 100))
        follow1 = f1.render("SCORE", 1, (255, 255, 255))
        screen.blit(follow1, (510, 200))
        ochki = f1.render(str(self.score), 1, (255, 255, 255))
        screen.blit(ochki, (580, 250))
        follow2 = f1.render("NEXT", 1, (255, 255, 255))
        screen.blit(follow2, (525, 350))
        follow3 = f1.render("LEVEL", 1, (255, 255, 255))
        screen.blit(follow3, (520, 700))
        uroven = f1.render(str(self.level), 1, (255, 255, 255))
        screen.blit(uroven, (530, 750))


    def burn_filled_rows(self):
        rows_to_burn = []
        row_fullness_check = True
        '''
        Очищает полностью заполненные ряды и добавляет очки за них.
        '''
        for i in range(20):
            for j in range(10):
                if self.field[i][j] == 0:
                    row_fullness_check = False
                #continue
            if row_fullness_check == True:
                rows_to_burn.append(i)
                '''for j in range(10):
                    self.field[i][j] = 5'''
            row_fullness_check = True
        if len(rows_to_burn) != 0:
            for i in range(rows_to_burn[0]):
                self.field[rows_to_burn[len(rows_to_burn) - 1] - i] = copy.deepcopy(self.field[rows_to_burn[len(rows_to_burn) - 1] - len(rows_to_burn) - i])
            self.static_field = copy.deepcopy(self.field)
        self.lines += len(rows_to_burn)
        if len(rows_to_burn) == 1:
            self.score += 40*(self.level + 1)
        if len(rows_to_burn) == 2:
            self.score += 100*(self.level + 1)
        if len(rows_to_burn) == 3:
            self.score += 300 * (self.level + 1)
        if len(rows_to_burn) == 4:
            self.score += 1200*(self.level + 1)
        print(self.score)
        print(self.lines)
        self.level = self.lines // 10 + 5
    def update_static_field(self, moving_figure):
        self.update_field_for_drawing(moving_figure)
        self.static_field = copy.deepcopy(self.field)
