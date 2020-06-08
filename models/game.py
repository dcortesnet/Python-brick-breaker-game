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
        self.lives            = 3
        self.ball_in_pallet  = True

        self.window = pygame.display.set_mode(
            (self.window_width, self.window_height)
        )

        self.clock          = pygame.time.Clock()
        self.ball: Ball     = Ball()
        self.pallet: Pallet = Pallet()
        self.wall: Wall     = Wall()

    def run(self):
        """ Método Principal loop del juego """

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self.check_move_pallet(event)
                    
            self.update_game()
            self.check_take_out()
            self.check_collide_ball_pallet() # 
            self.check_collite_ball_wall()  # Un boleado con los spirte tocados deben ser destruidos
            self.check_win_game() # Lógica para ganar el juego
            self.check_end_game() # Lógica de finalizar juego
            pygame.display.flip() # Actualización de pantalla

    def update_game(self):
        """ Actualizar, dibuja y refrescar objetos en pantalla, fps """
        self.window.fill(self.color_rgb_blue) # Rellenar pantalla fondo azul
        self.show_points() # Mostrar puntos
        self.show_lives() # Mostrar vidas
        self.clock.tick(self.frames_x_seconds) # fps
        self.window.blit(self.ball.image, self.ball.rect) # Draw Ball
        self.window.blit(self.pallet.image, self.pallet.rect) # Draw Pallet
        self.wall.draw(self.window)  # Dibujar ladrillos

    def check_move_pallet(self, event):
        """ Método de verificación si el jugador movió la paleta izquierda y derecha """
        self.pallet.update_pallet(event)
        # Evento de lanzar la bolita
        if self.ball_in_pallet == True and event.key == pygame.K_SPACE:
            self.ball_in_pallet = False

    def check_take_out(self):
        """ Método de verificación si el jugador sacó la pelota y actualiza eje x y pelota """
        if self.ball_in_pallet:
            self.ball.rect.midbottom = self.pallet.rect.midtop
        else:
            self.ball.update_ball()
    
    def check_collide_ball_pallet(self):
        """ Método de verificación si la pelota colisionó con la paleta """
        if pygame.sprite.collide_rect(self.ball, self.pallet):
            # Colición entre pelota y paleta, recibe 2 sprite como agumento
            self.ball.collide_y()

    def check_end_game(self):
        """ Método de verificación si termino el juegó """
        if self.ball.rect.top > self.window_height:
            if self.lives <= 1:
                self.end_game()
            else:
                self.lives -= 1
                self.ball_in_pallet = True

    def check_win_game(self):
        """ Método de verificación si gano el juegó """
        if len(self.wall.sprites()) == 0:
            self.win_game()
        
    def check_collite_ball_wall(self):
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
        """ Método que muestra los puntos en pantalla """

        font                     = pygame.font.SysFont('Consolas', 20)
        text_points              = font.render( 'Puntos : ' + str(self.points).zfill(5), True, self.color_rgb_white)
        text_points_rect         = text_points.get_rect()
        text_points_rect.topleft = [0, 0]
        self.window.blit(text_points, text_points_rect)

    def show_lives(self):
        """ Método que muestra las vidas en pantalla """

        font = pygame.font.SysFont('Consolas', 20)
        text_lives               = font.render('Vidas : ' + str(self.lives), True, self.color_rgb_white)
        text_lives_rect          = text_lives.get_rect()
        text_lives_rect.topright = [self.window_width, 0]
        self.window.blit(text_lives, text_lives_rect)

    def end_game(self):
        """ Método encargado de finalizar juego en estado perdido """

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

    def win_game(self):
        """ Método encargado de finalizar el juego en estado ganado """
        font = pygame.font.SysFont('Arial', 30)
        text_win_game = font.render('Juego Ganado! Total Puntos : ' + str(self.points) , True, self.color_rgb_white)
        text_win_game_rect = text_win_game.get_rect()

        # Pos text en el centro del juego
        text_win_game_rect.center = [self.window_width / 2, self.window_height / 2]

        # Dibujamos el texto en la pantalla
        self.window.blit(text_win_game, text_win_game_rect)

        # Actualización de la pantalla
        pygame.display.flip()
        time.sleep(3)
        sys.exit()



