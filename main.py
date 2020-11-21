import pygame
import sys
import random


class Ghost:
    def __init__(self, clr, x, y):
        self.color = clr
        self.x = 10 + 20 * x
        self.y = 10 + 20 * y
        self.x_mat = x
        self.y_mat = y
        self.vector = [False, False, False, False]

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_xmat(self):
        return self.x_mat

    def get_ymat(self):
        return self.y_mat

    def get_vector(self):
        return self.vector

    def get_color(self):
        return self.color

    def move(self, x, y):
        self.x += x
        self.y += y

    def move_mat(self, x, y):
        self.x_mat += x
        self.y_mat += y

    def set_vector(self, v):
        self.vector = v

    def killPacman(self):
        pass

def save(area, score, x, y, x_mat, y_mat, highscore, lives):  # Сохранение
    f = open('memo.txt', 'w')  # Файл сохранения
    for i in range(len(area)):  # Запись поля
        for j in range(len(area[0])):
            f.write(str(area[i][j]) + ' ')
        f.write('\n')
    f.write(str(score) + '\n')  # Запись счета
    f.write(str(x) + '\n')  # Запись x pacman-а
    f.write(str(y) + '\n')  # Запись y pacman-а
    f.write(str(x_mat) + '\n')  # Запись x pacman-а в массиве поля
    f.write(str(y_mat) + '\n')  # Запись y pacman-а в массиве поля
    f.write(str(highscore) + '\n') # Запись рекорда
    f.write(str(lives) + '\n')  # Запись жизней


