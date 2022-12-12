import pygame
import csv
import os
import InstanceModel.Platform.spr_platform as platform
import InstanceModel.Platform.spr_neutral_platform as neu_p
import InstanceModel.Platform.spr_happy_platform as hap_p
import InstanceModel.Platform.spr_fire_platform as fire_p
import InstanceModel.Platform.spr_ice_platform as ice_p
import InstanceModel.Environment.spr_checkpoint as cp
import InstanceModel.Environment.spr_enemy as em
import InstanceModel.Environment.spr_goal as goal


class TileMap:
    def __init__(self, filename):
        self.tile_size = 16
        self.start_x, self.start_y = 0, 0
        self.map_h, self.map_w = None, None

        self.tiles = self.load_tiles(filename)
        self.map_surface = pygame.Surface((self.map_w, self.map_h))
        self.map_surface.set_colorkey((0, 0, 0))
        self.load_map()

    def load_map(self):
        for tile in self.tiles:
            tile.draw(self.map_surface)

    def load_tiles(self, filename):
        tiles = []
        map_grid = []
        with open(os.path.join(filename)) as data:
            data = csv.reader(data, delimiter=',')
            for row in data:
                map_grid.append(list(row))
        x, y = 0, 0
        for row in map_grid:
            x = 0
            for tile in row:
                if tile == '1':
                    tiles.append(platform.Platform(x * self.tile_size, y * self.tile_size))
                elif tile == '2':
                    tiles.append(neu_p.NeuPlatform(x * self.tile_size, y * self.tile_size))
                elif tile == '3':
                    tiles.append(hap_p.HapPlatform(x * self.tile_size, y * self.tile_size))
                elif tile == '4':
                    tiles.append(fire_p.FirePlatform(x * self.tile_size, y * self.tile_size))
                elif tile == '5':
                    tiles.append(ice_p.IcePlatform(x * self.tile_size, y * self.tile_size))
                elif tile == '6':
                    tiles.append(em.Enemy(x * self.tile_size, y * self.tile_size))
                elif tile == '7':
                    tiles.append(cp.Checkpoint(x * self.tile_size, y * self.tile_size))
                elif tile == '8':
                    tiles.append(goal.Goal(x * self.tile_size, y * self.tile_size))

                x += 1

            # Move to next row
            y += 1
            # Store the size of the tile mapp
        self.map_w, self.map_h = x * self.tile_size, y * self.tile_size
        return tiles
