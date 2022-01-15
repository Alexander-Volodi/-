# Установка
import pygame as pg
import sys

pg.init()
sc = pg.display.set_mode((760, 760))
clock = pg.time.Clock()
# Называние окна
pg.display.set_caption("Chess")
chess_icon = pg.image.load('Шахматный знак.png')
chess_icon.set_colorkey((255, 255, 255))
pg.display.set_icon(chess_icon)
# Обозначение координатных обозначений
sc.fill((222, 222, 222))
f1 = pg.font.Font(None, 60)
text1 = f1.render('8', True,
                  (0, 0, 0))
for i in range(8):
    text1 = f1.render(str(8 - i), True,
                      (0, 0, 0))
    sc.blit(text1, (10, 30 + i * 90))
for i in range(8):
    text1 = f1.render(chr(ord('A') + i), True,
                      (0, 0, 0))
    sc.blit(text1, (70 + i * 90, 721))
# Подготовка к зарисовке шахматного поля
LGREY = (200, 200, 200)
DGREY = (100, 100, 100)
x = 12
y = 3
swx = 40
swy = 0
chess_board = [[('', '')] * 8 for i in range(8)]

# Рисуем белые поля
for i in range(4):
    for j in range(4):
        pg.draw.rect(sc, LGREY,
                     (swx, swy, 90, 90))
        swx += 180
    swy += 180
    swx = 40
swx = 130
swy = 90
for i in range(4):
    for j in range(4):
        pg.draw.rect(sc, LGREY,
                     (swx, swy, 90, 90))
        swx += 180
    swy += 180
    swx = 130
    pg.display.update()
# Рисуем чёрные поля
swx = 130
swy = 0
for i in range(4):
    for j in range(4):
        pg.draw.rect(sc, DGREY,
                     (swx, swy, 90, 90))
        swx += 180
    swy += 180
    swx = 130
swx = 40
swy = 90
for i in range(4):
    for j in range(4):
        pg.draw.rect(sc, DGREY,
                     (swx, swy, 90, 90))
        swx += 180
    swy += 180
    swx = 40


# Функции, ищющие препятствия
def find_border_not_diagonal(tmp_c, minimum, maximum, vertical):
    r = 0
    if vertical:
        for a in range(minimum, maximum):
            if chess_board[a][tmp_c] != ('', ''):
                r = True
                break
            else:
                r = False
    else:
        for a in range(minimum, maximum):
            if chess_board[tmp_c][a] != ('', ''):
                r = True
                break
            else:
                r = False
    return r


def find_border_diagonal(minimum_x, minimum_y, maximum_x, maximum_y):
    r = 0
    for a in range(maximum_x - minimum_x):
        if ((tmp_coordinate_x - x_position) > 0) == ((tmp_coordinate_y - y_position) > 0):
            if chess_board[a + minimum_x][a + minimum_y] != ('', ''):
                r = True
                break
            else:
                r = False
        else:
            if chess_board[a + minimum_x][maximum_y - a - 1] != ('', ''):
                r = True
                break
            else:
                r = False
    return r


# Процедура по поставке фигур
def create_figure(vertical, horizontal, figure_title, figure_color):
    global tmp_coordinate_x
    global tmp_coordinate_y
    figure_surf = 0
    if figure_color == "Light":
        if figure_title == "Pawn":
            figure_surf = pg.image.load('Белая пешка.png')
        elif figure_title == "Rook":
            figure_surf = pg.image.load('Белая ладья.png')
        elif figure_title == "Knight":
            figure_surf = pg.image.load('Белый конь.png')
        elif figure_title == "Bishop":
            figure_surf = pg.image.load('Белый слон.png')
        elif figure_title == "Queen":
            figure_surf = pg.image.load('Белый ферзь.png')
        elif figure_title == "King":
            figure_surf = pg.image.load('Белый король.png')
    if figure_color == "Dark":
        if figure_title == "Pawn":
            figure_surf = pg.image.load('Чёрная пешка.png')
        elif figure_title == "Rook":
            figure_surf = pg.image.load('Чёрная ладья.png')
        elif figure_title == "Knight":
            figure_surf = pg.image.load('Чёрный конь.png')
        elif figure_title == "Bishop":
            figure_surf = pg.image.load('Чёрный слон.png')
        elif figure_title == "Queen":
            figure_surf = pg.image.load('Чёрный ферзь.png')
        elif figure_title == "King":
            figure_surf = pg.image.load('Чёрный король.png')
    figure_surf.set_colorkey((255, 255, 255))
    figure_rect = figure_surf.get_rect(
        bottomright=((vertical + 1) * 90 + x, (8 - horizontal) * 90 - y))
    sc.blit(figure_surf, figure_rect)
    chess_board[vertical][horizontal] = (figure_title, figure_color)


