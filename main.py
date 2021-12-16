import pygame

from menu import Menu
pygame.init()

scr = pygame.display.set_mode((500, 800))

running = True

CURSOR = pygame.image.load("textures/mouse_last_vers.png").convert_alpha()
pygame.mouse.set_cursor((8, 8), (4, 4), (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0))
pygame.mouse.set_visible(False)
field = pygame.image.load("textures/first_side_field.jpg").convert()
play = pygame.image.load("textures/start.png").convert()
back = pygame.image.load("textures/back_2.jpg").convert()
posxy = (75, 15)
choose = pygame.image.load("textures/big_choose.jpg").convert()
chxy = (179, 706)
side = "front"
user_coords = (225, 615)
u_pos = (side, user_coords)
user = pygame.image.load("textures/user.png").convert_alpha()
flag = "front"
stage = Menu(back, play)
while running:
    for event in pygame.event.get():
        stage.render(scr)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            click_return = stage.click(event.pos)
            if click_return == 'Level':
                pass#здесь поменять переменную stage из Menu на класс Level
        if pygame.mouse.get_focused():
            scr.blit(CURSOR, (pygame.mouse.get_pos()))
            pygame.display.update()
    pygame.display.flip()

