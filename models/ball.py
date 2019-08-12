import pygame
from settings import WINDOW_WIDTH, WINDOW_HEIGHT


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('img/ball.png')
        self.rect = self.image.get_rect()
        self.speed_x = 3
        self.speed_y = 3

    def update(self):
        """ Actualizar la posición actual y velocidad """
        self.rect.move_ip(self.speed_x, self.speed_y) # Se cambia el valor de rect en X,Y

        if self.rect.bottom >= WINDOW_HEIGHT or self.rect.top <= 0:
            self.speed_y = self.speed_y * -1

        if self.rect.left >= WINDOW_WIDTH or self.rect.right <= 0:
            self.speed_x = self.speed_x * -1

        # print(self.rect.bottom, 'Bottom')
        # print(self.rect.left, 'Left')
        # print(self.rect.right, 'Right')
        # print(self.rect.top, 'Top')

