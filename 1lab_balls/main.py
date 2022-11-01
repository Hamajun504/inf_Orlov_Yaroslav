import pygame
from random import randint
from math import sin, cos, radians
import pandas as pd


FPS = 30
BALLS_QUANTITY = 10
VELOCITY = 30
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900


class Ball:
    def __init__(self):
        global COLORS
        """ каждый круг обладает короординатой, радиусом и скоростью"""
        self.x = randint(100, 700)
        self.y = randint(100, 500)
        self.r = randint(30, 50)
        self.vx = randint(-VELOCITY, VELOCITY)
        self.vy = randint(-VELOCITY, VELOCITY)
        self.color = COLORS[randint(0, 5)]

    def draw(self):
        """ открисовывает круг """
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)

    def move_step(self):
        """ сдвигает круг по скорости """
        self.x += self.vx
        self.y += self.vy

    def wall_reflection(self):
        """ отражает круг от стены"""
        global SCREEN_HEIGHT, SCREEN_WIDTH
        if self.x < self.r:
            self.x = 2 * self.r - self.x
            self.vx = -self.vx
        if self.y < self.r:
            self.y = 2 * self.r - self.y
            self.vy = -self.vy
        if self.x > SCREEN_WIDTH - self.r:
            self.x = 2 * SCREEN_WIDTH - 2 * self.r - self.x
            self.vx = -self.vx
        if self.y > SCREEN_HEIGHT - self.r:
            self.y = 2 * SCREEN_HEIGHT - 2 * self.r - self.y
            self.vy = -self.vy


class Target:
    def __init__(self):
        """ мишень движется по окружности радиуса r и описывается одним углом """
        self.angle = randint(0, 360)
        self.angle_vel = randint(-VELOCITY, VELOCITY)
        self.r = randint(200, 350)
        self.x = SCREEN_WIDTH // 2 + self.r * cos(radians(self.angle))
        self.y = SCREEN_HEIGHT // 2 + self.r * sin(radians(self.angle))

    def draw(self):
        """ открисовывает мишень """
        pygame.draw.circle(screen, GREEN, (self.x, self.y), 50)
        pygame.draw.circle(screen, YELLOW, (self.x, self.y), 35)
        pygame.draw.circle(screen, RED, (self.x, self.y), 20)

    def move_step(self):
        """ шаг движения с угловой скоростью """
        self.angle += self.angle_vel
        self.x = SCREEN_WIDTH // 2 + self.r * cos(radians(self.angle))
        self.y = SCREEN_HEIGHT // 2 + self.r * sin(radians(self.angle))


def event_processing(balls, target):
    """ обрабатывает события:
        закрытие, клик в круг"""
    global finished, points, clicks
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            clicks += 1
            for ball in balls:
                if (event.pos[0] - ball.x) ** 2 + (event.pos[1] - ball.y) ** 2 <= ball.r ** 2:
                    points += 1
            if (event.pos[0] - target.x) ** 2 + (event.pos[1] - target.y) ** 2 <= target.r ** 2:
                points += 5


def write_table(points, clicks):
    try:
        score = round(points / clicks, 3)
    except ZeroDivisionError:
        score = 0.
    name = input('Введите имя (Enter если не нужно сохранять результат)\n')
    if name != '':
        df = pd.read_csv('table.csv', header=0, index_col=0)
        df = pd.concat([df, pd.DataFrame({'Name': [name], 'Score': [score]})], ignore_index=True)
        df = df.sort_values(by='Score', ascending=False)
        df.to_csv('table.csv')


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.update()
clock = pygame.time.Clock()
clicks = 0
points = 0
finished = False
balls = [Ball() for i in range(BALLS_QUANTITY)]
target = Target()

while not finished:
    screen.fill(BLACK)
    for ball in balls:
        ball.move_step()
        ball.wall_reflection()
        ball.draw()
    target.move_step()
    target.draw()
    pygame.display.update()
    clock.tick(FPS)
    event_processing(balls, target)

pygame.quit()

write_table(points, clicks)
