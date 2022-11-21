import sys
from InstanceModel.spr_platform import *
from InstanceModel.spr_camera import *
from InstanceModel.spr_player import *
import GlobalVariable.game_setting as gb_setting
import GlobalVariable.sprite_group as gb_spr


class MainPygameWindow:
    def __init__(self):
        pygame.init()
        self.FramePerSec = pygame.time.Clock()

        self.display_surface = pygame.display.set_mode((gb_setting.WIDTH, gb_setting.HEIGHT))
        pygame.display.set_caption("Emotional Platformer")

        self.P1 = Player()
        self.env = gb_spr.env_sprites

        # load stage
        self.map = TileMap(gb_setting.ROOT_PATH + "/StageData/stage_test.csv")
        self.P1.rect.x, self.P1.rect.y = self.map.start_x, self.map.start_y

        self.camera = Camera(self.P1)
        self.follow = Follow(self.camera, self.P1)
        self.border = Border(self.camera, self.P1)
        self.auto = Auto(self.camera, self.P1)
        self.camera.setmethod(self.border)

    def main_loop(self):
        self.P1.move()
        self.P1.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        self.display_surface.fill((0, 0, 0))

        self.camera.scroll()
        for entity in gb_spr.all_sprites:
            self.display_surface.blit(entity.surf, entity.rect)

        self.display_surface.blit(self.env.surf, (self.env.surf.rect.x - self.camera.offset.x, self.env.surf.rect.y -
                                                  self.camera.offset.y))
        self.display_surface.blit(self.P1.surf, (self.P1.rect.x - self.camera.offset.x, self.P1.rect.y -
                                                 self.camera.offset.y))

        pygame.display.update()
        self.FramePerSec.tick(gb_setting.FPS)
