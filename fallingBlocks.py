import pygame
import sys
import random

pygame.init()

width = 800
height = 600

RED = (255, 0, 0)
BACKGROUND_COLOR = (0, 0, 0)
BLUE = (0, 0, 255)

player_size = 50
player_pos = [width / 2, height - player_size * 2]

enemy_size = 50
enemy_pos = [random.randrange(width - enemy_size), 0]
enemy_list = [enemy_pos]

falling_speed = 10

clock = pygame.time.Clock()

screen = pygame.display.set_mode((width, height))

game_over = False


def detect_collision(player_pos, enemy_pos):
    p_x = player_pos[0]
    p_y = player_pos[1]

    e_x = enemy_pos[0]
    e_y = enemy_pos[1]

    if (e_x >= p_x and e_x < (p_x + player_size)) or ((p_x >= e_x) and p_x < (e_x + enemy_size)):
        if (e_y >= p_y) and e_y < (p_y + player_size) or (p_y >= e_y) and p_y < (e_y + enemy_size):
            return True
    return False


def drop_blocks(enemy_list):
    delay = random.random()
    if len(enemy_list) < 10 and delay < 0.3:
        x_pos = random.randrange(width - enemy_size)
        y_pos = 0
        enemy_list.append([x_pos, y_pos])


def draw_enemies(enemy_list):
    for enemy_pos in enemy_list:
        # define enemy block
        pygame.draw.rect(screen, BLUE, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))


def update_enemy_position(enemy_list):
    for index, enemy_pos in enumerate(enemy_list):
        if enemy_pos[1] >= 0 and enemy_pos[1] < height:
            enemy_pos[1] += falling_speed
        else:
            enemy_list.pop(index)

def collision_check(enemy_list, player_position):

    for enemy_pos in enemy_list:
        if detect_collision(enemy_pos, player_pos):
            return True
    return False


while not game_over:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        # move the player
        if event.type == pygame.KEYDOWN:

            x = player_pos[0]
            y = player_pos[1]

            if event.key == pygame.K_LEFT:
                x -= player_size
            elif event.key == pygame.K_RIGHT:
                x += player_size
            elif event.key == pygame.K_UP:
                y -= 20
            elif event.key == pygame.K_DOWN:
                y += 20

            player_pos = [x, y]

    # define the background color after every event
    screen.fill(BACKGROUND_COLOR)

    if detect_collision(player_pos, enemy_pos):
        game_over = True
        break

    drop_blocks(enemy_list)
    update_enemy_position(enemy_list)
    if collision_check(enemy_list, player_pos):
        game_over = True

    draw_enemies(enemy_list)
    # defnie player block
    pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))

    clock.tick(30)
    pygame.display.update()
