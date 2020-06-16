import pygame
from models.brick import Brick
from settings import WINDOW_WIDTH

class Wall(pygame.sprite.Group):
    def __init__(self):
        pygame.sprite.Group.__init__(self)
        self.pos_x = 0
        self.pos_y = 20
        # 640 / 16 = Cantidad de ladrillos por fila
        # Construcción de muro
        # Cantidad de ladrillos múltiplos de 16
        for x in range(0, 64):
            if self.pos_x >= WINDOW_WIDTH:
                self.pos_x = 0
                self.pos_y = self.pos_y + brick.rect.height
            brick = Brick((self.pos_x, self.pos_y))
            # Agregar Sprite al grupo
            self.add(brick)
            self.pos_x = self.pos_x + brick.rect.width
