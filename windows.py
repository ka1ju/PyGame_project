import pygame
import os
import sys
import time
import json

size = width, height = 500, 800


def sde(user, t_choose, t_field, flag, side):
    choose = pygame.image.load(t_choose).convert()
    field = pygame.image.load(t_field).convert()
    flag = flag
    if side == flag:
        user = pygame.image.load("textures/user.png").convert_alpha()
    else:
        user.fill((0, 0, 0, 0))
    return choose, flag, field, user


def load_image(name, color_key=None):
    fullname = os.path.join('', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


pygame.init()
screen = pygame.display.set_mode((500, 800))
main_screen_sprites = pygame.sprite.Group()

background = pygame.sprite.Sprite()
background.image = pygame.transform.scale(load_image('sprites/background.png'), (width, height))
background.rect = background.image.get_rect()
background.rect.x = 0
background.rect.y = 0
main_screen_sprites.add(background)

field = pygame.image.load("textures/first_side_field.jpg").convert()
back = pygame.image.load("textures/back_2.jpg").convert()
posxy = (75, 15)
choose = pygame.image.load("textures/big_choose.jpg").convert()
chxy = (179, 706)
side = "front"
user_coords = (325, 415)
u_pos = [side, user_coords]
user = pygame.image.load("textures/user.png").convert_alpha()
flag = "front"
goup = pygame.image.load("textures/go_up.png").convert_alpha()
godown = pygame.image.load("textures/go_down.png").convert_alpha()
goright = pygame.image.load("textures/go_right.png").convert_alpha()
goleft = pygame.image.load("textures/go_left.png").convert_alpha()
wall = pygame.image.load("textures/wall.jpg").convert_alpha()
first_is = True


class Bad:
    def __init__(self, s):
        self.screen = s
        self.background = load_image('textures/level_pcik_back.png')
        self.myfont1 = pygame.font.SysFont('arial', 50)
        self.good = pygame.transform.scale(load_image('textures/good.png', (100, 100)), (100, 100))

    def render(self, arg):
        surf = self.myfont1.render(str('ТЫ ПОДОРВАЛСЯ:('), False, pygame.Color('red'))
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.good, (200, 600))
        self.screen.blit(surf, (25, 100))

    def click(self, pos):
        if 200 <= pos[0] <= 300 and 600 <= pos[1] <= 700:
            return 'start'


class Win:
    def __init__(self, s, time, level):
        self.star_frame = 0
        self.time = time
        self.screen = s
        self.background = load_image('textures/level_pcik_back.png')
        self.good = pygame.transform.scale(load_image('textures/good.png', (100, 100)), (100, 100))
        self.myfont1 = pygame.font.SysFont('arial', 70)
        self.myfont = pygame.font.SysFont('arial', 50)
        self.k = 0
        if time < 240:
            self.k = 3
        elif time < 360:
            self.k = 2
        else:
            self.k = 1
        f = open('progress.json', 'r', encoding='utf-8')
        g = json.load(f)
        f.close()
        f = open('progress.json', 'w', encoding='utf-8')
        if g[str(level)] < self.k:
            p = self.k - g[str(level)]
            g[str(level)] = self.k
            g['stars'] += p
        json.dump(g, f)
        f.close()

    def render(self, arg):
        star = pygame.transform.scale(load_image(f'star_animation/{self.star_frame}.gif', (100, 100)), (100, 100))
        surf = self.myfont1.render(str('ТЫ ПРОШЕЛ!'), False, pygame.Color('red'))
        surf1 = self.myfont.render(str(f'Время: {round(self.time)}c.'), False, pygame.Color('red'))
        surf2 = self.myfont1.render(str(f'{self.k}'), False, pygame.Color('yellow'))
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.good, (200, 600))
        self.screen.blit(surf1, (100, 300))
        self.screen.blit(surf, (25, 100))
        self.screen.blit(star, (225, 400))
        self.screen.blit(surf2, (175, 420))

    def click(self, pos):
        if 200 <= pos[0] <= 300 and 600 <= pos[1] <= 700:
            return 'start'

    def star_plus(self):
        self.star_frame += 1
        if self.star_frame == 16:
            self.star_frame = 0


