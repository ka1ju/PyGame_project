import os
import sys
import keyboard
import pygame
pygame.init()

scr = pygame.display.set_mode((500, 800))
running = True

CURSOR = pygame.image.load("textures/mouse_last_vers.png").convert_alpha()
pygame.mouse.set_cursor((8, 8), (4, 4), (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0))
pygame.mouse.set_visible(False)
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
############################################################################################################## для 1 лвл
walls = {"front": ((175, 65), (175, 115), (75, 115), (75, 65), (225, 615), (375, 65), (375, 415), (375, 15), (375, 465),
                   (225, 65), (375, 515), (325, 215), (175, 515), (375, 565), (375, 615), (375, 365), (175, 465),
                   (375, 315), (275, 615), (325, 365), (275, 365), (325, 615), (175, 165), (275, 465), (275, 65),
                   (275, 415), (375, 115), (225, 515), (275, 515), (275, 165), (275, 215), (275, 265), (75, 165),
                   (75, 315), (75, 365), (125, 365), (175, 365), (125, 465), (125, 515), (125, 565), (225, 265),
                   (175, 265), (325, 15), (275, 15)),
         "up": ((175, 525), (275, 525), (75, 275), (175, 325), (225, 425), (325, 425), (375, 425), (75, 375), (75, 325),
                (175, 425), (375, 525), (225, 325), (75, 225), (225, 225), (275, 325), (75, 475), (125, 225),
                (325, 325), (175, 225), (175, 475), (325, 475), (375, 475), (75, 525), (325, 375), (125, 525),
                (325, 275), (325, 525)),
         "right": ((225, 615), (125, 115), (125, 65), (325, 515), (225, 215), (325, 565), (275, 565), (225, 265),
                   (75, 515), (375, 315), (375, 565), (75, 615), (375, 165), (275, 615), (375, 415), (75, 465),
                   (125, 615), (375, 265), (375, 515), (75, 565), (175, 615), (375, 365), (375, 615), (75, 415),
                   (375, 215), (375, 465), (375, 65), (225, 465), (275, 115), (125, 265), (325, 15), (275, 365),
                   (375, 15), (325, 615), (275, 215), (125, 15), (325, 215), (175, 15), (75, 15), (325, 465),
                   (275, 265), (75, 65), (175, 515), (225, 415), (125, 215), (175, 365), (375, 115), (125, 315),
                   (225, 115), (225, 365), (275, 15), (125, 165)),
         "back": ((225, 615), (75, 115), (175, 215), (175, 115), (175, 165), (175, 65), (275, 515), (125, 565),
                  (175, 565), (175, 15), (275, 115), (275, 15), (225, 265), (325, 15), (275, 265), (175, 265),
                  (375, 65), (125, 415), (125, 15), (375, 315), (375, 565), (225, 465), (75, 615), (275, 365),
                  (125, 265), (375, 165), (275, 615), (375, 15), (275, 465), (125, 365), (125, 615), (325, 365),
                  (325, 615), (375, 265), (75, 565), (125, 215), (125, 465), (225, 15), (325, 465), (175, 615),
                  (375, 365), (375, 615), (275, 165), (125, 315), (175, 465), (375, 215), (225, 365), (325, 165)),
         "left": ((75, 115), (75, 515), (75, 365), (375, 565), (75, 615), (125, 265), (175, 165), (275, 215),
                  (75, 465),
                  (325, 365), (75, 315), (75, 565), (125, 465), (75, 415), (375, 615), (125, 15), (175, 565),
                  (375, 315), (225, 465), (275, 115), (275, 365), (325, 15), (375, 165), (75, 215), (375, 415),
                  (175, 15), (325, 115), (225, 565), (375, 15), (275, 465), (175, 265), (75, 65), (375, 265),
                  (375, 515), (175, 115), (175, 365), (225, 15), (375, 115), (275, 565), (75, 165), (225, 265),
                  (375, 365), (175, 465), (75, 15), (375, 215), (225, 115), (325, 565), (75, 265), (275, 15),
                  (375, 465), (225, 365), (275, 265)),
         "down": ((75, 225), (175, 325), (225, 425), (275, 425), (275, 325), (125, 475), (175, 275), (275, 375),
                  (125, 425), (175, 425), (375, 425), (75, 475), (275, 225), (175, 525), (375, 275), (375, 525),
                  (75, 325), (125, 225), (325, 225), (375, 375), (225, 525), (75, 425), (175, 225), (375, 225),
                  (375, 475), (75, 525), (275, 525), (225, 225), (375, 325), (75, 375), (125, 525), (325, 525))}
