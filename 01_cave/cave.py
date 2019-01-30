""" cave.py """
import sys
from random import randint
import pygame
from pygame.locals import QUIT, Rect, KEYDOWN, K_SPACE
from pygame import Surface

pygame.init()
pygame.key.set_repeat(5, 5)
SURFACE = pygame.display.set_mode((800, 600))  # type:Surface
FPSCLOCK = pygame.time.Clock()


class Ship:
    def __init__(self):
        self._pos_y = 250
        self._image = None
        self.load_ship_image()

        self._height = self._image.get_height()

    def load_ship_image(self):
        self.image: Surface = pygame.image.load("./assets/ship.png")

    def on_key_down_event(self, is_space_down):
        self.pos_y += -3 if is_space_down else 3

    def movement_gameover(self):
        # rotation ship
        rotate_image: Surface = pygame.transform.rotate(self._image, 1)
        w1, h1 = self.image.get_size()
        w2, h2 = rotate_image.get_size()

        dx, dy = (w2 - w1) / 2, (h2 - h1) / 2
        topleft = (0 - dx, self.pos_y - dy)
        return rotate_image, topleft

    @property
    def image(self) -> Surface:
        return self._image

    @image.setter
    def image(self, value):
        self._image = value

    @property
    def pos_y(self):
        return self._pos_y

    @pos_y.setter
    def pos_y(self, value):
        self._pos_y = value

    @property
    def height(self):
        return self._height

    @property
    def pos(self):
        return self.image.get_size()


class Holls:
    def __init__(self):
        _walls = 80
        self._holes_rect = []

        self._slope = randint(1, 6)
        for xpos in range(_walls):
            self._holes_rect.append(Rect(xpos * 10, 100, 10, 400))

    def scroll_cave(self):
        _speed = -10
        _edge = self._holes_rect[-1].copy()
        _test = _edge.move(0, self._slope)

        if _test.top <= 0 or _test.bottom > 600:
            self._slope = randint(1, 6) * (-1 if self._slope > 0 else 1)
            _edge.inflate_ip(0, -20)

        _edge.move_ip(10, self._slope)
        self._holes_rect.append(_edge)
        del self._holes_rect[0]
        self._holes_rect = [x.move(_speed, 0) for x in self._holes_rect]

    def check_collision(self, ship):
        _ship_bottom = ship.pos_y + ship.height

        if self._holes_rect[0].top > ship.pos_y or self._holes_rect[0].bottom < _ship_bottom:
            return True
        else:
            return False

    @property
    def holes_rect(self):
        return self._holes_rect


class Message:
    def __init__(self, message, color):
        self._score = 0
        self._message = message
        self._sysfont = pygame.font.SysFont(None, 36)
        self._color = color

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value

    @property
    def image(self) -> Surface:
        image = self._sysfont.render(self.message, True, self._color)
        return image


def text_position_center(text):

    surface_size = (SURFACE.get_size())
    gameover_text_size = text.image.get_size()
    posx = surface_size[0] / 2 - gameover_text_size[0] / 2
    posy = surface_size[1] / 2 - gameover_text_size[1] / 2

    return (posx, posy)


def main():
    """ main routine """
    ship = Ship()
    holles = Holls()

    score = Message("", (0, 0, 255))

    gameover_text = Message("GAME OVER", (255, 0, 0))
    gameover_text_pos = text_position_center(gameover_text)

    gameover_flg = False

    while True:

        is_space_down = False
        if on_event_listener():
            is_space_down = True

        if holles.check_collision(ship):
            gameover_flg = True

        # drawing
        SURFACE.fill((0, 255, 0))

        for hole in holles.holes_rect:
            pygame.draw.rect(SURFACE, (0, 0, 0), hole)

        if gameover_flg:
            ship.image, topleft = ship.movement_gameover()
            SURFACE.blit(ship.image, topleft)

            SURFACE.blit(gameover_text.image, gameover_text_pos)

        else:
            score.score += 10
            ship.on_key_down_event(is_space_down)
            topleft = (0, ship.pos_y)
            SURFACE.blit(ship.image, topleft)

        holles.scroll_cave()

        score.message = f"score is {score.score}"
        SURFACE.blit(score.image, (600, 20))

        pygame.display.update()
        FPSCLOCK.tick(20)


def on_event_listener():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                return True


if __name__ == "__main__":
    main()
