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
GROUNDY = SCREENHEIGHT * 0.8

# For displaying the images
GROUND_SPRITES = {}

#For playing the sounds.
GROUND_SOUNDS = {}

PLAYER = 'gallery/sprites/bird.png'
BACKGROUND = 'gallery/sprites/background.png'
PIPE = 'gallery/sprites/pipe.png'


def welcomeScreen():
    playerx = int(SCREENWIDTH/5)
    playery = int(SCREENHEIGHT-GROUND_SPRITES['player'].get_height())/2
    messagex = int(SCREENWIDTH-GROUND_SPRITES['message'].get_width())/2
    messagey = int(SCREENHEIGHT*0.13)
    basex = 0

    while True:
        for event in pygame.event.get():

            # If the user press cross button or escape then close the game.
            if event.type == QUIT or (event.type == KEYDOWN or event.type==K_ESCAPE):
                pygame.quit()
                sys.exit()
            
            # If user presses space or up arrow key then start the game.
            elif event.type == KEYDOWN and (event.type == K_SPACE or event.type == K_UP):
                return
            
            else:
                
                SCREEN.blit(GROUND_SPRITES['background'],(0,0))
                SCREEN.blit(GROUND_SPRITES['player'],(playerx,playery))
                SCREEN.blit(GROUND_SPRITES['message'],(messagex,messagey))
                SCREEN.blit(GROUND_SPRITES['base'],(basex,GROUNDY))
                pygame.display.update()
                FPSCLOCK.tick(FPS)

def maingame():
    score = 0
    playerx = int(SCREENWIDTH/5)
    playery = int(SCREENWIDTH/2)
    basex = 0

    # Create 2 pipes for blitting on the screen
    newPipe1 = getRandomPipe()
    newPipe2 = getRandomPipe()

    # list for upper pipes
    upperPipes = [
        {'x':SCREENWIDTH+200,'y':newPipe1[0]['y']},
        {'x':SCREENWIDTH+200+(SCREENWIDTH/2),'y':newPipe2[1]['y']}
    ]

    # list for lower pipes
    lowerPipes = [
        {'x':SCREENWIDTH+200,'y':newPipe1[0]['y']},
        {'x':SCREENWIDTH+200+(SCREENWIDTH/2),'y':newPipe2[1]['y']}
    ]
    
    
    pipeVelX = -4

    playerVelY = -9
    playerMaxVelY = 10
    playerMinVelY = -8
    playerAccY = 1

    playerFlapAccv = -8 # velocity while flapping
    playerFlapped = False # It is true only when the bird is flapping


    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if playery > 0:
                    playerVelY = playerFlapAccv
                    playerFlapped = True
                    GROUND_SOUNDS['wing'].play()

def getRandomPipe():
    """
    Generate random pipes one is from top and second is from bottom for blitting
    """
    pipeHeight = GROUND_SPRITES['pipe'][0].get_height()
    offset = SCREENHEIGHT/3
    y2 = offset + random.randrange(0,int(SCREENHEIGHT-GROUND_SPRITES['base'].get_height()-1.2*offset))
    pipeX = SCREENWIDTH+10
    y1 = pipeHeight-y2+offset

    pipe = [
        {'x':pipeX,'y':-y1},
        {'x':pipeX,'y':y2}
    ]
    return pipe


if __name__ == "__main__":
    
    # This is the main point from where our game will start.
    
    pygame.init() # Initializes the game.
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption("Flappy Bird")

    GROUND_SPRITES['numbers'] = (
        pygame.image.load('gallery/sprites/0.png').convert_alpha(),
        pygame.image.load('gallery/sprites/1.png').convert_alpha(),
        pygame.image.load('gallery/sprites/2.png').convert_alpha(),
        pygame.image.load('gallery/sprites/3.png').convert_alpha(),
        pygame.image.load('gallery/sprites/4.png').convert_alpha(),
        pygame.image.load('gallery/sprites/5.png').convert_alpha(),
        pygame.image.load('gallery/sprites/6.png').convert_alpha(),
        pygame.image.load('gallery/sprites/7.png').convert_alpha(),
        pygame.image.load('gallery/sprites/8.png').convert_alpha(),
        pygame.image.load('gallery/sprites/9.png').convert_alpha()
    )

    GROUND_SPRITES['message'] = pygame.image.load('gallery/sprites/message.png').convert_alpha()
    GROUND_SPRITES['base'] = pygame.image.load('gallery/sprites/base.png').convert_alpha()
    
    # transform.rotate is used for displaying the image of pipe inverted
    GROUND_SPRITES['pipe'] = (
    pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(),180),
    pygame.image.load(PIPE).convert_alpha()
    )

    GROUND_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
    GROUND_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()


    # Game Sounds

    GROUND_SOUNDS['die'] = pygame.mixer.Sound('gallery/audio/die.wav')
    GROUND_SOUNDS['hit'] = pygame.mixer.Sound('gallery/audio/hit.wav')
    GROUND_SOUNDS['point'] = pygame.mixer.Sound('gallery/audio/point.wav')
    GROUND_SOUNDS['swoosh'] = pygame.mixer.Sound('gallery/audio/swoosh.wav')
    GROUND_SOUNDS['wing'] = pygame.mixer.Sound('gallery/audio/wing.wav')


while True:
    welcomeScreen()
    maingame()