import pygame
from settings import WINDOW_WIDTH

class Live:
    def __init__(self, lives: int, color):
        self.color = color
        self.lives = lives
        self.font = pygame.font.SysFont('Consolas', 20)

    def draw(self, window):
        self.text_lives               = self.font.render('Vidas : ' + str(self.lives), True, self.color)
        self.text_lives_rect          = self.text_lives.get_rect()
        self.text_lives_rect.topright = [WINDOW_WIDTH, 0]
        window.blit(self.text_lives, self.text_lives_rect)