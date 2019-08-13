import pygame
import sys
from models.ball import Ball
from models.pallet import Pallet


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

            pygame.display.flip()
