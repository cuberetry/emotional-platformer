import GlobalVariable.sprite_group as gb_spr
import GlobalVariable.game_var as gb_var
from InstanceModel import spr_platform
from GlobalVariable import sprite_group

class FirePlatform(Platform):
    def __init__(self, x, y):
        super().__init__(x, y)
        gb_spr.fire_sprites.add(self)

        self.surf.fill(gb_var.PLATFORM_STATE_COLOR['ap'])
