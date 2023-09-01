from Scene import *
import pygame as pg
import locale


class Budget:
    def __init__(self, game_screen, building_info, budget):
        self.game_screen = game_screen
        self.building_info = building_info
        self.budget = budget

    def handle_events(self):
        pass

    def update(self, cost):
        self.budget -= cost

    def draw(self):
        font = pg.font.SysFont(None, 33)

        locale.setlocale(locale.LC_ALL, 'de_DE.utf-8')
        formatted_budget = locale.currency(self.budget, grouping=True, symbol=True)
        data = font.render(formatted_budget, True, (0, 0, 0))
        self.game_screen.blit(data, (130, 65))

        return self.budget