# Функция хода
def move(coordinate_x, coordinate_y, tmp_x, tmp_y, tmp_f):
    global attempt_to_make_a_move
    global l_turn
    global quantity_light_figures
    global quantity_dark_figures
    if chess_board[x_position][y_position] != ('', '') and chess_board[x_position][y_position] != tmp_f[1]:
        if chess_board[x_position][y_position][1] == 'Dark':
            quantity_dark_figures -= 1
        else:
            quantity_light_figures -= 1
    if chess_board[x_position][8 - (coordinate_y - y) // 90 - 1][1] != \
            tmp_f[1]:
        if ((i.pos[0] + swx) // 90 - 1) % 2 == (coordinate_y // 90 - 1) % 2:
            pg.draw.rect(sc, DGREY,
                         (((coordinate_x + swx) // 90 - 1) * 90 + swx, (coordinate_y // 90) * 90, 90, 90))
        else:
            pg.draw.rect(sc, LGREY,
                         (((coordinate_x + swx) // 90 - 1) * 90 + swx, (coordinate_y // 90) * 90, 90, 90))
    if tmp_x % 2 == tmp_y % 2:
        pg.draw.rect(sc, DGREY,
                     (tmp_x * 90 + swx, (8 - tmp_y - 1) * 90, 90, 90))
    else:
        pg.draw.rect(sc, LGREY,
                     (tmp_x * 90 + swx, (8 - tmp_y - 1) * 90, 90, 90))
    chess_board[(coordinate_x + swx + x) // 90 - 1][8 - (coordinate_y - y) // 90 - 1] = tmp_f
    chess_board[tmp_x][tmp_y] = ('', '')
    create_figure(x_position, 8 - (coordinate_y - y) // 90 - 1, tmp_f[0],
                  tmp_f[1])
    attempt_to_make_a_move = not attempt_to_make_a_move
    l_turn = not l_turn


# Обозначние атакуемыех клеток, как переменную
attacked_pleases_light = [[[False], 0] * 8 for i in range(8)]
attacked_pleases_dark = [[[False], 0] * 8 for i in range(8)]
# Начальная позиция: чёрные пешки
for i in range(8):
    create_figure(i, 6, "Pawn", "Dark")
# Начальная позиция: белые пешки
for i in range(8):
    create_figure(i, 1, "Pawn", "Light")
# Начальная позиция: чёрные ладьи
create_figure(0, 7, "Rook", "Dark")
create_figure(7, 7, "Rook", "Dark")
# Начальная позиция: белые ладьи
create_figure(0, 0, "Rook", "Light")
create_figure(7, 0, "Rook", "Light")
# Начальная позиция: чёрные кони
create_figure(1, 7, "Knight", "Dark")
create_figure(6, 7, "Knight", "Dark")
# Начальная позиция: белые кони
create_figure(1, 0, "Knight", "Light")
create_figure(6, 0, "Knight", "Light")
# Начальная позиция: чёрные слоны
create_figure(2, 7, "Bishop", "Dark")
create_figure(5, 7, "Bishop", "Dark")
# Начальная позиция: белые слоны
create_figure(2, 0, "Bishop", "Light")
create_figure(5, 0, "Bishop", "Light")
# Начальная позиция: чёрный ферзь
create_figure(3, 7, "Queen", "Dark")
# Начальная позиция: белый ферзь
create_figure(3, 0, "Queen", "Light")
# Начальная позиция: чёрный король
create_figure(4, 7, "King", "Dark")
# Начальная позиция: белый король
create_figure(4, 0, "King", "Light")
# Обновление экрана
pg.display.update()
# Каркас программы
attempt_to_make_a_move = False
tmp_coordinate_x, tmp_coordinate_y, tmp_figure = 0, 0, 0
l_turn = True
light_king_coordinate_x = 4
dark_king_coordinate_x = 4
light_king_coordinate_y = 0
dark_king_coordinate_y = 7
quantity_light_figures = 16
quantity_dark_figures = 16
while True:
    for i in pg.event.get():
        # Если игрок произвёл нажатие
        if i.type == pg.MOUSEBUTTONDOWN:
            x_position = (i.pos[0] + swx + x) // 90 - 1
            y_position = 8 - (i.pos[1] - y) // 90 - 1
            # Собирается ли игрок делать ход?
            if attempt_to_make_a_move:
                if i.button == 1:
                    if chess_board[x_position][y_position][1] != tmp_figure[1] and chess_board[x_position][y_position][0] \
                            != 'King':
                        if ((tmp_figure[0] == "Knight") and (abs(x_position - tmp_coordinate_x) *
                                                             abs(y_position - tmp_coordinate_y)) == 2):
                            # Совершение хода
                            move(i.pos[0], i.pos[1], tmp_coordinate_x, tmp_coordinate_y, tmp_figure)
                            continue
                        elif ((tmp_figure[0] == "Bishop") and (abs(x_position - tmp_coordinate_x)
                                                               == abs(y_position - tmp_coordinate_y))):
                            if not find_border_diagonal(min(tmp_coordinate_x, x_position) + 1,
                                                        min(tmp_coordinate_y, y_position) + 1,
                                                        max(tmp_coordinate_x, x_position),
                                                        max(tmp_coordinate_y, y_position)):
                                # Совершение хода
                                move(i.pos[0], i.pos[1], tmp_coordinate_x, tmp_coordinate_y, tmp_figure)
                                continue
                        elif ((tmp_figure[0] == "Rook") and ((abs(x_position - tmp_coordinate_x) == 0) or abs(
                                y_position - tmp_coordinate_y) == 0)):
                            # Проверяем, не преграждают ли нам путь фигуры
                            if ((not find_border_not_diagonal(tmp_coordinate_y, min(x_position, tmp_coordinate_x) + 1,
                                                              max(x_position, tmp_coordinate_x), True))
                                and (y_position - tmp_coordinate_y == 0)) or ((not find_border_not_diagonal
                                (tmp_coordinate_x, min(y_position, tmp_coordinate_y) + 1,
                                 max(y_position, tmp_coordinate_y), False))
                                                                              and (x_position - tmp_coordinate_x == 0)):
                                # Совершение хода
                                move(i.pos[0], i.pos[1], tmp_coordinate_x, tmp_coordinate_y, tmp_figure)
                                continue
                        elif ((tmp_figure[0] == "Queen") and (((abs(x_position - tmp_coordinate_x) == 0) or
                                                               abs(y_position - tmp_coordinate_y) == 0) or
                                                              (abs(x_position - tmp_coordinate_x) == abs(
                                                                  y_position - tmp_coordinate_y)))):
                            if abs(x_position - tmp_coordinate_x) == 0 or abs(y_position - tmp_coordinate_y) == 0:
                                if ((not find_border_not_diagonal(tmp_coordinate_y,
                                                                  min(x_position, tmp_coordinate_x) + 1,
                                                                  max(x_position, tmp_coordinate_x), True)) and
                                    (y_position - tmp_coordinate_y == 0)) or ((not find_border_not_diagonal
                                    (tmp_coordinate_x, min(y_position, tmp_coordinate_y) + 1,
                                     max(y_position, tmp_coordinate_y), False))
                                                                              and (x_position - tmp_coordinate_x == 0)):
                                    # Совершение хода
                                    move(i.pos[0], i.pos[1], tmp_coordinate_x, tmp_coordinate_y, tmp_figure)
                                    continue
                            else:
                                if not find_border_diagonal(min(tmp_coordinate_x, x_position) + 1,
                                                            min(tmp_coordinate_y, y_position) + 1,
                                                            max(tmp_coordinate_x, x_position),
                                                            max(tmp_coordinate_y, y_position)):
                                    # Совершение хода
                                    move(i.pos[0], i.pos[1], tmp_coordinate_x, tmp_coordinate_y, tmp_figure)
                                    continue
                        elif ((tmp_figure[0] == "King") and (((abs(x_position - tmp_coordinate_x) == 1) and
                                                              (abs(y_position - tmp_coordinate_y) <= 1)) or
                                                             ((abs(x_position - tmp_coordinate_x) <= 1) and
                                                              (abs(y_position - tmp_coordinate_y) == 1))) and
                              (((not attacked_pleases_dark[x_position][y_position][0]) and (tmp_figure[1] == 'Dark')) or
                               ((not attacked_pleases_light[x_position][y_position][0]) and (tmp_figure[1] == 'Light')))):
                            # Совершение хода
                            move(i.pos[0], i.pos[1], tmp_coordinate_x, tmp_coordinate_y, tmp_figure)
                            if tmp_figure[1] == 'Light':
                                light_king_coordinate_x = x_position
                                light_king_coordinate_y = y_position
                            else:
                                dark_king_coordinate_x = x_position
                                dark_king_coordinate_y = y_position
                            continue
                        elif tmp_figure[0] == "Pawn":
                            if (chess_board[x_position][y_position][1] != "Light") and \
                                    (chess_board[x_position][y_position][1] != "Dark"):
                                if tmp_figure[1] == "Light":
                                    if ((y_position - tmp_coordinate_y == 1) and (x_position - tmp_coordinate_x == 0)) \
                                            or ((tmp_coordinate_y == 1) and ((y_position - tmp_coordinate_y == 2) and
                                                                             (x_position - tmp_coordinate_x == 0)) and
                                                (chess_board[tmp_coordinate_x][2] == ('', ''))):
                                        # Совершение хода
                                        move(i.pos[0], i.pos[1], tmp_coordinate_x, tmp_coordinate_y, tmp_figure)
                                        continue
                                else:
                                    if ((y_position - tmp_coordinate_y == -1) and (x_position - tmp_coordinate_x == 0)) \
                                            or ((tmp_coordinate_y == 6) and ((y_position - tmp_coordinate_y == -2) and
                                                                             (x_position - tmp_coordinate_x == 0)) and
                                                (chess_board[tmp_coordinate_x][5] == ('', ''))):
                                        # Совершение хода
                                        move(i.pos[0], i.pos[1], tmp_coordinate_x, tmp_coordinate_y, tmp_figure)
                                        continue
                            else:
                                if tmp_figure[1] == "Light":
                                    if (y_position - tmp_coordinate_y == 1) \
                                            and (abs(x_position - tmp_coordinate_x) == 1):
                                        # Совершение хода
                                        move(i.pos[0], i.pos[1], tmp_coordinate_x, tmp_coordinate_y, tmp_figure)
                                        continue
                                else:
                                    if (y_position - tmp_coordinate_y == -1) and (
                                            abs(x_position - tmp_coordinate_x) == 1):
                                        # Совершение хода
                                        move(i.pos[0], i.pos[1], tmp_coordinate_x, tmp_coordinate_y, tmp_figure)
                                        continue
                elif i.button == 3:
                    attempt_to_make_a_move = not attempt_to_make_a_move
            else:
                # Ищем фигуру, которой игрок решил походить
                for c in ["Dark", "Light"]:
                    if attempt_to_make_a_move:
                        break
                    for f in ["Pawn", "Rook", "Knight", "Bishop", "Queen", "King"]:
                        # Если мы нашли фигуру, которую игрок решил использовать для своего хода
                        if (chess_board[x_position][y_position] == (f, c)) and (
                                chess_board[x_position][y_position] != ('', '')):
                            if ((chess_board[x_position][y_position][1] == "Light") and l_turn) or \
                                    ((chess_board[x_position][y_position][1] == "Dark") and (not l_turn)):
                                tmp_figure, tmp_coordinate_x, tmp_coordinate_y, = chess_board[x_position][
                                                                                      y_position], x_position, y_position
                                attempt_to_make_a_move = True
                                print(1)
                                break
        # Выход
        if i.type == pg.QUIT:
            sys.exit()
        # Окончание действие с целью не допустить зависание и с целью сделать ходы видимыми
        pg.display.update()
        clock.tick(20)
