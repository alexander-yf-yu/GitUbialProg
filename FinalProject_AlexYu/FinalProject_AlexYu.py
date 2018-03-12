'''

FinalProject_AlexYu.py
Alex Yu
December 19th 2017
Version 1.0
My code creates the game Pong!

'''

import pygame
import random
import math

# bug fix: memory error
pygame.mixer.init(44100, -16, 2, 2048)

# Constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (34, 139, 34)
ORANGE = (255, 228, 155)
RED = (255, 50, 50)

WIDTH = 800
HEIGHT = 600

# Ball Globals

multiplier = 2
multiplying_rate = 0.2
mult_lim = 3.2
x_minimum_vel = 3
y_minimum_vel = 2
x_maximum_vel = 10
y_maximum_vel = 5

# Trig Ball Globals
BALL_VEL = 5

# Score Globals
left_score = 0
right_score = 0

# Paddle Globals
PADDLE_SPEED = 6
LEFT_PADDLE_X = 30
RIGHT_PADDLE_X = WIDTH - 40
paddle_velocity = 0
right_paddle_vel = 0

# Sounds
load_sound = pygame.mixer.Sound("chafing.ogg")
reset_sound = pygame.mixer.Sound("decay.ogg")
contact_sound = pygame.mixer.Sound("inquisitiveness.ogg")
death_sound = pygame.mixer.Sound("man-heartily-laughing.ogg")
jingle_song = pygame.mixer.Sound("Jingle_Bells.ogg")

# Classes

class Ball(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([20, 20])
        pygame.draw.circle(self.image, RED, [10, 10], 20, 0)

        self.rect = self.image.get_rect()

        self.rect.x = 0
        self.rect.y = 0

        self.x_vel = 0.0
        self.y_vel = 0.0

        angle = 0.0

        self.reset()

        reset_sound.stop()

    def reset(self):

        self.rect.x = WIDTH / 2
        self.rect.y = HEIGHT / 2

        ### Generate a random starting direction
        # Loop that prevents non-permissible values of angle that result in x_vel --> around 0
        # Non-Permissable Values are around: 270 or 90 degrees
        # Or in radian form: pi / 2 or 3 * pi / 2
        # Both measurements are in standard position Trig
        # A padding of 0.5 is used as an estimate

        angle = math.pi / 2

        while ((math.pi / 2 - 0.5) < angle < (math.pi / 2 + 0.5) or (3 * math.pi / 2 - 0.5) < angle < (3 * math.pi / 2 + 0.5)):
            angle = float(random.uniform(0, math.pi * 2))

        # Using angle to generate random x and y velocities within contraints

        self.x_vel = float(math.cos(angle) * BALL_VEL)
        self.y_vel = float(math.sin(angle) * BALL_VEL)

        multiplier = 2

        reset_sound.play()


    def update(self):
        self.rect.x += float(self.x_vel)
        self.rect.y += float(self.y_vel)

        # Boundaries

        if self.rect.left < left_paddle.rect.left:

            self.rect.x = 0
            self.x_vel = float(self.x_vel * -1)

            global right_score
            right_score += 1

            my_ball.reset()

        elif self.rect.right > right_paddle.rect.right:

            self.rect.x = WIDTH - self.rect.width
            self.x_vel = float(self.x_vel * -1)

            global left_score
            left_score += 1

            my_ball.reset()

        elif self.rect.top < 0:

            self.rect.y = 0
            self.y_vel = float(self.y_vel * -1)

        elif self.rect.bottom > HEIGHT:

            self.rect.y = HEIGHT - self.rect.height
            self.y_vel = float(self.y_vel * -1)


class Paddle(pygame.sprite.Sprite):

    def __init__(self, x, flag):

        pygame.sprite.Sprite.__init__(self)

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([15, 120])
        self.image.fill(GREEN)

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = HEIGHT / 2 - self.rect.height / 2

        self.paddle_velocity = 0

        self.flag = flag

    def update(self):

        self.rect.y += self.paddle_velocity

        if self.rect.y >= HEIGHT - self.rect.height:
            self.rect.y = HEIGHT - self.rect.height
        elif self.rect.y <= 0:
            self.rect.y = 0

pygame.init()

# Screen properties
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)

jingle_song.play(-1)


print("Welcome to Pong!")
print("Pong is a two-player game.")
print("The object of the game is to score on your opponent!")
print("The game ends at 10 points!")
print("You use the up and down arrows as well as the shift and tab keys to move the paddles.")

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


load_sound.play()

while not done:
    # -- Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # -- Paddle Movement Input
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                left_paddle.paddle_velocity = - PADDLE_SPEED
            elif event.key == pygame.K_LSHIFT:
                left_paddle.paddle_velocity = PADDLE_SPEED
            elif event.key == pygame.K_UP:
                right_paddle.paddle_velocity = - PADDLE_SPEED
            elif event.key == pygame.K_DOWN:
                right_paddle.paddle_velocity = PADDLE_SPEED
            elif event.key == pygame.K_SPACE:
                my_ball.reset()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_TAB or event.key == pygame.K_LSHIFT:
                left_paddle.paddle_velocity = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                right_paddle.paddle_velocity = 0

    # Death Check

    if right_score >= 10 or left_score >= 10:

        left_paddle = 0
        right_score = 0

        my_ball.reset()
        death_sound.play()
        contact_sound.stop()
        jingle_song.stop()

        done = True



    # Paddle and Ball collisions
    # -- Decided against using sprite collision because it wasn't accurate enough to segment the paddles into their angles.

    if my_ball.rect.left <= left_paddle.rect.right and my_ball.rect.top >= left_paddle.rect.top - my_ball.rect.h / 2 and my_ball.rect.bottom <= left_paddle.rect.bottom + my_ball.rect.h / 2:

        if multiplier < mult_lim:
            multiplier += multiplying_rate
        else:
            pass

        # Update the x and y velocities in the same way as the beginning using the difference between the collision point of the ball and the center of the platform as angles.
        # A multiplier is used on the x velocity to make the game increasingly difficult.

        # Calculating where the ball hit the paddle relative to the paddle height
        angleleft = float(left_paddle.rect.midright[1] - my_ball.rect.centery)

        # Adjusting the velocities
        my_ball.x_vel = float(math.cos(math.radians(angleleft)) * BALL_VEL) * multiplier
        my_ball.y_vel = - float(math.sin(math.radians(angleleft)) * BALL_VEL)

        contact_sound.play()

    elif my_ball.rect.right >= right_paddle.rect.left and my_ball.rect.top >= right_paddle.rect.top - my_ball.rect.h / 2 and my_ball.rect.bottom <= right_paddle.rect.bottom + my_ball.rect.h / 2:

        if multiplier < mult_lim:
            multiplier += multiplying_rate
        else:
            pass

        angleright = float(right_paddle.rect.midleft[1] - my_ball.rect.centery)

        my_ball.x_vel = - float(math.cos(math.radians(angleright)) * BALL_VEL) * multiplier
        my_ball.y_vel = - float(math.sin(math.radians(angleright)) * BALL_VEL)

        contact_sound.play()

    screen.fill(WHITE)

    # Score-Keeper
    pygame.display.set_caption("Left-Score: " + str(left_score) + "      ||      Right-Score: " + str(right_score))

    # Debugger Mouse
    pos = pygame.mouse.get_pos()
    # print(pos[0], pos[1])

    # Drawing

    all_sprites.draw(screen)
    all_sprites.update()




    pygame.display.flip()
    clock.tick(60)

pygame.quit()
