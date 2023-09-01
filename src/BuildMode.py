import pygame as pg
import Button
from Scene import *
import datetime
from dateutil.relativedelta import relativedelta


class BuildMode:
    def __init__(self, game_screen, building_settings):
        self.game_screen = game_screen
        self.building = building_settings
        self.current_date = datetime.datetime(self.building[0]["Time"]["y"], self.building[0]["Time"]["m"],
                                              self.building[0]["Time"]["d"])
        self.current_time = 0
        self.last_time = 0
        self.next_event = 10000

    def handle_events(self):
        pass

    def update(self, budget):
        self.current_time = pg.time.get_ticks()

        if (self.current_time - self.last_time) > self.next_event:
            self.current_date += relativedelta(months=1)  # Monatlich hochzählen
            self.last_time = self.current_time

    def draw(self):
        font = pg.font.SysFont(None, 33)

        t_day = f"{self.current_date.day:02d}"
        t_month = f" - {self.current_date.month:02d}"
        t_year = f" - {self.current_date.year}"
        time = font.render(t_day, True, (0, 0, 0))
        self.game_screen.blit(time, (1165, 65))
        time = font.render(t_month, True, (0, 0, 0))
        self.game_screen.blit(time, (1185, 65))
        time = font.render(t_year, True, (0, 0, 0))
        self.game_screen.blit(time, (1225, 65))

        data = font.render(self.building[0]["Name"], True, (0, 0, 0))
        self.game_screen.blit(data, (630, 65))

        year = self.current_date.year
        month = self.current_date.month
        day = self.current_date.day

        return year, month, day
