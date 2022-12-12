from InstanceModel.System import spr_tilemap as tm
import GlobalVariable.game_setting as gb_setting


class BoundaryMap(tm.TileMap):
    def __init__(self, filename):
        super().__init__(filename)

        self.left_border_x, self.right_border_x = 0, tm.TileMap(filename).map_w-20
        self.top_border_y, self.bottom_border_y = 0, gb_setting.HEIGHT


class Boundary:
    def __init__(self, player, boundary):
        self.player = player
        self.boundary = boundary

    def line(self):
        if self.player.rect.x >= self.boundary.right_border_x:
            self.player.rect.x = self.boundary.right_border_x
            print("case1")
        elif self.player.rect.x <= self.boundary.left_border_x:
            self.player.rect.x = 0
            print('case2')
        if self.player.rect.y >= self.boundary.bottom_border_y:
            self.player.player_kill()
