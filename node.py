import pygame

COLORS = {
    "RED": (255, 0, 0),
    "GREEN": (0, 255, 0),
    "BLUE": (0, 255, 0),
    "YELLOW": (255, 255, 0),
    "WHITE": (255, 255, 255),
    "BLACK": (0, 0, 0),
    "PURPLE": (128, 0, 128),
    "ORANGE": (255, 165 ,0),
    "GREY": (128, 128, 128),
    "TURQUOISE": (64, 224, 208),
}

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))

class Node:
    def __init(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.width = width
        self.total_rows = total_rows
        self.color = COLORS["WHITE"]
        self.neighbors = []

    def get_pos(self):
        return self.row, self.col
    
    def is_open(self):
        return self.color == COLORS["GREEN"]
    
    def is_closed(self):
        return self.color == COLORS["RED"]
    
    def is_start(self):
	    return self.color == COLORS["ORANGE"]

    def is_end(self):
	    return self.color == COLORS["TURQUOISE"]
    
    def is_barrier(self):
	    return self.color == COLORS["BLACK"]

    def reset(self):
	    self.color = COLORS["WHITE"]
    
    def make_open(self):
	    self.color = COLORS["GREEN"]

    def make_closed(self):
	    self.color = COLORS["RED"]
    
    def make_start(self):
	    self.color = COLORS["ORANGE"]

    def make_end(self):
	    self.color = COLORS["TURQUOISE"]
    
    def make_barrier(self):
	    self.color = COLORS["BLACK"]

    def make_path(self):
	    self.color = COLORS["PURPLE"]
    
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        pass

    def __lt__(self, other):
        return False   
