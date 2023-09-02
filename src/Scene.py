import pygame as pg
import json
import Button
import FileSelection
from Building import *
from BuildMode import *
from Budget import *


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
            game_scene = GameScene(self.game, "./map/Field.json", "./setting/Setting.json")
            super().handle_events()
            game_scene.run()

        elif self.button_load.push():
            self.running = False
            file_selection = FileSelection.FileSelection()
            selected_file_path = file_selection.select_json_file()
            if selected_file_path:
                selected_file_path_setting = file_selection.select_json_file()
                if selected_file_path_setting:
                    game_scene = GameScene(self.game, selected_file_path, selected_file_path_setting)
                    super().handle_events()
                    game_scene.run()
                else:
                    pass
            else:
                pass

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
            new_key = self.get_user_input()
            self.update_control("map_move_up", new_key)

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

                    if input_complete:
                        for control_name, key in self.controls[1]["manually"].items():
                            if key == user_input:
                                input_complete = False

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
    def __init__(self, game, game_path_map, game_path_setting):
        super().__init__(game)
        self.game_path_map = game_path_map
        self.game_path_setting = game_path_setting

        self.window_width = 1400
        self.window_height = 850

        self.GRID_SIZE = 200
        self.CELL_SIZE = 30

        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.BLUE = (0, 0, 255)
        self.YELLOW = (255, 255, 0)

        self.window = pg.display.set_mode((self.window_width, self.window_height))

        # Transparente Surface für das Raster
        self.grid_surface = pg.Surface((self.GRID_SIZE * self.CELL_SIZE, self.GRID_SIZE * self.CELL_SIZE))
        self.grid_surface.fill(self.BLACK)

        # Felder initialisieren
        try:
            with open(self.game_path_map, "r") as json_file:
                self.fields = json.load(json_file)
            with open(self.game_path_setting, "r") as json_file:
                self.setting = json.load(json_file)
        except FileNotFoundError:
            # self.fields = [{"state": 0, "x": x * self.CELL_SIZE, "y": y * self.CELL_SIZE}
            # for y in range(self.GRID_SIZE) for x in range(self.GRID_SIZE)]
            print("Error")
            exit()

        self.scroll_x = 150
        self.scroll_y = 100

        self.drawing = False
        self.select_button = False
        self.selected_building_type = None
        self.start_pos = (0, 0)
        self.end_pos = (0, 0)

        self.mouse_x = None
        self.mouse_y = None

        self.key_pressed = pg.key.get_pressed()

        self.top_menu = pg.image.load("./image/Topmenu.png")
        self.top = pg.image.load("./image/Top.png")
        self.left_menu = pg.image.load("./image/Leftmenu.png")
        self.leftbelow = pg.image.load("./image/Leftbelow.png")
        self.bottom = pg.image.load("./image/Bottom.png")

        # Button
        self.font = pg.font.SysFont(None, 33)

        self.building_info = {
            "demolition": {
                "instance": Demolition(self.game, 17),
                "button": Button.Button(self.game.window, 4, 115, pg.image.load("./image/Dummy.png"), 1.0),
                "button_xy": [4, 115],
                "state": 17,
                "cost": 1,
                "text": self.font.render("Demolition: 1€", True, self.BLUE)
            },
            "power_lines": {
                "instance": PowerLines(self.game, 4),
                "button": Button.Button(self.game.window, 4, 198, pg.image.load("./image/Dummy.png"), 1.0),
                "button_xy": [4, 198],
                "state": 4,
                "cost": 5,
                "text": self.font.render("Power lines: 5€", True, self.BLUE)
            },
            "park": {
                "instance": Park(self.game, 5, self.setting[1]["park"]),
                "button": Button.Button(self.game.window, 4, 281, pg.image.load("./image/Dummy.png"), 1.0),
                "button_xy": [4, 281],
                "state": 5,
                "cost": 50,
                "expense": 5,
                "text": self.font.render("Park: 50€, per month: 5€", True, self.BLUE)
            },
            "commercial": {
                "instance": Commercial(self.game, 6, self.setting[1]["commercial"]),
                "button": Button.Button(self.game.window, 4, 363, pg.image.load("./image/Dummy.png"), 1.0),
                "button_xy": [4, 363],
                "state": 6,
                "cost": 150,
                "profit": 10,
                "text": self.font.render("Commercial: 150€, tax: 10€", True, self.BLUE)
            },
            "police_station": {
                "instance": PoliceStation(self.game, 7, self.setting[1]["police_station"]),
                "button": Button.Button(self.game.window, 4, 445, pg.image.load("./image/Dummy.png"), 1.0),
                "button_xy": [4, 445],
                "state": 7,
                "cost": 500,
                "expense": 80,
                "text": self.font.render("Police station: 500€, per month: 80€", True, self.BLUE)
            },
            "stadium": {
                "instance": Stadium(self.game, 8, self.setting[1]["stadium"]),
                "button": Button.Button(self.game.window, 4, 527, pg.image.load("./image/Dummy.png"), 1.0),
                "button_xy": [4, 527],
                "state": 8,
                "cost": 2000,
                "expense": 50,
                "text": self.font.render("Stadium: 2000€, per month: 50€", True, self.BLUE)
            },
            "ship_port": {
                "instance": ShipPort(self.game, 9, self.setting[1]["ship_port"]),
                "button": Button.Button(self.game.window, 4, 610, pg.image.load("./image/Dummy.png"), 1.0),
                "button_xy": [4, 610],
                "state": 9,
                "cost": 3000,
                "expense": 100,
                "text": self.font.render("Ship port: 3000€, per month: 100€", True, self.BLUE)
            },
            "road": {
                "instance": Road(self.game, 10, self.setting[1]["road"]),
                "button": Button.Button(self.game.window, 76, 115, pg.image.load("./image/Dummy.png"), 1.0),
                "button_xy": [76, 115],
                "state": 10,
                "cost": 10,
                "expense": 0.50,
                "text": self.font.render("Road: 10€, per month: 0,50€", True, self.BLUE)
            },
            "railroad": {
                "instance": Railroad(self.game, 11, self.setting[1]["railroad"]),
                "button": Button.Button(self.game.window, 76, 198, pg.image.load("./image/Dummy.png"), 1.0),
                "button_xy": [76, 198],
                "state": 11,
                "cost": 15,
                "expense": 1,
                "text": self.font.render("Railroad: 15€, per month: 1€", True, self.BLUE)
            },
            "residential": {
                "instance": Residential(self.game, 12, self.setting[1]["residential"], self.setting[2]["population"]),
                "button": Button.Button(self.game.window, 76, 281, pg.image.load("./image/Dummy.png"), 1.0),
                "button_xy": [76, 281],
                "state": 12,
                "cost": 100,
                "profit": 0.5,
                "text": self.font.render("Residential: 100€, tax: 0,50€", True, self.BLUE)
            },
            "industrial": {
                "instance": Industrial(self.game, 13, self.setting[1]["industrial"]),
                "button": Button.Button(self.game.window, 76, 363, pg.image.load("./image/Dummy.png"), 1.0),
                "button_xy": [76, 363],
                "state": 13,
                "cost": 200,
                "profit": 20,
                "text": self.font.render("Industrial: 200€, tax: 20€", True, self.BLUE)
            },
            "fire_station": {
                "instance": FireStation(self.game, 14, self.setting[1]["fire_station"]),
                "button": Button.Button(self.game.window, 76, 445, pg.image.load("./image/Dummy.png"), 1.0),
                "button_xy": [76, 445],
                "state": 14,
                "cost": 500,
                "expense": 80,
                "text": self.font.render("Fire station: 500€, per month: 80€", True, self.BLUE)
            },
            "power_plant": {
                "instance": PowerPlant(self.game, 15, self.setting[1]["power_plant"]),
                "button": Button.Button(self.game.window, 76, 527, pg.image.load("./image/Dummy.png"), 1.0),
                "button_xy": [76, 527],
                "state": 15,
                "cost": 5000,
                "expense": 400,
                "text": self.font.render("Power plant: 5000€, per month: 400€", True, self.BLUE)
            },
            "airport": {
                "instance": Airport(self.game, 16, self.setting[1]["airport"]),
                "button": Button.Button(self.game.window, 76, 610, pg.image.load("./image/Dummy.png"), 1.0),
                "button_xy": [76, 610],
                "state": 16,
                "cost": 3000,
                "expense": 100,
                "text": self.font.render("Airport: 3000€, per month: 100€", True, self.BLUE)
            }
        }

        self.budget = Budget(self.screen, self.building_info, self.setting[0]["Budget"])
        self.time = BuildMode(self.screen, self.setting)

        self.grid_image_ground = pg.image.load("../Simcity/image/Ground.png")
        self.grid_image_forest = pg.image.load("../Simcity/image/forest.png")
        self.grid_image_water = pg.image.load("../Simcity/image/Water.png")

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

                # Speichern der Felder in JSON-Datei
                try:
                    with open(self.game_path_map, "w") as json_file:
                        json.dump(self.fields, json_file)
                    with open(self.game_path_setting, "w") as json_file:
                        json.dump(self.setting, json_file)
                except FileNotFoundError:
                    print("Error")
                    exit()

            if event.type == pg.KEYDOWN:
                self.key_pressed = pg.key.get_pressed()

            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                for building_type, info in self.building_info.items():
                    if info["button"].push():
                        if self.select_button and self.selected_building_type == info["state"]:
                            # Deaktiviere die Auswahl
                            self.select_button = False
                        else:
                            # Aktiviere die Auswahl
                            self.select_button = True
                            self.selected_building_type = info["state"]

                self.drawing = True
                self.start_pos = (event.pos[0] - self.scroll_x, event.pos[1] - self.scroll_y)
                self.end_pos = (event.pos[0] - self.scroll_x, event.pos[1] - self.scroll_y)
            elif event.type == pg.MOUSEMOTION and self.drawing:
                self.end_pos = (event.pos[0] - self.scroll_x, event.pos[1] - self.scroll_y)
            elif event.type == pg.MOUSEBUTTONUP and event.button == 1:
                self.drawing = False
                for y in range(min(self.start_pos[1] // self.CELL_SIZE, self.end_pos[1] // self.CELL_SIZE),
                               max(self.start_pos[1] // self.CELL_SIZE, self.end_pos[1] // self.CELL_SIZE) + 1):
                    for x in range(min(self.start_pos[0] // self.CELL_SIZE, self.end_pos[0] // self.CELL_SIZE),
                                   max(self.start_pos[0] // self.CELL_SIZE, self.end_pos[0] // self.CELL_SIZE) + 1):
                        if 0 <= x < self.GRID_SIZE and 0 <= y < self.GRID_SIZE:
                            idx = y * self.GRID_SIZE + x
                            if self.select_button:
                                if self.selected_building_type:
                                    if self.fields[idx]["state"] != self.selected_building_type:
                                        for i, info in self.building_info.items():
                                            if info["state"] == self.selected_building_type:
                                                if (self.budget.budget - info["cost"]) > 0:
                                                    prev = self.fields[idx]["state"]
                                                    self.fields[idx]["state"] = self.selected_building_type
                                                    self.budget.update(info["cost"])
                                                    if info["state"] in (5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17):
                                                        if info["state"] == 17:
                                                            # vorherigen status ermitteln
                                                            for v, c in self.building_info.items():
                                                                if c["state"] == prev:
                                                                    c["instance"].handle_events()
                                                                    self.setting[1][v] = c["instance"].count
                                                        else:
                                                            info["instance"].update()
                                                            self.setting[1][i] = info["instance"].count

                            # In der Vollversion nicht mehr enthalten
                            if self.key_pressed[pg.K_n]:
                                self.fields[idx]["state"] = 2
                            if self.key_pressed[pg.K_m]:
                                self.fields[idx]["state"] = 3

    def update(self):
        keys = pg.key.get_pressed()
        move_up_key = ord(self.controls[1]["manually"]["map_move_up"])
        move_down_key = ord(self.controls[1]["manually"]["map_move_down"])
        move_left_key = ord(self.controls[1]["manually"]["map_move_left"])
        move_right_key = ord(self.controls[1]["manually"]["map_move_right"])

        if keys[move_up_key]:
            if self.scroll_y < 100:
                self.scroll_y += self.CELL_SIZE
        if keys[move_down_key]:
            # Scroll-Grenzen (dynamisch)
            if self.scroll_y > (-1 * (self.GRID_SIZE * self.CELL_SIZE) + self.window_height) + 40:
                self.scroll_y -= self.CELL_SIZE
        if keys[move_left_key]:
            if self.scroll_x < 150:
                self.scroll_x += self.CELL_SIZE
        if keys[move_right_key]:
            if self.scroll_x > (-1 * (self.GRID_SIZE * self.CELL_SIZE) + self.window_width) + 40:
                self.scroll_x -= self.CELL_SIZE

        # Mausposition abfragen
        self.mouse_x, self.mouse_y = pg.mouse.get_pos()
        self.mouse_x -= self.scroll_x
        self.mouse_y -= self.scroll_y
        self.mouse_x //= self.CELL_SIZE
        self.mouse_y //= self.CELL_SIZE

        for i, data in self.building_info.items():
            if data["state"] == 12:
                self.setting[2]["population"] = data["instance"].population
        self.time.update(self.budget, self.building_info)

    def draw(self):
        # Es wäre sinnvoll, den sichtbaren Bereich zu verwenden, aber der
        # Algorithmus dafür ist mir momentan nicht klar.
        for field in self.fields:
            x = field["x"]
            y = field["y"]
            state = field["state"]

            type = None
            for building, info in self.building_info.items():
                if state == info["state"]:
                    type = info["instance"]
                    break

            if state not in (1, 2, 3, 17):
                type.draw(self.grid_surface, x, y)
            elif state in (1, 17):
                self.grid_surface.blit(self.grid_image_ground, (x, y))
            elif state == 2:
                self.grid_surface.blit(self.grid_image_forest, (x, y))
            elif state == 3:
                self.grid_surface.blit(self.grid_image_water, (x, y))
            else:
                exit()

        # Zeichne blauen Rahmen um das Feld, über das der Mauszeiger schwebt
        if 0 <= self.mouse_x < self.GRID_SIZE and 0 <= self.mouse_y < self.GRID_SIZE:
            pg.draw.rect(self.grid_surface, self.BLUE, (self.mouse_x * self.CELL_SIZE, self.mouse_y *
                         self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE), 2)

        self.window.fill(self.BLACK)
        self.window.blit(self.grid_surface, (self.scroll_x, self.scroll_y))

        self.screen.blit(self.bottom, (150, 795))

        # Button
        for building_type, info in self.building_info.items():
            button = info["button"]
            if self.select_button:
                if self.selected_building_type == info["state"]:
                    text = info["text"]
                    self.screen.blit(text, (155, 800))
            button.draw()

        self.screen.blit(self.top_menu, (0, 0))
        self.screen.blit(self.top, (0, 50))
        self.screen.blit(self.left_menu, (0, 100))
        self.screen.blit(self.leftbelow, (0, 700))

        if self.drawing and self.start_pos and self.end_pos:
            rect_x = min(self.start_pos[0], self.end_pos[0]) + self.scroll_x
            rect_y = min(self.start_pos[1], self.end_pos[1]) + self.scroll_y
            rect_width = abs(self.end_pos[0] - self.start_pos[0])
            rect_height = abs(self.end_pos[1] - self.start_pos[1])
            pg.draw.rect(self.window, self.YELLOW, (rect_x, rect_y, rect_width, rect_height), 3)

        if self.select_button:
            for building_type, info in self.building_info.items():
                if self.selected_building_type == info["state"]:
                    pg.draw.rect(self.window, self.YELLOW, (info["button_xy"][0], info["button_xy"][1], 68, 78), 3)

        year, month, day = self.time.draw()
        self.setting[0]["Time"]["y"] = year
        self.setting[0]["Time"]["m"] = month
        self.setting[0]["Time"]["d"] = day

        self.setting[0]["Budget"] = self.budget.draw()
