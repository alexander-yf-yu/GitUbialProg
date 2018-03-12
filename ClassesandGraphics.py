"""
 ClassesandGraphics.py
 Alex Yu
 November 16th 2017
 Version 1.0
 The program creates a bunch of moving ellipses and rectangles!
"""

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

size = (700, 500)


class Rectangle(object):
    def __init__(self):
        self.x = random.randrange(700)
        self.y = random.randrange(500)
        self.change_x = random.randrange(-3, 3)
        self.change_y = random.randrange(-3, 3)

        # making sure that change(s) cannot be zero
        while self.change_x == 0 or self.change_y == 0:
            self.change_x = random.randrange(-3, 3)
            self.change_y = random.randrange(-3, 3)

        self.width = random.randrange(20, 70)
        self.height = random.randrange(20, 70)

        self.colour = [random.randrange(255), random.randrange(255), random.randrange(255)]

    def move(self):
        self.x += self.change_x
        self.y += self.change_y

        # if self.x > 700:
        #     self.x = 700
        #     self.change_x *= -1
        #     print("hit")

    def draw(self, screen):
        # self.width = random.randrange(20, 70)
        # self.height = random.randrange(20, 70)
        pygame.draw.rect(screen, self.colour, [self.x, self.y, self.width, self.height], 0)

    def collision(self):
        if self.x > size[0] - self.width:
            self.x = size[0] - self.width
            self.change_x = - self.change_x
        elif self.x < 0:
            self.x = 0
            self.change_x = - self.change_x
        elif self.y > size[1] - self.height:
            self.y = size[1] - self.height
            self.change_y = - self.change_y
        elif self.y < 0:
            self.y = 0
            self.change_y = - self.change_y


class Ellipse(Rectangle):
    def __init__ (self):
        super(Ellipse, self).__init__()

    def draw(self, screen):
        pygame.draw.ellipse(screen, self.colour, [self.x, self.y, self.width, self.height], 0)


pygame.init()

# Set the width and height of the screen [width, height]

screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

my_list = []

for i in range(200):
    my_object = Rectangle()
    my_ellipse = Ellipse()
    my_list.append(my_object)
    my_list.append(my_ellipse)


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)

    # --- Drawing code should go here
    # my_object.draw(screen)
    # my_object.move()

    for j in my_list:
        j.draw(screen)
        j.collision()
        j.move()


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
