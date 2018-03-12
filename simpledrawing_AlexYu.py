'''
simpledrawing_AlexYu.py
Alex Yu
Oct 16th 2017
version 1.0
The program creates an arrow on screen


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



    # Use these as a replacement for "size" if you want the shape to stay the same!
    # rect_width = 30
    # rect_height = 30




    modulus = random.randrange( 1 , 255 )
    # modulus = 200


    size = random.randrange( 5 , 20 )





    for i in range(0, 1020, 1):

        colour_one = (i % modulus, i % modulus, i % modulus)
        colour_two = (random.randrange(1 , 255) , random.randrange( 1, 255 ) , random.randrange( 1, 255 ) , random.randrange( 1, 255 ))


        # CURRENT HAND IN
        # pygame.draw.rect(screen, colour_two, [ width - i , height - i, size , size], (i / 90) ** 3)

        #ALTERNATIVE VERSION
        pygame.draw.rect(screen, colour_one, [ width - i , height - i, size , size], (i / 90) ** 3)



    #RECORD

    # circle_radius = 0
    # circle_radius2 = 210
    # circle_radius3 = 280


    # for j in range(255, 0, -1):
    #     colour_one = (i % 255, i % 255, i % 255)
    #     pygame.draw.circle(screen, colour_one, [width / 2, height / 2], 255 + j, j)

    # for r in range(0, 200, 1):
    #
    #     pygame.draw.circle(screen, RED, [width / 2, height / 2], circle_radius + r, r)
    #
    # for r2 in range(200, 250, 1):
    #
    #     pygame.draw.circle(screen, PURPLE, [width / 2, height / 2], circle_radius2 + r, r)
    #
    # for r2 in range(300, 310, 1):
    #
    #     pygame.draw.circle(screen, GREY, [width / 2, height / 2], circle_radius3 + r, r)

    pygame.display.flip()


    clock.tick(5)


pygame.quit()
