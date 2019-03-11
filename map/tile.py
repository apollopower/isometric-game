import pygame
from pygame.locals import *

TILESIZE = 40
MAPWIDTH = 6
MAPHEIGHT = 6

DIRT = 0
GRASS = 1
WATER = 2
COAL = 3

BLACK = (0, 0, 0)
BROWN = (153, 26, 0) 
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

colors = {
    DIRT: BROWN,
    GRASS: pygame.image.load('./assets/grass.png'),
    WATER: BLUE,
    COAL: BLACK
}

# A list representing a tilemap

tilemap = [
    [GRASS, GRASS, GRASS, GRASS, GRASS, GRASS],
    [GRASS, GRASS, GRASS, GRASS, GRASS, GRASS],
    [GRASS, GRASS, GRASS, GRASS, GRASS, GRASS],
    [GRASS, GRASS, GRASS, GRASS, GRASS, GRASS],
    [GRASS, GRASS, GRASS, GRASS, GRASS, GRASS],
    [GRASS, GRASS, GRASS, GRASS, GRASS, GRASS]
]