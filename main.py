import sys
import pygame
import time
import math
import random
import threading


class Ghost:
    def __init__(self, clr, x, y):
        self.color = clr
        self.x = 10 + 20 * x
        self.y = 10 + 20 * y
        self.x_mat = x
        self.y_mat = y
        self.base_x = x
        self.base_y = y
        self.vector = [False, False, False, False]
        self.start = time.monotonic()

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def setKilled(self):
        self.x = 10 + 20 * self.base_x
        self.y = 10 + 20 * self.base_y
        self.x_mat = self.base_x
        self.y_mat = self.base_y

    def get_xmat(self):
        return self.x_mat

    def get_ymat(self):
        return self.y_mat

    def get_vector(self):
        return self.vector

    def get_color(self):
        return self.color

    def move(self, pX, pY, area, end, eating):
        self.vector = [False, False, False, False]

        # рассчет расстояния до пакмана
        dests = [-1] * 4
        if area[self.y_mat][self.x_mat - 1] != 3:
            dests[0] = math.sqrt((self.x_mat - 1 - pX) ** 2 + (self.y_mat - pY) ** 2)
        # вправо
        if area[self.y_mat][self.x_mat + 1] != 3:
            dests[1] = math.sqrt((self.x_mat + 1 - pX) ** 2 + (self.y_mat - pY) ** 2)
        # вверх
        if area[self.y_mat - 1][self.x_mat] != 3:
            dests[2] = math.sqrt((self.x_mat - pX) ** 2 + (self.y_mat - 1 - pY) ** 2)
        # вниз
        if area[self.y_mat + 1][self.x_mat] != 3:
            dests[3] = math.sqrt((self.x_mat - pX) ** 2 + (self.y_mat + 1 - pY) ** 2)

        if not eating:
            Vector = 20
            if end - self.start <= 5:
                step = random.randint(0, 3)
                if step == 0:  # влево
                    if area[self.y_mat][self.x_mat - 1] != 3:
                        self.vector[step] = True
                if step == 1:  # вправо
                    if area[self.y_mat][self.x_mat + 1] != 3:
                        self.vector[step] = True
                if step == 2:  # вверх
                    if area[self.y_mat - 1][self.x_mat] != 3:
                        self.vector[step] = True
                if step == 3:  # вниз
                    if area[self.y_mat + 1][self.x_mat] != 3:
                        self.vector[step] = True

            if (end - self.start <= 12) and (end - self.start > 5):
                min = 100000
                for d in range(0, 4):
                    if (dests[d] <= min) and (dests[d] != -1):
                        min = dests[d]
                        Vector = d
                self.vector[Vector] = True

            if end - self.start > 12:
                self.start = time.monotonic()
        if eating:
            Vector = 20
            max = -1
            for d in range(0, 4):
                if (dests[d] >= max) and (dests[d] != -1):
                    max = dests[d]
                    Vector = d
            self.vector[Vector] = True

        if self.vector[0]:
            self.x_mat -= 1
        if self.vector[1]:
            self.x_mat += 1
        if self.vector[2]:
            self.y_mat -= 1
        if self.vector[3]:
            self.y_mat += 1

    def move_mat(self, x, y):
        self.x += x
        self.y += y

    def set_vector(self, v):
        self.vector = v

    def killPacman(self, lives, game_status):
        lives -= 1
        if lives == 0:
            game_status = 2  # Смена статуса на 2 - экран Game Over
        return lives, game_status


def save(area, score, x, y, x_mat, y_mat, highscore, lives, level, points):  # Сохранение
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
    f.write(str(level) + '\n')  # Запись level
    f.write(str(points) + '\n')
    f.close()


