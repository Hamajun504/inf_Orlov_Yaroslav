from config import *
from math import atan, pi
import pygame


class Cannon:
    def __init__(self, screen):
        self.x = WIDTH // 2
        self.y = HEIGHT * 5 // 6
        self.v = VELOCITY
        self.an = 0
        self.power_max = 70
        self.power_min = 10
        self.power_bound = 30
        self.power = self.power_min
        self.charging = False
        self.self_color = GREEN
        self.gun = pygame.Surface((80, 80))
        self.gun.fill(BLACK)
        pygame.draw.rect(self.gun, DARK_GREEN, (40, 35, 40, 10))
        self.gun.set_colorkey((0, 0, 0))
        self.r = 20
        self.screen = screen
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def start_move_right(self):
        if self.moving_left:
            self.moving_left = False
        else:
            self.moving_right = True

    def start_move_left(self):
        if self.moving_right:
            self.moving_right = False
        else:
            self.moving_left = True

    def start_move_up(self):
        if self.moving_down:
            self.moving_down = False
        else:
            self.moving_up = True

    def start_move_down(self):
        if self.moving_up:
            self.moving_up = False
        else:
            self.moving_down = True

    def stop_move_right(self):
        if not self.moving_right:
            self.moving_left = True
        else:
            self.moving_right = False

    def stop_move_left(self):
        if not self.moving_left:
            self.moving_right = True
        else:
            self.moving_left = False

    def stop_move_up(self):
        if not self.moving_up:
            self.moving_down = True
        else:
            self.moving_up = False

    def stop_move_down(self):
        if not self.moving_down:
            self.moving_up = True
        else:
            self.moving_down = False

    def move_right(self):
        if self.x < WIDTH - self.r:
            self.x += self.v
        if self.x > WIDTH - self.r:
            self.x = WIDTH - self.r

    def move_left(self):
        if self.x > self.r:
            self.x -= self.v
        if self.x < self.r:
            self.x = self.r

    def move_down(self):
        if self.y < HEIGHT - self.r:
            self.y += self.v
        if self.y > HEIGHT - self.r:
            self.y = HEIGHT - self.r

    def move_up(self):
        if self.y > HEIGHT * 2 / 3 + self.r:
            self.y -= self.v
        if self.y < HEIGHT * 2 / 3 + self.r:
            self.y = HEIGHT * 2 / 3 + self.r

    def move(self):
        if self.moving_right:
            self.move_right()
        if self.moving_left:
            self.move_left()
        if self.moving_up:
            self.move_up()
        if self.moving_down:
            self.move_down()
        self.charge()

    def targeting(self, x, y):
        if x > self.x:
            self.an = -atan((y - self.y) / (x - self.x))
        elif x == self.x:
            self.an = pi / 2 * ((y < self.y) * 2 - 1)
        elif x < self.x:
            self.an = pi + atan((y - self.y) / (self.x - x))

    def charge(self):
        if self.charging:
            if self.power <= self.power_max:
                self.power += 1

    def fire_start(self):
        pygame.draw.rect(self.gun, RED, (40, 35, 40, 10))
        self.charging = True

    def fire_end(self):
        pygame.draw.rect(self.gun, DARK_GREEN, (40, 35, 40, 10))
        self.power = self.power_min
        self.charging = False

    def draw(self):
        gun = self.gun
        if self.power > self.power_bound:
            gun = pygame.transform.scale(gun, (80 * (1 + (self.power - self.power_bound) /
                                                     (self.power_max - self.power_bound)), 80))
        gun = pygame.transform.rotate(gun, self.an / pi * 180)
        gun_coords = gun.get_rect(center=(self.x, self.y))
        self.screen.blit(gun, gun_coords)
        pygame.draw.circle(self.screen, DARK_GREEN, (self.x, self.y), self.r)
