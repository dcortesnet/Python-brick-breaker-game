import pygame
import sys
from models.ball import Ball
from models.pallet import Pallet
from models.wall import Wall
from models.brick import Brick

class Game:


    def __init__(self, window_width: int, window_height: int, frames_x_seconds: int):

        self.window_width = window_width
        self.window_height = window_height
        self.frames_x_seconds = frames_x_seconds
        self.color_rgb_blue = (0, 0, 64)

        self.window = pygame.display.set_mode(
            (self.window_width, self.window_height)
        )

        self.clock = pygame.time.Clock()
        pygame.key.set_repeat(30) # Retraso en milisegundos
        self.ball = Ball()
        self.pallet = Pallet()
        self.wall = Wall()

    def run(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self.pallet.update(event)

            self.window.fill(self.color_rgb_blue)
            self.clock.tick(self.frames_x_seconds)

            self.ball.update()

            self.window.blit(self.ball.image, self.ball.rect) # Draw Ball
            self.window.blit(self.pallet.image, self.pallet.rect) # Draw Pallet
            
            # Dibujar ladrillos
            self.wall.draw(self.window)

            # Colición entre pelota y paleta, recibe 2 sprite como agumento
            # Regresa un bool
            if pygame.sprite.collide_rect(self.ball, self.pallet):
                self.ball.collide_y()

            # Colición entre pelota y Sprite collide ( El muro )
            # Un boleado con los spirte tocados deben ser destruidos
            self.colliteBallInWall()

            pygame.display.flip()


    def colliteBallInWall(self):
        """ Se comprueba las coliciones en que eje fúe para cambiar direccion de la bolita,
            destruyendo la el ladrillo afectado en el muro
        """
        list_bricks: list[Brick] = pygame.sprite.spritecollide(self.ball, self.wall, False)

        if list_bricks:
            brick: Brick = list_bricks[0]

            ball_rect_coords_x = self.ball.rect.centerx

            # Comprobación colición por eje X, Izquierda y Derecha
            if ball_rect_coords_x < brick.rect.left or ball_rect_coords_x > brick.rect.right:
                self.ball.collide_x()
            else:
                self.ball.collide_y()

            # Eliminar ladrillo del muro Manualmente
            self.wall.remove(brick)

