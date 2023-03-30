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
    
    pygame.init() # Initializes the game.
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption("Flappy Bird")

    GROUND_SPRITES['numbers'] = (
        pygame.image.load('/gallery/sprites/0.png').convert_alpha(),
        pygame.image.load('/gallery/sprites/1.png').convert_alpha(),
        pygame.image.load('/gallery/sprites/2.png').convert_alpha(),
        pygame.image.load('/gallery/sprites/3.png').convert_alpha(),
        pygame.image.load('/gallery/sprites/4.png').convert_alpha(),
        pygame.image.load('/gallery/sprites/5.png').convert_alpha(),
        pygame.image.load('/gallery/sprites/6.png').convert_alpha(),
        pygame.image.load('/gallery/sprites/7.png').convert_alpha(),
        pygame.image.load('/gallery/sprites/8.png').convert_alpha(),
        pygame.image.load('/gallery/sprites/9.png').convert_alpha()
    )

    GROUND_SPRITES['message'] = pygame.image.load('/gallery/sprites/message.png').convert_alpha()
    GROUND_SPRITES['base'] = pygame.image.load('/gallery/sprites/base.png').convert_alpha()
    
    # transform.rotate is used for displaying the image of pipe inverted
    GROUND_SPRITES['pipe'] = (
    pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(),180),
    pygame.image.load(PIPE).convert_alpha()
    )

    # Game Sounds

    GROUND_SOUNDS['die'] = pygame.mixer.Sound('/gallery/audio/die.wav')
    GROUND_SOUNDS['hit'] = pygame.mixer.Sound('/gallery/audio/hit.wav')
    GROUND_SOUNDS['point'] = pygame.mixer.Sound('/gallery/audio/point.wav')
    GROUND_SOUNDS['swoosh'] = pygame.mixer.Sound('/gallery/audio/swoosh.wav')
    GROUND_SOUNDS['wing'] = pygame.mixer.Sound('/gallery/audio/wing.wav')
    