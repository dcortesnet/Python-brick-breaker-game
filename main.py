import pygame
from models.game import Game
from settings import WINDOW_WIDTH, WINDOW_HEIGHT, FRAMES_X_SECONDS

pygame.display.set_caption('Juego de ladrillos en Python')


if __name__ == '__main__':
    game = Game( 
        WINDOW_WIDTH, WINDOW_HEIGHT, FRAMES_X_SECONDS
    )
    
    game.run()
