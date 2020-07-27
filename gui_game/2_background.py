import pygame

pygame.init()

pygame.display.set_caption("First Game")
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# set background
background = pygame.image.load(r"C:\Users\lhs-DT\Desktop\coding\python\pythonExam\gui_game\pics\background.png")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background, (0,0))
    #screen.fill((0,0,255))

    pygame.display.update()

pygame.quit()