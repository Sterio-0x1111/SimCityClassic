import pygame as pg


class Button:
    def __init__(self, window, x, y, image, scale):
        self.window = window
        width = image.get_width()
        height = image.get_height()
        self.image = image.convert()
        self.image = pg.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def push(self):
        action = False
        pos = pg.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pg.mouse.get_pressed()[0] == 1:
                action = True
                self.clicked = True
                pg.time.delay(200) # Intervall von 0.2 Sekunde, da sofortiger Übergang

        if pg.mouse.get_pressed()[0] == 0:
            self.clicked = False

        return action

    def set_invisible(self):
        self.image.set_alpha(0)

    def draw(self):
        self.window.blit(self.image, (self.rect.x, self.rect.y))
