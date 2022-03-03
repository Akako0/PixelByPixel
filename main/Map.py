import pygame
from tiles import Tile
from setings import Json, tile_size

class Map:
    def __init__(self, map_data, surface):
        self.direction = pygame.math.Vector2(0,0)
        self.display_surface = surface
        self.setup_map(map_data)
    
    def setup_map(self, layout):
        print("start")
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        print("setup map")
        for player_index, player in enumerate(layout.keys()):
            tile = Tile((player[0] * Json.chunck_size * tile_size, player[1] * Json.chunck_size * tile_size), list(layout.values())[player_index])
            self.tiles.add(tile)

    def run(self):
        # map
        self.tiles.update()
        self.tiles.draw(self.display_surface)