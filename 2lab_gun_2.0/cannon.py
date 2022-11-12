from config import *
from math import atan, pi, sin, cos
import pygame
import projectile


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
        self.gun_length = 40
        self.gun = pygame.Surface((2 * self.gun_length, 2 * self.gun_length))
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
                self.power += 1.5

    def fire_start(self):
        pygame.draw.rect(self.gun, RED, (40, 35, 40, 10))
        self.charging = True

    def fire_end(self):
        length = 2 * self.gun_length * (1 + (self.power - self.power_bound) /
                                        (self.power_max - self.power_bound))
        ball_x = self.x + length * cos(self.an)
        ball_y = self.y - length * sin(self.an)
        ball_vx = VELOCITY * cos(self.an) * self.power / self.power_min / 1.8 + \
                  self.moving_right * VELOCITY - self.moving_left * VELOCITY
        ball_vy = -VELOCITY * sin(self.an) * self.power / self.power_min / 1.8 + \
                  self.moving_down * VELOCITY - self.moving_up * VELOCITY

        pygame.draw.rect(self.gun, DARK_GREEN, (self.gun_length, self.gun_length - 5, self.gun_length, 10))
        self.power = self.power_min
        self.charging = False

        return projectile.Ball(self.screen, ball_x, ball_y, ball_vx, ball_vy, BALL_SIZE)

    def draw(self):
        gun = self.gun
        if self.power > self.power_bound:
            gun = pygame.transform.scale(gun, (2 * self.gun_length * (1 + (self.power - self.power_bound) /
                                                     (self.power_max - self.power_bound)), 2 * self.gun_length))
        gun = pygame.transform.rotate(gun, self.an / pi * 180)
        gun_coords = gun.get_rect(center=(self.x, self.y))
        self.screen.blit(gun, gun_coords)
        pygame.draw.circle(self.screen, DARK_GREEN, (self.x, self.y), self.r)
