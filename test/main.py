import pygame as pg
import json

pg.init()

GRID_SIZE = 100
CELL_SIZE = 30
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700

BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

window = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pg.RESIZABLE)

grid_surface = pg.Surface((GRID_SIZE * CELL_SIZE, GRID_SIZE * CELL_SIZE), pg.RESIZABLE) # Transparente Surface für das Raster
grid_surface.fill(BLACK)

# Felder initialisieren
try:
    with open("Field.json", "r") as json_file:
        fields = json.load(json_file)
except FileNotFoundError:
    fields = [{"state": 0, "x": x * CELL_SIZE, "y": y * CELL_SIZE} for y in range(GRID_SIZE) for x in range(GRID_SIZE)]
    with open("Fail.json", "w") as json_file:
        json.dump(fields, json_file, indent=4)

scroll_x = 0
scroll_y = 0

drawing = False
start_pos = None
end_pos = None
o = False
p = False
l = False

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.KEYDOWN:
            key_pressed = pg.key.get_pressed()

        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            drawing = True
            start_pos = (event.pos[0] - scroll_x, event.pos[1] - scroll_y)
            end_pos = (event.pos[0] - scroll_x, event.pos[1] - scroll_y)
        elif event.type == pg.MOUSEMOTION and drawing:
            end_pos = (event.pos[0] - scroll_x, event.pos[1] - scroll_y)
        elif event.type == pg.MOUSEBUTTONUP and event.button == 1:
            drawing = False
            for y in range(min(start_pos[1] // CELL_SIZE, end_pos[1] // CELL_SIZE),
                           max(start_pos[1] // CELL_SIZE, end_pos[1] // CELL_SIZE) + 1):
                for x in range(min(start_pos[0] // CELL_SIZE, end_pos[0] // CELL_SIZE),
                               max(start_pos[0] // CELL_SIZE, end_pos[0] // CELL_SIZE) + 1):
                    if 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE:
                        idx = y * GRID_SIZE + x
                        if key_pressed[pg.K_o] or o:
                            fields[idx]["state"] = 1
                            o = True
                            p = False
                            l = False
                        if key_pressed[pg.K_p] or p:
                            fields[idx]["state"] = 2
                            o = False
                            p = True
                            l = False
                        if key_pressed[pg.K_l] or l:
                            fields[idx]["state"] = 3
                            o = False
                            p = False
                            l = True

    keys = pg.key.get_pressed()
    if keys[pg.K_w]:
        scroll_y += CELL_SIZE
    if keys[pg.K_s]:
        scroll_y -= CELL_SIZE
    if keys[pg.K_a]:
        scroll_x += CELL_SIZE
    if keys[pg.K_d]:
        scroll_x -= CELL_SIZE

    # Mausposition abfragen
    mouse_x, mouse_y = pg.mouse.get_pos()
    mouse_x -= scroll_x
    mouse_y -= scroll_y
    mouse_x //= CELL_SIZE
    mouse_y //= CELL_SIZE

    grid_image_ground = pg.image.load("../Simcity/image/Ground.png")
    grid_image_forest = pg.image.load("../Simcity/image/forest.png")
    grid_image_water = pg.image.load("../Simcity/image/Water.png")

    for field in fields:
        x = field["x"]
        y = field["y"]
        state = field["state"]

        if state:
            grid_surface.blit(grid_image_ground, (x, y))
        if state == 2:
            grid_surface.blit(grid_image_forest, (x, y))
        if state == 3:
            grid_surface.blit(grid_image_water, (x, y))
        if not state in range(0, 4):
            pg.draw.rect(grid_surface, BLACK, (x, y, CELL_SIZE, CELL_SIZE))

    # Zeichne blauen Rahmen um das Feld, über das der Mauszeiger schwebt
    if 0 <= mouse_x < GRID_SIZE and 0 <= mouse_y < GRID_SIZE:
        pg.draw.rect(grid_surface, BLUE, (mouse_x * CELL_SIZE, mouse_y * CELL_SIZE, CELL_SIZE, CELL_SIZE), 2)

    window.fill(BLACK)
    window.blit(grid_surface, (scroll_x, scroll_y))

    if drawing and start_pos and end_pos:
        rect_x = min(start_pos[0], end_pos[0]) + scroll_x
        rect_y = min(start_pos[1], end_pos[1]) + scroll_y
        rect_width = abs(end_pos[0] - start_pos[0])
        rect_height = abs(end_pos[1] - start_pos[1])
        pg.draw.rect(window, YELLOW, (rect_x, rect_y, rect_width, rect_height), 3)

    pg.display.update()

    # Speichern der Felder in JSON-Datei
    with open("Field.json", "w") as json_file:
        json.dump(fields, json_file)

pg.quit()
