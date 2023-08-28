import pygame as pg
import Scene


class Game:
    def __init__(self):
        pg.init()

        self.window_width = 1200
        self.window_height = 700
        self.window = pg.display.set_mode((self.window_width, self.window_height), pg.RESIZABLE)
        pg.display.set_caption("SimCity")
        self.scene = Scene.MainMenuScene(self)

        self.run()

    def run(self):
        '''
        self.delta_time = self.clock.tick(60) / 1000
        self.press = pg.key.get_pressed()

        speed = 900
        if self.press[pg.K_RIGHT]:
            player_x += speed * self.delta_time
        elif self.press[pg.K_LEFT]:
            player_x -= speed * self.delta_time

        if self.press[pg.K_DOWN]:
            player_y += speed * self.delta_time
        elif self.press[pg.K_UP]:
            player_y -= speed * self.delta_time

        pg.draw.rect(self.window, (0, 0, 0), (player_x, player_y, width, height))
        print(f"x: {player_x} y:  {player_y}")

        pg.display.update()
        '''

        self.scene.run()
        pg.quit()


game = Game()
