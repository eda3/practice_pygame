""" draw_image_subregion2.py """
import sys
import pygame
from pygame.locals import QUIT

pygame.init()
SURFACE = pygame.display.set_mode((300, 200))
FPSCLOCK = pygame.time.Clock()


def main():
    """ main routine """
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit

        SURFACE.fill((255, 255, 255))

        pygame.display.update()
        FPSCLOCK.tick(30)


if __name__ == "__main__":
    main()
