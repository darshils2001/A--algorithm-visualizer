import pygame
import constants

class Node:
    def __init(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.width = width
        self.total_rows = total_rows
        self.color = constants.WHITE
        self.neighbors = []

    def get_pos(self):
        return self.row, self.col
    
    def is_open(self):
        return self.color == constants.GREEN
    
    def is_closed(self):
        return self.color == constants.RED
    
    def is_start(self):
	    return self.color == constants.ORANGE

    def is_end(self):
	    return self.color == constants.TURQUOISE
    
    def is_barrier(self):
	    return self.color == constants.BLACK

    def reset(self):
	    self.color = constants.WHITE
    
    def make_open(self):
	    self.color = constants.GREEN

    def make_closed(self):
	    self.color = constants.RED
    
    def make_start(self):
	    self.color = constants.ORANGE

    def make_end(self):
	    self.color = constants.TURQUOISE
    
    def make_barrier(self):
	    self.color = constants.BLACK

    def make_path(self):
	    self.color = constants.PURPLE
    
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        pass

    def __lt__(self, other):
        return False   
