import pygame
import sys


def save(area, score, x, y, x_mat, y_mat):  # Сохранение
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
    return area, score, x, y, x_mat, y_mat

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
    return area, score, x, y, x_mat, y_mat

def main():
    pygame.init()
    len_side_cell = 20  # Длина стороны клетки в пикселях
    win_width_cell = 19  # Количество клеток по ширине окна
    win_height_cell = 25  # Количество клеток по длине окна
    screen = pygame.display.set_mode((len_side_cell * win_width_cell, len_side_cell * win_height_cell))
    pygame.display.set_caption("Pacman")  # Имя окна приложения
    area, score, x, y, x_mat, y_mat = init(win_height_cell)
    speed = 2  # Скорость pacman-а
    run = True  # Индикатор состояния игры
    # 0 - пусто 1 - пакмен 2 - призрак 3 - стена      5 - зерно

    FPS = 60  # Кадры в секунду
    clock = pygame.time.Clock()

    # Пример заполнения матрицы
    # for i in range(win_height_cell):
    #     area.append([0] * win_width_cell)
    # for i in range(win_width_cell):
    #     area[0][i] = 3
    # for i in range(win_width_cell):
    #     area[win_height_cell-1][i] = 3
    # for i in range(win_height_cell):
    #     area[i][0] = 3
    # for i in range(win_height_cell):
    #     area[i][win_width_cell-1] = 3
    # for i in range(win_height_cell):
    #     area.append([0] * win_width_cell)

    # Вывод массива поля для отладки
    for row in area:
        for elem in row:
            print(elem, end=',')
        print()
    pygame.font.SysFont('', 36)  # Установка шрифта
    vector = [False, False, False, False]  # Вектор движения: влево, вправо, вверх, вниз
    tick = 0  # Номер тика
    pause = False  # Включена ли пауза
    reset = False # Положение сброса
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
                if (pause == True) & (mouse_x >= 150) & (mouse_x <= 240) & (mouse_y >= 200) & (mouse_y <= 300):
                    pause = False
        if (reset):
            reset = False
            area, score, x, y, x_mat, y_mat = reset_area()
        if (tick == 0) & (not pause):
            vector = [False, False, False, False]
            # Отлавливание нажатий клавиш
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:  # Влево
                if area[y_mat][x_mat - 1] != 3:  # Коллизия со стенками
                    x_mat -= 1
                    vector[0] = True
                if area[y_mat][x_mat] == 5:  # Поглощение зерен
                    score += 5
                    area[y_mat][x_mat] = 0
            if keys[pygame.K_d]:  # Вправо
                if area[y_mat][x_mat + 1] != 3:  # Коллизия со стенками
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
            p_prev_pressed = keys[pygame.K_p]
            pause = keys[pygame.K_p]
        elif pause:
            keys = pygame.key.get_pressed()
            if (not p_prev_pressed) & keys[pygame.K_p]:
                pause = False
            p_prev_pressed = keys[pygame.K_p]
        if not pause:
            if vector[0]:
                x -= speed
            if vector[1]:
                x += speed
            if vector[2]:
                y -= speed
            if vector[3]:
                y += speed
            tick = (1 + tick) % (len_side_cell / speed)

        # Отрисовка
        screen.fill((0, 0, 0))
        # Поклеточная отрисовка
        for i in range(win_height_cell):
            for j in range(win_width_cell):
                if area[i][j] == 3:  # Отрисовка стенок
                    pygame.draw.rect(screen, (0, 85, 200), (0 + len_side_cell * j, 0 + len_side_cell * i, len_side_cell, len_side_cell))
                if area[i][j] == 5:  # Отрисовка зерен
                    pygame.draw.circle(screen, (255, 230, 0), (10 + 20 * j, 10 + 20 * i), 3)
        pygame.draw.circle(screen, (0, 250, 200), (x, y), 7)  # Отрисовка pacman-а
        f2 = pygame.font.Font("font.ttf", 20)  # Объявление шрифта
        score_text = f2.render("Score   " + str(score), False, (190, 235, 255))
        highscore_text = f2.render("Highcore   " + str(score), False, (190, 235, 255))
        live_text = f2.render("Lives   ", False, (190, 235, 255))
        screen.blit(score_text, (265, 0))  # Вывод текущих очков
        screen.blit(highscore_text, (20, 0))  # Вывод рекорда
        screen.blit(live_text, (20, 480))  # Вывод количества жизней
        pygame.draw.rect(screen, (190, 235, 255), (205, 5, 12, 12)) #отрисовка кнопки сброса
        pygame.draw.rect(screen, (190, 235, 255), (184, 5, 4, 13))  # Отрисовка паузы
        pygame.draw.rect(screen, (190, 235, 255), (194, 5, 4, 13))  # Отрисовка паузы
        if pause:  # Отрисовка "play" во время паузы
            pygame.draw.polygon(screen, (190, 235, 255), [[150, 200], [150, 300], [240, 250]])
        # print(score)
        pygame.display.update()

    # Выход из игры
    save(area, score, x, y, x_mat, y_mat)
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
