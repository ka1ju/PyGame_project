import pygame

pygame.init()

scr = pygame.display.set_mode((500, 800))
running = True

CURSOR = pygame.image.load("mouse_last_vers.png").convert_alpha()
pygame.mouse.set_cursor((8, 8), (4, 4), (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0))
pygame.mouse.set_visible(False)
field = pygame.image.load("first_side_field.jpg").convert()
back = pygame.image.load("back_2.jpg").convert()
posxy = (75, 15)
choose = pygame.image.load("big_choose.jpg").convert()
chxy = (179, 706)
side = "front"
user_coords = (225, 615)
u_pos = (side, user_coords)
user = pygame.image.load("user.png").convert_alpha()
flag = "front"

while running:
    for event in pygame.event.get():
        scr.blit(back, (0, 0))
        scr.blit(field, posxy)  # (800-n) // 2
        scr.blit(choose, chxy)
        scr.blit(user, u_pos[1])
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            print(pygame.mouse.get_pos())
            pos = pygame.mouse.get_pos()
            if 225 <= pos[0] <= 252 and 704 >= pos[1] >= 675:  # up
                choose = pygame.image.load("mini_choose.jpg").convert()
                chxy = (234, 677)
                field = pygame.image.load("frond_field.jpg").convert()
                posxy = (100, 250)
                flag = "up"
                if u_pos[0] == "up":
                    user = pygame.image.load("user.png").convert_alpha()
                else:
                    user.fill((0, 0, 0, 0))
            elif 226 <= pos[0] <= 252 and 705 <= pos[1] <= 763:  # back
                choose = pygame.image.load("big_choose.jpg").convert()
                chxy = (234, 706)
                field = pygame.image.load("first_side_field.jpg").convert()
                posxy = (75, 15)
                flag = "back"
                if u_pos[0] == "back":
                    user = pygame.image.load("user.png").convert_alpha()
                else:
                    user.fill((0, 0, 0, 0))
            elif 171 <= pos[0] <= 197 and 704 <= pos[1] <= 763:  # front
                choose = pygame.image.load("big_choose.jpg").convert()
                chxy = (179, 706)
                field = pygame.image.load("first_side_field.jpg").convert()
                posxy = (75, 15)
                flag = "front"
                if u_pos[0] == "front":
                    user = pygame.image.load("user.png").convert_alpha()
                else:
                    user.fill((0, 0, 0, 0))
            elif 198 <= pos[0] <= 225 and 705 <= pos[1] <= 763:  # left
                choose = pygame.image.load("left_right_big_choose.jpg").convert()
                chxy = (206, 706)
                field = pygame.image.load("first_side_field.jpg").convert()
                posxy = (75, 15)
                flag = "left"
                if u_pos[0] == "left":
                    user = pygame.image.load("user.png").convert_alpha()
                else:
                    user.fill((0, 0, 0, 0))
            elif 254 <= pos[0] <= 280 and 706 <= pos[1] <= 763:  # right
                choose = pygame.image.load("left_right_big_choose.jpg").convert()
                chxy = (261, 706)
                field = pygame.image.load("first_side_field.jpg").convert()
                posxy = (75, 15)
                flag = "right"
                if u_pos[0] == "right":
                    user = pygame.image.load("user.png").convert_alpha()
                else:
                    user.fill((0, 0, 0, 0))
            elif 226 <= pos[0] <= 252 and 765 <= pos[1] <= 794:  # down
                choose = pygame.image.load("mini_choose.jpg").convert()
                chxy = (234, 765)
                field = pygame.image.load("back_field.jpg").convert()
                posxy = (100, 250)
                flag = "down"
                if u_pos[0] == "down":
                    user = pygame.image.load("user.png").convert_alpha()
                else:
                    user.fill((0, 0, 0, 0))
            # блок с отрисовкой граней и персонажа на них
            if flag == u_pos[0]:
                if u_pos[1][0] - 58 <= pos[0] <= u_pos[1][0] + 90 and u_pos[1][1] - 50 <= pos[1] <= u_pos[1][1] + 100:
                    user_coords = list(user_coords)
                    if u_pos[1][0] - 10 < pos[0] and u_pos[1][0] + 39 < pos[0] or u_pos[1][0] - 10 > pos[0] and \
                            u_pos[1][0] + 39 > pos[0] and u_pos[1][1] <= pos[1] <= u_pos[1][1] + 48:  # <-
                        if u_pos[1][0] - 58 <= pos[0] <= u_pos[1][0] and u_pos[1][1] <= pos[1] <= u_pos[1][1] + 48:
                            user_coords[0] -= 50
                        elif u_pos[1][0] <= pos[0] <= u_pos[1][0] + 90 and u_pos[1][1] <= pos[1] <= u_pos[1][
                            1] + 48:  # ->
                            user_coords[0] += 50
                    elif u_pos[1][1] < pos[1] and u_pos[1][1] + 50 < pos[1] or u_pos[1][1] > pos[1] and u_pos[1][
                        1] + 50 > pos[1] and u_pos[1][0] - 10 <= pos[0] <= u_pos[1][0] + 50:
                        print("QQQ")
                        if u_pos[1][1] - 50 <= pos[1] <= u_pos[1][1] and u_pos[1][0] - 8 <= pos[0] <= u_pos[1][0] + 50:
                            user_coords[1] -= 50
                        elif u_pos[1][1] <= pos[1] <= u_pos[1][1] + 100 and u_pos[1][0] - 8 <= pos[0] <= u_pos[1][
                            0] + 50:
                            user_coords[1] += 50
                    print(u_pos[1][1], pos[1], u_pos[1][1] + 50)
                    user_coords = tuple(user_coords)
                    u_pos = (side,
                             user_coords)  # сделать 0 элемент как переменную, которая будет меняться. Также сделать
                    # обработку. Если на другой грани и нажимаю, то не ходить. Делать ход, если нахожусь на грани с
                    # персонажем

        if pygame.mouse.get_focused():
            scr.blit(CURSOR, (pygame.mouse.get_pos()))
            pygame.display.update()
    pygame.display.flip()

# если в field будет только поле, то сделать функции с отрисовкой
# изменение положения юзера на грани через кнопку перехода на грань(если  нажал, то меняем)
# сделать стены. тогда не будет выхода за карту
