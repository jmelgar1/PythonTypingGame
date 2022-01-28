# Imports
import pygame, sys
from pygame.locals import *
import random

# Initializing
pygame.init()

# Setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Creating colors
BLACK = (0, 0, 0)
ALICEBLUE = (240, 248, 255)

# Other Variables for use in the program
SPEED = 5
wordSpeed = 0.05

# Create a white screen
SPACEVIEW = pygame.display.set_mode((1000, 600))
SPACEVIEW.fill(BLACK)
pygame.display.set_caption("Typing Game")

font = pygame.font.SysFont("arial", 32)

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

def new_word():
    global firstWord, nextWord, word_X, word_Y, text, pointCaption, wordSpeed
    word_Y = random.randint(150, 550)
    word_X = 0
    wordSpeed += 0.07
    nextWord = ""
    lines = open("wordlist.txt").read().splitlines()
    firstWord = random.choice(lines)
    text = font.render(firstWord, True, ALICEBLUE)

background = Background()

# Adding a new User event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

new_word()

# Game Loop
while True:
    word_X += wordSpeed

    SPACEVIEW.blit(text, (word_X, word_Y))

    # Cycles through all occurring events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            nextWord += pygame.key.name(event.key)
            if firstWord.startswith(nextWord):
                new_word()
        else:
            nextWord + ""

    pygame.display.update()

    background.update()
    background.render()

    FramePerSec.tick(FPS)
