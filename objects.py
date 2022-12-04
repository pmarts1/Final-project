from random import choice
import random

screen_width = 1920
screen_height = 1080
game_field_height = 20
game_field_width = 10

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
GAME_COLORS = [RED, BLUE, YELLOW, GREEN]
'''
Цвета, случайно выбирающиеся при появлении новой тетрамино
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
Создание всех типов тетрамино.
'''

class figure:
    '''
    Фигуры, состоящие из 4-х квадратиков.
    '''
    def __init__(self):
        self.x = 0
        self.y = 5
        '''
        Координаты цетра вращения фигуры...
        '''
        self.color = RED
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
        self.color = choice(GAME_COLORS)
        '''
        Создает новый тетрамино сверху экрана со случайным выбором новой формы и цвета
        '''
    def move_down(self):
        '''
        Движение вниз на одну клетку.
        '''
        self.y += 1

    def move_left(self):
        """
        Движение влева на одну клетку.
        :return:
        """
        self.x -= 1

    def move_right(self):
        self.x += 1

    def rotate_clockwise(self):
        """
        Обновляет список, отвечающий за форму тетрамино (без привязки к координате) в соотвествии с поворотом по часовой стрелке.
        """
        for i in range(5):
            for j in range(5):
                if self.coordinates[i][j] == 1:
                    self.supporting_coordinates[j][4 - i] = 1
        self.coordinates = self.supporting_coordinates
        self.supporting_coordinates = [[0, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0]]

    def rotate_counterclockwise(self):
        """
        Обновляет список, отвечающий за форму тетрамино (без привязки к координате) в соотвествии с поворотом против часовой стрелки.
        """
        for i in range(5):
            for j in range(5):
                if self.coordinates[i][j] == 1:
                    self.supporting_coordinates[4-j][i] = 1
        self.coordinates =  self.supporting_coordinates
        self.supporting_coordinates = [[0, 0, 0, 0, 0],
                                      [0, 0, 0, 0, 0],
                                      [0, 0, 0, 0, 0],
                                      [0, 0, 0, 0, 0],
                                      [0, 0, 0, 0, 0]]

class game_field():
    '''
    Игровое поле + поле с информацией (очки, уровень, следующая фигура)
    '''

    def __init__(self, x0, y0, game_field_width, game_field_height, info_field_width, info_field_height):
        """
        x0, y0 - координаты левого верхнего угла игрового поля.
        game_field_width, game_field_height - ширина и высота игрового поля.
        info_field_width, info_field_height

        """
        self.x0 = x0
        self.y0 = y0
        self.game_field_width = game_field_width
        self.game_field_height = game_field_height
        self.info_field_width = info_field_width
        self.info_field_height = info_field_height

        self.score = 0
        self.field = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        """
        Cписок клеток. 0 - пустая клетка. Другая цифра (в зависимости от цвета) - заполненная клетка.
        """
        def draw(self, figure):
            '''
            figure - текущая движущаяся фигура
            Рисует ячейки из field и фигуру, которая движется.
            '''
            pass

    def burn_field_rows(self):
        '''
        Очищает полностью заполненные ряды и добавляет очки за них.
        '''
        pass

'''
f1 = figure()
f1.new_figure()
print(f1.coordinates)
f1.rotate_clockwise()
print(f1.coordinates)
f1.rotate_clockwise()
print(f1.coordinates)
'''
g1 = game_field(100, 100, 400, 800, 100, 100)

print(g1.x0)