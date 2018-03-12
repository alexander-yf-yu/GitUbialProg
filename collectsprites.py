"""
CollectSprites.py

Step-by-step at: http://programarcadegames.com/index.php?chapter=lab_sprite_collecting&lang=en
Adapted from http://programarcadegames.com
"""
import pygame
import random

#Constants
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 400
PLAYER_VELOCITY = 3

class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super(Block, self).__init__()

        # Visual representation of Block
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Rectangle to represent position
        self.rect = self.image.get_rect()

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Player, self).__init__()

        self.image = pygame.Surface((20, 15))
        self.image.fill(BLACK)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.xvel = 0
        self.yvel = 0

    def changevelocity(self, x, y):
        """ Changes velocity of the player """
        self.xvel += x
        self.yvel += y

    def update(self):
        """ Updates the position of the Player according to velocity """
        self.rect.x += self.xvel
        self.rect.y += self.yvel

pygame.init()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# TODO: Create bad_block_list
# TODO: Create good_block_list

block_list = pygame.sprite.Group()

# All sprites in app
all_sprites_list = pygame.sprite.Group()

for i in range(50):
    block = Block(BLACK, 20, 15)

    # Random location for block
    block.rect.x = random.randrange(SCREEN_WIDTH)
    block.rect.y = random.randrange(SCREEN_HEIGHT)

    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)

# TODO: Create instance of player class
player = Block(RED, 20, 15)
all_sprites_list.add(player)

done = False
lock = pygame.time.Clock()

score = 0

# -------- Main Program Loop -----------
while not done:
    # TODO: Control character with keyboard
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Clear the screen
    screen.fill(WHITE)

    # Get the current mouse position. This returns the position
    # as a list of two numbers.
    pos = pygame.mouse.get_pos()

    # Fetch the x and y out of the list,
       # just like we'd fetch letters out of a string.
    # Set the player object to the mouse location
    player.rect.x = pos[0]
    player.rect.y = pos[1]

    # TODO: Check for good and bad collisions
    # See if the player block has collided with anything.
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)

    # TODO: Update score - good collisions = score + 1
    # TODO: Update score - bad collisions = score - 1
    # Check the list of collisions.
    for block in blocks_hit_list:
        score += 1
        print(score)

    # Draw all the spites
    all_sprites_list.draw(screen)

    pygame.display.flip()
    # Clock.tick(60)

pygame.quit()
