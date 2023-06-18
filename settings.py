import math


# game settings
WIDTH = 1200
HEIGHT = 800
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 60
TILE = 100

# player settings
player_pos = (HALF_WIDTH, HALF_HEIGHT)
player_angle = 0
player_speed = 4
angle_speed = 0.04

# ray casting settings
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 120
MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COFF = DIST * TILE * 3
SCALE = WIDTH // NUM_RAYS

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (220, 0, 0)
GREEN = (0 , 220, 0)
BLUE = (0, 0, 220)
DARKGREY = (100, 100, 100)
