import pygame
from player import Player

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
Player.screen = screen
running = True
RED = (255, 0, 0)
BLUE = (0, 0, 255)

player_one = Player(BLUE, (0, screen.get_size()[1]/2-Player.size[1]/2))
player_two = Player(RED, (screen.get_size()[0]-Player.size[0], screen.get_size()[1]/2-Player.size[1]/2))

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_s]:
        player_one.move("down")
    if keys[pygame.K_w]:
        player_one.move("up")

    if keys[pygame.K_DOWN]:
        player_two.move("down")
    if keys[pygame.K_UP]:
        player_two.move("up")

    screen.fill("black")
    player_one.draw()
    player_two.draw()

    pygame.display.flip()

    clock.tick(60) 

pygame.quit()