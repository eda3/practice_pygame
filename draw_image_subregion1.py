""" draw_image_subregion1.py """
import sys

import pygame
from pygame import Surface
from pygame.locals import QUIT, Rect

pygame.init()
SURFACE = pygame.display.set_mode((400, 300))  # type: Surface
FPSCLOCK = pygame.time.Clock()


def main():
    """ main routine """
    logo = pygame.image.load("./assets/pythonlogo.png")  # type: Surface

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit

        SURFACE.fill((255, 255, 255))

        # draw a logo at the (0, 0) upper left corner
        SURFACE.blit(logo, (0, 0))
        SURFACE.blit(logo, (250, 50), Rect(50, 50, 100, 100))

        pygame.display.update()
        FPSCLOCK.tick(30)


if __name__ == "__main__":
    main()