class level:
    def __init__(self, screen, walls, level):
        self.mines_already = {"front": [],
                              "up": [],
                              "right": [],
                              "back": [],
                              "left": [],
                              "down": []}
        self.k = []
        f = open('mines.json', 'r', encoding='utf-8')
        d = json.load(f)
        f.close()
        self.img_close = pygame.image.load('sprites/close.png')
        self.img_close = pygame.transform.scale(load_image('sprites/close.png'), (25, 25))
        self.mines_activesprites = []
        self.mines_deactivesprites = []
        self.mines = d[level - 1]
        self.mines_active = []
        self.mines_deactive = []
        self.level = level
        self.time = time.time()
        self.scr = screen
        self.walls = walls
        self.all_sprites = pygame.sprite.Group()
        self.flag = "front"
        self.user = pygame.image.load("textures/user.png").convert_alpha()
        self.first_is = True
        self.posxy = (75, 15)
        self.choose = pygame.image.load("textures/big_choose.jpg").convert()
        self.chxy = (179, 706)
        self.side = "front"
        self.user_coords = (325, 415)
        self.u_pos = [side, user_coords]
        self.field = pygame.image.load("textures/first_side_field.jpg").convert()

    def render_onclick(self, pos):
        if 225 <= pos[0] <= 252 and 704 >= pos[1] >= 675:  # up
            self.posxy = (75, 225)
            self.chxy = (234, 677)
            upp = sde(self.user, "textures/mini_choose.jpg", "textures/frond_field.jpg", "up", self.side)
            self.choose, self.flag, self.field, self.user = upp[0], upp[1], upp[2], upp[3]
        elif 226 <= pos[0] <= 252 and 705 <= pos[1] <= 763:  # back
            self.chxy = (234, 706)
            self.posxy = (75, 15)
            upp = sde(self.user, "textures/big_choose.jpg", "textures/first_side_field.jpg", "back", self.side)
            self.choose, self.flag, self.field, self.user = upp[0], upp[1], upp[2], upp[3]
        elif 171 <= pos[0] <= 197 and 704 <= pos[1] <= 763:  # front
            self.chxy = (179, 706)
            self.posxy = (75, 15)
            upp = sde(self.user, "textures/big_choose.jpg", "textures/first_side_field.jpg", "front", self.side)
            self.choose, self.flag, self.field, self.user = upp[0], upp[1], upp[2], upp[3]
        elif 198 <= pos[0] <= 225 and 705 <= pos[1] <= 763:  # left
            self.chxy = (206, 706)
            self.posxy = (75, 15)
            upp = sde(self.user, "textures/left_right_big_choose.jpg", "textures/first_side_field.jpg", "left",
                      self.side)
            self.choose, self.flag, self.field, self.user = upp[0], upp[1], upp[2], upp[3]
        elif 254 <= pos[0] <= 280 and 706 <= pos[1] <= 763:  # right
            self.chxy = (261, 706)
            self.posxy = (75, 15)
            upp = sde(self.user, "textures/left_right_big_choose.jpg", "textures/first_side_field.jpg", "right",
                      self.side)
            self.choose, self.flag, self.field, self.user = upp[0], upp[1], upp[2], upp[3]
        elif 226 <= pos[0] <= 252 and 765 <= pos[1] <= 794:  # down
            self.chxy = (234, 765)
            self.posxy = (75, 225)
            upp = sde(self.user, "textures/mini_choose.jpg", "textures/back_field.jpg", "down", self.side)
            self.choose, self.flag, self.field, self.user = upp[0], upp[1], upp[2], upp[3]
        self.rend = [self.choose, self.chxy, self.field, self.flag, self.posxy, self.user]
        return self.choose, self.chxy, self.field, self.flag, self.posxy, self.user
        pass

    def render(self, arg):
        self.scr.blit(back, (0, 0))
        self.scr.blit(self.field, self.posxy)  # (800-n) // 2
        self.scr.blit(self.choose, self.chxy)
        self.scr.blit(self.user, self.u_pos[1])
        self.scr.blit(self.img_close, (500 - 50, 800 - 50))
        if self.flag == self.walls['win'][0]:
            sprite = pygame.sprite.Sprite()
            sprite.image = load_image("textures/finish.png")
            sprite.rect = pygame.Rect((self.walls['win'][1][0], self.walls['win'][1][1], 50, 50))
            self.scr.blit(sprite.image, (self.walls['win'][1][0], self.walls['win'][1][1]))
        if self.first_is:
            self.mines_active = []
            self.mines_deactive = []
            self.mines_deactivesprites = []
            self.mines_activesprites = []
            for el in self.walls[self.flag]:
                sprite = pygame.sprite.Sprite()
                sprite.image = load_image("textures/wall.jpg")
                sprite.rect = pygame.Rect((el[0], el[1], 50, 50))
                self.all_sprites.add(sprite)
        self.first_is = False
        self.all_sprites.draw(self.scr)
        ct = self.check_turn()
        self.up_flag, self.left_flag, self.right_flag, self.down_flag = ct[0], ct[1], ct[2], ct[3]

    def check_turn(self):
        self.up_flag = False
        self.down_flag = False
        self.right_flag = False
        self.left_flag = False

        if self.u_pos[1] == (225, 15) and self.flag == self.u_pos[0]:
            self.scr.blit(goup, (227, 3))
            self.up_flag = True
        elif self.u_pos[1] == (225, 525) and self.flag == self.u_pos[0]:
            self.scr.blit(godown, (227, 575))
            self.down_flag = True
        elif self.u_pos[1] == (375, 375) and self.flag == self.u_pos[0]:
            self.scr.blit(goright, (380, 349))
            self.right_flag = True
        elif self.u_pos[1] == (75, 115) and self.flag == self.u_pos[0]:
            self.scr.blit(goleft, (24, 90))
            self.left_flag = True
        elif self.u_pos[1] == (375, 115) and self.flag == self.u_pos[0]:
            self.scr.blit(goright, (380, 91))
            self.right_flag = True
        elif self.u_pos[1] == (75, 65) and self.flag == self.u_pos[0]:
            self.scr.blit(goleft, (24, 40))
            self.left_flag = True
        elif self.u_pos[1] == (375, 65) and self.flag == self.u_pos[0]:
            self.scr.blit(goright, (380, 41))
            self.right_flag = True
        elif self.u_pos[1] == (325, 615) and self.flag == self.u_pos[0]:
            self.scr.blit(godown, (327, 665))
            self.down_flag = True
        elif self.u_pos[1] == (75, 275) and self.flag == self.u_pos[0]:
            self.scr.blit(goleft, (24, 250))
            self.left_flag = True
        return self.up_flag, self.left_flag, self.right_flag, self.down_flag

    def click(self, pos):
        self.pos = pos
        try:
            stp = self.step(self.u_pos, self.user_coords)
            self.user_coords, self.u_pos = stp[0], stp[1]
        except UnboundLocalError:
            pass
        if self.up_flag or self.down_flag or self.right_flag or self.left_flag:
            try:
                turn = self.turnit(self.u_pos)
                self.choose, self.flag, self.field, self.u_pos, self.chxy, self.posxy, self.side, self.user_coords = \
                    turn[0], turn[1], turn[2], turn[3], \
                    turn[4], turn[5], turn[6], turn[7]
                self.first_is = True
                self.all_sprites.remove(*[el for el in self.all_sprites])
            except UnboundLocalError:
                pass
        if pos[1] in range(800 - 70, 800):
            if pos[0] in range(500 - 70, 500):
                return "GOTOCHOISE"
        if self.side == self.walls['win'][0] and self.user_coords == tuple(self.walls['win'][1]):
            return 'win'
        if list(self.user_coords) in self.mines[self.flag] and list(self.user_coords) not in self.mines_already[
            self.flag]:
            self.mines_already[self.flag].append(list(self.user_coords))
            self.mines_active.append(list(self.user_coords))
            self.mines[self.flag].remove(list(self.user_coords))
            sprite = pygame.sprite.Sprite()
            sprite.image = load_image("textures/mine.png")
            sprite.rect = pygame.Rect((self.user_coords[0], self.user_coords[1], 50, 50))
            self.mines_activesprites.append(sprite)
            self.all_sprites.add(sprite)
            self.timer = time.time()

    def step(self, u_pos, user_coords):
        f_u_pos = u_pos
        f_user_coords = user_coords
        if self.flag == u_pos[0]:
            # проверка на границы поля
            if self.posxy[0] < self.pos[0] < self.posxy[0] + 340 and (
                    self.posxy[1] < self.pos[1] < self.posxy[1] + 350 or (
                    self.posxy[1] < self.pos[1] < self.posxy[1] + 650 and self.side != "up" and self.side != "down")):
                if u_pos[1][0] - 58 <= self.pos[0] <= u_pos[1][0] + 90 and u_pos[1][1] - 50 <= self.pos[1] <= u_pos[1][
                    1] + 100:
                    user_coords = list(user_coords)
                    if u_pos[1][0] - 10 < self.pos[0] and u_pos[1][0] + 39 < self.pos[0] or u_pos[1][0] - 10 > self.pos[
                        0] and \
                            u_pos[1][0] + 39 > self.pos[0] and u_pos[1][1] <= self.pos[1] <= u_pos[1][1] + 48:  # <-
                        if u_pos[1][0] - 58 <= self.pos[0] <= u_pos[1][0] and u_pos[1][1] <= self.pos[1] <= u_pos[1][
                            1] + 48:
                            user_coords[0] -= 50
                        elif u_pos[1][0] <= self.pos[0] <= u_pos[1][0] + 90 and u_pos[1][1] <= self.pos[1] <= u_pos[1][
                            1] + 48:  # ->
                            user_coords[0] += 50
                    elif u_pos[1][1] < self.pos[1] and u_pos[1][1] + 50 < self.pos[1] or u_pos[1][1] > self.pos[1] and \
                            u_pos[1][
                                1] + 50 > self.pos[1] and u_pos[1][0] - 10 <= self.pos[0] <= u_pos[1][0] + 50:
                        if u_pos[1][1] - 50 <= self.pos[1] <= u_pos[1][1] and u_pos[1][0] - 8 <= self.pos[0] <= \
                                u_pos[1][0] + 50:
                            user_coords[1] -= 50
                        elif u_pos[1][1] <= self.pos[1] <= u_pos[1][1] + 100 and u_pos[1][0] - 8 <= self.pos[0] <= \
                                u_pos[1][
                                    0] + 50:
                            user_coords[1] += 50
                    self.user_coords = tuple(user_coords)
                    self.u_pos = (self.side, self.user_coords)
                    usr = pygame.sprite.Sprite()
                    usr.rect = pygame.Rect((self.u_pos[1][0] + 2, self.u_pos[1][1] + 2, 48, 48))
                    if pygame.sprite.spritecollideany(usr, self.all_sprites) is None:
                        return self.user_coords, self.u_pos
        return f_user_coords, f_u_pos

    def mineses(self):
        k = 0
        if time.time() - self.timer > 1.5:
            if list(self.user_coords) in self.mines_active or list(self.user_coords) in self.mines_deactive:
                k = 1
            for en in self.mines_activesprites:
                self.all_sprites.remove(en)
            self.mines_active = []
            self.mines_deactive = []
            self.mines_deactivesprites = []
            self.mines_activesprites = []
        if self.mines_active:
            for en in self.mines_activesprites:
                g = [en.rect.x, en.rect.y]
                if g in self.mines_active:
                    self.all_sprites.add(en)
        if self.mines_deactive:
            for en in self.mines_activesprites:
                g = [en.rect.x, en.rect.y]
                if g in self.mines_deactive:
                    self.all_sprites.remove(en)
        self.mines_deactive, self.mines_active = self.mines_active, self.mines_deactive
        if k == 1:
            return 'died'

    def turnit(self, u_pos):
        if self.up_flag and 227 <= self.pos[0] <= 275 and 3 <= self.pos[1] <= 15:
            if u_pos[0] == "front":
                self.side = "up"
                self.user_coords = (225, 525)
                upp = sde(self.user, "textures/mini_choose.jpg", "textures/frond_field.jpg", "up", self.side)
            elif u_pos[0] == "right":
                self.side = "up"
                self.user_coords = (375, 375)
                upp = sde(self.user, "textures/mini_choose.jpg", "textures/frond_field.jpg", "up", self.side)
            self.u_pos = [self.side, self.user_coords]
            self.posxy = (75, 225)
            self.chxy = (234, 677)
            self.choose, self.flag, self.field, self.user = upp[0], upp[1], upp[2], upp[3]
        elif self.down_flag and (227 <= self.pos[0] <= 275 and 575 <= self.pos[1] <= 587) or (
                319 <= self.pos[0] <= 365 and 664 <= self.pos[1] <= 675):
            if u_pos[0] == "up":
                self.side = "front"
                self.user_coords = (225, 15)
                self.chxy = (179, 706)
                self.posxy = (75, 15)
                upp = sde(self.user, "textures/big_choose.jpg", "textures/first_side_field.jpg", "front", self.side)
            elif u_pos[0] == "left":
                self.side = "down"
                self.user_coords = (75, 275)
                self.chxy = (234, 765)
                self.posxy = (75, 225)
                upp = sde(self.user, "textures/mini_choose.jpg", "textures/back_field.jpg", "down", self.side)
            self.u_pos = [self.side, self.user_coords]
            self.choose, self.flag, self.field, self.user = upp[0], upp[1], upp[2], upp[3]
        elif self.right_flag and 418 <= self.pos[0] <= 427 and (
                376 <= self.pos[1] <= 421 or 117 <= self.pos[1] <= 163 or 67 <= self.pos[1] <= 113):
            if u_pos[0] == "up":
                self.side = "right"
                self.user_coords = (225, 15)
                self.chxy = (261, 706)
                upp = sde(self.user, "textures/left_right_big_choose.jpg", "textures/first_side_field.jpg", "right",
                          self.side)
            elif u_pos[0] == "back":
                self.side = "right"
                self.user_coords = (75, 115)
                self.chxy = (261, 706)
                upp = sde(self.user, "textures/left_right_big_choose.jpg", "textures/first_side_field.jpg", "right",
                          self.side)
            elif u_pos[0] == "left":
                self.side = "back"
                self.user_coords = (75, 65)
                self.chxy = (234, 706)
                upp = sde(self.user, "textures/big_choose.jpg", "textures/first_side_field.jpg", "back", self.side)
            self.u_pos = [self.side, self.user_coords]
            self.posxy = (75, 15)
            self.choose, self.flag, self.field, self.user = upp[0], upp[1], upp[2], upp[3]
        elif self.left_flag and (
                56 <= self.pos[0] <= 66 and (
                115 <= self.pos[1] <= 161 or 65 <= self.pos[1] <= 111 or 275 <= self.pos[1] <= 321)):
            if u_pos[0] == "right":
                self.side = "back"
                self.user_coords = (375, 115)
                self.chxy = (234, 706)
                upp = sde(self.user, "textures/big_choose.jpg", "textures/first_side_field.jpg", "back", self.side)
            elif u_pos[0] == "back":
                self.side = "left"
                self.user_coords = (375, 65)
                self.chxy = (206, 706)
                upp = sde(self.user, "textures/left_right_big_choose.jpg", "textures/first_side_field.jpg", "left",
                          self.side)
            elif u_pos[0] == "down":
                self.side = "left"
                self.user_coords = (325, 615)
                self.chxy = (206, 706)
                upp = sde(self.user, "textures/left_right_big_choose.jpg", "textures/first_side_field.jpg", "left",
                          self.side)
            self.posxy = (75, 15)
            self.u_pos = [self.side, self.user_coords]
            self.choose, self.flag, self.field, self.user = upp[0], upp[1], upp[2], upp[3]
        return self.choose, self.flag, self.field, self.u_pos, self.chxy, self.posxy, self.side, self.user_coords


