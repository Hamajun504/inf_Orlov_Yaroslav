import pygame
from random import randint
pygame.init()

FPS = 30
BALLS_QUANTITY = 5
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
        self.vx = randint(0, VELOCITY)
        self.vy = randint(0, VELOCITY)
        self.color = COLORS[randint(0, 5)]

    def draw(self):
        """ открисовывает круг """
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)

    def move_step(self):
        """ сдвигает круг по скорости """
        global dT
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


def new_ball():
    """ draw new ball """
    global x, y, r
    x = randint(100, 700)
    y = randint(100, 500)
    r = randint(30, 50)
    color = COLORS[randint(0, 5)]
    pygame.draw.circle(screen, color, (x, y), r)


def click(event):
    print(x, y, r)


def event_processing(balls):
    """ обрабатывает события:
        закрытие, клик в круг"""
    global finished, points
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for ball in balls:
                if (event.pos[0] - ball.x) ** 2 + (event.pos[1] - ball.y) ** 2 <= ball.r ** 2:
                    points += 1


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.update()
clock = pygame.time.Clock()
points = 0
finished = False
balls = [Ball() for i in range(BALLS_QUANTITY)]

while not finished:
    screen.fill(BLACK)
    for ball in balls:
        ball.move_step()
        ball.wall_reflection()
        ball.draw()
    pygame.display.update()
    clock.tick(FPS)
    event_processing(balls)

pygame.quit()
print(points)
