import pygame
import sys


def main():
    pygame.init()
    len_side_cell = 20  # Длина стороны клетки в пикселях
    win_width_cell = 19  # Количество клеток по ширине окна
    win_height_cell = 25  # Количество клеток по длине окна
    screen = pygame.display.set_mode((len_side_cell * win_width_cell, len_side_cell * win_height_cell))
    pygame.display.set_caption("Pacman")  # Имя окна приложения
    x = 30  # x pacman-а
    y = 30  # y pacman-а
    x_mat = 1  # x pacman-а в массиве
    y_mat = 1  # y pacman-а в массиве
    score = 0  # Счет
    speed = 2  # Скорость pacman-а
    run = True  # Индикатор состояния игры
    # 0 - пусто 1 - пакмен 2 - призрак 3 - стена      5 - зерно

    FPS = 120  # Кадры в секунду
    clock = pygame.time.Clock()
    area = [[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [3, 1, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3],
            [3, 0, 3, 3, 0, 3, 3, 3, 0, 3, 0, 3, 3, 3, 0, 3, 3, 0, 3],
            [3, 0, 3, 3, 0, 3, 3, 3, 0, 3, 0, 3, 3, 3, 0, 3, 3, 0, 3],
            [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
            [3, 0, 3, 3, 0, 3, 0, 3, 3, 3, 3, 3, 0, 3, 0, 3, 3, 0, 3],
            [3, 0, 0, 0, 0, 3, 0, 3, 3, 3, 3, 3, 0, 3, 0, 0, 0, 0, 3],
            [3, 3, 3, 3, 0, 3, 0, 0, 0, 3, 0, 0, 0, 3, 0, 3, 3, 3, 3],
            [3, 3, 3, 3, 0, 3, 3, 3, 0, 3, 0, 3, 3, 3, 0, 3, 3, 3, 3],
            [3, 3, 3, 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 3, 3, 3, 3],
            [3, 3, 3, 3, 0, 3, 0, 3, 3, 0, 3, 3, 0, 3, 0, 3, 3, 3, 3],
            [3, 3, 3, 3, 0, 3, 0, 3, 0, 2, 0, 3, 0, 3, 0, 3, 3, 3, 3],
            [3, 0, 0, 0, 0, 0, 0, 3, 2, 2, 2, 3, 0, 0, 0, 0, 0, 0, 3],
            [3, 3, 3, 3, 0, 3, 0, 3, 3, 3, 3, 3, 0, 3, 0, 3, 3, 3, 3],
            [3, 3, 3, 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 3, 3, 3, 3],
            [3, 3, 3, 3, 0, 3, 0, 3, 3, 3, 3, 3, 0, 3, 0, 3, 3, 3, 3],
            [3, 3, 3, 3, 0, 3, 0, 3, 3, 3, 3, 3, 0, 3, 0, 3, 3, 3, 3],
            [3, 3, 3, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 3, 3, 3],
            [3, 0, 0, 0, 0, 3, 3, 3, 0, 3, 0, 3, 3, 3, 0, 0, 0, 0, 3],
            [3, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 3],
            [3, 0, 3, 3, 0, 3, 0, 3, 3, 3, 3, 3, 0, 3, 0, 3, 3, 0, 3],
            [3, 0, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 0, 3],
            [3, 0, 3, 3, 3, 3, 3, 3, 0, 3, 0, 3, 3, 3, 3, 3, 3, 0, 3],
            [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
            [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
            ]

    # Заполнение поля зернами
    for i in range(win_width_cell):
        for j in range(win_height_cell):
            if area[j][i] == 0:
                area[j][i] = 5
    area[11][8] = 0
    area[11][10] = 0

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
    pygame.font.SysFont('arial', 36)  # Установка шрифта
    vector = [False, False, False, False]  # Вектор движения: влево, вправо, вверх, вниз
    tick = 0  # Номер тика
    pause = False  # Включена ли пауза
    p_prev_pressed = True  # Была ли нажата буква p в предыдущий тик
    # Главный цикл
    while run:
        clock.tick(FPS)
        # Отлавливание событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

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
        f2 = pygame.font.SysFont('arial', 20)
        text2 = f2.render("Score: " + str(score), True, (0, 180, 0))
        screen.blit(text2, (135, 0))
        if pause:  # Отрисовка паузы
            pygame.draw.rect(screen, (169, 169, 169), (160, 200, 15, 100))
            pygame.draw.rect(screen, (169, 169, 169), (210, 200, 15, 100))
        # print(score)
        pygame.display.update()

    # Выход из игры
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
