import pygame
import os
import sys
from windows import MainScreen, Shop, Level_Pick

pygame.display.set_caption('cube-lab')
size = width, height = 500, 800
screen = pygame.display.set_mode(size)
running = True

screen.fill(pygame.Color('purple'))

CURSOR = pygame.image.load("sprites/img_cursor.png").convert_alpha()
pygame.mouse.set_cursor((8, 8), (4, 4), (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0))
pygame.mouse.set_visible(False)

player_sprites = pygame.sprite.Group()
wall_sprites = pygame.sprite.Group()
color_sprites = pygame.sprite.Group()


ms = MainScreen()
ms.screen = screen
ren = ''

while running:
    for event in pygame.event.get():
        ms.screen = screen
        ms.render(ren)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            place = event.pos
            out = ms.click(place)
            if out == 'exit':
                running = False
            elif out == 'start':
                ms = Level_Pick()
            elif out == 'shop':
                ms = Shop()
                ren = player_sprites
            elif out == 'shop_exit':
                ms = MainScreen()
                ren = ''
            elif out == 'player':
                ren = player_sprites
            elif out == 'wall':
                ren = wall_sprites
            elif out == 'color':
                ren = color_sprites
        if pygame.mouse.get_focused():
            screen.blit(CURSOR, (pygame.mouse.get_pos()))
            pygame.display.update()
        pygame.display.flip()