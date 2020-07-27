import pygame

pygame.init()

pygame.display.set_caption("My First Game")
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.image.load(r"C:\Users\lhs-DT\Desktop\coding\python\pythonExam\gui_game\pics\background.png")

# load character
character = pygame.image.load(r"C:\Users\lhs-DT\Desktop\coding\python\pythonExam\gui_game\pics\character.png")
character_size = character.get_rect().size # get image size
character_width = character_size[0] # character width length
character_height = character_size[1] # character height length

character_x_pos = screen_width/2 - character_width/2
character_y_pos = screen_height - character_height

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0,0))
    screen.blit(character, (character_x_pos, character_y_pos))
    pygame.display.update()

pygame.quit()
