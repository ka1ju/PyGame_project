import pygame
import os
import sys

pygame.display.set_caption('cube-lab')
size = width, height = 500, 800
screen = pygame.display.set_mode(size)
running = True

screen.fill(pygame.Color('purple'))

CURSOR = pygame.image.load("sprites/img_cursor.png").convert_alpha()
pygame.mouse.set_cursor((8, 8), (4, 4), (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0))
pygame.mouse.set_visible(False)


def load_image(name, color_key=None):
    fullname = os.path.join('', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


main_screen_sprites = pygame.sprite.Group()

background = pygame.sprite.Sprite()
background.image = pygame.transform.scale(load_image('sprites/background.png'), (width, height))
background.rect = background.image.get_rect()
background.rect.x = 0
background.rect.y = 0
main_screen_sprites.add(background)


class MainScreen:
    def __init__(self):
        self.img_start_btn = pygame.sprite.Sprite()
        self.img_start_btn.image = pygame.transform.scale(load_image('sprites/img_start_btn.png'), (100, 100))
        self.img_start_btn.rect = self.img_start_btn.image.get_rect()
        self.img_start_btn.rect.x = 0
        self.img_start_btn.rect.y = height // 2 - 50
        main_screen_sprites.add(self.img_start_btn)

        self.img_start = pygame.sprite.Sprite()
        self.img_start.image = pygame.transform.scale(load_image('sprites/play.png'), (80, 80))
        self.img_start.rect = self.img_start.image.get_rect()
        self.img_start.rect.x = 15
        self.img_start.rect.y = height // 2 - 40
        main_screen_sprites.add(self.img_start)

        self.img_shop_btn = pygame.sprite.Sprite()
        self.img_shop_btn.image = pygame.transform.scale(load_image('sprites/img_shop_btn.png'), (100, 100))
        self.img_shop_btn.rect = self.img_shop_btn.image.get_rect()
        self.img_shop_btn.rect.x = (width - 50) // 2 - 25
        self.img_shop_btn.rect.y = height // 2 - 50
        main_screen_sprites.add(self.img_shop_btn)

        self.img_bag = pygame.sprite.Sprite()
        self.img_bag.image = pygame.transform.scale(load_image('sprites/корзина.png'), (60, 60))
        self.img_bag.rect = self.img_bag.image.get_rect()
        self.img_bag.rect.x = (width - 50) // 2 - 5
        self.img_bag.rect.y = height // 2 - 30
        main_screen_sprites.add(self.img_bag)

        self.img_settings_btn = pygame.sprite.Sprite()
        self.img_settings_btn.image = pygame.transform.scale(load_image('sprites/img_settings_btn.png'), (100, 100))
        self.img_settings_btn.rect = self.img_settings_btn.image.get_rect()
        self.img_settings_btn.rect.x = width - 100
        self.img_settings_btn.rect.y = height // 2 - 50
        main_screen_sprites.add(self.img_settings_btn)

        self.img_settings = pygame.sprite.Sprite()
        self.img_settings.image = pygame.transform.scale(load_image('sprites/settings.png'), (60, 60))
        self.img_settings.rect = self.img_settings.image.get_rect()
        self.img_settings.rect.x = width - 50 - 30
        self.img_settings.rect.y = height // 2 - 30
        main_screen_sprites.add(self.img_settings)

        self.img_game_close = pygame.sprite.Sprite()
        self.img_game_close.image = pygame.transform.scale(load_image('sprites/img_shop_close_btn.png'), (50, 50))
        self.img_game_close.rect = self.img_game_close.image.get_rect()
        self.img_game_close.rect.x = width - 50
        self.img_game_close.rect.y = height - 50
        main_screen_sprites.add(self.img_game_close)

        self.img_close = pygame.sprite.Sprite()
        self.img_close.image = pygame.transform.scale(load_image('sprites/close.png'), (25, 25))
        self.img_close.rect = self.img_close.image.get_rect()
        self.img_close.rect.x = width - 37
        self.img_close.rect.y = height - 37
        main_screen_sprites.add(self.img_close)

    def render(self, arg):
        main_screen_sprites.draw(screen)
        if ren != '':
            arg.draw(screen)

    def click(self, position):
        if position[1] in range(height // 2 - 50, height // 2 + 50):
            if position[0] in range(0, 100):
                return 'start'
            elif position[0] in range((width - 50) // 2 - 25, (width - 50) // 2 + 75):
                return 'shop'
            elif position[0] in range(width - 100, width):
                return 'settings'
        elif position[1] in range(height - 50, height) and position[0] in range(width - 50, width):
            return 'exit'


shop_sprites = pygame.sprite.Group()

shop_sprites.add(background)

player_sprites = pygame.sprite.Group()
wall_sprites = pygame.sprite.Group()
color_sprites = pygame.sprite.Group()


class Shop:
    def __init__(self):
        # спрайты магазина
        self.type = 'player'

        self.img_player_btn = pygame.sprite.Sprite()
        self.img_player_btn.image = pygame.transform.scale(load_image('sprites/img_player_btn.png'), (100, 100))
        self.img_player_btn.rect = self.img_player_btn.image.get_rect()
        self.img_player_btn.rect.x = 0
        self.img_player_btn.rect.y = 0
        shop_sprites.add(self.img_player_btn)

        self.img_player = pygame.sprite.Sprite()
        self.img_player.image = pygame.transform.scale(load_image('sprites/img_player.png'), (50, 50))
        self.img_player.rect = self.img_player.image.get_rect()
        self.img_player.rect.x = 25
        self.img_player.rect.y = 20
        shop_sprites.add(self.img_player)

        self.img_wall_btn = pygame.sprite.Sprite()
        self.img_wall_btn.image = pygame.transform.scale(load_image('sprites/img_wall_btn.png'), (100, 100))
        self.img_wall_btn.rect = self.img_wall_btn.image.get_rect()
        self.img_wall_btn.rect.x = (width - 100) // 2
        self.img_wall_btn.rect.y = 0
        shop_sprites.add(self.img_wall_btn)

        self.img_wall = pygame.sprite.Sprite()
        self.img_wall.image = pygame.transform.scale(load_image('sprites/img_wall.png'), (70, 70))
        self.img_wall.rect = self.img_wall.image.get_rect()
        self.img_wall.rect.x = (width - 50) // 2 - 10
        self.img_wall.rect.y = 15
        shop_sprites.add(self.img_wall)

        self.img_color_btn = pygame.sprite.Sprite()
        self.img_color_btn.image = pygame.transform.scale(load_image('sprites/img_color_btn.png'), (100, 100))
        self.img_color_btn.rect = self.img_wall_btn.image.get_rect()
        self.img_color_btn.rect.x = width - 100
        self.img_color_btn.rect.y = 0
        shop_sprites.add(self.img_color_btn)

        self.img_color = pygame.sprite.Sprite()
        self.img_color.image = pygame.transform.scale(load_image('sprites/капля.png'), (40, 56))
        self.img_color.rect = self.img_color.image.get_rect()
        self.img_color.rect.x = width - 70
        self.img_color.rect.y = 20
        shop_sprites.add(self.img_color)

        self.img_shop_close_btn = pygame.sprite.Sprite()
        self.img_shop_close_btn.image = pygame.transform.scale(load_image('sprites/img_shop_close_btn.png'), (50, 50))
        self.img_shop_close_btn.rect = self.img_shop_close_btn.image.get_rect()
        self.img_shop_close_btn.rect.x = width - 50
        self.img_shop_close_btn.rect.y = height - 50
        shop_sprites.add(self.img_shop_close_btn)

        self.img_close = pygame.sprite.Sprite()
        self.img_close.image = pygame.transform.scale(load_image('sprites/close.png'), (25, 25))
        self.img_close.rect = self.img_close.image.get_rect()
        self.img_close.rect.x = width - 37
        self.img_close.rect.y = height - 37
        shop_sprites.add(self.img_close)

        # спрайты персонажей
        self.player_1 = pygame.sprite.Sprite()
        self.player_1.image = pygame.transform.scale(load_image('sprites/player_1.png'), (50, 50))
        self.player_1.rect = self.player_1.image.get_rect()
        self.player_1.rect.x = 25
        self.player_1.rect.y = 150
        player_sprites.add(self.player_1)

        self.buy_player_1_btn = pygame.sprite.Sprite()
        self.buy_player_1_btn.image = pygame.transform.scale(load_image('sprites/img_buy_btn.png'), (25, 25))
        self.buy_player_1_btn.rect = self.buy_player_1_btn.image.get_rect()
        self.buy_player_1_btn.rect.x = 25
        self.buy_player_1_btn.rect.y = 210
        player_sprites.add(self.buy_player_1_btn)

        self.buy_player_1 = pygame.sprite.Sprite()
        self.buy_player_1.image = pygame.transform.scale(load_image('sprites/img_buy.png'), (25, 25))
        self.buy_player_1.rect = self.buy_player_1.image.get_rect()
        self.buy_player_1.rect.x = 27
        self.buy_player_1.rect.y = 210
        player_sprites.add(self.buy_player_1)

        self.choose_player_1_btn = pygame.sprite.Sprite()
        self.choose_player_1_btn.image = pygame.transform.scale(load_image('sprites/img_choose_btn.png'), (25, 25))
        self.choose_player_1_btn.rect = self.choose_player_1_btn.image.get_rect()
        self.choose_player_1_btn.rect.x = 50
        self.choose_player_1_btn.rect.y = 210
        player_sprites.add(self.choose_player_1_btn)

        self.choose_player_1 = pygame.sprite.Sprite()
        self.choose_player_1.image = pygame.transform.scale(load_image('sprites/img_choose.png'), (15, 15))
        self.choose_player_1.rect = self.choose_player_1.image.get_rect()
        self.choose_player_1.rect.x = 55
        self.choose_player_1.rect.y = 215
        player_sprites.add(self.choose_player_1)

        self.player_2 = pygame.sprite.Sprite()
        self.player_2.image = pygame.transform.scale(load_image('sprites/player_2.png'), (50, 50))
        self.player_2.rect = self.player_2.image.get_rect()
        self.player_2.rect.x = 125
        self.player_2.rect.y = 150
        player_sprites.add(self.player_2)

        self.buy_player_2_btn = pygame.sprite.Sprite()
        self.buy_player_2_btn.image = pygame.transform.scale(load_image('sprites/img_buy_btn.png'), (25, 25))
        self.buy_player_2_btn.rect = self.buy_player_2_btn.image.get_rect()
        self.buy_player_2_btn.rect.x = 125
        self.buy_player_2_btn.rect.y = 210
        player_sprites.add(self.buy_player_2_btn)

        self.buy_player_2 = pygame.sprite.Sprite()
        self.buy_player_2.image = pygame.transform.scale(load_image('sprites/img_buy.png'), (25, 25))
        self.buy_player_2.rect = self.buy_player_2.image.get_rect()
        self.buy_player_2.rect.x = 127
        self.buy_player_2.rect.y = 210
        player_sprites.add(self.buy_player_2)

        self.choose_player_2_btn = pygame.sprite.Sprite()
        self.choose_player_2_btn.image = pygame.transform.scale(load_image('sprites/img_choose_btn.png'), (25, 25))
        self.choose_player_2_btn.rect = self.choose_player_2_btn.image.get_rect()
        self.choose_player_2_btn.rect.x = 150
        self.choose_player_2_btn.rect.y = 210
        player_sprites.add(self.choose_player_2_btn)

        self.choose_player_2 = pygame.sprite.Sprite()
        self.choose_player_2.image = pygame.transform.scale(load_image('sprites/img_choose.png'), (15, 15))
        self.choose_player_2.rect = self.choose_player_2.image.get_rect()
        self.choose_player_2.rect.x = 155
        self.choose_player_2.rect.y = 215
        player_sprites.add(self.choose_player_2)

        self.player_3 = pygame.sprite.Sprite()
        self.player_3.image = pygame.transform.scale(load_image('sprites/player_3.png'), (50, 50))
        self.player_3.rect = self.player_3.image.get_rect()
        self.player_3.rect.x = 225
        self.player_3.rect.y = 150
        player_sprites.add(self.player_3)

        self.buy_player_3_btn = pygame.sprite.Sprite()
        self.buy_player_3_btn.image = pygame.transform.scale(load_image('sprites/img_buy_btn.png'), (25, 25))
        self.buy_player_3_btn.rect = self.buy_player_3_btn.image.get_rect()
        self.buy_player_3_btn.rect.x = 225
        self.buy_player_3_btn.rect.y = 210
        player_sprites.add(self.buy_player_3_btn)

        self.buy_player_3 = pygame.sprite.Sprite()
        self.buy_player_3.image = pygame.transform.scale(load_image('sprites/img_buy.png'), (25, 25))
        self.buy_player_3.rect = self.buy_player_3.image.get_rect()
        self.buy_player_3.rect.x = 227
        self.buy_player_3.rect.y = 210
        player_sprites.add(self.buy_player_3)

        self.choose_player_3_btn = pygame.sprite.Sprite()
        self.choose_player_3_btn.image = pygame.transform.scale(load_image('sprites/img_choose_btn.png'), (25, 25))
        self.choose_player_3_btn.rect = self.choose_player_3_btn.image.get_rect()
        self.choose_player_3_btn.rect.x = 250
        self.choose_player_3_btn.rect.y = 210
        player_sprites.add(self.choose_player_3_btn)

        self.choose_player_3 = pygame.sprite.Sprite()
        self.choose_player_3.image = pygame.transform.scale(load_image('sprites/img_choose.png'), (15, 15))
        self.choose_player_3.rect = self.choose_player_3.image.get_rect()
        self.choose_player_3.rect.x = 255
        self.choose_player_3.rect.y = 215
        player_sprites.add(self.choose_player_3)

        # спрайты стен
        self.wall_1 = pygame.sprite.Sprite()
        self.wall_1.image = pygame.transform.scale(load_image('sprites/wall_1.png'), (50, 50))
        self.wall_1.rect = self.wall_1.image.get_rect()
        self.wall_1.rect.x = 25
        self.wall_1.rect.y = 150
        wall_sprites.add(self.wall_1)

        self.wall_2 = pygame.sprite.Sprite()
        self.wall_2.image = pygame.transform.scale(load_image('sprites/wall_2.png'), (50, 50))
        self.wall_2.rect = self.wall_2.image.get_rect()
        self.wall_2.rect.x = 125
        self.wall_2.rect.y = 150
        wall_sprites.add(self.wall_2)

        self.wall_3 = pygame.sprite.Sprite()
        self.wall_3.image = pygame.transform.scale(load_image('sprites/wall_3.png'), (50, 50))
        self.wall_3.rect = self.wall_3.image.get_rect()
        self.wall_3.rect.x = 225
        self.wall_3.rect.y = 150
        wall_sprites.add(self.wall_3)

    def render(self, arg):
        shop_sprites.draw(screen)
        if ren != '':
            arg.draw(screen)

    def click(self, position):
        if position[1] in range(0, 100):
            if position[0] in range(0, 100):
                self.type = 'player'
                return 'player'
            elif position[0] in range((width - 100) // 2, (width - 100) // 2 + 100):
                self.type = 'wall'
                return 'wall'
            elif position[0] in range(width - 100, width):
                self.type = 'color'
                return 'color'
        elif position[1] in range(height - 50, height):
            if position[0] in range(width - 50, width):
                return 'shop_exit'
        if self.type == 'player':
            if position[1] in range(210, 235):
                if position[0] in range(25, 50):
                    return 'buy_player_1'
                elif position[0] in range(125, 150):
                    return 'buy_player_2'
                elif position[0] in range(225, 250):
                    return 'buy_player_3'


ms = MainScreen()
ren = ''

while running:
    ms.render(ren)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            place = event.pos
            out = ms.click(place)
            if out == 'exit':
                running = False
            elif out == 'start':
                pass
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
            elif out == 'buy_player_1':
                print(out)
            elif out == 'buy_player_2':
                print(out)
            elif out == 'buy_player_3':
                print(out)
    if pygame.mouse.get_focused():
        screen.blit(CURSOR, (pygame.mouse.get_pos()))
        pygame.display.update()
    pygame.display.flip()
