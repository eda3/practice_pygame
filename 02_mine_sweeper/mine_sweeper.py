import sys
from math import floor
from random import randint
import pygame
from pygame import Surface, Rect
from pygame.locals import QUIT, MOUSEBUTTONDOWN
import pprint

WIDTH = 20
HEIGHT = 15
SIZE = 50
NUM_OF_BOMBS = 20
EMPTY = 0
BOMB = 1
OPENED = 2
OPEN_COUNT = 0
CHECKED = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]

pygame.init()
SURFACE = pygame.display.set_mode([WIDTH * SIZE, HEIGHT * SIZE])
FPSCLOCK = pygame.time.Clock()


def num_of_bomb(field, x_pos, y_pos) -> int:
    """ return surrounding mines"""
    count: int = 0
    for yoffset in range(-1, 2):
        for xoffset in range(-1, 2):
            xpos, ypos = (x_pos + xoffset, y_pos + yoffset)
            if 0 <= xpos < WIDTH and 0 <= ypos < HEIGHT and field[ypos][xpos] == BOMB:
                count += 1
    return count


def open_tile(field, x_pos, y_pos):
    global OPEN_COUNT
    if CHECKED[y_pos][x_pos]:
        return

    CHECKED[y_pos][x_pos] = True

    for yoffset in range(-1, 2):
        for xoffset in range(-1, 2):
            xpos, ypos = (x_pos + xoffset, y_pos + yoffset)
            print(f"xpos{xpos}")
            print(f"ypos{ypos}")
            if 0 <= xpos < WIDTH and 0 <= ypos < HEIGHT and field[ypos][xpos] == EMPTY:
                field[ypos][xpos] = OPENED
                OPEN_COUNT += 1
                count = num_of_bomb(field, xpos, ypos)
                if count == 0 and not(xpos == x_pos and ypos == y_pos):
                    open_tile(field, xpos, ypos)


def main():
    smallfont: Surface = pygame.font.SysFont(None, 36)
    largefont: Surface = pygame.font.SysFont(None, 72)

    s = "!!GAME CLEAR!!"
    message_clear: Surface = largefont.render(s, True, (0, 255, 225))

    s = "GAME OVER!!"
    message_over: Surface = largefont.render(s, True, (0, 255, 225))

    message_rect: Rect = message_clear.get_rect()
    message_rect.center = (WIDTH * SIZE / 2, HEIGHT * SIZE / 2)

    game_over = False

    field = [[EMPTY for xpos in range(WIDTH)] for ypos in range(HEIGHT)]

    # set up mines
    count = 0
    while count < NUM_OF_BOMBS:
        xpos, ypos = randint(0, WIDTH - 1), randint(0, HEIGHT - 1)
        if field[ypos][xpos] == EMPTY:
            field[ypos][xpos] = BOMB
            count += 1

    pprint.pprint(field)

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                mousex = event.pos[0]
                mousey = event.pos[1]
                xpos, ypos = floor(mousex / SIZE), floor(mousey / SIZE)

                if field[ypos][xpos] == BOMB:
                    game_over = True
                else:
                    open_tile(field, xpos, ypos)

        # drawing
        SURFACE.fill((0, 0, 0))
        for ypos in range(HEIGHT):
            for xpos in range(WIDTH):
                tile: int = field[ypos][xpos]
                rect: Rect = (xpos * SIZE, ypos * SIZE, SIZE, SIZE)

                if tile == EMPTY or tile == BOMB:
                    pygame.draw.rect(SURFACE, (192, 192, 192), rect)
                    if game_over and tile == BOMB:
                        pygame.draw.ellipse(SURFACE, (225, 225, 0), rect)
                elif tile == OPENED:
                    count = num_of_bomb(field, xpos, ypos)
                    if count > 0:
                        print(f"count{count}")
                        color = (255, 255, 0)
                        num_image = smallfont.render(f"{count}", True, color)
                        pos = (xpos * SIZE + 10, ypos * SIZE + 10)
                        SURFACE.blit(num_image, pos)

        # drawing line
        color = (96, 96, 96)
        for i in range(0, WIDTH * SIZE, SIZE):
            pygame.draw.line(SURFACE, color, (i, 0), (i, HEIGHT * SIZE))
        for i in range(0, HEIGHT * SIZE, SIZE):
            pygame.draw.line(SURFACE, color, (0, i), (WIDTH * SIZE, i))

        # drawing message
        if OPEN_COUNT == WIDTH * HEIGHT - NUM_OF_BOMBS:
            SURFACE.blit(message_clear, message_rect.topleft)
        elif game_over:
            SURFACE.blit(message_over, message_rect.topleft)

        pygame.display.update()
        FPSCLOCK.tick(15)


if __name__ == '__main__':
    main()
