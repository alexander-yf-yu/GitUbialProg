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

# Ball Globals

# multiplier = 1.1



# Paddle Globals
paddle_speed = 5
LEFT_PADDLE_X = 20
RIGHT_PADDLE_X = WIDTH - 30
paddle_velocity = 0
right_paddle_vel = 0

# Classes

# class Ball(object):
#
#     def __init__(self):
#         self.x = WIDTH / 2
#         self.y = HEIGHT / 2
#         self.radius = 20
#         self.colour = ORANGE
#
#         self.x_vel = random.randrange(-5, 5)
#         self.y_vel = random.randrange(-2, 2)
#
#     def draw(self, surface):
#         pygame.draw.circle(surface, self.colour, [int(self.x), int(self.y)], self.radius, 0)
#
#     def move(self):
#         self.x += self.x_vel
#         self.y += self.y_vel
#
#     def wall_collision(self):
#
#         # Boundaries
#
#         if self.x - self.radius < 0:
#             self.x = self.radius
#         elif self.x + self.radius > WIDTH:
#             self.x = WIDTH - self.radius
#         elif self.y - self.radius < 0:
#             self.y = self.radius
#         elif self.y + self.radius > HEIGHT:
#             self.y = HEIGHT - self.radius
#
#
#
#         # Velocity Reverse
#
#         if self.x - self.radius== 0 or self.x + self.radius == WIDTH:
#             # self.x_vel *= - multiplier
#             self.x_vel *= - 1
#         elif self.y - self.radius == 0 or self.y + self.radius== HEIGHT:
#             # self.y_vel *= - multiplier
#             self.y_vel *= - 1



class Ball(pygame.sprite.Sprite):

    def __init__(self):
        self.image = pygame.Surface([40, 40])
        pygame.draw.circle(self.image, ORANGE, [20, 20], 20, 0)

        self.rect = self.image.get_rect()
        self.rect.x = WIDTH / 2
        self.rect.y = HEIGHT / 2

        self.x_vel = random.randrange(-5, 5)
        self.y_vel = random.randrange(-2, 2)

    def update(self):
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel

        # Boundaries

        if self.rect.left < 0:
            self.rect.x = 0
        elif self.rect.right > WIDTH:
            self.rect.x = WIDTH - self.rect.width
        elif self.rect.top < 0:
            self.rect.y = 0
        elif self.rect.bottom > HEIGHT:
            self.rect.y = HEIGHT - self.rect.height

        # Velocity Reverse
'''
        if self.x - self.radius == 0 or self.x + self.radius == WIDTH:
            # self.x_vel *= - multiplier
            self.x_vel *= - 1
        elif self.y - self.radius == 0 or self.y + self.radius== HEIGHT:
            # self.y_vel *= - multiplier
            self.y_vel *= - 1
'''
class Paddle(pygame.sprite.Sprite):

    def __init__(self, x, flag):

        pygame.sprite.Sprite.__init__(self)

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([10, 75])
        self.image.fill(GREEN)

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = HEIGHT / 2 - self.rect.height / 2

        self.paddle_velocity = 0

        self.flag = flag

    def update(self):


        # CANNOT PUT THE EVENT HANDLER HERE FOR SOME REASON???

        # for event in pygame.event.get():
        #     if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_UP:
        #             self.paddle_velocity = -2
        #         elif event.key == pygame.K_DOWN:
        #             self.paddle_velocity = 2
        #     elif event.type == pygame.KEYUP:
        #         if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        #             self.paddle_velocity = 0



        self.rect.y += self.paddle_velocity

        if self.rect.y >= HEIGHT - self.rect.height:
            self.rect.y = HEIGHT - self.rect.height
        elif self.rect.y <= 0:
            self.rect.y = 0


pygame.init()

# Screen properties
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("PONG_SPRITES")

done = False

clock = pygame.time.Clock()




left_paddle = Paddle(LEFT_PADDLE_X, "left_paddle")
right_paddle = Paddle(RIGHT_PADDLE_X, "right_paddle")

paddle_sprites = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

my_ball = Ball()

paddle_sprites.add(left_paddle)
paddle_sprites.add(right_paddle)
all_sprites.add(left_paddle)
all_sprites.add(right_paddle)
all_sprites.add(my_ball)





while not done:
    # -- Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # -- Paddle Movement Input
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                left_paddle.paddle_velocity = - paddle_speed
            elif event.key == pygame.K_LSHIFT:
                left_paddle.paddle_velocity = paddle_speed
            elif event.key == pygame.K_UP:
                right_paddle.paddle_velocity = - paddle_speed
            elif event.key == pygame.K_DOWN:
                right_paddle.paddle_velocity = paddle_speed
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_TAB or event.key == pygame.K_LSHIFT:
                left_paddle.paddle_velocity = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                right_paddle.paddle_velocity = 0

    # -- Sprite Collision
'''
    sprite_list = pygame.sprite.spritecollide(my_ball, paddle_sprites, False)


    for sprite in sprite_list:


        if sprite.flag == "left_paddle":
            # TODO: VELOCITY Reverse
        elif sprite.
'''


    screen.fill((4, 43, 71))

    # Excecution


    all_sprites.draw(screen)
    all_sprites.update()




    pygame.display.flip()
    clock.tick(60)


pygame.quit()
