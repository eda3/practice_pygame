""" draw_image_subregion2.py """
import sys
import pygame
from pygame.locals import QUIT, Rect
from pygame import Surface

pygame.init()
SURFACE = pygame.display.set_mode((300, 200))  # type:Surface
FPSCLOCK = pygame.time.Clock()


def main():
    """ main routine """
    strip = pygame.image.load('./assets/strip.png')  # type : Surface
    images = []
    for index in range(9):
        image = pygame.Surface((24, 24))
        image.blit(strip, (0, 0), Rect(index * 24, 0, 24, 24))
        images.append(image)

    counter = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit

        SURFACE.fill((255, 255, 255))

        SURFACE.blit(images[counter % 2 + 0], (50, 50))
        SURFACE.blit(images[counter % 2 + 2], (100, 50))
        SURFACE.blit(images[counter % 2 + 4], (150, 50))
        SURFACE.blit(images[counter % 2 + 6], (200, 50))
        counter += 1

        pygame.display.update()
        FPSCLOCK.tick(5)


if __name__ == "__main__":
    main()
