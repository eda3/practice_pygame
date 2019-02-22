import sys
import math
import random
import pygame
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_RIGHT, Rect


class Block:
    """ block, ball, paddle object"""

    def __init__(self: Rect, col, rect, speed=0):
        self.col = col
        self.rect: Rect = rect
        self.speed = speed
        self.direction = random.randint(-45, 45) + 270

    def move(self):
        """ move the ball"""
        dx = math.cos(math.radians(self.direction)) * self.speed
        dy = math.sin(math.radians(self.direction)) * self.speed

        self.rect.centerx += dx
        self.rect.centery -= dy

    def draw(self):
        """ draw the block, ball, paddle"""
        if self.speed == 0:
            pygame.draw.rect(SURFACE, self.col, self.rect)
        else:
            pygame.draw.ellipse(SURFACE, self.col, self.rect)


def tick():
    """ every frame processing"""
    global BLOCKS
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                PADDLE.rect.centerx -= 10
            if event.key == K_RIGHT:
                PADDLE.rect.centerx += 10
    if BALL.rect.centery < 1000:
        BALL.move()

    # collision block?
    prevlen = len(BLOCKS)

    BLOCKS = [x for x in BLOCKS if not x.rect.colliderect(BALL.rect)]

    if len(BLOCKS) != prevlen:
        BALL.direction *= -1

    # collision paddle?
    if PADDLE.rect.colliderect(BALL.rect):
        dx = PADDLE.rect.centerx - BALL.rect.centerx
        BALL.direction = 90 + (dx / PADDLE.rect.width * 80)

    # collision wall?
    if BALL.rect.centerx < 0 or BALL.rect.centerx > 600:
        BALL.direction = 180 - BALL.direction
    if BALL.rect.centery < 0:
        BALL.direction = -BALL.direction
        BALL.speed = 15


pygame.init()
pygame.key.set_repeat(5, 5)
SURFACE = pygame.display.set_mode((600, 800))
FPSCLOCK = pygame.time.Clock()
BLOCKS = []
PADDLE = Block((242, 242, 0), Rect(300, 700, 100, 30))
BALL = Block((242, 242, 0), Rect(300, 400, 20, 20), 10)


def main():
    myfont = pygame.font.SysFont(None, 80)
    mess_clear = myfont.render("Cleared!", True, (255, 255, 0))
    mess_over = myfont.render("Game Over!", True, (255, 255, 0))
    fps = 30
    colors = [(255, 0, 0), (255, 165, 0), (242, 242, 0),
              (0, 128, 0), (128, 0, 128), (0, 0, 250)]

    for ypos, color in enumerate(colors, start=0):
        for xpos in range(0, 5):
            rect = Rect(xpos * 100 + 60, ypos * 50 + 40, 80, 30)
            BLOCKS.append(Block(color, rect))

    while True:
        tick()

        SURFACE.fill((0, 0, 0))
        BALL.draw()
        PADDLE.draw()
        for block in BLOCKS:
            block.draw()

        if len(BLOCKS) == 0:
            SURFACE.blit(mess_clear, (200, 400))
        if BALL.rect.centery > 800 and len(BLOCKS) > 0:
            SURFACE.blit(mess_over, (150, 400))

        pygame.display.update()
        FPSCLOCK.tick(fps)


if __name__ == '__main__':
    main()
