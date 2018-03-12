'''
snow.py
Alex Yu
Oct 19th 2017
version 1.0
The program creates snow!


'''

import pygame
import random
import math

# colours

GREEN = (60, 179, 113, 0)
BLACK = (0,0,0)
RED = (112, 0, 0, 50)
PURPLE = (75,0,130, 50)
WHITE = (255, 255, 255)
GREY = (50, 50, 50)
ORANGE = (255,140,0)



pygame.init()


# screen

width = 1000
height = 700
# width = 2047
# height = 1151

number_of_snow = 300

fall_speed = 1

size = (width , height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Snow!")

done = False



clock = pygame.time.Clock()

flake_coords = []

for item in range(number_of_snow):
    x = random.randrange(0, width)
    y = random.randrange(0, height)
    wind = random.randrange(-2, 2)
    flake_size = random.randrange(1, 5)

    flake_coords.append([x, y, flake_size, wind])

def draw_snowman(screen, x, y):
    '''draws a snowman on the screen at defined coordinates'''
    # Head
    pygame.draw.ellipse(screen, WHITE, [35 + x, y, 25, 25])
    # Eyes
    pygame.draw.ellipse(screen, BLACK, [41 + x, y + 5, 5, 5])
    pygame.draw.ellipse(screen, BLACK, [49 + x, y + 5, 5, 5])
    # Nose
    pygame.draw.ellipse(screen, ORANGE, [45 + x, y + 10, 5, 5])
    # Middle
    pygame.draw.ellipse(screen, WHITE, [23 + x, 22 + y, 50, 50])
    # Bottom
    pygame.draw.ellipse(screen, WHITE, [x, y + 65, 100, 100])

pygame.mouse.set_visible(False)


while done != True:
    # main loop

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            done = True

    pos = pygame.mouse.get_pos()

    screen.fill(BLACK)

    for item in flake_coords:

        # y = y + flake-size (FALLING speed)
        item[1] += item[2] + 3

        # x = x + global wind (STATIC wind)
        item[0] += item[3]


        # DO THIS IF YOU FIGURE OUT how to use NON_INT VALUES WITH THIS
        # item[0] += item[3] * (1 / item[2])

        # x = x + random wind (CHANGING wind)
        # item[0] += random.randrange(-2, 2) * (1 / item[2])
        pygame.draw.circle(screen, WHITE, [item[0], item[1]], item[2])



        if item[1] > height:
            item[0] = random.randrange(width)
            item[1] = random.randrange(-10, -2)

        # if item[0] > width:
        #     item[0] = random.randrange(width)
        #     item[1] = random.randrange(-10, -2)





        draw_snowman(screen, pos[0], pos[1])


    pygame.display.flip()


    clock.tick(60)

pygame.quit()
