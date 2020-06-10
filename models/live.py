import pygame
from settings import WINDOW_WIDTH, COLOR_RGB_WHITE

class Live:
    def __init__(self):
        self.color = COLOR_RGB_WHITE
        self.lives = 3
        self.font = pygame.font.SysFont('Consolas', 20)

    def draw(self, window):
        self.text_lives               = self.font.render('Vidas : ' + str(self.lives), True, self.color)
        self.text_lives_rect          = self.text_lives.get_rect()
        self.text_lives_rect.topright = [WINDOW_WIDTH, 0]
        window.blit(self.text_lives, self.text_lives_rect)