import pygame as pg
import Button
from Scene import *


class Building:
    def __init__(self, game_scene, state, y, x):
        self.game_scene = game_scene
        self.state = state
        self.x = x
        self.y = y

    def handle_events(self):
        pass

    def update(self):
        pass

    def draw(self, grid_surface):
        pass


class Demolition(Building):
    def __init__(self, game_scene, state, x, y):
        super().__init__(game_scene, state, x, y)
        self.grid_image_ground = pg.image.load("../Simcity/image/Ground.png")

    def handle_events(self):
        pass

    def update(self):
        pass

    def draw(self, grid_surface):
        grid_surface.blit(self.grid_image_ground, (self.x, self.y))


class PowerLines(Building):
    def __init__(self, game_scene, state, x, y):
        super().__init__(game_scene, state, x, y)
        self.power_lines = pg.image.load("./image/Building/1.png")

    def handle_events(self):
        pass

    def update(self):
        pass

    def draw(self, grid_surface):
        grid_surface.blit(self.power_lines, (self.x, self.y))


class Park(Building):
    def __init__(self, game_scene, state, x, y):
        super().__init__(game_scene, state, x, y)
        self.park = pg.image.load("./image/Building/2.png")

    def handle_events(self):
        pass

    def update(self):
        pass

    def draw(self, grid_surface):
        grid_surface.blit(self.park, (self.x, self.y))


class Commercial(Building):
    def __init__(self, game_scene, state, x, y):
        super().__init__(game_scene, state, x, y)
        self.commercial = pg.image.load("./image/Building/3.png")

    def handle_events(self):
        pass

    def update(self):
        pass

    def draw(self, grid_surface):
        grid_surface.blit(self.commercial, (self.x, self.y))


class PoliceStation(Building):
    def __init__(self, game_scene, state, x, y):
        super().__init__(game_scene, state, x, y)
        self.police_station = pg.image.load("./image/Building/4.png")

    def handle_events(self):
        pass

    def update(self):
        pass

    def draw(self, grid_surface):
        grid_surface.blit(self.police_station, (self.x, self.y))


class Stadium(Building):
    def __init__(self, game_scene, state, x, y):
        super().__init__(game_scene, state, x, y)
        self.stadium = pg.image.load("./image/Building/5.png")

    def handle_events(self):
        pass

    def update(self):
        pass

    def draw(self, grid_surface):
        grid_surface.blit(self.stadium, (self.x, self.y))


class ShipPort(Building):
    def __init__(self, game_scene, state, x, y):
        super().__init__(game_scene, state, x, y)
        self.ship_port = pg.image.load("./image/Building/6.png")

    def handle_events(self):
        pass

    def update(self):
        pass

    def draw(self, grid_surface):
        grid_surface.blit(self.ship_port, (self.x, self.y))


class Road(Building):
    def __init__(self, game_scene, state, x, y):
        super().__init__(game_scene, state, x, y)
        self.road = pg.image.load("./image/Building/7.png")

    def handle_events(self):
        pass

    def update(self):
        pass

    def draw(self, grid_surface):
        grid_surface.blit(self.road, (self.x, self.y))


class Railroad(Building):
    def __init__(self, game_scene, state, x, y):
        super().__init__(game_scene, state, x, y)
        self.railroad = pg.image.load("./image/Building/8.png")

    def handle_events(self):
        pass

    def update(self):
        pass

    def draw(self, grid_surface):
        grid_surface.blit(self.railroad, (self.x, self.y))


class Residential(Building):
    def __init__(self, game_scene, state, x, y):
        super().__init__(game_scene, state, x, y)
        self.residential = pg.image.load("./image/Building/9.png")

    def handle_events(self):
        pass

    def update(self):
        pass

    def draw(self, grid_surface):
        grid_surface.blit(self.residential, (self.x, self.y))


class Industrial(Building):
    def __init__(self, game_scene, state, x, y):
        super().__init__(game_scene, state, x, y)
        self.industrial = pg.image.load("./image/Building/10.png")

    def handle_events(self):
        pass

    def update(self):
        pass

    def draw(self, grid_surface):
        grid_surface.blit(self.industrial, (self.x, self.y))


class FireStation(Building):
    def __init__(self, game_scene, state, x, y):
        super().__init__(game_scene, state, x, y)
        self.fire_station = pg.image.load("./image/Building/11.png")

    def handle_events(self):
        pass

    def update(self):
        pass

    def draw(self, grid_surface):
        grid_surface.blit(self.fire_station, (self.x, self.y))


class PowerPlant(Building):
    def __init__(self, game_scene, state, x, y):
        super().__init__(game_scene, state, x, y)
        self.power_plant = pg.image.load("./image/Building/12.png")

    def handle_events(self):
        pass

    def update(self):
        pass

    def draw(self, grid_surface):
        grid_surface.blit(self.power_plant, (self.x, self.y))


class Airport(Building):
    def __init__(self, game_scene, state, x, y):
        super().__init__(game_scene, state, x, y)
        self.airport = pg.image.load("./image/Building/13.png")

    def handle_events(self):
        pass

    def update(self):
        pass

    def draw(self, grid_surface):
        grid_surface.blit(self.airport, (self.x, self.y))
