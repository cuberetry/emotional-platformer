from InstanceModel import spr_tilemap as tm
import GlobalVariable.game_setting as gb_setting


class BoundaryMap(tm.TileMap):
    def __init__(self, filename):
        super().__init__(filename)

        self.left_border_x, self.right_border_x = -10, tm.TileMap(filename).map_w
        self.top_border_y, self.bottom_border_y = 0, 50


class Boundary:
    def __init__(self, player, boundary):
        self.player = player
        self.boundary = boundary

    def line(self):
        print(self.player.pos.y)
        # print(self.player.pos.x)
        if self.player.pos.x > self.boundary.right_border_x:
            self.player.pos.x = 0
        if self.player.pos.x < 0:
            self.player.pos.x = self.boundary.right_border_x
        if self.player.pos.y > self.boundary.bottom_border_y:
            self.player.pos.x = 0
            self.player.pos.y = -10
