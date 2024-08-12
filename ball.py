import pygame

class Ball:
    screen = None
    radius = 25
    def __init__(self, color: tuple, pos: tuple):
        self.color = color 
        self.rect = pygame.Rect(pos[0], pos[1], self.radius*2, self.radius*2)

    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.rect.center, self.radius)