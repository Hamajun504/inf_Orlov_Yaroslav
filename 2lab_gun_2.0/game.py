import pygame
from config import *
import projectile
from random import randint


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
        self.enemy_period = PERIODS
        self.enemy_time = {}
        for enemy in self.enemy_period.keys():
            self.enemy_time[enemy] = randint(0, self.enemy_period[enemy])
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
            self.move()
            self.spawn()

    def event_processing(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.finished = True

    def move(self):
        for proj in self.projectiles:
            proj.move()
        for enemy in self.enemies:
            enemy.move()

    def spawn(self):
        if self.enemy_time['Ball'] < self.enemy_period['Ball']:
            self.enemy_time['Ball'] += 1
        else:
            self.enemy_time['Ball'] = 0
            self.enemies.append(projectile.Ball(self.screen,
                                                x=randint(0, WIDTH), y=randint(0, HEIGHT * 2 / 3),
                                                vx=randint(-VELOCITY, VELOCITY), vy=randint(-VELOCITY, VELOCITY),
                                                r=randint(30, 60)))

