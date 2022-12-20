import pygame
from objects import figure
from objects import game_field
import copy
from objects import screen


gameFieldHeight = 20
gameFieldWidth = 10
BLACK = 0x000000
WHITE = (255, 255, 255)
GREY = 0xc0c0c0
FPS = 30
pygame.init()

a = []

clock = pygame.time.Clock()
fnt = pygame.font.Font(None, 72)
finished = False
level_table = [48, 43, 38, 33, 28, 23, 18, 13, 8, 6, 5, 5, 5, 4, 4, 4, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]

#field1 = game_field(100, 100, 400, 10, 10)
frame = 0

finished = False
'''
moving_left_start = 0
moving_left = 0
moving_right_start = 0
moving_right = 0
moving_down_start = 0
moving_down = 0'''
def run_game(figure, field, left, right, down, clockwise, counterclockwise):

    global finished
    global frame
    #frame += 1
    #clock.tick(FPS)

    #screen.fill(BLACK)
    field.draw()
    #pygame.display.update()


    if frame - figure.moving_down_start == level_table[field.level]:
        yold = figure.y
        figure.move_down(field)
        if figure.y != yold:
            figure.moving_down_start = frame
        else:
            field.update_static_field(figure)
            figure.new_figure()
            figure.moving_left_start = 0
            figure.moving_left = 0
            figure.moving_right_start = 0
            figure.moving_right = 0
            figure.moving_down_start = frame
            field.burn_filled_rows()


    '''if frame - moving_down_start == level_table[level] + 30:
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
            field.burn_filled_rows()'''

    if figure.moving_left == 1 and frame - figure.moving_left_start == 16:
        figure.move_left(field)
        figure.moving_left = 2
        figure.moving_left_start = frame
    if figure.moving_left == 2 and frame - figure.moving_left_start == 6:
        figure.move_left(field)
        moving_left_start = frame

    if figure.moving_right == 1 and frame - figure.moving_right_start == 16:
        figure.move_right(field)
        figure.moving_right = 2
        figure.moving_right_start = frame
    if figure.moving_right == 2 and frame - figure.moving_right_start == 6:
        figure.move_right(field)
        figure.moving_right_start = frame

    if figure.moving_down == 1 and frame - figure.moving_down_start == 16:
        yold = figure.y
        figure.move_down(field)
        if figure.y != yold:
            figure.moving_down_start = frame
            field.score += 1
        figure.moving_down = 2
        figure.moving_down_start = frame
    if figure.moving_down == 2 and frame - figure.moving_down_start == 6:
        yold = figure.y
        figure.move_down(field)
        if figure.y != yold:
            figure.moving_down_start = frame
            field.score += 1
        figure.moving_down_start = frame

    for event in a:
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.KEYDOWN:
            if event.key == left:
                figure.move_left(field)
                figure.moving_left_start = frame
                figure.moving_left = 1
            if event.key == right:
                figure.move_right(field)
                figure.moving_right_start = frame
                figure.moving_right = 1
            if event.key == down:
                yold = figure.y
                figure.move_down(field)
                if figure.y != yold:
                    field.score += 1
                figure.moving_down = 1
            if event.key == counterclockwise:
                figure.rotate_counterclockwise(field)
            if event.key == clockwise:
                figure.rotate_clockwise(field)
        if event.type == pygame.KEYUP:
            if event.key == left:
                figure.moving_left = 0
            if event.key == right:
                figure.moving_right = 0
            if event.key == down:
                figure.moving_down = 0
    field.update_field_for_drawing(figure)
    if field.static_field[0] != [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]:
        field.game_over = True
        #print(moving_down_start - frame)
    #print(pygame.event.get())

def new_result(score, name):
    f = open('records.txt', 'r')
    records = []
    for i in range(10):
        records.append(f.readline().split())
        records[i][0] = int(records[i][0])
    for i in range(10):
        print(records[i])
    records.append([score, name])
    for i in range(10):
        for j in range(10):
            if records[j][0] < records[j+1][0]:
                h = records[j+1]
                records[j+1] = records[j]
                records[j] = h
    for i in range(10):
        print(records[i])
    f = open('records.txt', 'w')
    f.seek(0)
    for i in range(10):
        f.write(str(records[i][0]) + ' ' + records[i][1] + '\n')
    f.close()


