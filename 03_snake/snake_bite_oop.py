import sys
import random


import pygame
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN, Rect
from pygame import Surface

pygame.init()
SURFACE: Surface = pygame.display.set_mode((600, 600))
FPSCLOCK = pygame.time.Clock()


class Snake:
    def __init__(self, pos):
        self.bodies = [pos]

    def move(self, key):
        """ move snake one square """
        xpos, ypos = self.bodies[0]
        if key == K_LEFT:
            xpos -= 1
        elif key == K_RIGHT:
            xpos += 1
        elif key == K_UP:
            ypos -= 1
        elif key == K_DOWN:
            ypos += 1
        head = (xpos, ypos)

        is_game_over = head in self.bodies or \
            head[0] < 0 or head[0] >= W or \
            head[1] < 0 or head[1] >= H

        self.bodies.insert(0, head)
        if head in FOODS:
            # move food to another square
            i = FOODS.index(head)
            del FOODS[i]
            add_food(self)
        else:
            self.bodies.pop()

        return is_game_over

    def draw(self):
        """ draw Snake"""
        for body in self.bodies:
            rect = Rect(body[0] * 30, body[1] * 30, 30, 30)
            pygame.draw.rect(SURFACE, (0, 255, 255), rect)


FOODS = []
(W, H) = (20, 20)


def add_food(snake):
    while True:
        pos = (random.randint(0, W - 1), random.randint(0, H - 1))
        if (pos in FOODS) or (pos in snake.bodies):
            continue
        FOODS.append(pos)
        break


def move_food(pos):
    i = FOODS.index(pos)
    del FOODS[i]
    add_food()


def paint(snake, message):
    """ draw the entire screen """
    SURFACE.fill((0, 0, 0))
    snake.draw()
    for food in FOODS:
        rect = Rect(food[0] * 30, food[1] * 30, 30, 30)
        pygame.draw.ellipse(SURFACE, (0, 255, 0), rect)

    # draw line
    for index in range(20):
        color = (64, 64, 64)
        pygame.draw.line(SURFACE, color, (index * 30, 0), (index * 30, 600))
        pygame.draw.line(SURFACE, color, (0, index * 30), (600, index * 30))

    if message is not None:
        SURFACE.blit(message, (150, 300))
    pygame.display.update()


def main():
    """ main routine """
    myfont = pygame.font.SysFont(None, 80)
    key = K_DOWN
    message = None
    game_over = False

    snake = Snake((int(W / 2), int(H / 2)))
    for _ in range(10):
        add_food(snake)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit
            elif event.type == KEYDOWN:
                key = event.key

        if game_over:
            message = myfont.render("Game Over!", True, (255, 255, 0))
        else:
            game_over = snake.move(key)

        paint(snake, message)
        FPSCLOCK.tick(5)


if __name__ == "__main__":
    main()
