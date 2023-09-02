import pygame as pg
import json
import Scene


class Game:
    def __init__(self):
        pg.init()

        self.window_width = 1200
        self.window_height = 700
        self.window = pg.display.set_mode((self.window_width, self.window_height), pg.RESIZABLE)
        pg.display.set_caption("SimCity")

        with open("../controls/controls.json", "r") as json_controls:
            self.controls = json.load(json_controls)

        self.scene = Scene.MainMenuScene(self)

        self.run()

    def run(self):
        self.scene.run()
        pg.quit()


game = Game()
