import pygame
from config import *


class Button:
    def __init__(self, screen, coords, text, color, font_size):
        self.coords = coords
        self.color = color
        self.screen = screen
        self.font = pygame.font.SysFont("Verdana", font_size)
        self.text = self.font.render(str(text), True, (0, 0, 0))
        self.height = self.text.get_height()
        self.width = self.text.get_width()

    def draw(self):
        pygame.draw.rect(self.screen, self.color,
                         (self.coords[0], self.coords[1],
                          self.width, self.height))
        #self.screen.blit(self.text, self.text.get_rect(center=self.coords))
        #pygame.draw.rect(self.screen, BLACK, self.text.get_rect(center=self.coords), width=2)
        self.screen.blit(self.text, (self.coords[0], self.coords[1], self.width, self.height))
        pygame.draw.rect(self.screen, BLACK, (self.coords[0], self.coords[1], self.width, self.height), width=1)

    def check_click(self, x, y):
        if self.coords[0] <= x <= self.coords[0] + self.width and \
                self.coords[1] <= y <= self.coords[1] + self.height:
            return True
        else:
            return False


