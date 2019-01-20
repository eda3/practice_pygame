""" fps_test1.py"""
import sys
import pygame
from pygame.locals import QUIT

pygame.init()
SURFACE = pygame.display.set_mode((400, 300))


def main():
    """ main routine """
    sysfont = pygame.font.SysFont(None, 36)
    counter = 0
    while True:
        for event in pygame.event.get(QUIT):
            pygame.quit()
            sys.exit()

        counter += 1
        SURFACE.fill((0, 0, 0))
        color = (225, 225, 225)
        message = "count is {}".format(counter)
        count_image = sysfont.render(message, True, color)
        SURFACE.blit(count_image, (50, 50))
        pygame.display.update()


if __name__ == "__main__":
    main()
