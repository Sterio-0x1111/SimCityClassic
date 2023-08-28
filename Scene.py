import pygame as pg
import Button


class Scene:
    def __init__(self, game):
        self.game = game
        self.screen = game.window
        self.clock = pg.time.Clock()
        self.running = True

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

    def run(self):
        while self.running:
            self.clock.tick(60)
            self.handle_events()
            self.update()
            self.draw()
            pg.display.flip()

    def update(self):
        pass

    def draw(self):
        pass


class MainMenuScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.background = pg.image.load("image/Mainmenu.png")

        self.b1 = pg.image.load("image/START_NEW_CITY.png")
        self.button_play = Button.Button(self, 134, 358.5, self.b1, 1.0)

        self.b2 = pg.image.load("image/LOAD_A_CITY.png")
        self.button_load = Button.Button(self, 595, 363, self.b2, 1.0)

        self.b3 = pg.image.load("image/Settings.png")
        self.button_Settings = Button.Button(self, 370, 460, self.b3, 1.0)

    def handle_events(self):
        super().handle_events()
        if self.button_play.clicked:
            pg.time.delay(200)

            self.running = False
            game_scene = GameScene(self.game)
            game_scene.run()
        elif self.button_load.clicked:
            pg.time.delay(200)

            self.running = False
            # folgt
        elif self.button_Settings.clicked:
            pg.time.delay(200)

            self.running = False
            settings_scene = SettingsScene(self.game)
            settings_scene.run()

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.button_play.draw(self.game)
        self.button_load.draw(self.game)
        self.button_Settings.draw(self.game)


class SettingsScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.background = pg.image.load("image/Mainmenu.png")
        font = pg.font.SysFont(None, 55)

        self.b4 = pg.image.load("image/Back.png")
        self.button_back = Button.Button(self.game, 134, 540, self.b4, 1.0)

        # Buttons für Einstellungen
        self.up = pg.image.load("image/Up.png")
        self.button_up = Button.Button(self.game, 134, 358.5, self.up, 1.0)
        self.key_up = font.render("w", True, (255, 255, 255))

        self.down = pg.image.load("image/Down.png")
        self.button_down = Button.Button(self.game, 134, 450, self.down, 1.0)
        self.key_down = font.render("s", True, (255, 255, 255))

        self.left = pg.image.load("image/Left.png")
        self.button_left = Button.Button(self.game, 600, 358.5, self.left, 1.0)
        self.key_left = font.render("a", True, (255, 255, 255))

        self.right = pg.image.load("image/Right.png")
        self.button_right = Button.Button(self.game, 600, 450, self.right, 1.0)
        self.key_right = font.render("d", True, (255, 255, 255))


    def handle_events(self):
        super().handle_events()
        if self.button_back.clicked:
            pg.time.delay(200)  # Intervall von 0.2 Sekunde, da sofortiger Übergang

            self.running = False  # Beende die aktuelle Szene
            main_menu_scene = MainMenuScene(self.game)
            main_menu_scene.run()

    def update(self):
        # Aktualisierung der Einstellungen hier
        super().handle_events()


    def draw(self):
        self.screen.blit(self.background, (0, 0))

        # Zeichnen der UI-Elemente für die Einstellungsszene hier
        self.button_back.draw(self.game)

        self.button_up.draw(self.game)
        self.screen.blit(self.key_up, (445, 385))

        self.button_down.draw(self.game)
        self.screen.blit(self.key_down, (445, 478))

        self.button_left.draw(self.game)
        self.screen.blit(self.key_left, (930, 385))

        self.button_right.draw(self.game)
        self.screen.blit(self.key_right, (930, 478))


'''
Die Klasse sollte eigentlich ausgelagert werden, aber sie funktioniert dann in meiner IDE nicht. (GameScene.py)
Den Fehler habe ich bis heute nicht gefunden.

Traceback (most recent call last):
  File "E:\Studium\Fachbereiche\Skriptsprachen\SimCity\main.py", line 2, in <module>
    import Scene
  File "E:\Studium\Fachbereiche\Skriptsprachen\SimCity\Scene.py", line 3, in <module>
    from GameScene import *
  File "E:\Studium\Fachbereiche\Skriptsprachen\SimCity\GameScene.py", line 5, in <module>
    class GameScene(Scene):
'''
class GameScene(Scene):
    def __init__(self, game):
        super().__init__(game)

    def handle_events(self):
        super().handle_events()

    def update(self):
        super().handle_events()

    def draw(self):
        pass
