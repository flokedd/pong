import pygame

class Player:
    screen = None
    size = (20, 100)
    def __init__(self, color: tuple, start_pos:tuple, speed):
        self.color = color
        self.speed = speed
        self.start_pos = start_pos
        self.rect = pygame.Rect(start_pos[0], start_pos[1], self.size[0], self.size[1])

    def move(self, direction):
        if direction == "down":
            if self.rect.bottom != self.screen.get_size()[1]:
                self.rect = self.rect.move(0, self.speed)
        elif direction == "up":
            if self.rect.top != 0:
                self.rect = self.rect.move(0, -self.speed)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)