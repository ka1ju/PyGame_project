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
        self.img_start_btn.image = pygame.transform.scale(load_image('sprites/img_start_btn.png'), (50, 50))
        self.img_start_btn.rect = self.img_start_btn.image.get_rect()
        self.img_start_btn.rect.x = 0
        self.img_start_btn.rect.y = height // 2
        main_screen_sprites.add(self.img_start_btn)

        self.img_start = pygame.sprite.Sprite()
        self.img_start.image = pygame.transform.scale(load_image('sprites/play.png'), (40, 40))
        self.img_start.rect = self.img_start.image.get_rect()
        self.img_start.rect.x = 7
        self.img_start.rect.y = height // 2 + 5
        main_screen_sprites.add(self.img_start)

        self.img_shop_btn = pygame.sprite.Sprite()
        self.img_shop_btn.image = pygame.transform.scale(load_image('sprites/img_shop_btn.png'), (50, 50))
        self.img_shop_btn.rect = self.img_shop_btn.image.get_rect()
        self.img_shop_btn.rect.x = (width - 50) // 2
        self.img_shop_btn.rect.y = height // 2
        main_screen_sprites.add(self.img_shop_btn)

        self.img_bag = pygame.sprite.Sprite()
        self.img_bag.image = pygame.transform.scale(load_image('sprites/корзина.png'), (30, 30))
        self.img_bag.rect = self.img_bag.image.get_rect()
        self.img_bag.rect.x = (width - 50) // 2 + 10
        self.img_bag.rect.y = height // 2 + 10
        main_screen_sprites.add(self.img_bag)

        self.img_settings_btn = pygame.sprite.Sprite()
        self.img_settings_btn.image = pygame.transform.scale(load_image('sprites/img_settings_btn.png'), (50, 50))
        self.img_settings_btn.rect = self.img_settings_btn.image.get_rect()
        self.img_settings_btn.rect.x = width - 50
        self.img_settings_btn.rect.y = height // 2
        main_screen_sprites.add(self.img_settings_btn)

        self.img_settings = pygame.sprite.Sprite()
        self.img_settings.image = pygame.transform.scale(load_image('sprites/settings.png'), (30, 30))
        self.img_settings.rect = self.img_settings.image.get_rect()
        self.img_settings.rect.x = width - 50 + 10
        self.img_settings.rect.y = height // 2 + 10
        main_screen_sprites.add(self.img_settings)

        self.img_game_close = pygame.sprite.Sprite()
        self.img_game_close.image = pygame.transform.scale(load_image('sprites/img_shop_close_btn.png'), (25, 25))
        self.img_game_close.rect = self.img_game_close.image.get_rect()
        self.img_game_close.rect.x = width - 25
        self.img_game_close.rect.y = height - 25
        main_screen_sprites.add(self.img_game_close)

        self.img_close = pygame.sprite.Sprite()
        self.img_close.image = pygame.transform.scale(load_image('sprites/close.png'), (15, 15))
        self.img_close.rect = self.img_close.image.get_rect()
        self.img_close.rect.x = width - 20
        self.img_close.rect.y = height - 20
        main_screen_sprites.add(self.img_close)

    def render(self):
        main_screen_sprites.draw(screen)

    def click(self, position):
        if position[1] in range(height // 2, height // 2 + 50):
            if position[0] in range(0, 50):
                return 'start'
            elif position[0] in range((width - 50) // 2, (width - 50) // 2 + 50):
                return 'shop'
            elif position[0] in range(width - 50, width):
                return 'settings'
        elif position[1] in range(height - 25, height) and position[0] in range(width - 25, width):
            return 'exit'


shop_sprites = pygame.sprite.Group()

shop_sprites.add(background)


class Shop:
    def __init__(self):
        self.img_player_btn = pygame.sprite.Sprite()
        self.img_player_btn.image = pygame.transform.scale(load_image('sprites/img_player_btn.png'), (50, 50))
        self.img_player_btn.rect = self.img_player_btn.image.get_rect()
        self.img_player_btn.rect.x = 0
        self.img_player_btn.rect.y = 0
        shop_sprites.add(self.img_player_btn)

        self.img_player = pygame.sprite.Sprite()
        self.img_player.image = pygame.transform.scale(load_image('sprites/img_player.png'), (30, 30))
        self.img_player.rect = self.img_player.image.get_rect()
        self.img_player.rect.x = 10
        self.img_player.rect.y = 7.5
        shop_sprites.add(self.img_player)

        self.img_wall_btn = pygame.sprite.Sprite()
        self.img_wall_btn.image = pygame.transform.scale(load_image('sprites/img_wall_btn.png'), (50, 50))
        self.img_wall_btn.rect = self.img_wall_btn.image.get_rect()
        self.img_wall_btn.rect.x = (width - 50) // 2
        self.img_wall_btn.rect.y = 0
        shop_sprites.add(self.img_wall_btn)

        self.img_wall = pygame.sprite.Sprite()
        self.img_wall.image = pygame.transform.scale(load_image('sprites/img_wall.png'), (30, 30))
        self.img_wall.rect = self.img_wall.image.get_rect()
        self.img_wall.rect.x = (width - 50) // 2 + 10
        self.img_wall.rect.y = 10
        shop_sprites.add(self.img_wall)

        self.img_color_btn = pygame.sprite.Sprite()
        self.img_color_btn.image = pygame.transform.scale(load_image('sprites/img_color_btn.png'), (50, 50))
        self.img_color_btn.rect = self.img_wall_btn.image.get_rect()
        self.img_color_btn.rect.x = width - 50
        self.img_color_btn.rect.y = 0
        shop_sprites.add(self.img_color_btn)

        self.img_color = pygame.sprite.Sprite()
        self.img_color.image = pygame.transform.scale(load_image('sprites/капля.png'), (20, 28))
        self.img_color.rect = self.img_color.image.get_rect()
        self.img_color.rect.x = width - 35
        self.img_color.rect.y = 10
        shop_sprites.add(self.img_color)

        self.img_shop_close_btn = pygame.sprite.Sprite()
        self.img_shop_close_btn.image = pygame.transform.scale(load_image('sprites/img_shop_close_btn.png'), (25, 25))
        self.img_shop_close_btn.rect = self.img_shop_close_btn.image.get_rect()
        self.img_shop_close_btn.rect.x = width - 25
        self.img_shop_close_btn.rect.y = height - 25
        shop_sprites.add(self.img_shop_close_btn)

        self.img_close = pygame.sprite.Sprite()
        self.img_close.image = pygame.transform.scale(load_image('sprites/close.png'), (15, 15))
        self.img_close.rect = self.img_close.image.get_rect()
        self.img_close.rect.x = width - 20
        self.img_close.rect.y = height - 20
        shop_sprites.add(self.img_close)

    def render(self):
        shop_sprites.draw(screen)

    def click(self, position):
        if position[1] in range(0, 50):
            if position[0] in range(0, 50):
                return 'player'
            elif position[0] in range((width - 50) // 2, (width - 50) // 2 + 50):
                return 'wall'
            elif position[0] in range(width - 50, width):
                return 'color'
        elif position[1] in range(height - 25, height):
            if position[0] in range(width - 25, width):
                return 'shop_exit'


ms = MainScreen()

while running:
    ms.render()
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
            elif out == 'shop_exit':
                ms = MainScreen()
    if pygame.mouse.get_focused():
        screen.blit(CURSOR, (pygame.mouse.get_pos()))
        pygame.display.update()
    pygame.display.flip()
