import sys
from InstanceModel.spr_platform import *
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

        # load stage
        self.map = TileMap('stage_test.csv')
        self.P1.rect.x, self.P1.rect.y = self.map.start_x, self.map.start_y

    def main_loop(self):
        self.P1.move()
        self.P1.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        self.display_surface.fill((0, 0, 0))

        for entity in gb_spr.all_sprites:
            self.display_surface.blit(entity.surf, entity.rect)
        pygame.display.update()
        self.FramePerSec.tick(gb_setting.FPS)
