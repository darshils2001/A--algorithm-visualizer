import math
import pygame
from queue import PriorityQueue

def a_star_algorithm(draw, grid, start, end):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}

    # Current shortest distance from start to current node
    g_score = {node: float("inf") for row in grid for node in row}
    g_score[start] = 0
    # Predicted distance from current node to end 
    f_score = {node: float("inf") for row in grid for node in row}
    f_score[start] = get_heuristic(start.get_pos(), end.get_pos())

    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        cur = open_set.get()[2]
        open_set_hash.remove(cur)

        if cur == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True
        
        for neighbor in cur.neighbors:
            temp_g_score = g_score[cur] + 1

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = cur
                g_score[neighbor] = temp_g_score
                f_score[neighbor]  = temp_g_score + get_heuristic(neighbor.get_pos(), end.get_pos())

                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()
        
        draw()

        if cur != start:
            cur.make_closed()

    return False

# Uses Manhattan distance to calculate distance from current node to end
def get_heuristic(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

def reconstruct_path(came_from, cur, draw):
    while cur in came_from:
        cur = came_from[cur]
        cur.make_path()
        draw()
