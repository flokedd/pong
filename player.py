import pygame

class Player:
    def __init__(self, color: tuple, pos:list):
        self.color = color
        self.size = (20, 100)
        self.rect = pygame.Rect(pos[0], pos[1], self.size[0], self.size[1])