import pygame
import pygame.image
import sys
import time

from maze import Maze
 
def main():
     
    pygame.init()
    pygame.display.set_caption("Maze Solver")
     
    DISPLAY = pygame.display.set_mode((594,794))
     
    WHITE = (255,255,255)
    BLACK = (0,0,0)

    DISPLAY.fill(WHITE)
    time.sleep(2)
    maze = Maze(600)
    maze.draw_full_maze(DISPLAY)
    maze.make_maze(DISPLAY)
    maze.solve_maze(DISPLAY)
    
    # just wait for a command line exit at this stage
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
     
if __name__=="__main__":
    main()