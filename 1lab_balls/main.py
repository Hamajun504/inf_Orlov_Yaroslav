import pygame
from random import randint
pygame.init()

FPS = 1
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


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

def event_proceccing():
    """ обрабатывает события:
        закрытие, клик в круг"""
    global x, y, r, finished, points
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN and (event.pos[0] - x) ** 2 + (event.pos[1] - y) ** 2 <= r ** 2:
            points += 1


screen = pygame.display.set_mode((1200, 900))
pygame.display.update()
clock = pygame.time.Clock()
points = 0
finished = False

while not finished:
    screen.fill(BLACK)
    new_ball()
    pygame.display.update()
    clock.tick(FPS)
    event_proceccing()

pygame.quit()
print(points)
