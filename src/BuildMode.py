import pygame as pg
import Button
import datetime
from Scene import *
from dateutil.relativedelta import relativedelta

class BuildMode:
    def __init__(self, game_screen, building_settings):
        self.game_screen = game_screen
        self.building = building_settings
        self.current_date = datetime.datetime(self.building[0]["Time"]["y"], self.building[0]["Time"]["m"],
                                              self.building[0]["Time"]["d"])

        self.current_time = 0
        self.last_time = pg.time.get_ticks() - self.building[2]["Time_speed"]
        self.next_event = self.building[2]["Time_speed"]
        self.population = 0
        self.current_electricity = 0
        self.max_electricity = 0
        self.percent_residential = 0
        self.percent_commercial = 0
        self.percent_industrial = 0

    def handle_events(self):
        pass

    def update(self, budget, building_info):
        self.current_time = pg.time.get_ticks()

        if (self.current_time - self.last_time) > self.next_event:
            self.current_date += relativedelta(months=+1)  # Monatlich hochzählen
            self.last_time = self.current_time

            self.population = building_info["residential"]["instance"].event()
            self.max_electricity, self.current_electricity = (building_info["power_plant"]["instance"].
                                                              event(building_info))

            # Nachfrage ausrechnen
            res = building_info["residential"]["instance"].count
            com = building_info["commercial"]["instance"].count
            ind = building_info["industrial"]["instance"].count

            value = res + com + ind
            if res != 0 and com != 0 and ind != 0:
                # Skala (Einwohner)
                weighted_res = (res * (self.population / building_info["residential"]["instance"].max_population))
                self.percent_residential = (weighted_res / value) * 100
                self.percent_commercial = (com / value) * 100
                self.percent_industrial = (ind / value) * 100
            else:
                self.percent_residential = 0
                self.percent_commercial = 0
                self.percent_industrial = 0

            # Berechnung von Benefit
            budget.handle_events()

    def draw(self):
        # Zeichne Balken für Nachfrage nach Wohngebiet, Industrie und Gewerbe
        bar_width = 15
        bar_height = 145

        # Balkenpositionen
        bar_x_residential = 83
        bar_x_commercial = 45
        bar_x_industrial = 118
        bar_y = 700

        if self.percent_residential != 0 and self.percent_commercial != 0 and self.percent_industrial != 0:
            # Balken für Wohngebiet (grün)
            pg.draw.rect(self.game_screen, (0, 255, 0),
                         (bar_x_residential, bar_y, bar_width, bar_height * (self.percent_residential / 100)))

            # Balken für Industrie (rot)
            pg.draw.rect(self.game_screen, (255, 0, 0),
                         (bar_x_industrial, bar_y, bar_width, bar_height * (self.percent_industrial / 100)))

            # Balken für Gewerbe (blau)
            pg.draw.rect(self.game_screen, (0, 0, 255),
                         (bar_x_commercial, bar_y, bar_width, bar_height * (self.percent_commercial / 100)))

        font = pg.font.SysFont(None, 33)

        population = f"Population: {self.population}"
        population = font.render(population, True, (0, 0, 0))
        self.game_screen.blit(population, (365, 65))

        t_day = f"{self.current_date.day:02d}"
        t_month = f" - {self.current_date.month:02d}"
        t_year = f" - {self.current_date.year}"
        time = font.render(t_day, True, (0, 0, 0))
        self.game_screen.blit(time, (1145, 65))
        time = font.render(t_month, True, (0, 0, 0))
        self.game_screen.blit(time, (1165, 65))
        time = font.render(t_year, True, (0, 0, 0))
        self.game_screen.blit(time, (1205, 65))

        data = font.render(self.building[0]["Name"], True, (0, 0, 0))
        self.game_screen.blit(data, (630, 65))

        if self.current_electricity <= self.max_electricity:
            data = font.render(f"Electricity: {self.current_electricity} / {self.max_electricity}", True, (0, 0, 0))
            self.game_screen.blit(data, (850, 65))
        else:
            data = font.render(f"Electricity: {self.current_electricity} / {self.max_electricity}", True, (255, 0, 0))
            self.game_screen.blit(data, (850, 65))

        year = self.current_date.year
        month = self.current_date.month
        day = self.current_date.day

        return year, month, day
