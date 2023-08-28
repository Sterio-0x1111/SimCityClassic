import pygame as pg


class Button:
    def __init__(self, game, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = image
        self.image = pg.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, game):
        action = False
        pos = pg.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if (pg.mouse.get_pressed()[0] == 1) and (self.clicked is False):
                action = True
                self.clicked = True

        if pg.mouse.get_pressed()[0] == 0:
            self.clicked = False

        game.window.blit(self.image, (self.rect.x, self.rect.y))

        return action
