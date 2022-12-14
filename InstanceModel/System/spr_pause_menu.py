import pygame_menu as pgm
from GlobalVariable import game_var as gb_var
from GlobalVariable import game_setting as gb_setting


class PauseMenu:
    def __init__(self):
        self.menu = pgm.Menu('Pause Menu', gb_setting.WIDTH, gb_setting.HEIGHT, theme=pgm.themes.THEME_DARK)
        self.menu.add.button('Continue', self.game_continue)
        self.menu.add.button('Restart Stage', self.game_restart)
        self.menu.add.button('Quit', pgm.events.EXIT)
        self.menu.disable()

    def activate_menu(self):
        gb_var.IS_PAUSING = True
        self.menu.enable()

    def render_menu(self):
        self.menu.mainloop(gb_var.SURFACE, disable_loop=True)

    def game_continue(self):
        gb_var.IS_PAUSING = False
        self.menu.disable()

    def game_restart(self):
        gb_var.IS_PAUSING = False
        self.menu.disable()
        gb_var.CUR_SCENE.restart()

    def is_activated(self):
        return self.menu.is_enabled()
