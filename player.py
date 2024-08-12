import pygame

class Player:
    screen = None
    size = (20, 100)
    def __init__(self, color: tuple, pos:tuple, speed):
        self.color = color
        self.speed = speed
        self.rect = pygame.Rect(pos[0], pos[1], self.size[0], self.size[1])

    def move(self, direction):
        if direction == "down":
            if self.rect.bottom != self.screen.get_size()[1]:
                self.rect = self.rect.move(0, self.speed)
        elif direction == "up":
            if self.rect.top != 0:
                self.rect = self.rect.move(0, -self.speed)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)