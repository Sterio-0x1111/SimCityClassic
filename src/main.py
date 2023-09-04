import pygame as pg
import json
import Scene


class Game:
    def __init__(self):
        pg.init()

        # Da das Spiel auf dieser Einstellung läuft
        self.window_width = 1400
        self.window_height = 850
        self.window = pg.display.set_mode((self.window_width, self.window_height), pg.RESIZABLE)
        pg.display.set_caption("SimCity")
        icon = pg.image.load("../image/Sim_City_logo.png").convert_alpha()
        pg.display.set_icon(icon)

        with open("../controls/controls.json", "r") as json_controls:
            self.controls = json.load(json_controls)

        self.scene = Scene.MainMenuScene(self)

        self.run()

    def run(self):
        self.scene.run()
        pg.quit()


game = Game()
