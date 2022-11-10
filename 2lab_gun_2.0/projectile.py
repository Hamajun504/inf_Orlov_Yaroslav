from random import choice, randint
from config import *
import pygame

class Projectile:
    def __init__(self, screen: pygame.Surface, x, y, vx, vy):
        self.screen = screen
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def draw(self):
        pass


class Ball(Projectile):
    def __init__(self, screen: pygame.Surface, x=40, y=450, vx=0, vy=0, r=15):
        self.screen = screen
        self.x = x
        self.y = y
        self.r = r
        self.vx = vx
        self.vy = vy
        self.color = choice(GAME_COLORS)

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r,
            width=1
        )

    def move(self):
        self.x += self.vx
        self.y += self.vy
        if self.x > WIDTH - self.r:
            self.x = self.x = 2 * WIDTH - 2 * self.r - self.x
            self.vx = -self.vx
        if self.x < self.r:
            self.x = 2 * self.r - self.x
            self.vx = -self.vx
        if self.y > (HEIGHT * 2 / 3) - self.r:
            self.y = 2 * (HEIGHT * 2 / 3) - 2 * self.r - self.y
            self.vy = -self.vy
        if self.y < self.r:
            self.y = 2 * self.r - self.y
            self.vy = -self.vy
