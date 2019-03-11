import pygame
from pygame.locals import *

def render_map(DISPLAYSURF, tilemap, colors, SCREENWIDTH, SCREENHEIGHT, MAPWIDTH, MAPHEIGHT, TILESIZE):
    start_X = (SCREENWIDTH / 2) - (MAPWIDTH / 2)
    start_Y = (SCREENHEIGHT / 2) - (MAPHEIGHT / 2)
    for row in range(MAPHEIGHT):
        for col in range(MAPWIDTH):
            dist_X = start_X + (row * TILESIZE)
            dist_Y = start_Y + (col * TILESIZE)
            current_tile = tilemap[row][col]
            pygame.draw.rect(DISPLAYSURF, colors[current_tile], (dist_Y, dist_X, TILESIZE, TILESIZE))