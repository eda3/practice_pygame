""" draw_circle_onclick.py"""
import sys
import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN
from pygame import Surface

pygame.init()
SURFACE = pygame.display.set_mode((400, 300))  # type:Surface
FPSCLOCK = pygame.time.Clock()


def main():
    """ main routine """
    mousepos = []
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit
            elif event.type == MOUSEBUTTONDOWN:
                mousepos.append(event.pos)

        SURFACE.fill((255, 255, 255))

        for i, j in mousepos:
            pygame.draw.circle(SURFACE, (0, 255, 0), (i, j), 5)

        pygame.display.update()
        FPSCLOCK.tick(30)


if __name__ == "__main__":
    main()
