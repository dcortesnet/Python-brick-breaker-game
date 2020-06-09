import pygame
from settings import WINDOW_WIDTH, WINDOW_HEIGHT


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image   = pygame.image.load('img/ball.png')
        self.rect    = self.image.get_rect()
        self.speed_x = 3
        self.speed_y = 3

    def draw(self, window):
        window.blit(self.image, self.rect)

    def move(self):
        self.rect.move_ip(self.speed_x, self.speed_y)
        if self.rect.top <= 0:
            self.collide_y()

        if self.rect.left >= WINDOW_WIDTH or self.rect.right <= 0:
            self.collide_x()

    def collide_y(self):
        """ Revierte la dirección del eje Y """
        self.speed_y = self.speed_y * -1

    def collide_x(self):
        """ Revierte la dirección del eje X """
        self.speed_x = self.speed_x * -1

