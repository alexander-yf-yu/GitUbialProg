'''
Drawing_AlexYu
Alex Yu
Nov 21st 2017
version 1.0
The program creates a record with a smiley on it.


'''

import pygame
import random
import math

# colours

GREEN = (60, 179, 113, 0)
RED = (112, 0, 0, 50)
PURPLE = (75,0,130, 50)
WHITE = (255, 255, 255)
GREY = (100, 100, 100)
BLACK = (0, 0, 0)


pygame.init()


# screen

width = 1000
height = 1000

size = (width , height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Alex Yu's Simple Drawing!")

done = False



clock = pygame.time.Clock()

while done != True:
    # main loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            done = True



    screen.fill(WHITE)

    modulus = random.randrange( 1 , 255 )
    # modulus = 200
    size = random.randrange( 5 , 20 )

    #RECORD

    circle_radius = 0
    circle_radius2 = 210
    circle_radius3 = 280


    for j in range(255, 0, -1):
        pygame.draw.circle(screen, GREY, [width / 2, height / 2], 255 + j, j)

    for r in range(0, 200, 1):

        pygame.draw.circle(screen, RED, [width / 2, height / 2], circle_radius + r, r)

    for r2 in range(200, 250, 1):

        pygame.draw.circle(screen, PURPLE, [width / 2, height / 2], circle_radius2 + r, r)

    for r2 in range(300, 310, 1):

        pygame.draw.circle(screen, GREY, [width / 2, height / 2], circle_radius3 + r, r)



    #  FACE

    rect_size = 30
    x_center = width / 2 - rect_size / 2
    y_center = height / 2 - rect_size / 2

    # LEFT EYE
    pygame.draw.rect(screen, BLACK, (x_center  - 60, y_center - 60, rect_size, rect_size), 0)

    # RIGHT EYE
    pygame.draw.rect(screen, BLACK, (x_center  + 60, y_center - 60, rect_size, rect_size), 0)

    # MOUTH
    pygame.draw.arc(screen, BLACK, (x_center - (rect_size + 10), y_center + 60, rect_size * 8, rect_size * 2), math.pi, 3 * math.pi / 2, 10)


    pygame.display.flip()


    clock.tick(5)


pygame.quit()
