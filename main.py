import pygame
from sys import exit
from settings import *
from player import Player
from map import world_map
from ray_casting import ray_casting
import math


def run():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        player.movement()
        screen.fill(BLACK)

        pygame.draw.rect(screen, BLUE, (0, 0, WIDTH, HALF_HEIGHT))
        pygame.draw.rect(screen, DARKGREY,  (0, HALF_HEIGHT, WIDTH, HEIGHT))

        ray_casting(screen, player.pos, player.angle)
        #
        # pygame.draw.circle(screen, GREEN, player.pos, 10)
        # pygame.draw.line(screen, GREEN, player.pos, (player.x + WIDTH * math.cos(player.angle),
        #                                              player.y + HEIGHT * math.sin(player.angle)))
        # for x, y in  world_map:
        #     pygame.draw.rect(screen, DARKGREY, (x, y, TILE, TILE), 2)

        pygame.display.update()
        clock.tick(FPS)


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    player = Player()
    run()

