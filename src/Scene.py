import pygame as pg
import json
import Button


class Scene:
    def __init__(self, game):
        self.game = game
        self.screen = game.window
        self.controls = game.controls
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
        self.background = pg.image.load("./image/Mainmenu.png")

        self.b1 = pg.image.load("./image/START_NEW_CITY.png")
        self.button_play = Button.Button(game.window, 134, 358.5, self.b1, 1.0)

        self.b2 = pg.image.load("./image/LOAD_A_CITY.png")
        self.button_load = Button.Button(game.window, 595, 363, self.b2, 1.0)

        self.b3 = pg.image.load("./image/Settings.png")
        self.button_Settings = Button.Button(game.window, 370, 460, self.b3, 1.0)

    def handle_events(self):
        super().handle_events()
        if self.button_play.push():
            self.running = False
            game_scene = GameScene(self.game)
            game_scene.run()

        elif self.button_load.push():
            self.running = False
            # folgt

        elif self.button_Settings.push():
            self.running = False
            settings_scene = SettingsScene(self.game)
            settings_scene.run()

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.button_play.draw()
        self.button_load.draw()
        self.button_Settings.draw()


class SettingsScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.background = pg.image.load("./image/Mainmenu.png")
        self.font = pg.font.SysFont(None, 55)

        self.b4 = pg.image.load("./image/Back.png")
        self.button_back = Button.Button(self.game.window, 134, 540, self.b4, 1.0)

        self.b5 = pg.image.load("./image/Default.png")
        self.button_default = Button.Button(self.game.window, 600, 540, self.b5, 1.0)

        # Buttons für Einstellungen
        self.up = pg.image.load("./image/Up.png")
        self.button_up = Button.Button(self.game.window, 134, 358.5, self.up, 1.0)
        self.key_up = self.font.render(self.controls[1]["manually"]["map_move_up"], True, (255, 255, 255))

        self.down = pg.image.load("./image/Down.png")
        self.button_down = Button.Button(self.game.window, 134, 450, self.down, 1.0)
        self.key_down = self.font.render(self.controls[1]["manually"]["map_move_down"], True, (255, 255, 255))

        self.left = pg.image.load("./image/Left.png")
        self.button_left = Button.Button(self.game.window, 600, 358.5, self.left, 1.0)
        self.key_left = self.font.render(self.controls[1]["manually"]["map_move_left"], True, (255, 255, 255))

        self.right = pg.image.load("./image/Right.png")
        self.button_right = Button.Button(self.game.window, 600, 450, self.right, 1.0)
        self.key_right = self.font.render(self.controls[1]["manually"]["map_move_right"], True, (255, 255, 255))

    def handle_events(self):
        super().handle_events()
        if self.button_back.push():
            self.running = False  # Beende die aktuelle Szene
            main_menu_scene = MainMenuScene(self.game)
            main_menu_scene.run()

        if self.button_default.push():
            for control_name, key in self.controls[0]["default"].items():
                self.controls[1]["manually"][control_name] = key
            self.update(True)

        if self.button_up.push():
            new_key = self.get_user_input()  # Benutzereingabe erfassen
            self.update_control("map_move_up", new_key)  # Tastenzuordnung aktualisieren

        if self.button_down.push():
            new_key = self.get_user_input()
            self.update_control("map_move_down", new_key)

        if self.button_left.push():
            new_key = self.get_user_input()
            self.update_control("map_move_left", new_key)

        if self.button_right.push():
            new_key = self.get_user_input()
            self.update_control("map_move_right", new_key)

    def get_user_input(self):
        user_input = ""
        input_complete = False

        while not input_complete:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.unicode:  # Ignoriert Tasten ohne Unicode
                        user_input = event.unicode
                        input_complete = True
        return user_input

    def update_control(self, control_name, new_key):
        self.controls[1]["manually"][control_name] = new_key
        self.update(True)

    def update(self, new_key=False):
        # Aktualisierung der Einstellungen hier
        super().handle_events()
        if new_key:
            with open("./controls/controls.json", "w") as json_file:
                json.dump(self.controls, json_file, indent=4)
            self.key_up = self.font.render(self.controls[1]["manually"]["map_move_up"], True, (255, 255, 255))
            self.key_down = self.font.render(self.controls[1]["manually"]["map_move_down"], True, (255, 255, 255))
            self.key_left = self.font.render(self.controls[1]["manually"]["map_move_left"], True, (255, 255, 255))
            self.key_right = self.font.render(self.controls[1]["manually"]["map_move_right"], True, (255, 255, 255))

    def draw(self):
        self.screen.blit(self.background, (0, 0))

        # Zeichnen der UI-Elemente für die Einstellungsszene hier
        self.button_back.draw()
        self.button_default.draw()

        self.button_up.draw()
        self.screen.blit(self.key_up, (445, 385))

        self.button_down.draw()
        self.screen.blit(self.key_down, (445, 478))

        self.button_left.draw()
        self.screen.blit(self.key_left, (930, 385))

        self.button_right.draw()
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
        self.window_width = 1400
        self.window_height = 850

        self.window = pg.display.set_mode((self.window_width, self.window_height))

        self.top_menu = pg.image.load("./image/Topmenu.png")

    def handle_events(self):
        super().handle_events()


    def update(self):
        super().handle_events()

    def draw(self):
        self.screen.blit(self.top_menu, (0, 0))
