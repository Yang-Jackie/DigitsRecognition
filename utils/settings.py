import pygame

pygame.init()
pygame.font.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)

ROWS, COLS = 28, 28
PIXEL_SIZE = 20
TOOLBAR_HEIGHT = 100
HEIGHT, WIDTH = ROWS * PIXEL_SIZE + TOOLBAR_HEIGHT, COLS * PIXEL_SIZE

FPS = 240
grid_lines = False

draw_color = BLACK
bg_color = WHITE

def get_font(size):
    return pygame.font.SysFont("comicsans", size)