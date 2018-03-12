import pygame
import math
import random






c = ["over" , "under" , "around"]
x = [0, 1, 2, 3, 4]


print(c[1])
print(x[0])


# Iterating through the list

for item in x:
    print(item)


# NOTE: You do not need to use index [item]!


# Adding something to the list:

x.append("I'm a string!")

for item in x:
    print(item)

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

    pygame.draw.rect(screen, GREEN, [30,30,30,30], 900)

    pygame.display.flip()


    clock.tick(5)
