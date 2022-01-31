# Imports
import pygame, sys
from pygame.locals import *
import random
from playsound import playsound

# Initializing
pygame.init()

# Setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Creating colors
BLACK = (0, 0, 0)
ALICEBLUE = (240, 248, 255)
AQUAMARINE = (102, 205, 170)
COBALT = (61, 145, 64)
CFBLUE = (100, 149, 237)
RED = (255, 0, 0)

# Other Variables for use in the program
SPEED = 5
wordSpeed = 0.05
inputText = ""
inputTextActive = True
points = 0
background_speed = 5
wpm = 0

# Create a white screen
SPACEVIEW = pygame.display.set_mode((1000, 600))
SPACEVIEW.fill(BLACK)
pygame.display.set_caption("Typing Game")

#Adding various things to screen


font = pygame.font.SysFont("arial", 32)

class Background():
    def __init__(self):
        self.bgimage = pygame.image.load('spaceBackground.png')
        self.rectBGimg = self.bgimage.get_rect()

        self.bgY1 = 0
        self.bgX1 = 0

        self.bgY2 = 0
        self.bgX2 = self.rectBGimg.width

    def update(self):
        self.bgX1 -= background_speed
        self.bgX2 -= background_speed
        if self.bgX1 <= -self.rectBGimg.width:
            self.bgX1 = self.rectBGimg.width
        if self.bgX2 <= -self.rectBGimg.width:
            self.bgX2 = self.rectBGimg.width

    def render(self):
        SPACEVIEW.blit(self.bgimage, (self.bgX1, self.bgY1))
        SPACEVIEW.blit(self.bgimage, (self.bgX2, self.bgY2))

#creates a new word for the user
def new_word():
    global firstWord, nextWord, word_X, word_Y, text, PointHolder, wordSpeed, inputText
    word_Y = random.randint(100, 490)
    word_X = 0
    wordSpeed += 0.07
    nextWord = ""
    lines = open("wordlist.txt").read().splitlines()
    firstWord = random.choice(lines)
    text = font.render(firstWord, True, ALICEBLUE)
    inputText = ""

#sets background variable
background = Background()

#starts the game off with a word
new_word()

# Game Loop
while True:
    word_X += wordSpeed

    #draw word to screen
    SPACEVIEW.blit(text, (word_X, word_Y))

    #show users text entry
    text_surf = font.render(inputText, True, COBALT)
    text_rect = text_surf.get_rect(center=(1000/2, 565))
    SPACEVIEW.blit(text_surf, text_rect)

    #create bottom gui
    pygame.draw.rect(SPACEVIEW, AQUAMARINE, pygame.Rect(50, 530, 900, 150), 2, 100)

    #create score counter
    PointHolder = font.render(str(points), True, COBALT)
    SPACEVIEW.blit(PointHolder, (200,550))
    scoreCounter = font.render("Score:", True, CFBLUE)
    SPACEVIEW.blit(scoreCounter, (100, 550))

    #check if word is out of frame
    if word_X > 1000:
        background_speed == 0
        text_gameOver = font.render("Game Over", True, RED)
        text_rectGameOver = text_gameOver.get_rect(center=(500, 300))
        SPACEVIEW.blit(text_gameOver, text_rectGameOver)

    # Cycles through all occurring events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        #checks if user typed a word correctly
        if inputText == firstWord:
            new_word()
            #add 1 point for each word
            points += 100
            #speed up background
            background_speed += 0.35

            #play sound for correct answers (broken for versions over 3.8)
            if sys.version_info[0] > 3.8:
                playsound("correct.wav")

        #takes in user keyboard input
        elif event.type == pygame.KEYDOWN and inputTextActive:
            if event.key == pygame.K_RETURN:
                inputTextActive == False
            elif event.key == pygame.K_BACKSPACE:
                inputText = inputText[:-1]
            else:
                inputText += event.unicode

    pygame.display.flip()
    background.update()
    background.render()

    FramePerSec.tick(FPS)
