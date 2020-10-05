import pygame 
import random

class Cell(pygame.sprite.Sprite):

    # defined as 600 / number of cells per row
    width, height = 6, 6
    BLUE = (0, 0, 255)

    def __init__(self, x_position, y_position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x_position * self.width 
        self.rect.y = y_position * self.height
        self.is_wall = True 
    
    def draw_cell(self, screen):
        screen.blit(self.image, self.rect)
    
    def swap_color(self, color):
        self.image.fill(color)
    
    def make_path(self):
        self.is_wall = not self.is_wall

    

