import pygame
import os
import sys
import json
import time
from windows import MainScreen, Shop, Level_Pick, level, Win, Bad, Rules, Exit
from PIL import Image

pygame.display.set_caption('CHECH')
size = width, height = 500, 800
screen = pygame.display.set_mode(size)
running = True


def load_image(file_name):
    fullname = os.path.join('', file_name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


screen.fill(pygame.Color('purple'))

CURSOR = pygame.image.load("sprites/img_cursor.png").convert_alpha()
pygame.mouse.set_cursor((8, 8), (4, 4), (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0))
pygame.mouse.set_visible(False)

ren = ''
ms = Rules(s=screen)
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
                ms = Exit(s=screen)
            elif out == 'accept':
                running = False
            elif out == 'decline':
                ms = MainScreen(s=screen)
            elif out == 'ok':
                ms = MainScreen(s=screen)
            elif out == 'rules':
                ms = Rules(s=screen)
            elif out == 'win':
                ms = Win(screen, time.time() - ms.time, ms.level)
            elif out == "GOTOCHOISE":
                ms = Level_Pick(screen)
            elif out == "GOTOMAIN":
                ms = MainScreen(screen)
            elif out == 'level':
                g = walls_load(ms.level)
                achievements = ms.level
                ms = level(screen, g, achievements)
            elif out == 'start':
                ms = Level_Pick(screen)
            elif out == 'shop':
                ms = Shop(s=screen)
                ren = ms.player_sprites
            elif out == 'shop_exit':
                ms = MainScreen(s=screen)
                ren = ''
            elif out == 'player':
                ren = ms.player_sprites
            elif out == 'wall':
                ren = ms.wall_sprites
            elif out == 'color':
                ren = ms.color_sprites
            elif out == 'buy_player_1':
                my_money = open('progress.json', 'r', encoding='utf-8')
                money = json.load(my_money)
                my_money.close()
                my_money = open('progress.json', 'w', encoding='utf-8')
                achievements = open('achievements.json', 'r', encoding='utf-8')
                cost = json.load(achievements)
                achievements.close()
                achievements = open('achievements.json', 'w', encoding='utf-8')
                if money['stars'] >= cost['players']['player_1']['cost']:
                    money['stars'] -= cost['players']['player_1']['cost']
                    cost['players']['player_1']['opened'] = 1
                json.dump(cost, achievements)
                json.dump(money, my_money)
                my_money.close()
                achievements.close()
            elif out == 'buy_player_2':
                my_money = open('progress.json', 'r', encoding='utf-8')
                money = json.load(my_money)
                my_money.close()
                my_money = open('progress.json', 'w', encoding='utf-8')
                achievements = open('achievements.json', 'r', encoding='utf-8')
                cost = json.load(achievements)
                achievements.close()
                achievements = open('achievements.json', 'w', encoding='utf-8')
                if money['stars'] >= cost['players']['player_2']['cost']:
                    money['stars'] -= cost['players']['player_2']['cost']
                    cost['players']['player_2']['opened'] = 1
                json.dump(cost, achievements)
                json.dump(money, my_money)
                my_money.close()
                achievements.close()
            elif out == 'buy_player_3':
                my_money = open('progress.json', 'r', encoding='utf-8')
                money = json.load(my_money)
                my_money.close()
                my_money = open('progress.json', 'w', encoding='utf-8')
                achievements = open('achievements.json', 'r', encoding='utf-8')
                cost = json.load(achievements)
                achievements.close()
                achievements = open('achievements.json', 'w', encoding='utf-8')
                if money['stars'] >= cost['players']['player_3']['cost']:
                    money['stars'] -= cost['players']['player_3']['cost']
                    cost['players']['player_3']['opened'] = 1
                json.dump(cost, achievements)
                json.dump(money, my_money)
                my_money.close()
                achievements.close()
            elif out == 'choose_player_1':
                achievements = open('achievements.json', 'r', encoding='utf-8')
                cost = json.load(achievements)
                achievements.close()
                if cost['players']['player_1']['opened'] == 1:
                    player = Image.open('textures/player_1.png')
                    player = player.resize((50, 50))
                    prev_player = Image.open('textures/user.png')
                    n = open('player.txt', 'r', encoding='utf-8')
                    name = n.read()
                    n.close()
                    n = open('player.txt', 'w', encoding='utf-8')
                    n.write('player_1.png')
                    prev_player.save('textures/' + name)
                    player.save('textures/user.png')
            elif out == 'choose_player_2':
                achievements = open('achievements.json', 'r', encoding='utf-8')
                cost = json.load(achievements)
                achievements.close()
                if cost['players']['player_2']['opened'] == 1:
                    player = Image.open('textures/player_2.png')
                    player = player.resize((50, 50))
                    prev_player = Image.open('textures/user.png')
                    n = open('player.txt', 'r', encoding='utf-8')
                    name = n.read()
                    n.close()
                    n = open('player.txt', 'w', encoding='utf-8')
                    n.write('player_2.png')
                    prev_player.save('textures/' + name)
                    player.save('textures/user.png')
            elif out == 'choose_player_3':
                achievements = open('achievements.json', 'r', encoding='utf-8')
                cost = json.load(achievements)
                achievements.close()
                if cost['players']['player_3']['opened'] == 1:
                    player = Image.open('textures/player_3.png')
                    player = player.resize((50, 50))
                    prev_player = Image.open('textures/user.png')
                    n = open('player.txt', 'r', encoding='utf-8')
                    name = n.read()
                    n.close()
                    n = open('player.txt', 'w', encoding='utf-8')
                    n.write('player_3.png')
                    prev_player.save('textures/' + name)
                    player.save('textures/user.png')
        if event.type == star_up and ms.__class__.__name__ == 'Win':
            ms.star_plus()
            pygame.display.flip()
        if event.type == mines and ms.__class__.__name__ == 'level' and (
                ms.mines_active != [] or ms.mines_deactive != []):
            g = ms.mineses()
            if g == 'died':
                ms = Bad(screen)
    if pygame.mouse.get_focused():
        screen.blit(CURSOR, (pygame.mouse.get_pos()))
        pygame.display.flip()
    pygame.display.flip()
    clock.tick(60)
