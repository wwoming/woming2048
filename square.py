"""==========zhuming=========="""
import pygame
from color import Color


square_x = 25
square_y = 225


class Square:

    @staticmethod
    def square(window):
        pygame.draw.rect(window, Color.base_square, (square_x, square_y, 80, 80))
        pygame.draw.rect(window, Color.base_square, (square_x+90, square_y, 80, 80))
        pygame.draw.rect(window, Color.base_square, (square_x+90*2, square_y, 80, 80))
        pygame.draw.rect(window, Color.base_square, (square_x+90*3, square_y, 80, 80))

        pygame.draw.rect(window, Color.base_square, (square_x, square_y+90, 80, 80))
        pygame.draw.rect(window, Color.base_square, (square_x+90, square_y+90, 80, 80))
        pygame.draw.rect(window, Color.base_square, (square_x+90*2, square_y+90, 80, 80))
        pygame.draw.rect(window, Color.base_square, (square_x+90*3, square_y+90, 80, 80))

        pygame.draw.rect(window, Color.base_square, (square_x, square_y+90*2, 80, 80))
        pygame.draw.rect(window, Color.base_square, (square_x+90, square_y+90*2, 80, 80))
        pygame.draw.rect(window, Color.base_square, (square_x+90*2, square_y+90*2, 80, 80))
        pygame.draw.rect(window, Color.base_square, (square_x+90*3, square_y+90*2, 80, 80))

        pygame.draw.rect(window, Color.base_square, (square_x, square_y+90*3, 80, 80))
        pygame.draw.rect(window, Color.base_square, (square_x+90, square_y+90*3, 80, 80))
        pygame.draw.rect(window, Color.base_square, (square_x+90*2, square_y+90*3, 80, 80))
        pygame.draw.rect(window, Color.base_square, (square_x+90*3, square_y+90*3, 80, 80))

