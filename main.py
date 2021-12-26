import pygame
import os
import sys
import json
import time
from windows import MainScreen, Shop, Level_Pick, level, Win, Bad

pygame.display.set_caption('cube-lab')
size = width, height = 500, 800
screen = pygame.display.set_mode(size)
running = True


def load_image(name, color_key=None):
    fullname = os.path.join('', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


screen.fill(pygame.Color('purple'))

CURSOR = pygame.image.load("sprites/img_cursor.png").convert_alpha()
pygame.mouse.set_cursor((8, 8), (4, 4), (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0))
pygame.mouse.set_visible(False)

player_sprites = pygame.sprite.Group()
wall_sprites = pygame.sprite.Group()
color_sprites = pygame.sprite.Group()


ren = ''
ms = MainScreen()
ms.screen = screen


def walls_load(ind):
    ind -= 1
    f = open('levels.json', 'r', encoding='utf-8')
    g = json.load(f)
    f.close()
    return g[ind]


clock = pygame.time.Clock()

star_up = pygame.USEREVENT + 25
pygame.time.set_timer(star_up, 40)
mines = pygame.USEREVENT + 26
pygame.time.set_timer(mines, 500)

while running:
    ms.screen = screen
    ms.render(ren)
    for event in pygame.event.get():
        if pygame.mouse.get_focused():
            screen.blit(CURSOR, (pygame.mouse.get_pos()))
            pygame.display.flip()
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            place = event.pos
            out = ms.click(place)
            if out == 'exit':
                running = False
            elif out == 'win':
                ms = Win(screen, time.time() - ms.time, ms.level)
            elif out == 'level':
                g = walls_load(ms.level)
                h = ms.level
                ms = level(screen, g, h)
            elif out == 'start':
                ms = Level_Pick()
            elif out == 'shop':
                ms = Shop()
                ren = player_sprites
                money = json.load(open('progress.json', 'r', encoding='utf-8'))['stars']
                achievements_r = json.load(open('achievements.json', 'r'))
                achievements_w = json.load(open('achievements.json', 'w'))
            elif out == 'shop_exit':
                ms = MainScreen()
                ren = ''
            elif out == 'player':
                ren = player_sprites
            elif out == 'wall':
                ren = wall_sprites
            elif out == 'color':
                ren = color_sprites
            elif out == 'buy_player_1':
                if money >= ms.player_1_cost:
                    achievements_r['players']['player_1'] = "1"
            elif out == 'buy_player_2':
                print(out)
            elif out == 'buy_player_3':
                print(out)
        if event.type == star_up and ms.__class__.__name__ == 'Win':
            ms.star_plus()
            pygame.display.flip()
        if event.type == mines and ms.__class__.__name__ == 'level' and (ms.mines_active != [] or ms.mines_deactive != []):
            g = ms.mineses()
            if g == 'died':
                ms = Bad(screen)
    if pygame.mouse.get_focused():
        screen.blit(CURSOR, (pygame.mouse.get_pos()))
        pygame.display.flip()
    pygame.display.flip()
    clock.tick(60)