import pygame
from objects import figure
from objects import game_field
import copy
from objects import screen


gameFieldHeight = 20
gameFieldWidth = 10
BLACK = 0x000000
FPS = 60
pygame.init()



clock = pygame.time.Clock()

finished = False
level_table = [48, 43, 38, 33, 28, 23, 18, 13, 8, 6, 5, 5, 5, 4, 4, 4, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]

#field1 = game_field(100, 100, 400, 10, 10)
frame = 0
level = 5
finished = False
moving_left_start = 0
moving_left = 0
moving_right_start = 0
moving_right = 0
moving_down_start = 0
def run_game(figure, field):
    global moving_down_start
    global moving_left
    global moving_left_start
    global moving_right
    global moving_right_start
    global finished
    global frame
    global level
    frame += 1
    clock.tick(FPS)

    if frame - moving_down_start == level_table[level]:
        yold = figure.y
        figure.move_down(field)
        if figure.y != yold:
            moving_down_start = frame


    if frame - moving_down_start == level_table[level] + 30:
        yold = figure.y
        figure.move_down(field)
        if figure.y != yold:
            moving_down_start = frame
        else:
            field.update_static_field(figure)
            figure.new_figure()
            moving_left_start = 0
            moving_left = 0
            moving_right_start = 0
            moving_right = 0
            moving_down_start = frame
            field.burn_filled_rows()

    if moving_left == 1 and frame - moving_left_start == 16:
        figure.move_left(field)
        moving_left = 2
        moving_left_start = frame
    if moving_left == 2 and frame - moving_left_start == 6:
        figure.move_left(field)
        moving_left_start = frame

    if moving_right == 1 and frame - moving_right_start == 16:
        figure.move_right(field)
        moving_right = 2
        moving_right_start = frame
    if moving_right == 2 and frame - moving_right_start == 6:
        figure.move_right(field)
        moving_right_start = frame

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                figure.move_left(field)
                moving_left_start = frame
                moving_left = 1
            if event.key == pygame.K_d:
                figure.move_right(field)
                moving_right_start = frame
                moving_right = 1
            if event.key == pygame.K_s:
                figure.move_down(field)
                moving_down_start = frame
            if event.key == pygame.K_q:
                figure.rotate_counterclockwise(field)
            if event.key == pygame.K_e:
                figure.rotate_clockwise(field)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = 0

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                moving_right = 0

        #print(moving_down_start - frame)
    #print(pygame.event.get())



'''while not finished:
    screen.fill(BLACK)
    g1.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a

            elif event.type == pygame.MOUSEBUTTONUP:
                gun.fire2_end(event)
            elif event.type == pygame.MOUSEMOTION:
                gun.targetting(event)

    '''
    #Основной цикл программы.
'''
    clock.tick(1)
pygame.quit()
'''
f1 = figure()
f1.new_figure()
g1 = game_field(100, 100, 400, 100, 100)
#oldField = g1.static_field
print(g1.game_field_height)
while not finished:
    screen.fill(BLACK)

    g1.draw()
    pygame.display.update()
    run_game(f1, g1)
    g1.update_field_for_drawing(f1)

    #print(g1.field)
    #if oldField != g1.static_field:
    #print(g1.field)
    #oldField = g1.static_field
    #clock.tick(1)
    #print(pygame.event.get())
    #for i in pygame.event.get():
    #print(pygame.event.get())