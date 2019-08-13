import pygame


class Brick(pygame.sprite.Sprite):
    def __init__(self, position: tuple):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('img/wall.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        
        # print(ladrillo1.rect.width)  # Ancho de ladrillo en pantalla 60
        # print(ladrillo1.rect.height) # Altura de larillo en pantalla 40