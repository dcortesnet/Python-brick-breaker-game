import pygame
import sys
import time
from models.ball import Ball
from models.pallet import Pallet
from models.wall import Wall
from models.brick import Brick

pygame.init() # Necesario para el uso de fuentes

class Game:

    def __init__(self, window_width: int, window_height: int, frames_x_seconds: int):

        pygame.key.set_repeat(30)  # Retraso en milisegundos
        self.window_width     = window_width
        self.window_height    = window_height
        self.frames_x_seconds = frames_x_seconds
        self.color_rgb_blue   = (0, 0, 64)
        self.color_rgb_white  = (255, 255, 255)
        self.points           = 0

        self.window = pygame.display.set_mode(
            (self.window_width, self.window_height)
        )

        self.clock  = pygame.time.Clock()
        self.ball   = Ball()
        self.pallet = Pallet()
        self.wall   = Wall()

    def run(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self.pallet.update(event)

            # Rellenar pantalla con color azul
            self.window.fill(self.color_rgb_blue)
            self.show_points()

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
            self.collite_ball_in_wall()

            # Revisión si la bola sale del juego por abajo
            if self.ball.rect.top > self.window_height:
                # logica de perder
                self.end_game()

            pygame.display.flip()

    def collite_ball_in_wall(self):
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

            # Al eliminar un ladrillo aumentamos la puntiación en +10
            self.points += 10

    def show_points(self):
        font             = pygame.font.SysFont('Consolas', 20)
        text_points      = font.render( 'Puntos : ' + str(self.points).zfill(5), True, self.color_rgb_white)
        text_points_rect = text_points.get_rect()
        text_points_rect.topleft = [0, 0]
        self.window.blit(text_points, text_points_rect)

    def end_game(self):
        font               = pygame.font.SysFont('Arial', 72)
        text_end_game      = font.render('Juego Terminado', True, self.color_rgb_white)
        text_end_game_rect = text_end_game.get_rect()
        # Pos text en el centro del juego
        text_end_game_rect.center = [ self.window_width / 2, self.window_height / 2 ]
        # Dibujamos el texto en la pantalla
        self.window.blit(text_end_game, text_end_game_rect)
        # Actualización de la pantalla
        pygame.display.flip()
        time.sleep(3)
        sys.exit()



