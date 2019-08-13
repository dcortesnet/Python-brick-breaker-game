import pygame
from settings import WINDOW_WIDTH, WINDOW_HEIGHT


class Pallet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('img/pallet.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = ( WINDOW_WIDTH / 2, WINDOW_HEIGHT-10)
        self.speed_x = 0

    def update(self, event):
        """ Actualizar la posición dependiendo del evento del teclado
            Se escuchan las teclas izquierda y derecha
        """
        if event.key == pygame.K_LEFT:
            self.move_left()
        elif event.key == pygame.K_RIGHT:
            self.move_right()
        else:
            self.dont_move()

        self.rect.move_ip(self.speed_x, 0)

    def move_left(self):
        if self.rect.left >= 10:
            self.speed_x = - 5
        else:
            self.dont_move()

    def move_right(self):
        if self.rect.right <= 630:
            self.speed_x = 5
        else:
            self.dont_move()

    def dont_move(self):
        self.speed_x = 0