from InstanceModel.spr_player import *
import GlobalVariable.game_var as gb_var
import GlobalVariable.game_setting as gb_setting
import GlobalVariable.sprite_group as gb_spr
from InstanceModel import spr_tilemap as tm
import time


class Boundary(tm.TileMap):
    def __init__(self, filename):
        super().__init__(filename)

        self.left_border, self.right_border = -50, tm.TileMap(filename).map_w
        self.top_border_y, self.bottom_border_y = 0, 400


class SetB:
    def __init__(self, player, boundary):
        self.player = player
        self.boundary = boundary


class MakeB(SetB):
    def __init(self, player, boundary):
        SetB.__init__(self, player, boundary)

    def line(self):
        print(self.player.pos.y)
        if self.player.pos.x > self.boundary.right_border:
            self.player.pos.x = 0
        if self.player.pos.x < 0:
            self.player.pos.x = self.boundary.right_border
        if self.player.pos.y < self.boundary.bottom_border_y:
            self.player.pos.y = 0


