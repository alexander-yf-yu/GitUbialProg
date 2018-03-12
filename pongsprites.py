"""
final?

"""

import pygame
import random
import math


# Constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (167, 244, 66)
ORANGE = (255, 228, 155)

WIDTH = 800
HEIGHT = 600

# multiplier = 1.1


paddle_speed = 5
left_paddle_vel = 0
right_paddle_vel = 0

# Classes

class Ball(object):

    def __init__(self):
        self.x = WIDTH / 2
        self.y = HEIGHT / 2
        self.radius = 20
        self.colour = ORANGE

        self.x_vel = random.randrange(-5, 5)
        self.y_vel = random.randrange(-2, 2)

    def draw(self, surface):
        pygame.draw.circle(surface, self.colour, [int(self.x), int(self.y)], self.radius, 0)

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

    def wall_collision(self):

        # Limit

        if self.x - self.radius < 0:
            self.x = self.radius
        elif self.x + self.radius > WIDTH:
            self.x = WIDTH - self.radius
        elif self.y - self.radius < 0:
            self.y = self.radius
        elif self.y + self.radius > HEIGHT:
            self.y = HEIGHT - self.radius



        # Velocity Reverse

        if self.x - self.radius== 0 or self.x + self.radius == WIDTH:
            # self.x_vel *= - multiplier
            self.x_vel *= - 1
        elif self.y - self.radius == 0 or self.y + self.radius== HEIGHT:
            # self.y_vel *= - multiplier
            self.y_vel *= - 1


class Paddle_left(Ball):

    def __init__(self):

        self.width = 10
        self.height = 75
        self.x = 20
        self.y = HEIGHT / 2 - self.height / 2
        self.colour = GREEN

        self.left_paddle_vel = 0


    def draw(self, surface):
        # Ball.draw(self, surface)
        pygame.draw.rect(surface, self.colour, [self.x, self.y, self.width, self.height], 0)

    def update(self):


        # CANNOT PUT THE EVENT HANDLER HERE FOR SOME REASON???

        # for event in pygame.event.get():
        #     if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_UP:
        #             self.left_paddle_vel = -2
        #         elif event.key == pygame.K_DOWN:
        #             self.left_paddle_vel = 2
        #     elif event.type == pygame.KEYUP:
        #         if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        #             self.left_paddle_vel = 0



        self.left_paddle_vel = left_paddle_vel
        self.y += self.left_paddle_vel

        if self.y >= HEIGHT - self.height:
            self.y = HEIGHT - self.height
        elif self.y <= 0:
            self.y = 0

    def paddle_collision(self, ball):

        if ball.y >= self.y - self.radius and ball.y <= self.y + self.radius and ball.x <= self.x:
            print("hit")
        else:
            print("NO")
            

class Paddle_right(Paddle_left):

    def __init__(self):
        Paddle_left.__init__(self)

        self.x = WIDTH - (10 + self.x)

    def draw(self, surface):
        Paddle_left.draw(self, surface)

    def update(self):

        if self.y >= HEIGHT - self.height:
            self.y = HEIGHT - self.height
        elif self.y <= 0:
            self.y = 0


        self.right_paddle_vel = right_paddle_vel
        self.y += self.right_paddle_vel



pygame.init()

# Screen properties
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Window Title")

done = False

clock = pygame.time.Clock()


my_ball = Ball()

my_left_paddle = Paddle_left()
my_right_paddle = Paddle_right()

while not done:
    # -- Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # -- Paddle Movement Input
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                left_paddle_vel = - paddle_speed
            elif event.key == pygame.K_LSHIFT:
                left_paddle_vel = paddle_speed
            elif event.key == pygame.K_UP:
                right_paddle_vel = - paddle_speed
            elif event.key == pygame.K_DOWN:
                right_paddle_vel = paddle_speed
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_TAB or event.key == pygame.K_LSHIFT:
                left_paddle_vel = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                right_paddle_vel = 0

    screen.fill((4, 43, 71))

    # Excecution

    my_ball.draw(screen)
    my_ball.move()
    my_ball.wall_collision()


    my_left_paddle.draw(screen)
    my_left_paddle.update()

    my_right_paddle.draw(screen)
    my_right_paddle.update()




    pygame.display.flip()
    clock.tick(60)


pygame.quit()
