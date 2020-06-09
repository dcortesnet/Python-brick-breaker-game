import pygame
import sys
import time
from models.ball import Ball
from models.pallet import Pallet
from models.wall import Wall
from models.brick import Brick
from models.point import Point
from models.live import Live

pygame.init() # Necesario para el uso de fuentes

class Game:
    def __init__(self, window_width: int, window_height: int, frames_x_seconds: int):
        pygame.key.set_repeat(30)
        self.window_width     = window_width
        self.window_height    = window_height
        self.frames_x_seconds = frames_x_seconds
        self.color_rgb_blue   = (0, 0, 64)
        self.color_rgb_white  = (255, 255, 255)
        self.lives            = 3
        self.ball_in_pallet   = True
        self.clock            = pygame.time.Clock()
        self.point            = Point(0, self.color_rgb_white)
        self.live             = Live(3, self.color_rgb_white)
        self.ball: Ball       = Ball()
        self.pallet: Pallet   = Pallet()
        self.wall: Wall       = Wall()
        self.window = pygame.display.set_mode(
            (self.window_width, self.window_height)
        )

    def run(self):
        """ Método Principal loop del juego """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self.pallet.move(event)
                    if self.ball_in_pallet == True and event.key == pygame.K_SPACE:
                        self.ball_in_pallet = False
            
            self.clock.tick(self.frames_x_seconds)
            self.window.fill(self.color_rgb_blue) 
            self.point.draw(self.window) 
            self.live.draw(self.window) 
            self.ball.draw(self.window) 
            self.pallet.draw(self.window) 
            self.wall.draw(self.window)
            self.check_take_out()
            self.check_collide_ball_pallet()  
            self.check_collite_ball_wall() 
            self.check_win_game() 
            self.check_end_game()
            pygame.display.flip() 
   
    def check_take_out(self):
        """ Método de verificación si el jugador sacó la pelota y actualiza eje x y pelota """
        if self.ball_in_pallet:
            self.ball.rect.midbottom = self.pallet.rect.midtop
        else:
            self.ball.move()
    
    def check_collide_ball_pallet(self):
        """ Método de verificación si la pelota colisionó con la paleta """
        if pygame.sprite.collide_rect(self.ball, self.pallet):
            # Colición entre pelota y paleta, recibe 2 sprite como agumento
            self.ball.collide_y()

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
           
            self.wall.remove(brick)  # Eliminar ladrillo del muro Manualmente
            self.point.points += 10  # Al eliminar un ladrillo aumentamos la puntiación en +10

    def check_end_game(self):
        """ Método de verificación si termino el juegó """
        if self.ball.rect.top > self.window_height:
            if self.live.lives <= 1:
                self.finish_game('loss')
            else:
                self.live.lives -= 1
                self.ball_in_pallet = True

    def check_win_game(self):
        """ Método de verificación si gano el juegó """
        if len(self.wall.sprites()) == 0:
            self.finish_game('win')
        
    def finish_game(self, type_of_completion: str):
        """ Método de visualización de finalización del juego """
        if type_of_completion == "win":
            description = 'Juego Ganado!'
        else:
            description = 'Juego Perdido!'
        
        font = pygame.font.SysFont('Arial', 72)
        text = font.render(description, True, self.color_rgb_white)
        text_rect = text.get_rect()
        text_rect.center = [self.window_width / 2, self.window_height / 2] # Pos text en el centro del juego
        self.window.blit(text, text_rect) # Dibujamos el texto en la pantalla
        pygame.display.flip()
        time.sleep(3)
        sys.exit()



