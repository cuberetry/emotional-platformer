import pygame_menu as pgm
from GlobalVariable import game_var as gb_var
from GlobalVariable import game_setting as gb_setting


class PauseMenu:
    def __init__(self):
        self.is_activated = True
        self.menu = pgm.Menu('Pause Menu', gb_setting.WIDTH, gb_setting.HEIGHT, theme=pgm.themes.THEME_DARK)
        self.menu.add.button('Continue', self.game_continue)
        self.menu.add.button('Restart Stage', self.game_restart)
        self.menu.add.button('Select Stage', self.game_stage)
        self.menu.add.button('Quit', pgm.events.EXIT)
        self.menu.disable()

    def activate_menu(self):
        gb_var.IS_PAUSING = True
        self.is_activated = True
        self.menu.enable()

    def mainloop(self):
        if self.is_activated:
            self.menu.mainloop(gb_var.SURFACE, disable_loop=True)
        else:
            gb_var.STAGE_SELECT.menu.mainloop(gb_var.SURFACE, disable_loop=True)

    def game_continue(self):
        gb_var.IS_PAUSING = False
        self.menu.disable()

    def game_restart(self):
        gb_var.IS_PAUSING = False
        self.menu.disable()
        gb_var.CUR_SCENE.restart()

    def game_stage(self):
        self.is_activated = False
        self.menu.disable()
        gb_var.STAGE_SELECT.prev_menu = self
        gb_var.STAGE_SELECT.activate_menu()
