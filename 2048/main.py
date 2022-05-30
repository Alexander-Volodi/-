import pygame as pg
import sys
from random import choice
from math import log
pg.init()
pg.display.set_icon(pg.image.load('2048.png'))
pg.display.set_caption('2048')
sc = pg.display.set_mode((500, 650))
bars_color = (100, 100, 100)
background = (200, 200, 200)
pg.display.update()
table = [[0] * 4 for _ in range(4)]
pg.draw.rect(sc, background, (50, 580, 400, 600))
score = 0


def _2048():
    global table
    global score
    table = [[0] * 4 for _ in range(4)]
    score = 0
    sc.fill(background)
    pg.draw.rect(sc, bars_color, (50, 475, 400, 90), 10)
    f2 = pg.font.Font(None, 90)
    text6 = f2.render('New game', True, (50, 50, 50))
    sc.blit(text6, (90, 490))
    pg.draw.rect(sc, bars_color, (50, 50, 5, 400))
    pg.draw.rect(sc, bars_color, (150, 50, 5, 400))
    pg.draw.rect(sc, bars_color, (250, 50, 5, 400))
    pg.draw.rect(sc, bars_color, (350, 50, 5, 400))
    pg.draw.rect(sc, bars_color, (450, 50, 5, 400))
    pg.draw.rect(sc, bars_color, (50, 50, 400, 5))
    pg.draw.rect(sc, bars_color, (50, 150, 400, 5))
    pg.draw.rect(sc, bars_color, (50, 250, 400, 5))
    pg.draw.rect(sc, bars_color, (50, 350, 400, 5))
    pg.draw.rect(sc, bars_color, (50, 450, 405, 5))
    flag_game_over = False
    images = [0] * 11
    for i in range(11):
        images[i] = pg.image.load(f'{2 ** (i + 1)}.png')
    f = pg.font.Font(None, 40)
    text1 = f.render('Score: ', True, (50, 50, 50))
    text3 = f.render('Best: ', True, (50, 50, 50))
    sc.blit(text1, (55, 10))
    sc.blit(text3, (250, 10))
    pg.display.update()
    fps = 20
    clock = pg.time.Clock()
    with open('Score.txt') as score_file:
        best = score_file.read().strip()

    def move_right():
        global table, score
        for j in range(4):
            raw = [table[0][j], table[1][j], table[2][j], table[3][j]]
            if len(set(raw)) > 1:
                while table[3][j] == 0:
                    table[0][j], table[1][j], table[2][j], table[3][j] = 0, table[0][j], table[1][j], table[2][j]
            raw = [table[0][j], table[1][j], table[2][j]]
            if len(set(raw)) > 1:
                while table[2][j] == 0:
                    table[0][j], table[1][j], table[2][j] = 0, table[0][j], table[1][j]
            raw = [table[0][j], table[1][j]]
            if len(set(raw)) > 1:
                while table[1][j] == 0:
                    table[0][j], table[1][j] = 0, table[0][j]
            if table[2][j] == table[3][j] and table[0][j] == table[1][j]:
                score += table[2][j] + table[3][j] + table[0][j] + table[1][j]
                table[3][j], table[2][j], table[1][j], table[0][j] = table[2][j] + table[3][j], table[0][j] + table[1][j], 0, 0
            elif table[2][j] == table[3][j]:
                score += table[2][j] + table[3][j]
                table[3][j], table[2][j], table[1][j], table[0][j] = table[2][j] + table[3][j], table[1][j], table[0][j], 0
            elif table[1][j] == table[2][j]:
                score += table[2][j] + table[1][j]
                table[2][j], table[1][j], table[0][j] = table[2][j] + table[1][j], table[0][j], 0
            elif table[0][j] == table[1][j]:
                score += table[1][j] + table[0][j]
                table[1][j], table[0][j] = table[1][j] + table[0][j], 0

    def move_left():
        global table, score
        for j in range(4):
            raw = [table[0][j], table[1][j], table[2][j], table[3][j]]
            if len(set(raw)) > 1:
                while table[0][j] == 0:
                    table[0][j], table[1][j], table[2][j], table[3][j] = table[1][j], table[2][j], table[3][j], 0
            raw = [table[3][j], table[1][j], table[2][j]]
            if len(set(raw)) > 1:
                while table[1][j] == 0:
                    table[1][j], table[2][j], table[3][j] = table[2][j], table[3][j], 0
            raw = [table[2][j], table[3][j]]
            if len(set(raw)) > 1:
                while table[2][j] == 0:
                    table[2][j], table[3][j] = table[3][j], 0
            if table[2][j] == table[3][j] and table[0][j] == table[1][j]:
                score += table[2][j] + table[3][j] + table[0][j] + table[1][j]
                table[3][j], table[2][j], table[1][j], table[0][j] = 0, 0, table[2][j] + table[3][j], table[0][j] + table[1][j]
            elif table[0][j] == table[1][j]:
                score += table[0][j] + table[1][j]
                table[3][j], table[2][j], table[1][j], table[0][j] = 0, table[3][j], table[2][j], table[0][j] + table[1][j]
            elif table[1][j] == table[2][j]:
                score += table[2][j] + table[1][j]
                table[1][j], table[2][j], table[3][j] = table[2][j] + table[1][j], table[3][j], 0
            elif table[3][j] == table[2][j]:
                score += table[2][j] + table[3][j]
                table[2][j], table[3][j] = table[2][j] + table[3][j], 0

    def move_up():
        global table, score
        for j in range(4):
            raw = [table[j][0], table[j][1], table[j][2], table[j][3]]
            if len(set(raw)) > 1:
                while table[j][0] == 0:
                    table[j][0], table[j][1], table[j][2], table[j][3] = table[j][1], table[j][2], table[j][3], 0
            raw = [table[j][3], table[j][1], table[j][2]]
            if len(set(raw)) > 1:
                while table[j][1] == 0:
                    table[j][1], table[j][2], table[j][3] = table[j][2], table[j][3], 0
            raw = [table[j][2], table[j][3]]
            if len(set(raw)) > 1:
                while table[j][2] == 0:
                    table[j][2], table[j][3] = table[j][3], 0
            if table[j][2] == table[j][3] and table[j][0] == table[j][1]:
                score += table[j][2] + table[j][3] + table[j][0] + table[j][1]
                table[j][3], table[j][2], table[j][1], table[j][0] = 0, 0, table[j][2] + table[j][3], table[j][0] + table[j][1]
            elif table[j][0] == table[j][1]:
                score += table[j][0] + table[j][1]
                table[j][3], table[j][2], table[j][1], table[j][0] = 0, table[j][3], table[j][2], table[j][0] + table[j][1]
            elif table[j][1] == table[j][2]:
                score += table[j][2] + table[j][1]
                table[j][1], table[j][2], table[j][3] = table[j][2] + table[j][1], table[j][3], 0
            elif table[j][3] == table[j][2]:
                score += table[j][2] + table[j][3]
                table[j][2], table[j][3] = table[j][2] + table[j][3], 0

    def move_down():
        global table, score
        for j in range(4):
            raw = [table[j][0], table[j][1], table[j][2], table[j][3]]
            if len(set(raw)) > 1:
                while table[j][3] == 0:
                    table[j][0], table[j][1], table[j][2], table[j][3] = 0, table[j][0], table[j][1], table[j][2]
            raw = [table[j][0], table[j][1], table[j][2]]
            if len(set(raw)) > 1:
                while table[j][2] == 0:
                    table[j][0], table[j][1], table[j][2] = 0, table[j][0], table[j][1]
            raw = [table[j][0], table[j][1]]
            if len(set(raw)) > 1:
                while table[j][1] == 0:
                    table[j][0], table[j][1] = 0, table[j][0]
            if table[j][2] == table[j][3] and table[j][0] == table[j][1]:
                score += table[j][2] + table[j][3] + table[j][0] + table[j][1]
                table[j][3], table[j][2], table[j][1], table[j][0] = table[j][2] + table[j][3], table[j][0] + table[j][1], 0, 0
            elif table[j][2] == table[j][3]:
                score += table[j][2] + table[j][3]
                table[j][3], table[j][2], table[j][1], table[j][0] = table[j][2] + table[j][3], table[j][1], table[j][0], 0
            elif table[j][1] == table[j][2]:
                score += table[j][2] + table[j][1]
                table[j][2], table[j][1], table[j][0] = table[j][2] + table[j][1], table[j][0], 0
            elif table[j][0] == table[j][1]:
                score += table[j][1] + table[j][0]
                table[j][1], table[j][0] = table[j][1] + table[j][0], 0

    coordinates = []
    rand = range(10)
    for k in range(4):
        for m in range(4):
            coordinates.append((m, k))
    if choice(rand) == 6:
        a = choice(coordinates)
        b = choice(coordinates)
        while b == a:
            b = choice(coordinates)
        table[a[0]][a[1]] = 4
        if choice(rand) == 5:
            table[b[0]][b[1]] = 4
        else:
            table[b[0]][b[1]] = 2
    else:
        a = choice(coordinates)
        b = choice(coordinates)
        while b == a:
            b = choice(coordinates)
        table[a[0]][a[1]] = 2
        if choice(rand) == 5:
            table[b[0]][b[1]] = 4
        else:
            table[b[0]][b[1]] = 2
    for k in range(4):
        for m in range(4):
            if table[m][k] != 0:
                image_rect = images[int(log(table[m][k], 2)) - 1].get_rect(
                    topleft=(100 * m + 55, 100 * k + 55))
                sc.blit(images[int(log(table[m][k], 2)) - 1], image_rect)
                pg.display.update()
    text2 = f.render('0', True, (50, 50, 50), background)
    sc.blit(text2, (145, 10))
    text4 = f.render(best, True, (50, 50, 50), background)
    sc.blit(text4, (320, 10))
    pg.display.update()
    while True:
        for i in pg.event.get():
            if i.type == pg.KEYDOWN and not flag_game_over:
                for k in range(4):
                    for m in range(4):
                        pg.draw.rect(sc, background, (k * 100 + 55, m * 100 + 55, 95, 95))
                        pg.display.update()
                tmp_table = [[table[m][j] for j in range(4)] for m in range(4)]
                if i.key == pg.K_RIGHT:
                   move_right()
                elif i.key == pg.K_LEFT:
                    move_left()
                elif i.key == pg.K_UP:
                    move_up()
                elif i.key == pg.K_DOWN:
                    move_down()
                text2 = f.render(str(score), True, (50, 50, 50), background)
                sc.blit(text2, (145, 10))
                coordinates = []
                if tmp_table != table:
                    for k in range(4):
                        for m in range(4):
                            if table[m][k] == 0:
                                coordinates.append((m, k))
                    if choice(rand) == 6:
                        a = choice(coordinates)
                        table[a[0]][a[1]] = 4
                    else:
                        a = choice(coordinates)
                        table[a[0]][a[1]] = 2
                for k in range(4):
                    for m in range(4):
                        if table[m][k] != 0:
                            image_rect = images[int(log(table[m][k], 2)) - 1].get_rect(
                                topleft=(100 * m + 55, 100 * k + 55))
                            sc.blit(images[int(log(table[m][k], 2)) - 1], image_rect)
                            pg.display.update()
                flag = False
                flag_1024 = False
                flag_512 = False
                flag_256 = False
                flag_128 = False
                flag_64 = False
                f1 = pg.font.Font(None, 55)
                for k in table:
                    if 2048 in k:
                        flag = True
                    if 1024 in k:
                        flag_1024 = True
                    if 512 in k:
                        flag_512 = True
                    if 256 in k:
                        flag_256 = True
                    if 128 in k:
                        flag_128 = True
                    if 64 in k:
                        flag_64 = True
                pg.display.update()
                if flag:
                    text5 = f1.render("You win. That's possible?", True, (50, 50, 50))
                    sc.blit(text5, (10, 580))
                    pg.display.update()
                    break
                else:
                    flag = False
                    for k in table:
                        if 0 in k:
                            flag = True
                            break
                    if not flag:
                        for k in range(3):
                            for m in range(3):
                                if table[m][k] == table[m + 1][k] or table[m][k] == table[m][k + 1]:
                                    flag = True
                                    break
                        for k in range(3):
                            if table[3][k] == table[3][k + 1] or table[k][3] == table[k + 1][3]:
                                flag = True
                                break
                        if not flag:
                            f1 = pg.font.Font(None, 70)
                            for k in table:
                                if 1024 in k:
                                    flag = True
                            if flag:
                                flag_game_over = True
                                pg.draw.rect(sc, background, (50, 580, 400, 600))
                                text5 = f1.render('One step from... Game over', True, (50, 50, 50))
                                sc.blit(text5, (30, 580))
                            else:
                                flag_game_over = True
                                pg.draw.rect(sc, background, (50, 580, 400, 600))
                                text5 = f1.render('Game over', True, (50, 50, 50))
                                sc.blit(text5, (140, 575))
                            pg.display.update()
                            with open('Score.txt', 'w') as score_file:
                                if score > int(best):
                                    print(str(score), file=score_file)
                                else:
                                    print(best, file=score_file)
                if flag_1024:
                    pg.draw.rect(sc, background, (50, 580, 400, 600))
                    text5 = f1.render("One step from victory", True, (50, 50, 50))
                    sc.blit(text5, (50, 580))
                elif flag_512:
                    pg.draw.rect(sc, background, (50, 580, 400, 600))
                    text5 = f1.render("That was really hard", True, (50, 50, 50))
                    sc.blit(text5, (60, 580))
                elif flag_256:
                    pg.draw.rect(sc, background, (50, 580, 400, 600))
                    text5 = f1.render("That's big result!", True, (50, 50, 50))
                    sc.blit(text5, (90, 585))
                elif flag_128:
                    pg.draw.rect(sc, background, (50, 580, 400, 600))
                    text5 = f1.render("Well done!", True, (50, 50, 50))
                    sc.blit(text5, (150, 580))
                elif flag_64:
                    f1 = pg.font.Font(None, 60)
                    pg.draw.rect(sc, background, (50, 580, 400, 600))
                    text5 = f1.render("Good", True, (50, 50, 50))
                    sc.blit(text5, (180, 580))
            if i.type == pg.MOUSEBUTTONDOWN:
                if (i.pos[0] > 50 and i.pos[1] > 475) and i.pos[0] < 450 and i.pos[1] < 565:
                    _2048()
            if i.type == pg.QUIT:
                with open('Score.txt', 'w') as score_file:
                    if score > int(best):
                        print(str(score), file=score_file)
                    else:
                        print(best, file=score_file)
                sys.exit()
            clock.tick(fps)


_2048()
