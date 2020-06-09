import pygame

class Point:
    def __init__(self, points: int, color):
        self.color = color
        self.points = points
        self.font = pygame.font.SysFont('Consolas', 20)

    def draw(self, window):
        self.text_points = self.font.render( 'Puntos : ' + str(self.points).zfill(5), True, self.color)
        self.text_points_rect = self.text_points.get_rect()
        self.text_points_rect.topleft = [0, 0]
        window.blit(self.text_points, self.text_points_rect)