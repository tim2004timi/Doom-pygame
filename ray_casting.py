import pygame
from settings import *
from map import world_map


def ray_casting(screen, pos, angle):
    cur_angle = angle - HALF_FOV
    xo, yo = pos
    for ray in range(NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)
        for depth in range(MAX_DEPTH):
            depth *= math.cos(angle - cur_angle)
            x = xo + depth * cos_a
            y = yo + depth * sin_a
            # pygame.draw.line(screen, DARKGREY, pos, (x, y), 2)
            if (x // TILE * TILE, y // TILE * TILE) in world_map:
                c = 200 / (1 + depth ** 1.7 * 0.00005)
                color = (c / 2, c, c / 2)
                proj_height = PROJ_COFF / depth
                pygame.draw.rect(screen, color, (ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height))
                break
        cur_angle += DELTA_ANGLE
