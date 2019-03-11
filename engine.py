import pygame, sys
from pygame.locals import *

from map.tile import *
from render import render_map

pygame.init()

pygame.font.init()

SCREENWIDTH = 800
SCREENHEIGHT = 600

# Create a new drawing surface (window), width=300 height=300
DISPLAYSURF = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption("Isometric!")


while True:

    # Get all user events
    for event in pygame.event.get():
        # if the user wants to quit
        if event.type == QUIT:
            #end the game and close the window
            pygame.quit()
            sys.exit()
    
    render_map(DISPLAYSURF, tilemap, colors, SCREENWIDTH, SCREENHEIGHT, MAPWIDTH, MAPHEIGHT, TILESIZE)
    # Update the display
    pygame.display.update()