import sys
from InstanceModel.spr_platform import *
from InstanceModel.spr_camera import *
from InstanceModel.spr_player import *
import GlobalVariable.game_setting as gb_setting
import GlobalVariable.sprite_group as gb_spr


class Scene:
    def __init__(self):
        self.P1 = Player()

        # load stage
        self.map = TileMap(gb_setting.ROOT_PATH + "/StageData/stage_test.csv")
        self.P1.rect.x, self.P1.rect.y = self.map.start_x, self.map.start_y

        self.camera = Camera(self.P1)
        self.follow = Follow(self.camera, self.P1)
        self.border = Border(self.camera, self.P1)
        self.auto = Auto(self.camera, self.P1)
        self.camera.setmethod(self.border)

    def mainloop(self):
        self.P1.move()
        self.P1.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        gb_var.SURFACE.fill((0, 0, 0))

        self.camera.scroll()
        for env in gb_spr.env_sprites:
            gb_var.SURFACE.blit(env.surf, (env.rect.x - self.camera.offset.x, env.rect.y - self.camera.offset.y))
        for player in gb_spr.player_sprites:
            gb_var.SURFACE.blit(player.surf, (player.rect.x - self.camera.offset.x, player.rect.y - self.camera.offset.y))

        pygame.display.update()
        gb_var.FPS.tick(gb_setting.MAXFPS)
