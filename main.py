from utils import *
from model import predict_digit
import pygame

pygame.init()
pygame.font.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Digit Recognizer")

def init_grid(n, m, color):
    grid = [[color for _ in range(m)] for _ in range(n)]

    return grid


def draw_unit(win, x, y, color):
    pygame.draw.rect(win, color, (x * PIXEL_SIZE, y * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))


def draw_grid(win, grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            draw_unit(win, j, i, grid[i][j])
    
    if grid_lines:
        for i in range(ROWS + 1):
            pygame.draw.line(win, RED, (0, i * PIXEL_SIZE), (WIDTH, i * PIXEL_SIZE))
        
        for j in range(COLS + 1):
            pygame.draw.line(win, RED, (j * PIXEL_SIZE, 0), (j * PIXEL_SIZE, HEIGHT - TOOLBAR_HEIGHT))


def display_text(win, text, miliseconds = None):
    text_surface = get_font(200).render(text, 1, BLUE)
    win.blit(text_surface, (WIDTH/2 - text_surface.get_width()/2, (HEIGHT - TOOLBAR_HEIGHT)/2 - text_surface.get_height()/2))
    pygame.display.update()
    pygame.time.delay(miliseconds)


def predict(win, grid):
    res = predict_digit(grid)
    display_text(win, str(res), 1000)

def draw(win, grid, buttons):
    win.fill(bg_color)

    draw_grid(win, grid)

    for button in buttons:
        button.draw(win)

    pygame.display.update()


def set_dark_mode(val):
    dark_mode = val
    
    if dark_mode:
        bg_color = BLACK
        draw_color = WHITE
    else:
        bg_color = WHITE
        draw_color = BLACK


def get_row_col(pos):
    x, y = pos
    row = y // PIXEL_SIZE
    col = x // PIXEL_SIZE

    if row >= ROWS or row < 0 or col < 0 or col >= COLS:
        raise IndexError

    return row, col


dark_mode = False
run = True
clock = pygame.time.Clock()
grid = init_grid(ROWS, COLS, bg_color)
button_y = HEIGHT - TOOLBAR_HEIGHT/2 - 25

buttons = [
    Button(10, button_y, BLACK, text = "Draw", text_color = WHITE),
    Button(70, button_y, WHITE, text = "Erase", text_color = BLACK),
    Button(130, button_y, WHITE, text = "Clear", text_color = BLACK),

    Button(200, button_y, CYAN, text = "Guess", text_color = BLACK)
]



while (run):
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()

            try:
                row, col = get_row_col(pos)
                grid[row][col] = draw_color
            except IndexError:
                for button in buttons:
                    if not button.clicked(pos): continue
                    
                    if button.text == "Erase":
                        draw_color = WHITE
                    elif button.text == "Draw":
                        draw_color = BLACK
                    elif button.text == "Clear":
                        grid = init_grid(ROWS, COLS, bg_color)
                        draw_color = BLACK
                    elif button.text == "Guess":
                        predict(WIN, grid)

    
    draw(WIN, grid, buttons)

pygame.quit()