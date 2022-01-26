# Imports
import pygame, sys
from pygame.locals import *
import random, time

# Initializing
pygame.init()

# Setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Creating colors
BLACK = (0, 0, 0)

# Other Variables for use in the program
SPEED = 5

# Create a white screen
SPACEVIEW = pygame.display.set_mode((1000, 600))
SPACEVIEW.fill(BLACK)
pygame.display.set_caption("Typing Game")


class Background():
    def __init__(self):
        self.bgimage = pygame.image.load('spaceBackground.png')
        self.rectBGimg = self.bgimage.get_rect()

        self.bgY1 = 0
        self.bgX1 = 0

        self.bgY2 = 0
        self.bgX2 = self.rectBGimg.width

        self.moving_speed = 5

    def update(self):
        self.bgX1 -= self.moving_speed
        self.bgX2 -= self.moving_speed
        if self.bgX1 <= -self.rectBGimg.width:
            self.bgX1 = self.rectBGimg.width
        if self.bgX2 <= -self.rectBGimg.width:
            self.bgX2 = self.rectBGimg.width

    def render(self):
        SPACEVIEW.blit(self.bgimage, (self.bgX1, self.bgY1))
        SPACEVIEW.blit(self.bgimage, (self.bgX2, self.bgY2))

background = Background()

# Adding a new User event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Game Loop
while True:

    # Cycles through all occurring events
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    background.update()
    background.render()

    pygame.display.update()
    FramePerSec.tick(FPS)
