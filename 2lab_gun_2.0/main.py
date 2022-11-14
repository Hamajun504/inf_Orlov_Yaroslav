import game
import pygame
from config import *
import buttons


def event_processing():
    global finished_global
    finished_menu = False
    while not finished_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished_global = True
                finished_menu = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.check_click(event.pos[0], event.pos[1]):
                    finished_menu = True
                elif quit_button.check_click(event.pos[0], event.pos[1]):
                    finished_menu = True
                    finished_global = True


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
g = game.Game(screen)
finished_global = False
font1 = pygame.font.SysFont("Verdana", 40)
font2 = pygame.font.SysFont("Verdana", 30)
text1 = font1.render("You are dead", True, (0, 0, 0))
start_button = buttons.Button(screen, (WIDTH * 2 / 3, HEIGHT / 3), " Start ", GREEN, 40)
quit_button = buttons.Button(screen, (WIDTH * 2 / 3, HEIGHT / 2), " Quit ", GREY, 30)
screen.fill(RED)
start_button.draw()
quit_button.draw()
pygame.display.update()
event_processing()
while not finished_global:
    points, finished_global = g.run()
    if finished_global:
        break
    text2 = font2.render(f"You've got {points} point{'s' * (points != 1)}", True, (0, 0, 0))
    screen.fill(RED)
    start_button.draw()
    quit_button.draw()
    screen.blit(text1, (WIDTH / 4, HEIGHT / 3))
    screen.blit(text2, (WIDTH / 4, HEIGHT / 2))
    pygame.display.update()
    event_processing()
pygame.quit()
