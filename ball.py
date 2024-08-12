import pygame

class Ball:
    screen = None
    radius = 25
    def __init__(self, color: tuple, pos: tuple, speed, direction: list):
        self.color = color 
        self.speed = speed
        self.direction = direction
        self.rect = pygame.Rect(pos[0], pos[1], self.radius*2, self.radius*2)

    def change_direction(self):
        if self.rect.top == 0:
            self.direction[1] = 1
        elif self.rect.bottom == self.screen.get_size()[1]:
            self.direction[1] = -1

    def move(self):
        self.rect = self.rect.move(self.direction[0] * self.speed, self.direction[1] * self.speed)

    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.rect.center, self.radius)