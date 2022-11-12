import pygame
from config import *
import projectile
from random import randint
import enemy
import cannon


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
        self.cannon = cannon.Cannon(self.screen)

    def draw(self):
        self.screen.fill(WHITE)
        for proj in self.projectiles:
            proj.draw()
        for enemy in self.enemies:
            enemy.draw()
        self.cannon.draw()
        points = self.font.render(str(self.points), True, (0, 0, 0))
        self.screen.blit(points, (40, 40))
        pygame.draw.line(self.screen, RED, (0, HEIGHT * 2 / 3), (WIDTH, HEIGHT * 2 / 3))
        pygame.display.update()

    def run(self):
        while not self.finished:
            self.draw()
            self.clock.tick(FPS)
            self.event_processing()
            self.move()
            self.spawn()
            self.extinction()

    def event_processing(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.finished = True
            elif event.type == pygame.MOUSEMOTION:
                self.cannon.targeting(event.pos[0], event.pos[1])
            elif event.type == pygame.MOUSEBUTTONUP:
                self.projectiles.append(self.cannon.fire_end())
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.cannon.fire_start()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.cannon.start_move_up()
                elif event.key == pygame.K_s:
                    self.cannon.start_move_down()
                elif event.key == pygame.K_d:
                    self.cannon.start_move_right()
                elif event.key == pygame.K_a:
                    self.cannon.start_move_left()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.cannon.stop_move_up()
                elif event.key == pygame.K_s:
                    self.cannon.stop_move_down()
                elif event.key == pygame.K_d:
                    self.cannon.stop_move_right()
                elif event.key == pygame.K_a:
                    self.cannon.stop_move_left()

    def move(self):
        for proj in self.projectiles:
            proj.move()
        for enemy in self.enemies:
            enemy.move()
        self.cannon.move()

    def spawn(self):
        if self.enemy_time["Circle"] < self.enemy_period["Circle"]:
            self.enemy_time["Circle"] += 1
        else:
            self.enemy_time["Circle"] = 0
            r = randint(20, 40)
            self.enemies.append(enemy.Circle(self.screen,
                                             x=randint(r, WIDTH - r), y=randint(r, HEIGHT * 2 / 3 - r),
                                             vx=randint(-VELOCITY, VELOCITY), vy=randint(-VELOCITY, VELOCITY),
                                             r=r))

    def extinction(self):
        dead = []
        for i in range(len(self.projectiles)):
            if isinstance(self.projectiles[i], projectile.Ball):
                if self.projectiles[i].time >= BALL_LIFE:
                    dead.append(i)
        for i in dead[::-1]:
            del self.projectiles[i]



