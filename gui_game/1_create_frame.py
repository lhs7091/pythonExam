import pygame

# initialize for pygame
pygame.init()

# display
screen_width = 480
screen_height = 640

screen = pygame.display.set_mode((screen_width, screen_height))

# game title
pygame.display.set_caption("Game")

# event loop
running = True # on progress of game
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# pygame exit
pygame.quit()