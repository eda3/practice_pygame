from pygame.locals import Rect, QUIT, MOUSEMOTION, MOUSEBUTTONDOWN
import pygame
from math import hypot
from random import randint
import sys


class House:
    """ House Object"""

    def __init__(self, xpos):
        self.rect = Rect(xpos, 550, 40, 40)
        self.exploded = False

        sysfont = pygame.font.SysFont(None, 40)

        font_house_a = sysfont.render("A", False, (255, 255, 255))
        font_house_b = sysfont.render("X", False, (255, 255, 255))
        self.images = (pygame.Surface((20, 20), pygame.SRCALPHA),
                       pygame.Surface((20, 20), pygame.SRCALPHA))

        self.images[0].blit(font_house_a, (0, 0))
        self.images[1].blit(font_house_b, (0, 0))

    def draw(self):
        """ draw house"""
        if self.exploded:
            SURFACE.blit(self.images[1], self.rect.topleft)
        else:
            SURFACE.blit(self.images[0], self.rect.topleft)


class Missile:
    """ falling missile object """

    def __init__(self):
        self.max_count = 500
        self.interval = 1000
        self.pos = [0, 0]
        self.cpos = [0, 0]
        self.firetime = 0
        self.radius = 0
        self.reload(0)

    def reload(self, time_count):
        house_x = randint(0, 12) * 60 + 20
        self.pos = (randint(0, 800), house_x)
        self.interval = int(self.interval * 0.9)
        self.firetime = randint(0, self.interval) + time_count
        self.cpos = [0, 0]
        self.radius = 0

    def tick(self, time_count, shoot, houses):
        """ update missile status"""
        is_hit = False
        elapsed = time_count - self.firetime
        if elapsed < 0:
            return

        if self.radius > 0:  # exploding
            self.radius += 1
            if self.radius > 100:
                self.reload(time_count)
        else:
            self.cpos[0] = (self.pos[1] - self.pos[0]) * \
                elapsed / self.max_count + self.pos[0]
            self.cpos[1] = 575 * elapsed / self.max_count

        # shotted out?
        diff = hypot(shoot.shot_pos[0] - self.cpos[0],
                     shoot.shot_pos[1] - self.cpos[1])
        if diff < shoot.radius:
            is_hit = True
            self.radius = 1  # start explode

        # collde to ground?
        if elapsed > self.max_count:
            self.radius = 1  # start explode
            for house in houses:
                if hypot(self.cpos[0] - house.rect.center[0],
                         self.cpos[1] - house.rect.center[1]) < 30:
                    house.exploded = True
        return is_hit

    def draw(self):
        """ draw missile"""
        pygame.draw.line(SURFACE, (0, 255, 255), (self.pos[0], 0), self.cpos)

        if self.radius > 0:  # exploding
            rad = self.radius if self.radius < 50 else 100 - self.radius
            pos = (int(self.cpos[0]), int(self.cpos[1]))
            pygame.draw.circle(SURFACE, (0, 255, 255), pos, rad)


class Shoot:
    """ beam object to shoot"""

    def __init__(self):

        sysfont = pygame.font.SysFont(None, 50)
        font_shoot = sysfont.render("O", False, (255, 255, 255))

        self.scope = (400, 300)
        self.image = font_shoot
        self.count = 0
        self.file = False
        self.radius = 0
        self.shot_pos = (0, 0)

    def tick(self):
        """ update position and status of beam being lanched"""
        if self.file:
            self.count += 1

            if 100 <= self.count < 200:
                self.radius += 1
            elif 200 <= self.count < 300:
                self.radius -= 1
            elif self.count >= 300:
                self.file = False
                self.count = 0

    def draw(self):
        """ draw beam"""
        rect: Rect = self.image.get_rect()
        rect.center = self.scope
        SURFACE.blit(self.image, rect)
        if not self.file:
            return

        if self.radius == 0 and self.count < 100:
            ratio = self.count / 100
            ypos = 600 - (600 - self.shot_pos[1]) * ratio
            x_left = int((self.shot_pos[0]) * ratio)
            x_right = int(800 - (800 - self.shot_pos[0]) * ratio)
            pygame.draw.line(SURFACE, (0, 255, 0), (0, 600), (x_left, ypos))
            pygame.draw.line(SURFACE, (0, 255, 0), (800, 600), (x_right, ypos))
        elif self.radius > 0:
            pygame.draw.circle(
                SURFACE, (0, 255, 0), self.shot_pos, self.radius)


pygame.init()
SURFACE = pygame.display.set_mode((800, 600))
# SURFACE = pygame.display.set_mode((1000, 1000))
FPSCLOCK = pygame.time.Clock()


def main():
    game_over = False
    missiles = []
    score = 0
    time_count = 0
    shoot = Shoot()
    houses = []

    scorefont = pygame.font.SysFont(None, 36)
    sysfont = pygame.font.SysFont(None, 72)
    s = "GAME OVER!!"
    message_over = sysfont.render(s, True, (0, 255, 225))

    message_rect: Rect = message_over.get_rect()
    message_rect.center = (400, 300)

    for index in range(13):
        houses.append(House(index * 60 + 20))
    while len(missiles) < 18:
        missiles.append(Missile())

    while True:
        time_count += 1
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                shoot.scope = event.pos
            elif event.type == MOUSEBUTTONDOWN:
                if not shoot.file:
                    shoot.shot_pos = shoot.scope
                    shoot.file = True

        # every frame processing
        exploded = len(list(filter(lambda x: x.exploded, houses)))
        game_over = exploded == 13
        if not game_over:
            for missile in missiles:
                is_hit = missile.tick(time_count, shoot, houses)
                if is_hit:
                    score += 100
            shoot.tick()

        # drawing
        SURFACE.fill((0, 0, 0))
        shoot.draw()
        for house in houses:
            house.draw()
        for missile in missiles:
            missile.draw()

        score_str = str(score).zfill(6)
        score_image = scorefont.render(score_str, True, (0, 255, 0))
        SURFACE.blit(score_image, (700, 10))

        if game_over:
            SURFACE.blit(message_over, message_rect)

        pygame.display.update()
        FPSCLOCK.tick(60)


if __name__ == '__main__':
    main()
