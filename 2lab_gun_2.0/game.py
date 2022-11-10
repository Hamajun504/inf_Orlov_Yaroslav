import pygame
from config import *


class Game:
    def __init__(self):
        self.points = 0
        self.enemies = []
        self.projectiles = []
        self.finished = False
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.font = pygame.font.SysFont("Verdana", 40)
        self.clock = pygame.time.Clock()
        #self.canon =

    def draw(self):
        self.screen.fill(WHITE)
        #self.canon.draw()
        for proj in self.projectiles:
            proj.draw()
        for enemy in self.enemies:
            enemy.draw()
        points = self.font.render(str(self.points), True, (0, 0, 0))
        self.screen.blit(points, (40, 40))
        pygame.display.update()

    def run(self):
        while not self.finished:
            self.draw()
            self.clock.tick(FPS)
            self.event_processing()


    def event_processing(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.finished = True
