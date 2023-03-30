import random
import sys
import pygame
from pygame.locals import *

#Global variables for game

FPS = 32   # Frames per second
SCREENWIDTH = 289
SCREENHEIGHT = 511

# Initializing Window Size for the Game
SCREEN = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT)) 

# Assigning 80% area of the screen to the image of the ground.
GROUNDY = 0.8

# For displaying the images
GROUND_SPRITES = {}

#For playing the sounds.
GROUND_SOUNDS = {}

PLAYER = '/gallery/sprites/bird.png'
BACKGROUND = '/gallery/sprites/background.png'
PIPE = '/gallery/sprites/pipe.png'

if __name__ == "__main__":
    
    # This is the main point from where our game will start.
    pygame.init()
    