class Level_Pick:
    def __init__(self, s):
        f = open('progress.json', 'r', encoding='utf-8')
        self.screen = s
        self.g = json.load(f)
        f.close()
        self.img_close = pygame.image.load('sprites/close.png')
        self.img_close = pygame.transform.scale(load_image('sprites/close.png'), (25, 25))
        self.background = load_image('textures/level_pcik_back.png')
        self.left = pygame.transform.scale(load_image('textures/left.png', (100, 100)), (100, 100))
        self.right = pygame.transform.scale(load_image('textures/right.png', (100, 100)), (100, 100))
        self.myfont1 = pygame.font.SysFont('arial', 100)
        self.myfont = pygame.font.SysFont('arial', 50)
        self.start = load_image('textures/start.png')
        self.level = 1

    def render(self, arg):
        surf = self.myfont1.render(str(int(self.level)), False, pygame.Color('red'))
        surf1 = self.myfont.render(str('Выберите уровень'), False, pygame.Color('red'))
        surf2 = self.myfont.render(f'{self.g[str(self.level)]}/3', False, pygame.Color('yellow'))
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.left, (0, 300))
        self.screen.blit(self.right, (400, 300))
        self.screen.blit(surf, (225, 300))
        self.screen.blit(surf1, (25, 100))
        self.screen.blit(surf2, (220, 260))
        self.screen.blit(self.start, (125, 600))
        self.screen.blit(self.img_close, (500 - 50, 800 - 50))

    def click(self, pos):
        if 0 <= pos[0] <= 100 and 300 <= pos[1] <= 400:
            self.level -= 1
            if self.level < 1:
                self.level = 1
        elif 400 <= pos[0] <= 500 and 300 <= pos[1] <= 400:
            self.level += 1
            if self.level > 2:
                self.level = 2
        elif 125 <= pos[0] <= 385 and 600 <= pos[1] <= 745:
            return 'level'
        elif pos[1] in range(800 - 70, 800):
            if pos[0] in range(500 - 70, 500):
                return "GOTOMAIN"


