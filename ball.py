import pygame

class Ball:
    def __init__(self, color: tuple, size: tuple, pos: tuple):
        self.color = color  
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])