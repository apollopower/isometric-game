TILESIZE = 40
MAPWIDTH = 5
MAPHEIGHT = 5

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
    GRASS: GREEN,
    WATER: BLUE,
    COAL: BLACK
}

# A list representing a tilemap

tilemap = [
    [GRASS, GRASS, DIRT, DIRT, DIRT],
    [GRASS, WATER, WATER, DIRT, DIRT],
    [GRASS, COAL, DIRT, DIRT, DIRT],
    [GRASS, GRASS, GRASS, DIRT, DIRT],
    [GRASS, WATER, WATER, DIRT, DIRT]
]