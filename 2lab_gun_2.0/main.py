import game
import pygame
from config import *


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font1 = pygame.font.SysFont("Verdana", 40)
font2 = pygame.font.SysFont("Verdana", 30)
g = game.Game(screen)
points, finished = g.run()
screen.fill(RED)
text1 = font1.render("You are dead", True, (0, 0, 0))
text2 = font2.render(f"You've got {points} point{'s' * (points != 1)}", True, (0, 0, 0))
screen.blit(text1, (WIDTH / 4, HEIGHT / 3))
screen.blit(text2, (WIDTH / 4, HEIGHT / 2))
pygame.display.update()
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                finished = True
        elif event.type == pygame.QUIT:
            finished = True

pygame.quit()