def reset_area(level):
    if level == 1:
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
                [3, 3, 3, 3, 5, 3, 5, 3, 3, 4, 3, 3, 5, 3, 5, 3, 3, 3, 3],
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
    elif level == 2:
        # 0 - пусто 1 - пакмен 2 - призрак 3 - стена 4 - стена     5 - зерно
        area = [[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],  # 1   Инициализация поля
                [3, 1, 5, 5, 5, 5, 5, 3, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 3],  # 2
                [3, 5, 3, 3, 3, 3, 5, 3, 5, 3, 5, 3, 3, 3, 3, 5, 3, 5, 3],  # 3
                [3, 5, 3, 5, 5, 5, 5, 5, 5, 3, 5, 5, 5, 5, 3, 5, 3, 5, 3],  # 4
                [3, 5, 3, 5, 3, 5, 3, 5, 3, 3, 3, 3, 3, 5, 5, 5, 3, 5, 3],  # 5
                [3, 5, 5, 5, 3, 5, 3, 5, 5, 5, 5, 5, 3, 5, 3, 3, 3, 5, 3],  # 6
                [3, 5, 3, 3, 3, 5, 3, 3, 5, 3, 3, 5, 3, 5, 3, 3, 3, 5, 3],  # 7
                [3, 5, 5, 5, 5, 5, 3, 3, 5, 3, 5, 5, 5, 5, 5, 5, 5, 5, 3],  # 8
                [3, 3, 5, 3, 3, 5, 5, 5, 5, 5, 5, 3, 3, 5, 3, 3, 5, 3, 3],  # 9
                [3, 5, 5, 5, 3, 3, 5, 3, 3, 5, 3, 3, 3, 5, 3, 3, 5, 3, 3],  # 10
                [3, 5, 3, 5, 3, 5, 5, 3, 0, 2, 0, 3, 5, 5, 5, 5, 5, 3, 3],  # 11
                [3, 5, 5, 5, 5, 5, 3, 3, 2, 2, 2, 3, 5, 3, 5, 3, 3, 3, 3],  # 12
                [3, 5, 3, 5, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 5, 5, 6, 3],  # 13
                [3, 5, 5, 5, 5, 3, 5, 5, 5, 5, 3, 3, 5, 3, 5, 3, 3, 3, 3],  # 14
                [3, 3, 5, 5, 5, 3, 5, 3, 3, 5, 5, 5, 5, 3, 5, 5, 5, 3, 3],  # 15
                [3, 3, 5, 3, 5, 3, 5, 3, 3, 5, 3, 3, 5, 3, 5, 3, 5, 5, 3],  # 16
                [3, 5, 5, 3, 5, 3, 5, 3, 5, 5, 3, 3, 5, 3, 5, 3, 3, 5, 3],  # 17
                [3, 5, 3, 3, 5, 5, 5, 5, 5, 3, 5, 5, 5, 5, 5, 3, 3, 5, 3],  # 18
                [3, 5, 5, 5, 5, 3, 3, 3, 5, 3, 5, 3, 3, 3, 5, 5, 5, 5, 3],  # 19
                [3, 5, 3, 5, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 3, 3, 5, 3],  # 20
                [3, 3, 3, 5, 5, 3, 5, 3, 5, 3, 5, 3, 5, 3, 5, 3, 3, 5, 3],  # 21
                [3, 5, 5, 5, 5, 5, 5, 3, 5, 3, 5, 5, 5, 3, 5, 5, 5, 5, 3],  # 22
                [3, 5, 3, 3, 5, 3, 3, 3, 6, 3, 3, 5, 3, 3, 3, 3, 3, 5, 3],  # 23
                [3, 6, 5, 3, 5, 5, 5, 3, 3, 3, 3, 5, 5, 5, 5, 5, 3, 6, 3],  # 24
                [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]  # 25
                ]

    x = 30  # x pacman-а
    y = 30  # y pacman-а
    x_mat = 1  # x pacman-а в массиве
    y_mat = 1  # y pacman-а в массиве
    score = 0  # Счет
    lives = 3
    points = 0
    game_result_text = "Game Over"
    return area, score, x, y, x_mat, y_mat, lives, points


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
        level = int(f.readline())   # Считывание номера уровня
        points = int(f.readline())  # Считывание номера уровня
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
                [3, 3, 3, 3, 5, 3, 5, 3, 3, 4, 3, 3, 5, 3, 5, 3, 3, 3, 3],
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
        level = 1
        points = 0
        game_result_text = "Game Over"
    return area, score, x, y, x_mat, y_mat, highscore, lives, level, points


