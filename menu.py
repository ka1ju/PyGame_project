import pygame

class Menu:
    def __init__(self, back, play):
        self.play = play
        self.back = back
        pass

    def render(self, scr):
        scr.blit(self.back, (0, 0))
        scr.blit(self.play, (150, 150))

    def click(self, pos):
        if 150 <= pos[0] <= 350 and 150 <= pos[1] <= 229:
            return 'Level'