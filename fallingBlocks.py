import pygame
import sys

pygame.init()

width = 800
height = 600

RED = (255, 0, 0)
BACKGROUND_COLOR = (0, 0, 0)

player_pos = [400, 300]
player_size = 50

screen = pygame.display.set_mode((width, height))

game_over = False

while not game_over:

    for event in pygame.event.get():
        print(event)

        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:

            x = player_pos[0]
            y = player_pos[1]

            if event.key == pygame.K_LEFT:
                x -= 5
            elif event.key == pygame.K_RIGHT:
                x += 5
            elif event.key == pygame.K_UP:
                pass
            elif event.key == pygame.K_DOWN:
                pass

            player_pos = [x, y]

    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(
        screen, RED, (player_pos[0], player_pos[1], player_size, player_size))

    pygame.display.update()