def enter_name():
    global finished
    name = ''
    flag = False
    while not flag:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                if event.key == pygame.K_RETURN:
                    flag = True
                else:
                    name += event.unicode
        print(name)
    return name

def menu():
    start = False
    mode = 1
    global fnt
    while not start:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN and mode < 4:
                    mode = mode + 1
                if event.key == pygame.K_UP and mode > 1:
                    mode = mode - 1
                if event.key == pygame.K_RETURN:
                    start = True

        if mode == 1:
            player = fnt.render("1 PLAYER", 1, GREY)
        else:
            player = fnt.render("1 PLAYER", 1, WHITE)
        screen.blit(player, (800, 100))
        if mode == 2:
            player2 = fnt.render("P V P", 1, GREY)
        else:
            player2 = fnt.render("P V P", 1, WHITE)
        screen.blit(player2, (800, 300))
        if mode == 3:
            recs = fnt.render("RECORDS", 1, GREY)
        else:
            recs = fnt.render("RECORDS", 1, WHITE)
        screen.blit(recs, (800, 500))
        if mode == 4:
            q = fnt.render("QUIT", 1, GREY)
        else:
            q = fnt.render("QUIT", 1, WHITE)
        screen.blit(q, (800, 700))
        pygame.display.update()
        clock.tick(FPS)
    return mode
    print('ffffff')

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
'''f1 = figure()
f1.new_figure()
g1 = game_field(0, 0, 500)
f2 = figure()
f2.new_figure()
g2 = game_field(900, 0, 500)'''
#enter_name()
option = 2

frame = 0
gameOver = False
f1 = figure()
f1.new_figure()
g1 = game_field(0, 0, 500)
f2 = figure()
f2.new_figure()
g2 = game_field(900, 0, 500)

f = open('records.txt', 'r')
records = []
for i in range(10):
    records.append(f.readline().split())
    records[i][0] = int(records[i][0])
lowest = records[9][0]

while not finished:
    if option == 0:
        print('bbbbbbbbb')
        screen.fill((BLACK))
        option = menu()

    if option == 1:
        frame = 0
        gameOver = False
        f1 = figure()
        f1.new_figure()
        g1 = game_field(400, 0, 500)
        while not g1.game_over and not finished:
            frame += 1
            clock.tick(FPS)
            screen.fill(BLACK)
            a = pygame.event.get()
            run_game(f1, g1, pygame.K_a, pygame.K_d, pygame.K_s, pygame.K_e, pygame.K_q)
            pygame.display.update()
        screen.fill(BLACK)
        if g1.score > lowest:
            new_result(g1.score, enter_name())
        option = 0

    if option == 2:
        frame = 0
        gameOver = False
        f1 = figure()
        f1.new_figure()
        g1 = game_field(0, 0, 500)
        f2 = figure()
        f2.new_figure()
        g2 = game_field(900, 0, 500)
        while not gameOver and not finished:

            frame += 1
            clock.tick(FPS)
            screen.fill(BLACK)
            a = pygame.event.get()
            if g1.game_over == False:
                run_game(f1, g1, pygame.K_a, pygame.K_d, pygame.K_s, pygame.K_e, pygame.K_q)
            else:
                score1 = fnt.render(str(g1.score), 1, WHITE)
                screen.blit(score1, (500, 600))

            if g2.game_over == False:
                run_game(f2, g2, pygame.K_j, pygame.K_l, pygame.K_k, pygame.K_o, pygame.K_u)
            else:
                score2 = fnt.render(str(g2.score), 1, WHITE)
                screen.blit(score2, (1500, 600))
            if g1.game_over and g2.game_over:
                #clock.tick(1)
                #gameOver = True
                for event in a:
                    if event.type == pygame.KEYDOWN:
                        gameOver = True
            pygame.display.update()
        option = 0

    if option == 4:
        finished = True
#def one_player()

