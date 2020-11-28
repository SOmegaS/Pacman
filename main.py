import sys
import random
import pygame


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

    def killPacman(self, lives, game_status):
        lives -= 1
        if lives == 0:
            game_status = 2  # Смена статуса на 2 - экран Game Over
        return lives, game_status


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
    f.write(str(highscore) + '\n')  # Запись рекорда
    f.write(str(lives) + '\n')  # Запись жизней


def reset_area():
    area = [[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],  # Инициализация поля
            [3, 1, 5, 5, 5, 5, 5, 5, 5, 3, 5, 5, 5, 5, 5, 5, 5, 6, 3],
            [3, 5, 3, 3, 5, 3, 3, 3, 5, 3, 5, 3, 3, 3, 5, 3, 3, 5, 3],
            [3, 5, 3, 3, 5, 3, 3, 3, 5, 3, 5, 3, 3, 3, 5, 3, 3, 5, 3],
            [3, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 3],
            [3, 5, 3, 3, 5, 3, 5, 3, 3, 3, 3, 3, 5, 3, 5, 3, 3, 5, 3],
            [3, 5, 5, 5, 5, 3, 5, 3, 3, 3, 3, 3, 5, 3, 5, 5, 5, 5, 3],
            [3, 3, 3, 3, 5, 3, 6, 5, 5, 3, 5, 5, 6, 3, 5, 3, 3, 3, 3],
            [3, 3, 3, 3, 5, 3, 3, 3, 5, 3, 5, 3, 3, 3, 5, 3, 3, 3, 3],
            [3, 3, 3, 3, 5, 3, 5, 5, 5, 5, 5, 5, 5, 3, 5, 3, 3, 3, 3],
            [3, 3, 3, 3, 5, 3, 5, 3, 3, 5, 3, 3, 5, 3, 5, 3, 3, 3, 3],
            [3, 3, 3, 3, 5, 3, 5, 3, 0, 2, 0, 3, 5, 3, 5, 3, 3, 3, 3],
            [3, 6, 5, 5, 5, 5, 5, 3, 2, 2, 2, 3, 5, 5, 5, 5, 5, 6, 3],
            [3, 3, 3, 3, 5, 3, 5, 3, 3, 3, 3, 3, 5, 3, 5, 3, 3, 3, 3],
            [3, 3, 3, 3, 5, 3, 5, 5, 5, 5, 5, 5, 5, 3, 5, 3, 3, 3, 3],
            [3, 3, 3, 3, 5, 3, 5, 3, 3, 3, 3, 3, 5, 3, 5, 3, 3, 3, 3],
            [3, 3, 3, 3, 5, 3, 5, 3, 3, 3, 3, 3, 5, 3, 5, 3, 3, 3, 3],
            [3, 3, 3, 3, 5, 5, 5, 5, 5, 3, 5, 5, 5, 5, 5, 3, 3, 3, 3],
            [3, 5, 5, 5, 5, 3, 3, 3, 5, 3, 5, 3, 3, 3, 5, 5, 5, 5, 3],
            [3, 5, 3, 3, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 3, 3, 5, 3],
            [3, 5, 3, 3, 5, 3, 5, 3, 3, 3, 3, 3, 5, 3, 5, 3, 3, 5, 3],
            [3, 5, 5, 5, 5, 3, 5, 5, 5, 3, 5, 5, 5, 3, 5, 5, 5, 5, 3],
            [3, 5, 3, 3, 3, 3, 3, 3, 5, 3, 5, 3, 3, 3, 3, 3, 3, 5, 3],
            [3, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 3],
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
                [3, 1, 5, 5, 5, 5, 5, 5, 5, 3, 5, 5, 5, 5, 5, 5, 5, 6, 3],
                [3, 5, 3, 3, 5, 3, 3, 3, 5, 3, 5, 3, 3, 3, 5, 3, 3, 5, 3],
                [3, 5, 3, 3, 5, 3, 3, 3, 5, 3, 5, 3, 3, 3, 5, 3, 3, 5, 3],
                [3, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 3],
                [3, 5, 3, 3, 5, 3, 5, 3, 3, 3, 3, 3, 5, 3, 5, 3, 3, 5, 3],
                [3, 5, 5, 5, 5, 3, 5, 3, 3, 3, 3, 3, 5, 3, 5, 5, 5, 5, 3],
                [3, 3, 3, 3, 5, 3, 6, 5, 5, 3, 5, 5, 6, 3, 5, 3, 3, 3, 3],
                [3, 3, 3, 3, 5, 3, 3, 3, 5, 3, 5, 3, 3, 3, 5, 3, 3, 3, 3],
                [3, 3, 3, 3, 5, 3, 5, 5, 5, 5, 5, 5, 5, 3, 5, 3, 3, 3, 3],
                [3, 3, 3, 3, 5, 3, 5, 3, 3, 5, 3, 3, 5, 3, 5, 3, 3, 3, 3],
                [3, 3, 3, 3, 5, 3, 5, 3, 0, 2, 0, 3, 5, 3, 5, 3, 3, 3, 3],
                [3, 6, 5, 5, 5, 5, 5, 3, 2, 2, 2, 3, 5, 5, 5, 5, 5, 6, 3],
                [3, 3, 3, 3, 5, 3, 5, 3, 3, 3, 3, 3, 5, 3, 5, 3, 3, 3, 3],
                [3, 3, 3, 3, 5, 3, 5, 5, 5, 5, 5, 5, 5, 3, 5, 3, 3, 3, 3],
                [3, 3, 3, 3, 5, 3, 5, 3, 3, 3, 3, 3, 5, 3, 5, 3, 3, 3, 3],
                [3, 3, 3, 3, 5, 3, 5, 3, 3, 3, 3, 3, 5, 3, 5, 3, 3, 3, 3],
                [3, 3, 3, 3, 5, 5, 5, 5, 5, 3, 5, 5, 5, 5, 5, 3, 3, 3, 3],
                [3, 5, 5, 5, 5, 3, 3, 3, 5, 3, 5, 3, 3, 3, 5, 5, 5, 5, 3],
                [3, 5, 3, 3, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 3, 3, 5, 3],
                [3, 5, 3, 3, 5, 3, 5, 3, 3, 3, 3, 3, 5, 3, 5, 3, 3, 5, 3],
                [3, 5, 5, 5, 5, 3, 5, 5, 5, 3, 5, 5, 5, 3, 5, 5, 5, 5, 3],
                [3, 5, 3, 3, 3, 3, 3, 3, 5, 3, 5, 3, 3, 3, 3, 3, 3, 5, 3],
                [3, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 3],
                [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
                ]
        x = 30  # x pacman-а
        y = 30  # y pacman-а
        x_mat = 1  # x pacman-а в массиве
        y_mat = 1  # y pacman-а в массиве
        score = 0  # Счет
        lives = 3
        highscore = 0  # Рекорд
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
    game_status = 0  # состояния игры : 0 - стартовое меню, 1 - игра, 2 - смерть, любое другое число выхол из программы
    # массив призраков
    ghosts = [Ghost(RED, 9, 11), Ghost(YELLOW, 9, 12), Ghost(GREEN, 8, 12), Ghost(ORANGE, 10, 12)]
    # 0 - пусто 1 - пакмен 2 - призрак 3 - стена      5 - зерно

    FPS = 60  # Кадры в секунду
    clock = pygame.time.Clock()

    # Объявление глобальных переменных
    pygame.font.SysFont('', 36)  # Установка шрифта
    vector = [False, False, False, False]  # Вектор движения: влево, вправо, вверх, вниз
    tick = 0  # Номер тика
    pause = False  # Включена ли пауза
    reset = False  # Положение сброса
    p_prev_pressed = True  # Была ли нажата буква p в предыдущий тик
    lives = 3  # Количество жизней
    tickbig = 0  # для больших зерен просто забей
    volume_on = True  # Переменная, отвечающая за звук
    # Загрузка файлов
    image_restart = pygame.image.load('images/restart.png')  # Объявление изображения кнопки сброса
    image_restart_mini = pygame.image.load('images/restart_mini.png')  # Объявление изображения маленькой кнопки сброса
    image_pause = pygame.image.load('images/pause.png')  # Объявление изображения кнопки паузы
    image_map = pygame.image.load('images/map.png')  # Объявление изображения поля
    image_volume_on = pygame.image.load('images/Volume_on.png')  # Объявление изображения кнопки звука (вкл.)
    image_volume_off = pygame.image.load('images/Volume_off.png')  # Объявление изображения кнопки звука (выкл.)
    image_pacman_right = pygame.image.load('images/pacman_right.gif')  # Загрузка изображения пакмена
    image_pacman_left = pygame.image.load('images/pacman_left.gif')
    image_pacman_up = pygame.image.load('images/pacman_up.gif')
    image_pacman_down = pygame.image.load('images/pacman_down.gif')
    image_ghost = pygame.image.load('images/ghost.gif')  # Загрузка изображения призрака
    # Главный цикл
    while run:
        tickbig +=1

        # Экран стартового меню
        if game_status == 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Закрытие программы
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    # Старт новой игры
                    if (mouse_x >= 100) & (mouse_x <= 290) & (mouse_y >= 300) & (mouse_y <= 340):
                        game_status = 1  # Смена статуса на 1 - экран игры
                        area, score, x, y, x_mat, y_mat, lives = reset_area()  # Перезапуск
                        ghosts = [Ghost(RED, 9, 11), Ghost(YELLOW, 9, 12), Ghost(GREEN, 8, 12), Ghost(ORANGE, 10, 12)]  # Перенос призраков на их стартовые места
                    # Продолжить игру
                    if (mouse_x >= 100) & (mouse_x <= 290) & (mouse_y >= 380) & (mouse_y <= 420):
                        game_status = 1 # Смена статуса на 1 - экран игры
            pygame.draw.rect(screen, (0, 255, 0), (100, 300, 190, 40))  # Кнопка старта новый игры
            f1 = pygame.font.Font("font.ttf", 100)  # Объявление шрифта
            f2 = pygame.font.Font("font.ttf", 40)  # Объявление шрифта
            f3 = pygame.font.Font("font.ttf", 20)  # Объявление шрифта
            start_new_text = f2.render("New game   " , False, (255, 255, 255))  # Текст на кнопке старта новый игры
            game_name_text = f1.render("PACMAN   ", False, (255, 240, 0))  # Текст PACMAN
            highscore_text = f2.render("Highscore       " + str(highscore), False, (190, 235, 255))  # Текст рекордного счета

            created_by_text = f3.render("Created    by    promS101", False, (190, 235, 255))  # Авторы
            screen.blit(start_new_text, (115, 301))
            screen.blit(game_name_text, (30, 20))
            screen.blit(created_by_text, (88, 100))
            screen.blit(highscore_text, (45, 180))
            if score != 0:
                pygame.draw.rect(screen, (0, 255, 0), (100, 380, 190, 40))  # Кнопка продолжить игру
                continue_text = f2.render("Continue   ", False, (255, 255, 255))  # Текст на кнопке продолжить игру
                score_text = f2.render("Score                         " + str(score), False, (190, 235, 255))  # Текст счета
                screen.blit(continue_text, (107, 381))
                screen.blit(score_text, (45, 220))

            pygame.display.update()
        # Экран самой игры
        if game_status == 1:
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
                    # Обработка сброса, паузы и кнопки звука во время паузы через мышку
                    if pause:
                        if pause & (mouse_x >= 100) & (mouse_x <= 160) & (mouse_y >= 200) & (mouse_y <= 280):
                            pause = False
                        if (mouse_x >= 250) & (mouse_x <= 310) & (mouse_y >= 200) & (mouse_y <= 280):
                            reset = True
                        if volume_on & (mouse_x >= 30) & (mouse_x <= 70) & (mouse_y >= 20) & (mouse_y <= 60):
                            volume_on = False
                        elif (mouse_x >= 30) & (mouse_x <= 70) & (mouse_y >= 20) & (mouse_y <= 60):
                            volume_on = True
            if reset:
                reset = False
                area, score, x, y, x_mat, y_mat, lives = reset_area()
                ghosts = [Ghost(RED, 9, 11), Ghost(YELLOW, 9, 12), Ghost(GREEN, 8, 12), Ghost(ORANGE, 10, 12)]  # Перенос призраков на их стартовые места
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
                for g in ghosts:  # Перемещение призраков
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
            if highscore < score:
                highscore = score

            # Колизия пакмана и призрака
            for g in ghosts:
                if (g.get_x() == (x_mat + 1) * 20 - 10) & (g.get_y() == (y_mat + 1) * 20 - 10):
                    lives, game_status = ghosts[1].killPacman(lives, game_status)
                    x_mat = 1
                    y_mat = 1
                    x = 30
                    y = 30
                    vector = [False, False, False, False]
            # Отрисовка
            screen.fill((0, 0, 0))
            screen.blit(image_map, (0, 0))  # Отрисовка поля
            # Поклеточная отрисовка
            q = 0  # Счётчик для призраков
            for i in range(win_height_cell):
                for j in range(win_width_cell):
                    if area[i][j] == 2:
                        # Отрисовка призраков
                        screen.blit(image_ghost, (ghosts[q].get_x() - 10, ghosts[q].get_y() - 10))
                        q += 1
                    if area[i][j] == 5:  # Отрисовка зерен
                        pygame.draw.circle(screen, (255, 240, 220), (10 + 20 * j, 10 + 20 * i), 3)
                    if (area[i][j] == 6) and (tickbig % 25 < 12):  # Отрисовка зерен
                        pygame.draw.circle(screen, (255, 230, 0), (10 + 20 * j, 10 + 20 * i), 6)
                    if (area[i][j] == 6) and (tickbig % 25 >= 12):  # Отрисовка зерен
                        pygame.draw.circle(screen, (255, 230, 0), (10 + 20 * j, 10 + 20 * i), 0)
            if vector[0]:  # Отрисовка pacman-а
                screen.blit(image_pacman_left, (x - 10, y - 10))
            elif vector[2]:
                screen.blit(image_pacman_up, (x - 10, y - 10))
            elif vector[3]:
                screen.blit(image_pacman_down, (x - 10, y - 10))
            else:
                screen.blit(image_pacman_right, (x - 10, y - 10))

            f2 = pygame.font.Font("font.ttf", 20)  # Объявление шрифта
            score_text = f2.render("Score   " + str(score), False, (255, 255, 255))   # Текст текущего счета
            highscore_text = f2.render("Highscore   " + str(highscore), False, (255, 255, 255))  # Текст рекордного счета
            live_text = f2.render("Lives   " + str(lives), False, (230, 230, 255))  # Текст количестка жизней
            screen.blit(score_text, (265, 0))  # Вывод текущих очков
            screen.blit(highscore_text, (20, 0))  # Вывод рекорда
            screen.blit(live_text, (20, 480))  # Вывод количества жизней
            image_restart_mini.set_colorkey((0, 0, 0))  # Отрисовка кнопки сброса
            screen.blit(image_restart_mini, (205, 2))  # Отрисовка кнопки сброса
            pygame.draw.rect(screen, (255, 255, 255), (184, 5, 4, 13))  # Отрисовка паузы
            pygame.draw.rect(screen, (255, 255, 255), (194, 5, 4, 13))  # Отрисовка паузы
            if pause:
                sc = pygame.Surface((380, 500))  # Установка затемнённого поля
                sc.set_alpha(230)  # Установка уровня прозрачности
                sc.fill((0, 0, 0))  # Заполнение полупрозрачного фона
                screen.blit(sc, (0, 0))  # Отрисовка полупрозрачного фона
                image_restart.set_colorkey((0, 0, 0))  # Загрузка картинки без чёрного фона
                screen.blit(image_restart, (250, 200))  # Отрисовка кнопки сброса
                image_pause.set_colorkey((0, 0, 0))  # Загрузка картинки без чёрного фона
                screen.blit(image_pause, (100, 200))    # Отрисовка кнопки паузы
                image_restart.set_colorkey((0, 0, 0))  # Загрузка картинки без чёрного фона
                if volume_on:
                    screen.blit(image_volume_on, (30, 20))  # Отрисовка кнопки звука (вкл.)
                else:
                    screen.blit(image_volume_off, (30, 20))  # Отрисовка кнопки звука (выкл.)
            pygame.display.update()

        # Экран Game Over
        if game_status == 2:
            lives = 3
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Закрытие программы
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    # Обработка старта новый игры
                    if (mouse_x >= 100) & (mouse_x <= 290) & (mouse_y >= 340) & (mouse_y <= 380):
                        game_status = 1  # Смена статуса на 1 - экран игры
                        area, score, x, y, x_mat, y_mat, lives = reset_area()  # Перезапуск карты
                        ghosts = [Ghost(RED, 9, 11), Ghost(YELLOW, 9, 12), Ghost(GREEN, 8, 12), Ghost(ORANGE, 10, 12)]  # Перенос призраков на их стартовые места

            # Отрисовка
            screen.fill((0, 0, 0))
            pygame.draw.rect(screen, (0, 255, 0), (100, 340, 190, 40)) # Кнопка рестарта
            f1 = pygame.font.Font("font.ttf", 70)  # Объявление шрифта
            f2 = pygame.font.Font("font.ttf", 40)  # Объявление шрифта
            restart_text = f2.render("New game   ", False, (255, 255, 255))  # Текст на кнопке рестарта
            gameover_text = f1.render("Game Over   ", False, (255, 0, 0))  # Текст Game Over
            highscore_text = f2.render("Highscore       " + str(highscore), False, (190, 235, 255))  # Текст рекордного счета
            score_text = f2.render("Score                         " + str(score), False, (190, 235, 255))  # Текст счета
            screen.blit(restart_text, (115, 341))  # Отрисовка текста рестарт
            screen.blit(gameover_text, (30, 60))  # Отрисовка текста завершения игры
            screen.blit(highscore_text, (45, 180))  # Отрисовка рекорда
            screen.blit(score_text, (45, 220))  # Отрисовка счета
            pygame.display.update()

    # Выход из игры
    save(area, score, x, y, x_mat, y_mat, highscore, lives)  # Сохранение
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()