########################################################################################################################

############################################################################################################## для 2 лвл
walls = {"front": ((275, 65), (225, 315), (325, 65), (275, 315), (175, 315), (125, 215), (325, 315), (175, 215), (275, 215), (225, 215), (175, 115), (225, 115), (175, 365), (325, 115), (275, 115), (225, 365), (275, 365), (275, 515), (125, 565), (175, 565), (275, 465), (325, 365), (125, 515), (175, 515), (175, 415), (225, 415), (275, 415), (225, 615), (75, 515), (375, 65), (75, 115), (125, 15), (375, 315), (375, 565), (75, 365), (75, 615), (325, 15), (375, 165), (275, 615), (75, 215), (375, 415), (175, 15), (75, 465), (375, 15), (125, 615), (325, 615), (75, 65), (375, 265), (375, 515), (75, 315), (75, 565), (375, 115), (75, 165), (175, 615), (375, 365), (375, 615), (75, 415), (75, 15), (375, 215), (375, 465), (75, 265), (275, 15)),
         "up": ((175, 325), (225, 425), (275, 425), (275, 325), (325, 425), (325, 325), (175, 375), (325, 475), (275, 475), (275, 275), (325, 275), (175, 425), (75, 225), (375, 425), (75, 475), (275, 225), (175, 525), (375, 275), (75, 325), (375, 525), (125, 225), (325, 225), (75, 425), (175, 225), (375, 225), (75, 275), (375, 475), (75, 525), (275, 525), (225, 225), (375, 325), (75, 375), (125, 525), (325, 525)),
         "right": ((275, 515), (175, 315), (325, 415), (275, 115), (175, 165), (175, 415), (225, 315), (275, 215), (175, 265), (175, 515), (275, 315), (175, 115), (325, 215), (175, 365), (225, 515), (275, 415), (175, 215), (175, 465), (225, 115), (175, 65), (225, 615), (75, 515), (375, 65), (125, 15), (375, 315), (375, 565), (75, 365), (75, 615), (325, 15), (375, 165), (275, 615), (75, 215), (375, 415), (175, 15), (75, 465), (375, 15), (125, 615), (325, 615), (375, 265), (75, 65), (375, 515), (75, 315), (75, 565), (375, 115), (75, 165), (175, 615), (375, 365), (375, 615), (75, 415), (375, 215), (75, 15), (375, 465), (275, 15), (75, 265)),
         "back": ((175, 315), (225, 465), (275, 365), (175, 165), (175, 415), (225, 65), (275, 465), (325, 365), (175, 265), (175, 515), (275, 65), (175, 65), (175, 115), (175, 365), (275, 565), (225, 265), (275, 165), (325, 65), (175, 215), (175, 465), (325, 565), (275, 265), (325, 165), (75, 515), (225, 615), (375, 65), (75, 115), (125, 15), (375, 315), (75, 365), (375, 565), (75, 615), (325, 15), (375, 165), (275, 615), (75, 215), (375, 415), (175, 15), (75, 465), (375, 15), (125, 615), (325, 615), (375, 265), (75, 315), (375, 515), (75, 565), (225, 15), (75, 165), (175, 615), (375, 365), (75, 415), (375, 615), (75, 15), (375, 215), (75, 265), (275, 15), (375, 465)),
         "left": ((125, 415), (275, 515), (175, 315), (225, 215), (275, 115), (175, 415), (225, 315), (325, 515), (275, 215), (325, 115), (175, 515), (225, 415), (125, 215), (275, 315), (175, 115), (225, 515), (275, 415), (175, 215), (325, 315), (225, 115), (75, 515), (225, 615), (75, 115), (125, 15), (375, 315), (75, 365), (375, 565), (75, 615), (325, 15), (375, 165), (275, 615), (75, 215), (375, 415), (175, 15), (75, 465), (375, 15), (125, 615), (75, 65), (375, 265), (75, 315), (375, 515), (75, 565), (225, 15), (375, 115), (75, 165), (175, 615), (375, 365), (75, 415), (375, 615), (75, 15), (375, 215), (75, 265), (275, 15), (375, 465)),
         "down": ((175, 325), (225, 425), (225, 325), (125, 325), (275, 425), (275, 325), (325, 425), (175, 425), (75, 225), (375, 425), (75, 475), (275, 225), (175, 525), (375, 275), (375, 525), (75, 325), (125, 225), (325, 225), (375, 375), (225, 525), (75, 425), (175, 225), (375, 225), (375, 475), (75, 525), (275, 525), (225, 225), (375, 325), (75, 375), (125, 525), (325, 525))}
