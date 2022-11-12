import pygame
from config import *


class Target:
    points = 1
    def __init__(self, screen: pygame.Surface, x=40, y=450, vx=0, vy=0):
        self.screen = screen
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def move(self):
        self.x += self.vx
        self.y += self.vy


class Circle(Target):
    points = 1
    def __init__(self, screen: pygame.Surface, x=40, y=450, vx=0, vy=0, r=15):
        self.screen = screen
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.r = r
        self.color = RED

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r,
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



