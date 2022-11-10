import math
from random import choice, randint
import pygame


FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

GRAV_ACC = 5

WIDTH = 800
HEIGHT = 600




class Ball:
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

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.x += self.vx
        self.y -= self.vy
        self.vy -= GRAV_ACC
        self.live -= 1
        if self.x > WIDTH - self.r:
            self.x = self.x = 2 * WIDTH - 2 * self.r - self.x
            self.vx = -self.vx
        if self.x < self.r:
            self.x = 2 * self.r - self.x
            self.vx = -self.vx
        if self.y > HEIGHT - self.r:
            self.y = 2 * HEIGHT - 2 * self.r - self.y
            self.vy = - 0.6 * self.vy
        if self.y < self.r:
            self.y = 2 * self.r - self.y
            self.vy = - 0.6 * self.vy

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if isinstance(obj, Target):
            return (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 < (self.r + obj.r) ** 2
        else:
            raise "Unknown Object"

    def dead(self):
        return self.live <= 0


class Gun:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global bullet
        bullet += 1
        new_ball = Ball(self.screen, vx=self.f2_power * math.cos(self.an), vy=- self.f2_power * math.sin(self.an))
        #self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        #new_ball.vx = self.f2_power * math.cos(self.an)
        #new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            if event.pos[0] > 20:
                self.an = math.atan((event.pos[1]-450) / (event.pos[0]-20))
            elif event.pos[0] < 20:
                self.an = math.pi + math.atan((event.pos[1]-450) / (event.pos[0]-20))
            else:
                self.an = (event.pos[1] > 450) * math.pi / 2
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        pygame.draw.line(self.screen,
                         self.color,
                         (20, 450),
                         (20 + 2 * (self.f2_power + 20) * math.cos(self.an),
                          450 + 2 * (self.f2_power + 20) * math.sin(self.an)),
                         7)

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


class Target:
    def __init__(self, screen: pygame.Surface):
        self.points = 0
        self.alive = True
        self.screen = screen
        self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        global bullet
        bullet = 0
        self.alive = True
        self.x = randint(600, 780)
        self.y = randint(300, 550)
        self.r = randint(2, 50)
        self.color = RED

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points

    def draw(self):
        if self.alive:
            pygame.draw.circle(
                self.screen,
                self.color,
                (self.x, self.y),
                self.r
            )


def extinction():
    dead_indexes = []
    for i in range(len(balls)):
        if balls[i].dead():
            dead_indexes.append(i)
    for i in dead_indexes:
        del balls[i]


def drawing():
    screen.fill(WHITE)
    gun.draw()
    target.draw()
    for b in balls:
        b.draw()
    if target.alive:
        number = FONT.render(str(target.points), True, (0, 0, 0))
        screen.blit(number, (40, 40))
    else:
        global bullet
        bullet_message = FONT.render(f"You destroy target with {bullet} bullet{'s' * (bullet != 1)}", True, (0, 0, 0))
        screen.blit(bullet_message, (WIDTH / 4, HEIGHT / 2))
    pygame.display.update()


def event_processing():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            global finished
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)


def moving():
    global timeout
    timeout += 1
    for b in balls:
        b.move()
        if b.hittest(target) and target.alive:
            target.alive = False
            target.hit()
            timeout = 0
    if timeout > FPS and not target.alive:
        target.new_target()


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
FONT = pygame.font.Font(None, 40)
bullet = 0
balls = []

clock = pygame.time.Clock()
gun = Gun(screen)
target = Target(screen)
finished = False
timeout = 0

while not finished:
    drawing()
    clock.tick(FPS)
    event_processing()
    extinction()
    moving()
    gun.power_up()

pygame.quit()