def reset_area():
    area = [[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],  # Инициализация поля
            [3, 1, 5, 5, 5, 5, 5, 5, 5, 3, 5, 5, 5, 5, 5, 5, 5, 5, 3],
            [3, 5, 3, 3, 5, 3, 3, 3, 5, 3, 5, 3, 3, 3, 5, 3, 3, 5, 3],
            [3, 5, 3, 3, 5, 3, 3, 3, 5, 3, 5, 3, 3, 3, 5, 3, 3, 5, 3],
            [3, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 3],
            [3, 5, 3, 3, 5, 3, 5, 3, 3, 3, 3, 3, 5, 3, 5, 3, 3, 5, 3],
            [3, 5, 5, 5, 5, 3, 5, 3, 3, 3, 3, 3, 5, 3, 5, 5, 5, 5, 3],
            [3, 3, 3, 3, 5, 3, 5, 5, 5, 3, 5, 5, 5, 3, 5, 3, 3, 3, 3],
            [3, 3, 3, 3, 5, 3, 3, 3, 5, 3, 5, 3, 3, 3, 5, 3, 3, 3, 3],
            [3, 3, 3, 3, 5, 3, 5, 5, 5, 5, 5, 5, 5, 3, 5, 3, 3, 3, 3],
            [3, 3, 3, 3, 5, 3, 5, 3, 3, 5, 3, 3, 5, 3, 5, 3, 3, 3, 3],
            [3, 3, 3, 3, 5, 3, 5, 3, 0, 2, 0, 3, 5, 3, 5, 3, 3, 3, 3],
            [3, 5, 5, 5, 5, 5, 5, 3, 2, 2, 2, 3, 5, 5, 5, 5, 5, 5, 3],
            [3, 3, 3, 3, 5, 3, 5, 3, 3, 3, 3, 3, 5, 3, 5, 3, 3, 3, 3],
            [3, 3, 3, 3, 5, 3, 5, 5, 5, 5, 5, 5, 5, 3, 5, 3, 3, 3, 3],
            [3, 3, 3, 3, 5, 3, 5, 3, 3, 3, 3, 3, 5, 3, 5, 3, 3, 3, 3],
            [3, 3, 3, 3, 5, 3, 5, 3, 3, 3, 3, 3, 5, 3, 5, 3, 3, 3, 3],
            [3, 3, 3, 3, 5, 5, 5, 5, 5, 3, 5, 5, 5, 5, 5, 3, 3, 3, 3],
            [3, 5, 5, 5, 5, 3, 3, 3, 5, 3, 5, 3, 3, 3, 5, 5, 5, 5, 3],
            [3, 5, 3, 3, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 3, 3, 5, 3],
            [3, 5, 3, 3, 5, 3, 5, 3, 3, 3, 3, 3, 5, 3, 5, 3, 3, 5, 3],
            [3, 5, 5, 5, 5, 3, 5, 5, 5, 3, 5, 5, 5, 3, 5, 5, 5, 5, 3],
            [3, 5, 3, 3, 3, 3, 3, 3, 5, 3, 5, 3, 3, 3, 3, 3, 3, 5, 3],
            [3, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 3],
            [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
            ]
    x = 30  # x pacman-а
    y = 30  # y pacman-а
    x_mat = 1  # x pacman-а в массиве
    y_mat = 1  # y pacman-а в массиве
    score = 0  # Счет
    lives = 3
    return area, score, x, y, x_mat, y_mat, lives


def init(win_height_cell):  # Инициализация данных из сохранения
    try:
        f = open('memo.txt', 'r')  # Файл сохранения
        area = []
        for i in range(win_height_cell):  # Считывание поля
            area.append(list(map(int, f.readline().split())))
        score = int(f.readline())  # Считывание счета
        x = int(f.readline())  # Считывание x pacman-а
        y = int(f.readline())  # Считывание y pacman-а
        x_mat = int(f.readline())  # Считывание x pacman-а в массиве поля
        y_mat = int(f.readline())  # Считывание y pacman-а в массиве поля
        highscore = int(f.readline())  # Считывание рекорда
        lives = int(f.readline())  # Считывание жизней
    except FileNotFoundError:  # Ловим ошибку несуществования файла сохранения
        area = [[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],  # Инициализация поля
                [3, 1, 5, 5, 5, 5, 5, 5, 5, 3, 5, 5, 5, 5, 5, 5, 5, 5, 3],
                [3, 5, 3, 3, 5, 3, 3, 3, 5, 3, 5, 3, 3, 3, 5, 3, 3, 5, 3],
                [3, 5, 3, 3, 5, 3, 3, 3, 5, 3, 5, 3, 3, 3, 5, 3, 3, 5, 3],
                [3, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 3],
                [3, 5, 3, 3, 5, 3, 5, 3, 3, 3, 3, 3, 5, 3, 5, 3, 3, 5, 3],
                [3, 5, 5, 5, 5, 3, 5, 3, 3, 3, 3, 3, 5, 3, 5, 5, 5, 5, 3],
                [3, 3, 3, 3, 5, 3, 5, 5, 5, 3, 5, 5, 5, 3, 5, 3, 3, 3, 3],
                [3, 3, 3, 3, 5, 3, 3, 3, 5, 3, 5, 3, 3, 3, 5, 3, 3, 3, 3],
                [3, 3, 3, 3, 5, 3, 5, 5, 5, 5, 5, 5, 5, 3, 5, 3, 3, 3, 3],
                [3, 3, 3, 3, 5, 3, 5, 3, 3, 5, 3, 3, 5, 3, 5, 3, 3, 3, 3],
                [3, 3, 3, 3, 5, 3, 5, 3, 0, 2, 0, 3, 5, 3, 5, 3, 3, 3, 3],
                [3, 5, 5, 5, 5, 5, 5, 3, 2, 2, 2, 3, 5, 5, 5, 5, 5, 5, 3],
                [3, 3, 3, 3, 5, 3, 5, 3, 3, 3, 3, 3, 5, 3, 5, 3, 3, 3, 3],
                [3, 3, 3, 3, 5, 3, 5, 5, 5, 5, 5, 5, 5, 3, 5, 3, 3, 3, 3],
                [3, 3, 3, 3, 5, 3, 5, 3, 3, 3, 3, 3, 5, 3, 5, 3, 3, 3, 3],
                [3, 3, 3, 3, 5, 3, 5, 3, 3, 3, 3, 3, 5, 3, 5, 3, 3, 3, 3],
                [3, 3, 3, 3, 5, 5, 5, 5, 5, 3, 5, 5, 5, 5, 5, 3, 3, 3, 3],
                [3, 5, 5, 5, 5, 3, 3, 3, 5, 3, 5, 3, 3, 3, 5, 5, 5, 5, 3],
                [3, 5, 3, 3, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 3, 3, 5, 3],
                [3, 5, 3, 3, 5, 3, 5, 3, 3, 3, 3, 3, 5, 3, 5, 3, 3, 5, 3],
                [3, 5, 5, 5, 5, 3, 5, 5, 5, 3, 5, 5, 5, 3, 5, 5, 5, 5, 3],
                [3, 5, 3, 3, 3, 3, 3, 3, 5, 3, 5, 3, 3, 3, 3, 3, 3, 5, 3],
                [3, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 3],
                [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
                ]
        x = 30  # x pacman-а
        y = 30  # y pacman-а
        x_mat = 1  # x pacman-а в массиве
        y_mat = 1  # y pacman-а в массиве
        score = 0  # Счет
        lives = 3
        highscore = 0  # Рекрод
    return area, score, x, y, x_mat, y_mat, highscore, lives

RED = 255, 0, 0
ORANGE = 255, 153, 0
YELLOW = 251, 255, 0
GREEN = 0, 255, 0

def main():
    pygame.init()
    len_side_cell = 20  # Длина стороны клетки в пикселях
    win_width_cell = 19  # Количество клеток по ширине окна
    win_height_cell = 25  # Количество клеток по длине окна
    screen = pygame.display.set_mode((len_side_cell * win_width_cell, len_side_cell * win_height_cell))
    pygame.display.set_caption("Pacman")  # Имя окна приложения
    area, score, x, y, x_mat, y_mat, highscore, lives = init(win_height_cell)
    speed = 2  # Скорость pacman-а
    run = True  # Индикатор состояния игры
    # массив призраков
    ghosts = [Ghost(RED, 9, 11), Ghost(YELLOW, 9, 12), Ghost(GREEN, 8, 12), Ghost(ORANGE, 10, 12)]
    # 0 - пусто 1 - пакмен 2 - призрак 3 - стена      5 - зерно

    FPS = 60  # Кадры в секунду
    clock = pygame.time.Clock()

    # Вывод массива поля для отладки
    # for row in area:
    #     for elem in row:
    #         print(elem, end=',')
    #     print()

    pygame.font.SysFont('', 36)  # Установка шрифта
    vector = [False, False, False, False]  # Вектор движения: влево, вправо, вверх, вниз
    tick = 0  # Номер тика
    pause = False  # Включена ли пауза
    reset = False  # Положение сброса
    p_prev_pressed = True  # Была ли нажата буква p в предыдущий тик
    lives = 3  # Количество жизней

    # Главный цикл
    while run:
        clock.tick(FPS)
        # Отлавливание событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                # Обработка паузы, сброса и продолжения игры через мышку
                if (mouse_x >= 184) & (mouse_x <= 198) & (mouse_y >= 5) & (mouse_y <= 18):
                    pause = True
                if (mouse_x >= 205) & (mouse_x <= 220) & (mouse_y >= 5) & (mouse_y <= 18):
                    reset = True
                if pause & (mouse_x >= 150) & (mouse_x <= 240) & (mouse_y >= 200) & (mouse_y <= 300):
                    pause = False
        if reset:
            reset = False
            area, score, x, y, x_mat, y_mat, lives = reset_area()
        if (tick == 0) & (not pause):
            # Изменение координат призраков
            for g in ghosts:
                vectorGhost = [False, False, False, False]
                step = random.randint(0, 3)
                if step == 0:  # влево
                    if area[g.get_ymat()][g.get_xmat() - 1] != 3:
                        g.move_mat(-1, 0)
                        vectorGhost[step] = True
                if step == 1:  # вправо
                    if area[g.get_ymat()][g.get_xmat() + 1] != 3:
                        g.move_mat(1, 0)
                        vectorGhost[step] = True
                if step == 2:  # вверх
                    if area[g.get_ymat() - 1][g.get_xmat()] != 3:
                        g.move_mat(0, -1)
                        vectorGhost[step] = True
                if step == 3:  # вниз
                    if area[g.get_ymat() + 1][g.get_xmat()] != 3:
                        g.move_mat(0, 1)
                        vectorGhost[step] = True
                g.set_vector(vectorGhost)

            vector = [False, False, False, False]
            # Отлавливание нажатий клавиш
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:  # Влево
                if (x_mat == 1) & (y_mat == 12):  # Проверка на телепорт
                    x_mat = 17
                    x += 16 * len_side_cell
                elif area[y_mat][x_mat - 1] != 3:  # Коллизия со стенками
                    x_mat -= 1
                    vector[0] = True
                if area[y_mat][x_mat] == 5:  # Поглощение зерен
                    score += 5
                    area[y_mat][x_mat] = 0
            if keys[pygame.K_d]:  # Вправо
                if (x_mat == 17) & (y_mat == 12):  # Проверка на телепорт
                    x_mat = 1
                    x -= 16 * len_side_cell
                elif area[y_mat][x_mat + 1] != 3:  # Коллизия со стенками
                    x_mat += 1
                    vector[1] = True
                if area[y_mat][x_mat] == 5:  # Поглощение зерен
                    score += 5
                    area[y_mat][x_mat] = 0
            if keys[pygame.K_w]:  # Вверх
                if area[y_mat - 1][x_mat] != 3:  # Коллизия со стенками
                    y_mat -= 1
                    vector[2] = True
                if area[y_mat][x_mat] == 5:  # Поглощение зерен
                    score += 5
                    area[y_mat][x_mat] = 0
            if keys[pygame.K_s]:  # Вниз
                if area[y_mat + 1][x_mat] != 3:  # Коллизия со стенками
                    y_mat += 1
                    vector[3] = True
                if area[y_mat][x_mat] == 5:  # Поглощение зерен
                    score += 5
                    area[y_mat][x_mat] = 0
            p_prev_pressed = keys[pygame.K_p]  # Нажата ли клавиша p
            pause = keys[pygame.K_p]  # Включена ли пауза
        elif pause:  # Если пауза, проверять только кнопку p
            keys = pygame.key.get_pressed()
            if (not p_prev_pressed) & keys[pygame.K_p]:
                pause = False
            p_prev_pressed = keys[pygame.K_p]  # Это чтобы не было мигания паузы от удержания p
        if not pause:  # Движение, если не пауза
            if vector[0]:
                x -= speed
            if vector[1]:
                x += speed
            if vector[2]:
                y -= speed
            if vector[3]:
                y += speed
            for g in ghosts: # призраки
                vectorGhost = g.get_vector()
                if vectorGhost[0]:
                    g.move(speed * (-1), 0)
                if vectorGhost[1]:
                    g.move(speed, 0)
                if vectorGhost[2]:
                    g.move(0, speed * (-1))
                if vectorGhost[3]:
                    g.move(0, speed)

            tick = (1 + tick) % (len_side_cell / speed)  # Следующий тик

        # Обновление рекорда
        if highscore < score :
            highscore = score

        # Отрисовка
        screen.fill((0, 0, 0))
        # Поклеточная отрисовка
        q = 0  # счётчик для призраков
        for i in range(win_height_cell):
            for j in range(win_width_cell):
                if area[i][j] == 3:  # Отрисовка стенок
                    pygame.draw.rect(screen, (0, 85, 200),
                                     (0 + len_side_cell * j, 0 + len_side_cell * i, len_side_cell, len_side_cell))
                if area[i][j] == 2:
                    # отрисовка призраков
                    pygame.draw.circle(screen, ghosts[q].get_color(), (ghosts[q].get_x(), ghosts[q].get_y()), 7)
                    q += 1
                if area[i][j] == 5:  # Отрисовка зерен
                    pygame.draw.circle(screen, (255, 230, 0), (10 + 20 * j, 10 + 20 * i), 3)

        pygame.draw.circle(screen, (0, 250, 200), (x, y), 7)  # Отрисовка pacman-а
        f2 = pygame.font.Font("font.ttf", 20)  # Объявление шрифта
        score_text = f2.render("Score   " + str(score), False, (190, 235, 255))   # Текст текущего счета
        highscore_text = f2.render("Highscore   " + str(highscore), False, (190, 235, 255))  # Текст рекордного счета
        live_text = f2.render("Lives   " + str(lives), False, (190, 235, 255))  # Текст количестка жизней
        screen.blit(score_text, (265, 0))  # Вывод текущих очков
        screen.blit(highscore_text, (20, 0))  # Вывод рекорда
        screen.blit(live_text, (20, 480))  # Вывод количества жизней
        pygame.draw.rect(screen, (190, 235, 255), (205, 5, 12, 12))  # Отрисовка кнопки сброса
        pygame.draw.rect(screen, (190, 235, 255), (184, 5, 4, 13))  # Отрисовка паузы
        pygame.draw.rect(screen, (190, 235, 255), (194, 5, 4, 13))  # Отрисовка паузы
        if pause:  # Отрисовка "play" во время паузы
            pygame.draw.polygon(screen, (190, 235, 255), [[150, 200], [150, 300], [240, 250]])
        # print(score)
        pygame.display.update()

    # Выход из игры
    save(area, score, x, y, x_mat, y_mat, highscore, lives)
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
