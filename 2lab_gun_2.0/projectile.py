class Projectile:
    def __init__(self, screen: pygame.Surface, x=40, y=450, vx=0, vy=0, r=15):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = r
        self.vx = vx
        self.vy = vy
        self.color = choice(GAME_COLORS)
        self.live = 30

