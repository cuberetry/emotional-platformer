import GlobalVariable.sprite_group as gb_spr
import GlobalVariable.game_var as gb_var
import InstanceModel.Platform.spr_platform as platform_model


class HapPlatform(platform_model.Platform):
    def __init__(self, x, y):
        super().__init__(x, y)
        gb_spr.hap_sprites.add(self)

        self.surf.fill(gb_var.PLATFORM_STATE_COLOR['hp'])
