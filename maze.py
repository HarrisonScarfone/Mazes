from cell import Cell

import pygame
import time
import random

class Maze:

    def __init__(self, side_length, squares=100):

        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        self.LIGHT_BLUE = (0, 255, 255)

        self.squares = squares
        self.side_length = side_length

        self.cell_map, self.step_size = self.generate_cell_map(side_length, squares) 

    def generate_cell_map(self, side_length, squares):
        cell_map = {}
        x = 0
        y = 0

        step = side_length // squares

        for i in range(side_length // step):
            for j in range(side_length // step):
                cell_map[(i,j)] = Cell(i, j)
        
        return cell_map, step

    def draw_full_maze(self, screen):
        for i in range(self.side_length // self.step_size):
            for j in range(self.side_length // self.step_size):
                self.cell_map[(i,j)].draw_cell(screen)
                pygame.display.update()

    def update_cell(self, x, y, screen, color):
        self.cell_map[(x, y)].make_path()
        self.cell_map[(x, y)].swap_color(color)
        self.cell_map[(x, y)].draw_cell(screen)

    def get_neighbours(self, x, y, walls):
        valid_neighbours = []
        if x > 2:
            if (x - 2, y) in self.cell_map and self.cell_map[(x - 2, y)].is_wall == walls:
                valid_neighbours.append((x - 2, y))
        if x < 97:
            if (x + 2, y) in self.cell_map and self.cell_map[(x + 2, y)].is_wall == walls:
                valid_neighbours.append((x + 2, y))
        if y > 2:
            if (x, y - 2) in self.cell_map and self.cell_map[(x, y - 2)].is_wall == walls:
                valid_neighbours.append((x, y - 2))
        if y < 97:
            if (x, y + 2) in self.cell_map and self.cell_map[(x, y + 2)].is_wall == walls:
                valid_neighbours.append((x, y + 2))
        return valid_neighbours
    
    def connect_to_neighbour(self, x, y, neighbours, screen):
        if neighbours:
            selected_cell = random.choice(neighbours)
            location_as_tuple = ((x + selected_cell[0]) // 2, (y + selected_cell[1]) // 2)
            self.update_cell(location_as_tuple[0], location_as_tuple[1], screen, self.WHITE)
            self.update_cell(x, y, screen, self.WHITE)

    def make_maze(self, screen):

        next_cells = []
        wall_set = {}

        start = (1, 1)
        self.update_cell(start[0], start[1], screen, self.WHITE)
        next_cells += self.get_neighbours(start[0], start[1], True)

        while next_cells:

            next_cell = random.choice(next_cells)
            next_cells.remove(next_cell)

            neighbours = self.get_neighbours(next_cell[0], next_cell[1], False)
            self.connect_to_neighbour(next_cell[0], next_cell[1], neighbours, screen)
            for cell in self.get_neighbours(next_cell[0], next_cell[1], True):
                if cell not in next_cells:
                    next_cells.append(cell)

            time.sleep(0.001)
                
            pygame.display.update()
    
    def solve_maze(self, screen):

        start = (1,1)
        end = (97, 97)
        self.solve_path = None

        def get_direction_choices(x, y):
            choices = []
            if (x - 1, y) in self.cell_map and not self.cell_map[(x - 1, y)].is_wall:
                choices.append((x - 1, y))
            if (x + 1, y) in self.cell_map and not self.cell_map[(x + 1, y)].is_wall:
                choices.append((x + 1, y))
            if (x, y - 1) in self.cell_map and not self.cell_map[(x, y - 1)].is_wall:
                choices.append((x, y - 1))
            if (x, y + 1) in self.cell_map and not self.cell_map[(x, y + 1)].is_wall:
                choices.append((x, y + 1))
            return choices

        def solve(node, last_node, end, path):
            self.update_cell(node[0], node[1], screen, self.LIGHT_BLUE)
            pygame.display.update()
            time.sleep(0.003)
            if node == end:
                self.solve_path = path
            choices = get_direction_choices(node[0], node[1])
            if choices:
                for choice in choices:
                    if choice != last_node:
                        solve(choice, node, end, path + [node])

            
        solve(start, None, end, [])

        for key in self.solve_path:
            self.update_cell(key[0], key[1], screen, self.RED)
            pygame.display.update()
            time.sleep(0.05)
        self.update_cell(end[0], end[1], screen, self.RED)
