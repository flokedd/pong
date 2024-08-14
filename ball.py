import pygame
import random

class Ball:
    screen = None
    radius = 25
    def __init__(self, color: tuple, start_pos: tuple, start_speed: list):
        self.color = color 
        self.start_speed = start_speed
        self.speed = start_speed.copy()
        self.start_pos = start_pos
        self.rect = pygame.Rect(start_pos[0], start_pos[1], self.radius*2, self.radius*2)

    def change_direction_y(self):
        if self.rect.top <= 0:
            self.speed[1] = self.speed[1] * -1
        elif self.rect.bottom >= self.screen.get_size()[1]:
            self.speed[1] = self.speed[1] * -1

    def change_direction_x(self, r):
        if self.rect.colliderect(r):
            self.speed[0] *= -1

    def reset(self):
        self.rect.x = self.start_pos[0]
        self.rect.y = self.start_pos[1]
        self.speed = self.start_speed.copy()

    def move(self):
        self.rect = self.rect.move(self.speed[0], self.speed[1])

    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.rect.center, self.radius)