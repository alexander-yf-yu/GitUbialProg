'''
Controllers_AlexYu
Alex Yu
November 1st
Version 1.0
A ufo and planet move around and they hit each other.
'''

import pygame
import math
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
x_vel = 0
y_vel = 0
vel = 15
body_h = 25
body_w = 100
planet_c = (204, 153, 0)
ring_c = (153, 77, 0)
ring_s = [200, 20, 5]
size = (900, 700)
pos_mouse = [size[0] * 3 / 4, size[1] * 3 / 4]
pos_key = [size[0] / 4, size[1] / 4]
activation_d = 50


background_image = pygame.image.load("Space/img/galaxy.jpg")
# player = pygame.image.load("player.png")


pygame.init()

# Set the width and height of the screen [width, height]

screen = pygame.display.set_mode(size)

pygame.display.set_caption("Controller!")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

def draw_saturn(screen, x, y):
    '''draws a snowman on the screen at defined coordinates'''
    #Planet
    pygame.draw.circle(screen, planet_c, [x, y], 30, 0)
    #Ring
    pygame.draw.arc(screen, ring_c, [x - (ring_s[0] / 2 - 5), y - (ring_s[1] / 2 - 10) , ring_s[0], ring_s[1]], 2, 1.3, ring_s[2])

def draw_ufo(screen, x, y):

    body_i = [pos_key[0], pos_key[1]]

    #Body
    pygame.draw.circle(screen, GREEN, [pos_key[0] + (body_w / 2), pos_key[1] - body_h], body_h, 0)
    #Cabin
    pygame.draw.polygon(screen, WHITE, [ (body_i[0], body_i[1]), (body_i[0] + body_w, body_i[1]), (body_i[0] + (body_w * 3 / 4), body_i[1] - body_h), (body_i[0] + (body_w / 4), body_i[1] - body_h)], 0)


# Difficulty Selection & Intro:
print("Welcome to Controller!")
print("Controller is a two player game, where the objective is to crash the ufo into saturn. Saturn-controller's job is to avoid the ufo!")
print("The game ends when there is a collision.")
diff = raw_input("Choose your difficulty! - in the perspective of the ufo: Hard, Medium, or Easy   ")

if diff.lower() == "hard":
    activation_d = 75
    vel = 10
elif diff.lower() == "medium":
    activation_d = 50
    vel = 12
elif diff.lower() == "easy":
    activation_d = 30
    vel = 15
else:
    print("Invalid Input")
    done = True

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_vel = -vel
            elif event.key == pygame.K_RIGHT:
                x_vel = vel
            elif event.key == pygame.K_UP:
                y_vel = -vel
            elif event.key == pygame.K_DOWN:
                y_vel = vel
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_vel = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_vel = 0

    # --- Game logic should go here

    pos = pygame.mouse.get_pos()
    pos_key[0] += x_vel
    pos_key[1] += y_vel

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.blit(background_image, [0, 0])

    # --- Drawing code should go here
    draw_saturn(screen, pos_mouse[0], pos_mouse[1])
    draw_ufo(screen, 100, 100)


    if pygame.mouse.get_pressed()[0] and pos[0] >= pos_mouse[0] - activation_d and pos[0] <= pos_mouse[0] + activation_d and pos[1] >= pos_mouse[1] - activation_d and pos[1] <= pos_mouse[1] + activation_d:
        pos_mouse[0] = pos[0]
        pos_mouse[1] = pos[1]
        draw_saturn(screen, pos[0], pos[1])

    if pos_key[0] <= 0:
        pos_key[0] = vel + 1
    elif pos_key[1] <= body_h * 2:
        pos_key[1] = body_h * 2 + (vel + 1)
    elif pos_key[0] >= size[0] - body_w:
        pos_key[0] = size[0] - body_w - (vel + 1)
    elif pos_key[1] >= size[1]:
        pos_key[1] = size[1]

    print("Mouse pos: " + str(pos) + " / Saturn pos: " + str(pos_mouse))
    print("ufo pos " + str(pos_key))
    print("activation_d: " + str(activation_d))

    if pos_mouse[0] - body_h <= pos_key[0] + body_w and pos_mouse[0] + body_h >= pos_key[0] and pos_mouse[1] + body_h >= pos_key[1] - 2 * body_h and pos_mouse[1] - body_h <= pos_key[1]:
        # print("DEATH")
        print("You Win!")
        done = True




    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
