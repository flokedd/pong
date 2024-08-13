import pygame
from player import Player
from ball import Ball

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
Player.screen = screen
Ball.screen = screen
running = True
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

player_one = Player(BLUE, (0, screen.get_size()[1]/2-Player.size[1]/2), 5)
player_two = Player(RED, (screen.get_size()[0]-Player.size[0], screen.get_size()[1]/2-Player.size[1]/2), 5)

ball = Ball(WHITE, (screen.get_size()[0]/2-Ball.radius, screen.get_size()[1]/2-Ball.radius), 5, [1, 1])

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    keys = pygame.key.get_pressed()

    if keys[pygame.K_s]:
        player_one.move("down")
    if keys[pygame.K_w]:
        player_one.move("up")

    if keys[pygame.K_DOWN]:
        player_two.move("down")
    if keys[pygame.K_UP]:
        player_two.move("up")

    ball.move()

    if ball.rect.left < player_one.rect.centerx:
        player_two.score()
        ball.reset()
        player_one.reset()
        player_two.reset()
    elif ball.rect.right > player_two.rect.centerx:
        player_one.score()
        ball.reset()
        player_one.reset()
        player_two.reset()

    ball.change_direction_y()
    ball.change_direction_x(player_one.rect, 1)
    ball.change_direction_x(player_two.rect, -1)

    ball.draw()
    player_one.draw()
    player_two.draw()
    player_one.draw_score()
    player_two.draw_score()

    pygame.display.flip()

    clock.tick(60) 

pygame.quit()