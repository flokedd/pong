import pygame
from player import Player
from ball import Ball

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Pong')
clock = pygame.time.Clock()
Player.screen = screen
Ball.screen = screen
running = True
game_started  = False
font = pygame.font.SysFont('Comic Sans MS', 30)
start_text = font.render("Press any button to start", False, (255, 255, 255))
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

player_one = Player(BLUE, (0, screen.get_size()[1]/2-Player.size[1]/2), 5)
player_two = Player(RED, (screen.get_size()[0]-Player.size[0], screen.get_size()[1]/2-Player.size[1]/2), 5)

ball = Ball(WHITE, (screen.get_size()[0]/2-Ball.radius, screen.get_size()[1]/2-Ball.radius), [5, 5])

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            game_started = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            game_started = True
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

    if game_started:
        ball.move()
    else:
        screen.blit(start_text, (screen.get_size()[0]/2-start_text.get_size()[0]/2, 200))

    if ball.rect.left < player_one.rect.left:
        player_two.score()
        ball.reset()
        player_one.reset()
        player_two.reset()
    elif ball.rect.right > player_two.rect.right:
        player_one.score()
        ball.reset()
        player_one.reset()
        player_two.reset()

    ball.change_direction_y()
    ball.change_direction_x(player_one.rect)
    ball.change_direction_x(player_two.rect)

    ball.draw() 
    player_one.draw()
    player_two.draw()
    player_one.draw_score()
    player_two.draw_score()

    pygame.display.flip()

    clock.tick(60) 

pygame.quit()