########################################################################################################################


def sde(user, t_choose, t_field, flag, side):
    choose = pygame.image.load(t_choose).convert()
    field = pygame.image.load(t_field).convert()
    flag = flag
    if side == flag:
        user = pygame.image.load("textures/user.png").convert_alpha()
    else:
        user.fill((0, 0, 0, 0))
    return choose, flag, field, user


def load_image(name, colorkey=None):
    fullname = os.path.join('textures', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class level():
    def __init__(self):
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
            upp = sde(self.user, "textures/left_right_big_choose.jpg", "textures/first_side_field.jpg", "left", self.side)
            self.choose, self.flag, self.field, self.user = upp[0], upp[1], upp[2], upp[3]
        elif 254 <= pos[0] <= 280 and 706 <= pos[1] <= 763:  # right
            self.chxy = (261, 706)
            self.posxy = (75, 15)
            upp = sde(self.user, "textures/left_right_big_choose.jpg", "textures/first_side_field.jpg", "right", self.side)
            self.choose, self.flag, self.field, self.user = upp[0], upp[1], upp[2], upp[3]
        elif 226 <= pos[0] <= 252 and 765 <= pos[1] <= 794:  # down
            self.chxy = (234, 765)
            self.posxy = (75, 225)
            upp = sde(self.user, "textures/mini_choose.jpg", "textures/back_field.jpg", "down", self.side)
            self.choose, self.flag, self.field, self.user = upp[0], upp[1], upp[2], upp[3]
        self.rend = [self.choose, self.chxy, self.field, self.flag, self.posxy, self.user]
        return self.choose, self.chxy, self.field, self.flag, self.posxy, self.user
        pass

    def render(self):
        scr.blit(back, (0, 0))
        scr.blit(self.field, self.posxy)  # (800-n) // 2
        scr.blit(self.choose, self.chxy)
        scr.blit(self.user, self.u_pos[1])
        if self.first_is:
            for el in walls[self.flag]:
                sprite = pygame.sprite.Sprite()
                sprite.image = load_image("wall.jpg")
                sprite.rect = pygame.Rect((el[0], el[1], 50, 50))
                self.all_sprites.add(sprite)
        self.first_is = False
        self.all_sprites.draw(scr)
        ct = self.check_turn()
        self.up_flag, self.left_flag, self.right_flag, self.down_flag = ct[0], ct[1], ct[2], ct[3]

    def check_turn(self):
        self.up_flag = False
        self.down_flag = False
        self.right_flag = False
        self.left_flag = False

        if self.u_pos[1] == (225, 15) and self.flag == self.u_pos[0]:
            scr.blit(goup, (227, 3))
            self.up_flag = True
        elif self.u_pos[1] == (225, 525) and self.flag == self.u_pos[0]:
            scr.blit(godown, (227, 575))
            self.down_flag = True
        elif self.u_pos[1] == (375, 375) and self.flag == self.u_pos[0]:
            scr.blit(goright, (380, 349))
            self.right_flag = True
        elif self.u_pos[1] == (75, 115) and self.flag == self.u_pos[0]:
            scr.blit(goleft, (24, 90))
            self.left_flag = True
        elif self.u_pos[1] == (375, 115) and self.flag == self.u_pos[0]:
            scr.blit(goright, (380, 91))
            self.right_flag = True
        elif self.u_pos[1] == (75, 65) and self.flag == u_pos[0]:
            scr.blit(goleft, (24, 40))
            self.left_flag = True
        elif self.u_pos[1] == (375, 65) and self.flag == u_pos[0]:
            scr.blit(goright, (380, 41))
            self.right_flag = True
        elif self.u_pos[1] == (325, 615) and self.flag == self.u_pos[0]:
            scr.blit(godown, (327, 665))
            self.down_flag = True
        elif self.u_pos[1] == (75, 275) and self.flag == self.u_pos[0]:
            scr.blit(goleft, (24, 250))
            self.left_flag = True
        return self.up_flag, self.left_flag, self.right_flag, self.down_flag

    def click(self, pos):
        self.pos = pos
        if (pos[1] > self.posxy[1] + 350 and self.flag == "up" or self.flag == "down") or pos[1] > self.posxy[1] + 650:
            try:
                self.first_is = True
                self.all_sprites.remove(*[el for el in self.all_sprites])
                rend = stage.render_onclick(pos)
                self.choose, self.chxy, self.field, self.flag, self.posxy, self.user = rend[0], rend[1], rend[2], rend[3], rend[4], rend[5]
            except UnboundLocalError:
                pass
        try:
            stp = self.step(self.u_pos, self.user_coords)
            self.user_coords, self.u_pos = stp[0], stp[1]
        except UnboundLocalError:
            pass
        if self.up_flag or self.down_flag or self.right_flag or self.left_flag:
            try:
                turn = stage.turnit(self.u_pos)
                self.choose, self.flag, self.field, self.u_pos, self.chxy, self.posxy, self.side, self.user_coords = turn[0], turn[1], turn[2], turn[3], \
                                                                             turn[4], turn[5], turn[6], turn[7]
                self.first_is = True
                self.all_sprites.remove(*[el for el in self.all_sprites])
            except UnboundLocalError:
                pass
        pass



    def step(self, u_pos, user_coords):
        f_u_pos = u_pos
        f_user_coords = user_coords
        if self.flag == u_pos[0]:
            # проверка на границы поля
            if self.posxy[0] < self.pos[0] < self.posxy[0] + 340 and (self.posxy[1] < self.pos[1] < self.posxy[1] + 350 or (
                    self.posxy[1] < self.pos[1] < self.posxy[1] + 650 and self.side != "up" and self.side != "down")):
                if u_pos[1][0] - 58 <= self.pos[0] <= u_pos[1][0] + 90 and u_pos[1][1] - 50 <= self.pos[1] <= u_pos[1][1] + 100:
                    user_coords = list(user_coords)
                    if u_pos[1][0] - 10 < self.pos[0] and u_pos[1][0] + 39 < self.pos[0] or u_pos[1][0] - 10 > self.pos[0] and \
                            u_pos[1][0] + 39 > self.pos[0] and u_pos[1][1] <= self.pos[1] <= u_pos[1][1] + 48:  # <-
                        if u_pos[1][0] - 58 <= self.pos[0] <= u_pos[1][0] and u_pos[1][1] <= self.pos[1] <= u_pos[1][1] + 48:
                            user_coords[0] -= 50
                        elif u_pos[1][0] <= self.pos[0] <= u_pos[1][0] + 90 and u_pos[1][1] <= self.pos[1] <= u_pos[1][
                            1] + 48:  # ->
                            user_coords[0] += 50
                    elif u_pos[1][1] < self.pos[1] and u_pos[1][1] + 50 < self.pos[1] or u_pos[1][1] > self.pos[1] and u_pos[1][
                        1] + 50 > self.pos[1] and u_pos[1][0] - 10 <= self.pos[0] <= u_pos[1][0] + 50:
                        if u_pos[1][1] - 50 <= self.pos[1] <= u_pos[1][1] and u_pos[1][0] - 8 <= self.pos[0] <= u_pos[1][0] + 50:
                            user_coords[1] -= 50
                        elif u_pos[1][1] <= self.pos[1] <= u_pos[1][1] + 100 and u_pos[1][0] - 8 <= self.pos[0] <= u_pos[1][
                            0] + 50:
                            user_coords[1] += 50
                    self.user_coords = tuple(user_coords)
                    self.u_pos = (self.side, self.user_coords)
                    usr = pygame.sprite.Sprite()
                    usr.rect = pygame.Rect((self.u_pos[1][0] + 2, self.u_pos[1][1] + 2, 48, 48))
                    if pygame.sprite.spritecollideany(usr, self.all_sprites) is None:
                        return self.user_coords, self.u_pos
        return f_user_coords, f_u_pos

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
                upp = sde(self.user, "textures/left_right_big_choose.jpg", "textures/first_side_field.jpg", "right", self.side)
            elif u_pos[0] == "back":
                self.side = "right"
                self.user_coords = (75, 115)
                self.chxy = (261, 706)
                upp = sde(self.user, "textures/left_right_big_choose.jpg", "textures/first_side_field.jpg", "right", sself.side)
            elif u_pos[0] == "left":
                self.side = "back"
                self.user_coords = (75, 65)
                self.chxy = (234, 706)
                upp = sde(self.user, "textures/big_choose.jpg", "textures/first_side_field.jpg", "back", self.side)
            self.u_pos = [self.side, self.user_coords]
            self.posxy = (75, 15)
            self.choose, self.flag, self.field, self.user = upp[0], upp[1], upp[2], upp[3]
        elif self.left_flag and (
                56 <= self.pos[0] <= 66 and (115 <= self.pos[1] <= 161 or 65 <= self.pos[1] <= 111 or 275 <= self.pos[1] <= 321)):
            if u_pos[0] == "right":
                self.side = "back"
                self.user_coords = (375, 115)
                self.chxy = (234, 706)
                upp = sde(self.user, "textures/big_choose.jpg", "textures/first_side_field.jpg", "back", self.side)
            elif u_pos[0] == "back":
                self.side = "left"
                self.user_coords = (375, 65)
                self.chxy = (206, 706)
                upp = sde(self.user, "textures/left_right_big_choose.jpg", "textures/first_side_field.jpg", "left", self.side)
            elif u_pos[0] == "down":
                self.side = "left"
                self.user_coords = (325, 615)
                self.chxy = (206, 706)
                upp = sde(self.user, "textures/left_right_big_choose.jpg", "textures/first_side_field.jpg", "left", self.side)
            self.posxy = (75, 15)
            self.u_pos = [self.side, self.user_coords]
            self.choose, self.flag, self.field, self.user = upp[0], upp[1], upp[2], upp[3]
        return self.choose, self.flag, self.field, self.u_pos, self.chxy, self.posxy, self.side, self.user_coords


stage = level()
#Fа
while running:
    for event in pygame.event.get():
        stage.render()
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = event.pos
            stage.click(pos)
        if pygame.mouse.get_focused():
            scr.blit(CURSOR, (pygame.mouse.get_pos()))
            pygame.display.update()
    pygame.display.flip()

# если в field будет только поле, то сделать функции с отрисовкой
# изменение положения юзера на грани через кнопку перехода на грань(если  нажал, то меняем)
# сделать стены. тогда не будет выхода за карту