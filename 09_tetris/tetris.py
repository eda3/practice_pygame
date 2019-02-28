import sys
from random import randint
import pygame
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_RIGHT, K_DOWN, K_SPACE
from pygame.rect import Rect
from pygame.surface import Surface

BLOCK_DATA = (
    (
        (0, 0, 1,
         1, 1, 1,
         0, 0, 0),
        (0, 1, 0,
         0, 1, 0,
         0, 1, 1),
        (0, 0, 0,
         1, 1, 1,
         1, 0, 0),
        (1, 1, 0,
         0, 1, 0,
         0, 1, 0),
    ), (
        (2, 0, 0,
         2, 2, 2,
         0, 0, 0),
        (0, 2, 2,
         0, 2, 0,
         0, 2, 0),
        (0, 0, 0,
         2, 2, 2,
         0, 0, 2),
        (0, 2, 0,
         0, 2, 0,
         2, 2, 0)
    ), (
        (0, 3, 0,
         3, 3, 3,
         0, 0, 0),
        (0, 3, 0,
         0, 3, 3,
         0, 3, 0),
        (0, 0, 0,
         3, 3, 3,
         0, 3, 0),
        (0, 3, 0,
         3, 3, 0,
         0, 3, 0)
    ), (
        (4, 4, 0,
         0, 4, 4,
         0, 0, 0),
        (0, 0, 4,
         0, 4, 4,
         0, 4, 0),
        (0, 0, 0,
         4, 4, 0,
         0, 4, 4),
        (0, 4, 0,
         4, 4, 0,
         4, 0, 0)
    ), (
        (0, 5, 5,
         5, 5, 0,
         0, 0, 0),
        (0, 5, 0,
         0, 5, 5,
         0, 0, 5),
        (0, 0, 0,
         0, 5, 5,
         5, 5, 0),
        (5, 0, 0,
         5, 5, 0,
         0, 5, 0)
    ), (
        (6, 6, 6, 6),
        (6, 6, 6, 6),
        (6, 6, 6, 6),
        (6, 6, 6, 6),
    ), (
        (0, 7, 0, 0,
         0, 7, 0, 0,
         0, 7, 0, 0,
         0, 7, 0, 0),
        (0, 0, 0, 0,
         7, 7, 7, 7,
         0, 0, 0, 0,
         0, 0, 0, 0),
        (0, 0, 7, 0,
         0, 0, 7, 0,
         0, 0, 7, 0,
         0, 0, 7, 0),
        (0, 0, 0, 0,
         7, 7, 7, 7,
         0, 0, 0, 0,
         0, 0, 0, 0,
         )
    )
)


class Block:
    def __init__(self, count):
        pass

    def update(selfself, count):
        pass

    def draw(self):
        pass


def erase_line(self):
    """ erase the line filled with rows"""
    pass


def is_game_over():
    """ whether the game is over or not"""
    pass


def go_next_block(count):
    """ switch back to the next block """
    pass


def is_overlapped(xpos, ypos, turn):
    """ whether the block collides with a wall or another block"""
    pass


pygame.init()
pygame.key.set_repeat(30, 30)
SURFACE = pygame.display.set_mode([600, 600])
FPSCLOCK = pygame.time.Clock()
WIDTH = 12
HEIGHT = 22
INTERVAL = 40
FIELD = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
COLORS = ((0, 0, 0), (255, 165, 0), (0, 0, 255), (0, 255, 255), (0, 255, 0),
          (255, 0, 255), (255, 255, 0), (255, 0, 0), (128, 128, 128))
BLOCK = None
NEXT_BLOCK = None


def main():
    global INTERVAL
    count = 0
    score = 0
    game_over = False
    smallfont = pygame.font.SysFont(None, 36)
    largefont = pygame.font.SysFont(None, 72)

    s = "GAME OVER!!"
    message_over: Surface = largefont.render(s, True, (0, 255, 255))
    message_rect: Rect = message_over.get_rect()
    message_rect.center = (300, 300)

    go_next_block(INTERVAL)


if __name__ == '__main__':
    main()
