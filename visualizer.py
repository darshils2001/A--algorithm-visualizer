import math
import pygame
from queue import PriorityQueue
import constants
from node import Node

pygame.display.set_caption("A* Algorithm Visualizer")

# Uses Manhattan distance to calculate distance from current node to end node.
def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)