class Rules:
    def __init__(self, s):
        self.screen = s

        self.font = pygame.font.SysFont('arial', 15)
        self.text = self.font.render(str('Правила и механики'), False, pygame.Color('black'))
        self.rule_1 = self.font.render(str('1.Перемещение по лабиринту происходит с помощью клика мышью'), False,
                                       pygame.Color('black'))
        self.rule_2 = self.font.render(str('2.Перемещаться можно только по клеткам, на которых нет стен'), False,
                                       pygame.Color('black'))
        self.rule_3 = self.font.render(str('3.Просматривать все грани параллелепипеда без перемещения'), False,
                                       pygame.Color('black'))
        self.rule_3_1 = self.font.render(str('возможно с помощью развёртки расположеннной внизу экрана'), False,
                                         pygame.Color('black'))
        self.rule_4 = self.font.render(str('4.На карте присутсвуют мины, активирующиеся при наступании на них'), False,
                                       pygame.Color('black'))
        self.rule_5 = self.font.render(str('5.За прожодение уровней за достаточно хорошее время вы получаете ''звёзды'),
                                       False, pygame.Color('black'))
        self.rule_5_1 = self.font.render(str('на которые можно покупать в магазине различные предметы'), False,
                                         pygame.Color('black'))

        self.rules_sprites = pygame.sprite.Group()

        self.rules_sprites.add(background)

        self.ok_btn = pygame.sprite.Sprite()
        self.ok_btn.image = pygame.transform.scale(load_image('sprites/img_ok_btn.png'), (50, 50))
        self.ok_btn.rect = self.ok_btn.image.get_rect()
        self.ok_btn.rect.x = 225
        self.ok_btn.rect.y = height - 50
        self.rules_sprites.add(self.ok_btn)

        self.ok = pygame.sprite.Sprite()
        self.ok.image = pygame.transform.scale(load_image('sprites/img_ok.png'), (28, 28))
        self.ok.rect = self.ok_btn.image.get_rect()
        self.ok.rect.x = 235
        self.ok.rect.y = height - 37
        self.rules_sprites.add(self.ok)

    def render(self, _):
        self.rules_sprites.draw(self.screen)
        self.screen.blit(self.text, (0, 0))
        self.screen.blit(self.rule_1, (0, 50))
        self.screen.blit(self.rule_2, (0, 75))
        self.screen.blit(self.rule_3, (0, 100))
        self.screen.blit(self.rule_3_1, (0, 115))
        self.screen.blit(self.rule_4, (0, 140))
        self.screen.blit(self.rule_5, (0, 165))
        self.screen.blit(self.rule_5_1, (0, 180))

    def click(self, pos):
        if pos[1] in range(height - 50, height) and pos[0] in range(225, 275):
            return 'ok'


