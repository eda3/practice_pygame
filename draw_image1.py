""" draw_image1.py """
import sys

import pygame
from pygame import Surface
from pygame.locals import QUIT

pygame.init()
SURFACE = pygame.display.set_mode((400, 300))  # type: Surface
FPSCLOCK = pygame.time.Clock()


def main():
    """ main routine """
    logo = pygame.image.load("assets/pythonlogo.png")  # type: Surface

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit

        SURFACE.fill((255, 255, 255))

        # draw a logo at the (20, 50) upper left corner
        pygame.display.update()


if __name__ == "__main__":
    main()
