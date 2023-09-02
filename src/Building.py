import pygame as pg
import random
import Button
from Scene import *


class Building:
    def __init__(self, game_scene, state):
        self.game_scene = game_scene
        self.state = state
        self.count = 0

    def handle_events(self):
        self.count = self.count - 1

    def update(self):
        self.count += 1

    def draw(self, grid_surface, x, y):
        pass


class Demolition(Building):
    def __init__(self, game_scene, state):
        super().__init__(game_scene, state)
        self.grid_image_ground = pg.image.load("../Simcity/image/Ground.png").convert()

    def handle_events(self):
        pass

    def update(self):
        pass

    def draw(self, grid_surface, x, y):
        grid_surface.blit(self.grid_image_ground, (x, y))


class PowerLines(Building):
    def __init__(self, game_scene, state):
        super().__init__(game_scene, state)
        self.power_lines = pg.image.load("../Simcity/image/Building/1.png").convert()

    def handle_events(self):
        pass

    def update(self):
        pass

    def draw(self, grid_surface, x, y):
        grid_surface.blit(self.power_lines, (x, y))


class Park(Building):
    def __init__(self, game_scene, state, count):
        super().__init__(game_scene, state)
        self.park = pg.image.load("../Simcity/image/Building/2.png").convert()
        self.count = count

    def handle_events(self):
        super().handle_events()

    def update(self):
        super().update()

    def draw(self, grid_surface, x, y):
        grid_surface.blit(self.park, (x, y))


class Commercial(Building):
    def __init__(self, game_scene, state, count):
        super().__init__(game_scene, state)
        self.commercial = pg.image.load("../Simcity/image/Building/3.png").convert()
        self.count = count

    def handle_events(self):
        super().handle_events()

    def update(self):
        super().update()

    def draw(self, grid_surface, x, y):
        grid_surface.blit(self.commercial, (x, y))


class PoliceStation(Building):
    def __init__(self, game_scene, state, count):
        super().__init__(game_scene, state)
        self.police_station = pg.image.load("../Simcity/image/Building/4.png").convert()
        self.count = count

    def handle_events(self):
        super().handle_events()

    def update(self):
        super().update()

    def draw(self, grid_surface, x, y):
        grid_surface.blit(self.police_station, (x, y))


class Stadium(Building):
    def __init__(self, game_scene, state, count):
        super().__init__(game_scene, state)
        self.stadium = pg.image.load("../Simcity/image/Building/5.png").convert()
        self.count = count

    def handle_events(self):
        super().handle_events()

    def update(self):
        super().update()

    def draw(self, grid_surface, x, y):
        grid_surface.blit(self.stadium, (x, y))


class ShipPort(Building):
    def __init__(self, game_scene, state, count):
        super().__init__(game_scene, state)
        self.ship_port = pg.image.load("../Simcity/image/Building/6.png").convert()
        self.count = count

    def handle_events(self):
        super().handle_events()

    def update(self):
        super().update()

    def draw(self, grid_surface, x, y):
        grid_surface.blit(self.ship_port, (x, y))


class Road(Building):
    def __init__(self, game_scene, state, count):
        super().__init__(game_scene, state)
        self.road = pg.image.load("../Simcity/image/Building/7.png").convert()
        self.count = count

    def handle_events(self):
        super().handle_events()

    def update(self):
        super().update()

    def draw(self, grid_surface, x, y):
        grid_surface.blit(self.road, (x, y))


class Railroad(Building):
    def __init__(self, game_scene, state, count):
        super().__init__(game_scene, state)
        self.railroad = pg.image.load("../Simcity/image/Building/8.png").convert()
        self.count = count

    def handle_events(self):
        super().handle_events()

    def update(self):
        super().update()

    def draw(self, grid_surface, x, y):
        grid_surface.blit(self.railroad, (x, y))


class Residential(Building):
    def __init__(self, game_scene, state, count, population):
        super().__init__(game_scene, state)
        self.residential = pg.image.load("../Simcity/image/Building/9.png").convert()
        self.count = count
        self.population = population
        self.max_population = 0
        self.how_many = 0

    def handle_events(self):
        super().handle_events()

    def event(self):
        # max. 20 Personen pro haushalt (Mehrfamilienhaus)
        self.max_population = self.count * 20
        count = 0
        for i in range(0, self.count + 1):
            count = int(i % 20)
            if int(i % 20) == 0:
                count = 20
        if self.max_population > self.population and self.count != 0:
            self.population = ((self.population + (count * 2)) +
                               int(round(self.how_many * random.uniform(0.90, 1.50))))
        else:
            self.population = self.max_population
            self.how_many = 0
        return self.population

    def update(self):
        super().update()
        self.population += 1
        self.how_many += 1

    def draw(self, grid_surface, x, y):
        grid_surface.blit(self.residential, (x, y))


class Industrial(Building):
    def __init__(self, game_scene, state, count):
        super().__init__(game_scene, state)
        self.industrial = pg.image.load("../Simcity/image/Building/10.png").convert()
        self.count = count

    def handle_events(self):
        super().handle_events()

    def update(self):
        super().update()

    def draw(self, grid_surface, x, y):
        grid_surface.blit(self.industrial, (x, y))


class FireStation(Building):
    def __init__(self, game_scene, state, count):
        super().__init__(game_scene, state)
        self.fire_station = pg.image.load("../Simcity/image/Building/11.png").convert()
        self.count = count

    def handle_events(self):
        super().handle_events()

    def update(self):
        super().update()

    def draw(self, grid_surface, x, y):
        grid_surface.blit(self.fire_station, (x, y))


class PowerPlant(Building):
    def __init__(self, game_scene, state, count):
        super().__init__(game_scene, state)
        self.power_plant = pg.image.load("../Simcity/image/Building/12.png").convert()
        self.count = count

    def handle_events(self):
        super().handle_events()

    def update(self):
        super().update()

    def draw(self, grid_surface, x, y):
        grid_surface.blit(self.power_plant, (x, y))


class Airport(Building):
    def __init__(self, game_scene, state, count):
        super().__init__(game_scene, state)
        self.airport = pg.image.load("../Simcity/image/Building/13.png").convert()
        self.count = count

    def handle_events(self):
        super().handle_events()

    def update(self):
        super().update()

    def draw(self, grid_surface, x, y):
        grid_surface.blit(self.airport, (x, y))