class Exit:
    def __init__(self, s):
        self.screen = s

        self.font = pygame.font.SysFont('arial', 30)
        self.text = self.font.render(str('Вы уверены что хотите выйти?'), False, pygame.Color('black'))

        self.exit_sprites = pygame.sprite.Group()

        self.exit_sprites.add(background)

        self.accept_btn = pygame.sprite.Sprite()
        self.accept_btn.image = pygame.transform.scale(load_image('sprites/img_accept_btn.png'), (100, 100))
        self.accept_btn.rect = self.accept_btn.image.get_rect()
        self.accept_btn.rect.x = width // 3 - 50
        self.accept_btn.rect.y = height // 2 - 50
        self.exit_sprites.add(self.accept_btn)

        self.accept = pygame.sprite.Sprite()
        self.accept.image = pygame.transform.scale(load_image('sprites/img_ok.png'), (50, 50))
        self.accept.rect = self.accept.image.get_rect()
        self.accept.rect.x = width // 3 - 25
        self.accept.rect.y = height // 2 - 25
        self.exit_sprites.add(self.accept)

        self.decline_btn = pygame.sprite.Sprite()
        self.decline_btn.image = pygame.transform.scale(load_image('sprites/img_decline_btn.png'), (100, 100))
        self.decline_btn.rect = self.decline_btn.image.get_rect()
        self.decline_btn.rect.x = width // 3 * 2 - 50
        self.decline_btn.rect.y = height // 2 - 50
        self.exit_sprites.add(self.decline_btn)

        self.decline = pygame.sprite.Sprite()
        self.decline.image = pygame.transform.scale(load_image('sprites/close.png'), (50, 50))
        self.decline.rect = self.decline.image.get_rect()
        self.decline.rect.x = width // 3 * 2 - 25
        self.decline.rect.y = height // 2 - 25
        self.exit_sprites.add(self.decline)

    def render(self, _):
        self.exit_sprites.draw(self.screen)
        self.screen.blit(self.text, (70, 300))

    def click(self, pos):
        if pos[1] in range(height // 2 - 50, height // 2 + 50):
            if pos[0] in range(width // 3 - 50, width // 3 + 50):
                return 'accept'
            elif pos[0] in range(width // 3 * 2 - 50, width // 3 * 2 + 50):
                return 'decline'


ren = ''


class MainScreen:
    def __init__(self, s):
        self.screen = s

        self.img_rules_btn = pygame.sprite.Sprite()
        self.img_rules_btn.image = pygame.transform.scale(load_image('sprites/img_rules_btn.png'), (50, 50))
        self.img_rules_btn.rect = self.img_rules_btn.image.get_rect()
        self.img_rules_btn.rect.x = 0
        self.img_rules_btn.rect.y = height - 50
        main_screen_sprites.add(self.img_rules_btn)

        self.img_rules = pygame.sprite.Sprite()
        self.img_rules.image = pygame.transform.scale(load_image('sprites/img_rules.png'), (30, 30))
        self.img_rules.rect = self.img_rules.image.get_rect()
        self.img_rules.rect.x = 10
        self.img_rules.rect.y = height - 40
        main_screen_sprites.add(self.img_rules)

        self.img_start_btn = pygame.sprite.Sprite()
        self.img_start_btn.image = pygame.transform.scale(load_image('sprites/img_start_btn.png'), (100, 100))
        self.img_start_btn.rect = self.img_start_btn.image.get_rect()
        self.img_start_btn.rect.x = 0
        self.img_start_btn.rect.y = height // 2 - 50
        main_screen_sprites.add(self.img_start_btn)

        self.img_start = pygame.sprite.Sprite()
        self.img_start.image = pygame.transform.scale(load_image('sprites/play.png'), (50, 45))
        self.img_start.rect = self.img_start.image.get_rect()
        self.img_start.rect.x = 30
        self.img_start.rect.y = height // 2 - 22.5
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
        main_screen_sprites.draw(self.screen)
        if arg != '':
            arg.draw(self.screen)

    def click(self, position):
        if position[1] in range(height // 2 - 50, height // 2 + 50):
            if position[0] in range(0, 100):
                return 'start'
            elif position[0] in range((width - 50) // 2 - 25, (width - 50) // 2 + 75):
                return 'shop'
            elif position[0] in range(width - 100, width):
                return 'settings'
        elif position[1] in range(height - 50, height):
            if position[0] in range(width - 50, width):
                return 'exit'
            elif position[0] in range(0, 50):
                return 'rules'


class Shop:
    def __init__(self, s):
        self.screen = s
        self.shop_sprites = pygame.sprite.Group()
        self.player_sprites = pygame.sprite.Group()
        self.wall_sprites = pygame.sprite.Group()
        self.color_sprites = pygame.sprite.Group()

        self.font = pygame.font.SysFont('arial', 30)
        self.player_1_cost_text = self.font.render(str('1$'), False, pygame.Color('black'))
        self.player_2_cost_text = self.font.render(str('2$'), False, pygame.Color('black'))
        self.player_3_cost_text = self.font.render(str('3$'), False, pygame.Color('black'))

        # спрайты магазина
        self.type = 'player'

        self.shop_sprites.add(background)

        self.img_player_btn = pygame.sprite.Sprite()
        self.img_player_btn.image = pygame.transform.scale(load_image('sprites/img_player_btn.png'), (100, 100))
        self.img_player_btn.rect = self.img_player_btn.image.get_rect()
        self.img_player_btn.rect.x = 0
        self.img_player_btn.rect.y = 0
        self.shop_sprites.add(self.img_player_btn)

        self.img_player = pygame.sprite.Sprite()
        self.img_player.image = pygame.transform.scale(load_image('sprites/img_player.png'), (50, 50))
        self.img_player.rect = self.img_player.image.get_rect()
        self.img_player.rect.x = 25
        self.img_player.rect.y = 20
        self.shop_sprites.add(self.img_player)

        self.img_wall_btn = pygame.sprite.Sprite()
        self.img_wall_btn.image = pygame.transform.scale(load_image('sprites/img_wall_btn.png'), (100, 100))
        self.img_wall_btn.rect = self.img_wall_btn.image.get_rect()
        self.img_wall_btn.rect.x = (width - 100) // 2
        self.img_wall_btn.rect.y = 0
        self.shop_sprites.add(self.img_wall_btn)

        self.img_wall = pygame.sprite.Sprite()
        self.img_wall.image = pygame.transform.scale(load_image('sprites/img_wall.png'), (70, 70))
        self.img_wall.rect = self.img_wall.image.get_rect()
        self.img_wall.rect.x = (width - 50) // 2 - 10
        self.img_wall.rect.y = 15
        self.shop_sprites.add(self.img_wall)

        self.img_color_btn = pygame.sprite.Sprite()
        self.img_color_btn.image = pygame.transform.scale(load_image('sprites/img_color_btn.png'), (100, 100))
        self.img_color_btn.rect = self.img_wall_btn.image.get_rect()
        self.img_color_btn.rect.x = width - 100
        self.img_color_btn.rect.y = 0
        self.shop_sprites.add(self.img_color_btn)

        self.img_color = pygame.sprite.Sprite()
        self.img_color.image = pygame.transform.scale(load_image('sprites/капля.png'), (55, 55))
        self.img_color.rect = self.img_color.image.get_rect()
        self.img_color.rect.x = width - 77.5
        self.img_color.rect.y = 20
        self.shop_sprites.add(self.img_color)

        self.img_shop_close_btn = pygame.sprite.Sprite()
        self.img_shop_close_btn.image = pygame.transform.scale(load_image('sprites/img_shop_close_btn.png'), (50, 50))
        self.img_shop_close_btn.rect = self.img_shop_close_btn.image.get_rect()
        self.img_shop_close_btn.rect.x = width - 50
        self.img_shop_close_btn.rect.y = height - 50
        self.shop_sprites.add(self.img_shop_close_btn)

        self.img_close = pygame.sprite.Sprite()
        self.img_close.image = pygame.transform.scale(load_image('sprites/close.png'), (25, 25))
        self.img_close.rect = self.img_close.image.get_rect()
        self.img_close.rect.x = width - 37
        self.img_close.rect.y = height - 37
        self.shop_sprites.add(self.img_close)

        # спрайты персонажей
        self.player_1_cost = 1

        self.player_1 = pygame.sprite.Sprite()
        self.player_1.image = pygame.transform.scale(load_image('sprites/player_1.png'), (50, 50))
        self.player_1.rect = self.player_1.image.get_rect()
        self.player_1.rect.x = 25
        self.player_1.rect.y = 150
        self.player_sprites.add(self.player_1)

        self.buy_player_1_btn = pygame.sprite.Sprite()
        self.buy_player_1_btn.image = pygame.transform.scale(load_image('sprites/img_buy_btn.png'), (25, 25))
        self.buy_player_1_btn.rect = self.buy_player_1_btn.image.get_rect()
        self.buy_player_1_btn.rect.x = 25
        self.buy_player_1_btn.rect.y = 210
        self.player_sprites.add(self.buy_player_1_btn)

        self.buy_player_1 = pygame.sprite.Sprite()
        self.buy_player_1.image = pygame.transform.scale(load_image('sprites/img_buy.png'), (25, 25))
        self.buy_player_1.rect = self.buy_player_1.image.get_rect()
        self.buy_player_1.rect.x = 27
        self.buy_player_1.rect.y = 210
        self.player_sprites.add(self.buy_player_1)

        self.choose_player_1_btn = pygame.sprite.Sprite()
        self.choose_player_1_btn.image = pygame.transform.scale(load_image('sprites/img_choose_btn.png'), (25, 25))
        self.choose_player_1_btn.rect = self.choose_player_1_btn.image.get_rect()
        self.choose_player_1_btn.rect.x = 50
        self.choose_player_1_btn.rect.y = 210
        self.player_sprites.add(self.choose_player_1_btn)

        self.choose_player_1 = pygame.sprite.Sprite()
        self.choose_player_1.image = pygame.transform.scale(load_image('sprites/img_choose.png'), (15, 15))
        self.choose_player_1.rect = self.choose_player_1.image.get_rect()
        self.choose_player_1.rect.x = 55
        self.choose_player_1.rect.y = 215
        self.player_sprites.add(self.choose_player_1)

        self.player_2_cost = 2

        self.player_2 = pygame.sprite.Sprite()
        self.player_2.image = pygame.transform.scale(load_image('sprites/player_2.png'), (50, 50))
        self.player_2.rect = self.player_2.image.get_rect()
        self.player_2.rect.x = 125
        self.player_2.rect.y = 150
        self.player_sprites.add(self.player_2)

        self.buy_player_2_btn = pygame.sprite.Sprite()
        self.buy_player_2_btn.image = pygame.transform.scale(load_image('sprites/img_buy_btn.png'), (25, 25))
        self.buy_player_2_btn.rect = self.buy_player_2_btn.image.get_rect()
        self.buy_player_2_btn.rect.x = 125
        self.buy_player_2_btn.rect.y = 210
        self.player_sprites.add(self.buy_player_2_btn)

        self.buy_player_2 = pygame.sprite.Sprite()
        self.buy_player_2.image = pygame.transform.scale(load_image('sprites/img_buy.png'), (25, 25))
        self.buy_player_2.rect = self.buy_player_2.image.get_rect()
        self.buy_player_2.rect.x = 127
        self.buy_player_2.rect.y = 210
        self.player_sprites.add(self.buy_player_2)

        self.choose_player_2_btn = pygame.sprite.Sprite()
        self.choose_player_2_btn.image = pygame.transform.scale(load_image('sprites/img_choose_btn.png'), (25, 25))
        self.choose_player_2_btn.rect = self.choose_player_2_btn.image.get_rect()
        self.choose_player_2_btn.rect.x = 150
        self.choose_player_2_btn.rect.y = 210
        self.player_sprites.add(self.choose_player_2_btn)

        self.choose_player_2 = pygame.sprite.Sprite()
        self.choose_player_2.image = pygame.transform.scale(load_image('sprites/img_choose.png'), (15, 15))
        self.choose_player_2.rect = self.choose_player_2.image.get_rect()
        self.choose_player_2.rect.x = 155
        self.choose_player_2.rect.y = 215
        self.player_sprites.add(self.choose_player_2)

        self.player_3_cost = 3

        self.player_3 = pygame.sprite.Sprite()
        self.player_3.image = pygame.transform.scale(load_image('sprites/player_3.png'), (50, 50))
        self.player_3.rect = self.player_3.image.get_rect()
        self.player_3.rect.x = 225
        self.player_3.rect.y = 150
        self.player_sprites.add(self.player_3)

        self.buy_player_3_btn = pygame.sprite.Sprite()
        self.buy_player_3_btn.image = pygame.transform.scale(load_image('sprites/img_buy_btn.png'), (25, 25))
        self.buy_player_3_btn.rect = self.buy_player_3_btn.image.get_rect()
        self.buy_player_3_btn.rect.x = 225
        self.buy_player_3_btn.rect.y = 210
        self.player_sprites.add(self.buy_player_3_btn)

        self.buy_player_3 = pygame.sprite.Sprite()
        self.buy_player_3.image = pygame.transform.scale(load_image('sprites/img_buy.png'), (25, 25))
        self.buy_player_3.rect = self.buy_player_3.image.get_rect()
        self.buy_player_3.rect.x = 227
        self.buy_player_3.rect.y = 210
        self.player_sprites.add(self.buy_player_3)

        self.choose_player_3_btn = pygame.sprite.Sprite()
        self.choose_player_3_btn.image = pygame.transform.scale(load_image('sprites/img_choose_btn.png'), (25, 25))
        self.choose_player_3_btn.rect = self.choose_player_3_btn.image.get_rect()
        self.choose_player_3_btn.rect.x = 250
        self.choose_player_3_btn.rect.y = 210
        self.player_sprites.add(self.choose_player_3_btn)

        self.choose_player_3 = pygame.sprite.Sprite()
        self.choose_player_3.image = pygame.transform.scale(load_image('sprites/img_choose.png'), (15, 15))
        self.choose_player_3.rect = self.choose_player_3.image.get_rect()
        self.choose_player_3.rect.x = 255
        self.choose_player_3.rect.y = 215
        self.player_sprites.add(self.choose_player_3)

        # спрайты стен
        self.wall_1 = pygame.sprite.Sprite()
        self.wall_1.image = pygame.transform.scale(load_image('sprites/wall_1.png'), (50, 50))
        self.wall_1.rect = self.wall_1.image.get_rect()
        self.wall_1.rect.x = 25
        self.wall_1.rect.y = 150
        self.wall_sprites.add(self.wall_1)

        self.wall_2 = pygame.sprite.Sprite()
        self.wall_2.image = pygame.transform.scale(load_image('sprites/wall_2.png'), (50, 50))
        self.wall_2.rect = self.wall_2.image.get_rect()
        self.wall_2.rect.x = 125
        self.wall_2.rect.y = 150
        self.wall_sprites.add(self.wall_2)

        self.wall_3 = pygame.sprite.Sprite()
        self.wall_3.image = pygame.transform.scale(load_image('sprites/wall_3.png'), (50, 50))
        self.wall_3.rect = self.wall_3.image.get_rect()
        self.wall_3.rect.x = 225
        self.wall_3.rect.y = 150
        self.wall_sprites.add(self.wall_3)

    def render(self, arg):
        self.shop_sprites.draw(self.screen)
        if arg != '':
            arg.draw(self.screen)
            if arg == self.player_sprites:
                self.screen.blit(self.player_1_cost_text, (40, 230))
                self.screen.blit(self.player_2_cost_text, (140, 230))
                self.screen.blit(self.player_3_cost_text, (240, 230))
        my_money = open('progress.json', 'r', encoding='utf-8')
        money = json.load(my_money)
        my_money.close()
        self.money = self.font.render('Количество звёзд:' + str(money['stars']), False, pygame.Color('black'))
        self.screen.blit(self.money, (0, height - 30))

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
                elif position[0] in range(50, 75):
                    return 'choose_player_1'
                elif position[0] in range(150, 175):
                    return 'choose_player_2'
                elif position[0] in range(250, 275):
                    return 'choose_player_3'