RED = 255, 0, 0
ORANGE = 255, 153, 0
YELLOW = 251, 255, 0
GREEN = 0, 255, 0
game_result_text = "Game Over"

def play_music(run):  # Проигрывание музыки
    timer = 105
    music_time = 105  # Ждать столько, СКОЛЬКО ИДЕТ ВСЯ МУЗЫКА В СУММЕ в секундах
    while run[0]:
        if timer == music_time:
            timer = 0
            pygame.mixer.music.load('music/Arstotzkian_anthem.ogg')  # Добавление в очередь файлов с музыкой
            pygame.mixer.music.play()  # Проигрывание плейлиста
        timer += 1
        time.sleep(1)


def main():
    pygame.init()
    run = [True]  # Индикатор состояния игры
    pygame.mixer.init()
    music = threading.Thread(target=play_music, args=(run,))
    music.start()
    len_side_cell = 20  # Длина стороны клетки в пикселях
    win_width_cell = 19  # Количество клеток по ширине окна
    win_height_cell = 25  # Количество клеток по длине окна
    screen = pygame.display.set_mode((len_side_cell * win_width_cell, len_side_cell * win_height_cell))
    pygame.display.set_caption("Pacman")  # Имя окна приложения
    area, score, x, y, x_mat, y_mat, highscore, lives, level, points = init(win_height_cell)
    speed = 2  # Скорость pacman-а
    game_status = 0  # состояния игры : 0 - стартовое меню, 1 - игра, 2 - смерть, любое другое число выхол из программы
    max_points_on_level = [188,218]
    # массив призраков
    if level == 1:
        ghosts = [Ghost(RED, 9, 11), Ghost(YELLOW, 9, 12), Ghost(GREEN, 8, 12),
                  Ghost(ORANGE, 10, 12)]  # Перенос призраков на их стартовые места
    if level == 2:
        ghosts = [Ghost(RED, 9, 10), Ghost(YELLOW, 9, 11), Ghost(GREEN, 8, 11),
                  Ghost(ORANGE, 10, 11)]
    # Продолжить игру

    FPS = 60  # Кадры в секунду
    clock = pygame.time.Clock()

    # Объявление глобальных переменных
    pygame.font.SysFont('', 36)  # Установка шрифта
    vector = [False, False, False, False]  # Вектор движения: влево, вправо, вверх, вниз
    tick = 0  # Номер тика
    pause = False  # Включена ли пауза
    reset = False  # Положение сброса
    killed = False  # Смерть пакмана
    p_prev_pressed = True  # Была ли нажата буква p в предыдущий тик
    lives = 3  # Количество жизней
    tickbig = 0  # для больших зерен просто забей
    volume_on = True  # Переменная, отвечающая за звук
    eating = False
    eattime = 0
    # Загрузка файлов
    image = {
        'restart': pygame.image.load('images/restart.png'),  # Объявление изображения кнопки сброса
        'restart_mini': pygame.image.load('images/restart_mini.png'),  # Объявление изображения маленькой кнопки сброса
        'pause': pygame.image.load('images/pause.png'),  # Объявление изображения кнопки паузы
        'map': pygame.image.load('images/map.png'),  # Объявление изображения поля
        'map2': pygame.image.load('images/map2.png'),  # Объявление изображения поля уровня 2
        'volume_on': pygame.image.load('images/Volume_on.png'),  # Объявление изображения кнопки звука (вкл.)
        'volume_off': pygame.image.load('images/Volume_off.png'),  # Объявление изображения кнопки звука (выкл.)
        'pacman_right': pygame.image.load('images/pacman_right.gif'),  # Загрузка изображения пакмена
        'pacman_left': pygame.image.load('images/pacman_left.gif'),
        'pacman_up': pygame.image.load('images/pacman_up.gif'),
        'pacman_down': pygame.image.load('images/pacman_down.gif'),
        'ghost': pygame.image.load('images/angry.gif'),  # Загрузка изображения призрака
        'ghost_scared': pygame.image.load('images/ghost.gif'),  # Загрузка изображения призрака
        'big_seed': pygame.image.load('images/big_seed.png')  # Загрузка большого зерна-снежинки
    }
    # Главный цикл
    while run[0]:
        tickbig += 1
        if eating:
            eattime += 1
        if not eating:
            eattime = 0
        # Экран стартового меню
        if game_status == 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Закрытие программы
                    run[0] = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    # Старт новой игры
                    if (mouse_x >= 100) & (mouse_x <= 290) & (mouse_y >= 300) & (mouse_y <= 340):
                        game_status = 1  # Смена статуса на 1 - экран игры
                        area, score, x, y, x_mat, y_mat, lives, points = reset_area(level)  # Перезапуск
                        if level == 1:
                            ghosts = [Ghost(RED, 9, 11), Ghost(YELLOW, 9, 12), Ghost(GREEN, 8, 12),
                                      Ghost(ORANGE, 10, 12)]  # Перенос призраков на их стартовые места
                        if level == 2:
                            ghosts = [Ghost(RED, 9, 10), Ghost(YELLOW, 9, 11), Ghost(GREEN, 8, 11),
                                      Ghost(ORANGE, 10, 11)]
                    # Продолжить игру
                    if (mouse_x >= 100) & (mouse_x <= 290) & (mouse_y >= 380) & (mouse_y <= 420):
                        game_status = 1  # Смена статуса на 1 - экран игры
            pygame.draw.rect(screen, (0, 255, 0), (100, 300, 190, 40))  # Кнопка старта новый игры
            f1 = pygame.font.Font("font.ttf", 100)  # Объявление шрифта
            f2 = pygame.font.Font("font.ttf", 40)  # Объявление шрифта
            f3 = pygame.font.Font("font.ttf", 20)  # Объявление шрифта
            start_new_text = f2.render("New game   ", False, (255, 255, 255))  # Текст на кнопке старта новый игры
            game_name_text = f1.render("PACMAN   ", False, (255, 240, 0))  # Текст PACMAN
            highscore_text = f2.render("Highscore       " + str(highscore), False,
                                       (190, 235, 255))  # Текст рекордного счета

            created_by_text = f3.render("Created    by promS101", False, (190, 235, 255))  # Авторы
            screen.blit(start_new_text, (115, 301))
            screen.blit(game_name_text, (30, 20))
            screen.blit(created_by_text, (88, 100))
            screen.blit(highscore_text, (45, 180))
            if score != 0:
                pygame.draw.rect(screen, (0, 255, 0), (100, 380, 190, 40))  # Кнопка продолжить игру
                continue_text = f2.render("Continue   ", False, (255, 255, 255))  # Текст на кнопке продолжить игру
                score_text = f2.render("Score                         " + str(score), False,
                                       (190, 235, 255))  # Текст счета
                screen.blit(continue_text, (107, 381))
                screen.blit(score_text, (45, 220))

            pygame.display.update()
        # Экран самой игры
        if game_status == 1:
            clock.tick(FPS)
            # Отлавливание событий
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run[0] = False

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
                area, score, x, y, x_mat, y_mat, lives, points = reset_area(level)
                ghosts = [Ghost(RED, 9, 11), Ghost(YELLOW, 9, 12), Ghost(GREEN, 8, 12),
                          Ghost(ORANGE, 10, 12)]  # Перенос призраков на их стартовые места
            if (tick == 0) & (not pause) & (not killed):
                # Изменение координат призраков
                for g in ghosts:
                    g.move(x_mat, y_mat, area, time.monotonic(), eating)

                vector = [False, False, False, False]
                # Отлавливание нажатий клавиш
                keys = pygame.key.get_pressed()
                cheat = 0
                if keys[pygame.K_l]:
                    print('ok')
                    cheat = 1
                if cheat == 1 and keys[pygame.K_v]:
                    print('45670985678579576984760570394860')
                    cheat = 0
                    level = 2
                    reset = True
                if cheat == 1 and keys[pygame.K_k]:
                    print('4098097598347657943967439770966346')
                    cheat = 0
                    level = 1
                    reset = True
                # print(cheat)
                if keys[pygame.K_a]:  # Влево
                    if (x_mat == 1) & (y_mat == 12):  # Проверка на телепорт
                        x_mat = 17
                        x += 16 * len_side_cell
                    elif area[y_mat][x_mat - 1] not in [3, 4]:  # Коллизия со стенками
                        x_mat -= 1
                        vector[0] = True
                    if area[y_mat][x_mat] == 5:  # Поглощение зерен
                        score += 5
                        points += 1
                        area[y_mat][x_mat] = 0
                    if area[y_mat][x_mat] == 6:  # Поглощение зерен
                        score += 10
                        points += 1
                        area[y_mat][x_mat] = 0
                        eating = True
                if keys[pygame.K_d]:  # Вправо
                    if (x_mat == 17) & (y_mat == 12):  # Проверка на телепорт
                        x_mat = 1
                        x -= 16 * len_side_cell
                    elif area[y_mat][x_mat + 1] not in [3, 4]:  # Коллизия со стенками
                        x_mat += 1
                        vector[1] = True
                    if area[y_mat][x_mat] == 5:  # Поглощение зерен
                        score += 5
                        points += 1
                        area[y_mat][x_mat] = 0
                    if area[y_mat][x_mat] == 6:  # Поглощение зерен
                        score += 10
                        points += 1
                        area[y_mat][x_mat] = 0
                        eating = True
                if keys[pygame.K_w]:  # Вверх
                    if area[y_mat - 1][x_mat] not in [3, 4]:  # Коллизия со стенками
                        y_mat -= 1
                        vector[2] = True
                    if area[y_mat][x_mat] == 5:  # Поглощение зерен
                        score += 5
                        points += 1
                        area[y_mat][x_mat] = 0
                    if area[y_mat][x_mat] == 6:  # Поглощение зерен
                        score += 10
                        points += 1
                        area[y_mat][x_mat] = 0
                        eating = True
                if keys[pygame.K_s]:  # Вниз
                    if area[y_mat + 1][x_mat] not in [3, 4]:  # Коллизия со стенками
                        y_mat += 1
                        vector[3] = True
                    if area[y_mat][x_mat] == 5:  # Поглощение зерен
                        score += 5
                        points += 1
                        area[y_mat][x_mat] = 0
                    if area[y_mat][x_mat] == 6:  # Поглощение зерен
                        score += 10
                        points += 1
                        area[y_mat][x_mat] = 0
                        eating = True
                p_prev_pressed = keys[pygame.K_p]  # Нажата ли клавиша p
                pause = keys[pygame.K_p]  # Включена ли пауза
            elif pause:  # Если пауза, проверять только кнопку p
                keys = pygame.key.get_pressed()
                if (not p_prev_pressed) & keys[pygame.K_p]:
                    pause = False
                p_prev_pressed = keys[pygame.K_p]  # Это чтобы не было мигания паузы от удержания p
            if (not pause) & (not killed):  # Движение, если не пауза
                if vector[0]:
                    x -= speed
                if vector[1]:
                    x += speed
                if vector[2]:
                    y -= speed
                if vector[3]:
                    y += speed
                for g in ghosts:  # Перемещение призраков
                    vectorG = g.get_vector()
                    if vectorG[0]:
                        g.move_mat(speed * (-1), 0)
                    if vectorG[1]:
                        g.move_mat(speed, 0)
                    if vectorG[2]:
                        g.move_mat(0, speed * (-1))
                    if vectorG[3]:
                        g.move_mat(0, speed)

                tick = (1 + tick) % (len_side_cell / speed)  # Следующий тик

            # Обновление рекорда
            if highscore < score:
                highscore = score

            # Колизия пакмана и призрака
            for g in ghosts:
                if (g.get_x() == (x_mat + 1) * 20 - 10) & (g.get_y() == (y_mat + 1) * 20 - 10):
                    if not eating:
                        lives, game_status = ghosts[1].killPacman(lives, game_status)
                        time.sleep(1)
                        x_mat = 1
                        y_mat = 1
                        x = 30
                        y = 30
                        vector = [False, False, False, False]
                        for i in ghosts:  # возврат всех призраков
                            i.setKilled()
                    if eating:
                        score += 150
                        g.setKilled()  # возврат съеденного призрака
            # Отрисовка
            screen.fill((0, 0, 0))
            for i in range(win_height_cell):
                for j in range(win_width_cell):
                    if area[i][j] == 3:  # Отрисовка стенок
                        pygame.draw.rect(screen, (0, 85, 200),
                                         (0 + len_side_cell * j, 0 + len_side_cell * i, len_side_cell, len_side_cell))
            if level == 1:
                screen.blit(image['map'], (0, 0))  # Отрисовка поля
            elif level == 2:
                screen.blit(image['map2'], (0, 0))  # Отрисовка поля
            # Поклеточная отрисовка
            q = 0  # Счётчик для призраков
            if eating:
                if eattime % 300 == 299:
                    eating = 0
                    eattime = 0
            for i in range(win_height_cell):
                for j in range(win_width_cell):
                    if area[i][j] == 2:
                        if not eating:
                            # Отрисовка призраков
                            screen.blit(image['ghost'], (ghosts[q].get_x() - 10, ghosts[q].get_y() - 10))
                            q += 1
                        if eating:
                            # Отрисовка призраков
                            if tickbig % 35 >= 12:
                                screen.blit(image['ghost_scared'], (ghosts[q].get_x() - 10, ghosts[q].get_y() - 10))
                                q += 1
                    if area[i][j] == 5:  # Отрисовка зерен
                        pygame.draw.circle(screen, (255, 240, 220), (10 + 20 * j, 10 + 20 * i), 3)
                    if (area[i][j] == 6) and (tickbig % 25 < 12):  # Отрисовка больших зерен
                        screen.blit(image['big_seed'], (20 * j, 20 * i))
                    if (area[i][j] == 6) and (tickbig % 25 >= 12):  # Отрисовка больших зерен
                        pygame.draw.circle(screen, (255, 230, 0), (10 + 20 * j, 10 + 20 * i), 0)
            if vector[0]:  # Отрисовка pacman-а
                screen.blit(image['pacman_left'], (x - 10, y - 10))
            elif vector[2]:
                screen.blit(image['pacman_up'], (x - 10, y - 10))
            elif vector[3]:
                screen.blit(image['pacman_down'], (x - 10, y - 10))
            else:
                screen.blit(image['pacman_right'], (x - 10, y - 10))

            f2 = pygame.font.Font("font.ttf", 15)  # Объявление шрифта
            score_text = f2.render("Score   " + str(score), False, (255, 255, 255))   # Текст текущего счета
            highscore_text = f2.render("Highscore   " + str(highscore), False, (255, 255, 255))  # Текст рекордного счета
            live_text = f2.render("Lives   " + str(lives), False, (230, 230, 255))  # Текст количестка жизней
            screen.blit(score_text, (265, 0))  # Вывод текущих очков
            screen.blit(highscore_text, (20, 0))  # Вывод рекорда
            screen.blit(live_text, (20, 480))  # Вывод количества жизней
            image['restart_mini'].set_colorkey((0, 0, 0))  # Отрисовка кнопки сброса
            screen.blit(image['restart_mini'], (205, 2))  # Отрисовка кнопки сброса
            pygame.draw.rect(screen, (255, 255, 255), (184, 5, 4, 13))  # Отрисовка паузы
            pygame.draw.rect(screen, (255, 255, 255), (194, 5, 4, 13))  # Отрисовка паузы
            if pause:
                sc = pygame.Surface((380, 500))  # Установка затемнённого поля
                sc.set_alpha(230)  # Установка уровня прозрачности
                sc.fill((0, 0, 0))  # Заполнение полупрозрачного фона
                screen.blit(sc, (0, 0))  # Отрисовка полупрозрачного фона
                image['restart'].set_colorkey((0, 0, 0))  # Загрузка картинки без чёрного фона
                screen.blit(image['restart'], (250, 200))  # Отрисовка кнопки сброса
                image['pause'].set_colorkey((0, 0, 0))  # Загрузка картинки без чёрного фона
                screen.blit(image['pause'], (100, 200))    # Отрисовка кнопки паузы
                image['restart'].set_colorkey((0, 0, 0))  # Загрузка картинки без чёрного фона
                if volume_on:
                    screen.blit(image['volume_on'], (30, 20))  # Отрисовка кнопки звука (вкл.)
                else:
                    screen.blit(image['volume_off'], (30, 20))  # Отрисовка кнопки звука (выкл.)
            pygame.display.update()
            # Победа
            if max_points_on_level[level-1] == points:
                game_result_text = "   Victory "
                game_status = 2
            #print(points)
        # Экран Game Over/You Win
        if game_status == 2:
            lives = 3
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Закрытие программы
                    run[0] = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    # Обработка старта новый игры
                    if (mouse_x >= 100) & (mouse_x <= 290) & (mouse_y >= 340) & (mouse_y <= 380):
                        game_status = 1  # Смена статуса на 1 - экран игры
                        area, score, x, y, x_mat, y_mat, lives, points = reset_area(level)  # Перезапуск карты
                        ghosts = [Ghost(RED, 9, 11), Ghost(YELLOW, 9, 12), Ghost(GREEN, 8, 12), Ghost(ORANGE, 10, 12)]  # Перенос призраков на их стартовые места

            # Отрисовка
            screen.fill((0, 0, 0))
            pygame.draw.rect(screen, (0, 255, 0), (100, 340, 190, 40))  # Кнопка рестарта
            f1 = pygame.font.Font("font.ttf", 70)  # Объявление шрифта
            f2 = pygame.font.Font("font.ttf", 40)  # Объявление шрифта
            restart_text = f2.render("New game   ", False, (255, 255, 255))  # Текст на кнопке рестарта
            gameover_text = f1.render(game_result_text, False, (255, 0, 0))  # Текст Game Over
            highscore_text = f2.render("Highscore    " + str(highscore), False, (190, 235, 255))  # Текст рекордного счета
            score_text = f2.render("Score                     " + str(score), False, (190, 235, 255))  # Текст счета
            screen.blit(restart_text, (115, 341))  # Отрисовка текста рестарт
            screen.blit(gameover_text, (30, 60))  # Отрисовка текста завершения игры
            screen.blit(highscore_text, (25, 180))  # Отрисовка рекорда
            screen.blit(score_text, (25, 220))  # Отрисовка счета
            pygame.display.update()
    # Выход из игры
    save(area, score, x, y, x_mat, y_mat, highscore, lives, level, points)  # Сохранение
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
