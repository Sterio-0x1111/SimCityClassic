from Scene import *
import pygame as pg
import locale


class Budget:
    def __init__(self, game_screen, building_info, budget):
        self.game_screen = game_screen
        self.building_info = building_info
        self.budget = budget
        self.info_cost = 0
        self.info_profit = 0
        self.delta = 0

    def handle_events(self):
        self.delta = 0
        self.info_profit = 0
        self.info_cost = 0

        for info, exp in self.building_info.items():
            if "expense" in exp:
                self.budget -= (exp["expense"] * exp["instance"].count)
                self.info_cost -= (exp["expense"] * exp["instance"].count)
            if "profit" in exp:
                if exp["state"] == 12:
                    self.budget += (exp["profit"] * exp["instance"].population)
                    self.info_profit += (exp["profit"] * exp["instance"].population)
                else:
                    self.budget += (exp["profit"] * exp["instance"].count)
                    self.info_profit += (exp["profit"] * exp["instance"].count)
        self.draw()

    def update(self, cost):
        self.budget -= cost

    def draw(self):
        font = pg.font.SysFont(None, 33)
        locale.setlocale(locale.LC_ALL, 'de_DE.utf-8')

        if self.budget < 0:
            self.font = pg.font.SysFont(None, 33)
            text = "GAME OVER"
            text = self.font.render(text, True, (255, 0, 0))
            self.game_screen.blit(text, (125, 65))
        else:
            formatted_budget = locale.currency(self.budget, grouping=True, symbol=True)
            data = font.render(formatted_budget, True, (0, 0, 0))
            self.game_screen.blit(data, (125, 65))

        font = pg.font.SysFont(None, 20)
        formatted_budget = locale.currency(self.info_cost, grouping=True, symbol=True)
        data = font.render(formatted_budget, True, (255, 0, 0))
        self.game_screen.blit(data, (5, 69))

        formatted_budget = locale.currency(self.info_profit, grouping=True, symbol=True)
        data = font.render(formatted_budget, True, (0, 255, 0))
        self.game_screen.blit(data, (5, 54))

        self.delta = self.info_profit + self.info_cost
        formatted_budget = locale.currency(self.delta, grouping=True, symbol=True)
        data = font.render(formatted_budget, True, (0, 0, 0))
        self.game_screen.blit(data, (5, 84))

        return self.budget
