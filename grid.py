import pygame
import constants
from node import Node

def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            cur_node = Node(i, j, gap, rows)
            grid[i].append(cur_node)

    return grid

def draw(win, grid, rows, width):
    win.fill(constants.WHITE)

    for row in grid:
        for node in row:
            node.draw(win)
    
    draw_grid(win, rows, width)
    pygame.display.update()

def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, constants.GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, constants.GREY, (j * gap, 0), (j * gap, width))

def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap
    
    return row, col