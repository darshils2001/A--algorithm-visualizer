import math
import pygame
from queue import PriorityQueue
import constants
from node import Node
from grid import make_grid, get_clicked_pos, draw
from a_star_algorithm import a_star_algorithm

pygame.display.set_caption("A* Algorithm Visualizer")

def main(win, rows, width):
    grid = make_grid(rows, width)
    start = None
    end = None
    run = True
    started = False

    while run:
        draw(win, grid, rows, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if started:
                continue
            
            # Left mouse button
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, rows, width)
                node = grid[row][col]
                if not start and node != end:
                    start = node
                    start.make_start()
                elif not end and node != start:
                    end = node
                    end.make_end()
                elif node != start and node != end:
                    node.make_barrier()

            # Right mouse button
            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, rows, width)
                node = grid[row][col]
                node.reset()
                if node == start:
                    start = None         
                elif node == end:
                    end = None
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not started:
                    for row in grid:
                        for node in row:
                            node.update_neighbors()
                    
                    a_star_algorithm(lambda: draw(win, grid, rows, width), grid, start, end)
    pygame.quit()

# Uses Manhattan distance to calculate distance from current node to end node.
def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

main(constants.WIN, constants.ROWS, constants.WIDTH)
