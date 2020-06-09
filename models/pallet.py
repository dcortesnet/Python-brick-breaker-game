import pygame
from settings import WINDOW_WIDTH, WINDOW_HEIGHT

class Pallet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image          = pygame.image.load('img/pallet.png')
        self.rect           = self.image.get_rect()
        self.rect.midbottom = ( WINDOW_WIDTH / 2, WINDOW_HEIGHT-10)
        self.speed_x        = 0

    def draw(self, window):
        """ Dibuja la paleta en la pantalla """
        window.blit(self.image, self.rect)

    def move(self, event):
        """ Se mueve en la posición dependiendo del evento del teclado
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
        """ Método encargado de cambiar attr speed_x para posteriormente
            dibujar la paleta en la pantalla con cordenada diferente ( Hacia la izquierda )
        """
        if self.rect.left >= 10:
            self.speed_x = - 5
        else:
            self.dont_move()

    def move_right(self):
        """ Método encargado de cambiar attr speed_x para posteriormente
            dibujar la paleta en la pantalla con cordenada diferente ( Hacia la derecha )
        """

        if self.rect.right <= 630:
            self.speed_x = 5
        else:
            self.dont_move()

    def dont_move(self):
        """ Método que conserva la posición actual de la coordenada en X """
        self.speed_x = 0