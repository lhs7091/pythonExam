import pygame
import sys
from time import sleep

#BLACK = (0,0,0)
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640


#Draw object on game
def drawObject(obj, x, y):
    global gamePad
    gamePad.blit(obj, (x, y))


def initGame():
    global gamePad, clock, background
    pygame.init()
    gamePad = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('PyShooting game')
    background = pygame.image.load('./PyShooting/background.png')
    fighter = pygame.image.load('./PyShooting/fighter.png')
    clock = pygame.time.Clock()


def runGame():
    global gamePad, clock, background

    onGame = False
    while not onGame:
        for event in pygame.event.get():
            if event in [pygame.QUIT]:
                pygame.quit()
                sys.exit()

        #gamePad.fill(BLACK)
        drawObject(background, 0, 0)
        pygame.display.update()

        clock.tick(60) #60fps

    pygame.quit()


initGame()
runGame()

