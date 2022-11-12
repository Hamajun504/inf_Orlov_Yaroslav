import pygame


class Button:
    def __init__(self, screen, coords, text, color, font_size):
        self.coords = coords
        self.color = color
        self.screen = screen
        self.font = pygame.font.SysFont("Verdana", 20)
        self.text = text

    def draw(self):
        text = self.font.render(str(self.text), True, (0, 0, 0))
        pygame.draw.rect(self.screen, self.color,
                         (self.coords[0] - text.get_width() / 2, self.coords[1] - text.get_height() / 2,
                          self.coords[0] + text.get_width() / 2, self.coords[1] + text.get_height() / 2))
        self.screen.blit(text, text.get_rect(center=self.coords))

