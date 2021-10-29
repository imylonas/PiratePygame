import pygame
from tiles import Tile

class Level:
    def __init__(self,level_data,surface):
        self.display_surface =surface
        self.setup_level(level_data)

    def setup_level(self,layout):
        self.tiles = pygame.sprite.Group()
        for row_index,row in enumerate(layout):
            print(row_index)
            print(row)

    def run(self):
        self.tiles.draw(self.display_surface)