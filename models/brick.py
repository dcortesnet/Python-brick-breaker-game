import pygame

class Brick(pygame.sprite.Sprite):
    def __init__(self, position: tuple):
        pygame.sprite.Sprite.__init__(self)
        self.image        = pygame.image.load('img/wall.png')
        self.rect         = self.image.get_rect()
        self.rect.topleft = position