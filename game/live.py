import pygame
from game.sprite import Sprite


class Movable:

    def __init__(self, position=(30, 30), speed=3):
        self.position = list(position)
        self.speed = list(speed)

    def moveOn(self, chart):
        self.chart = chart
        return self

    def render(self, screen, fragment):
        screen.blit(fragment, self.position)

    def update_position(self, delta=(0, 0)):
        self.position = [self.position[0] + delta[0], self.position[1] + delta[1]]

    def move(self, dx, dy):
        if abs(dx) + abs(dy) == 0:
            return False
        return self.update_position((dx, dy))


class LiveItem(Movable, Sprite):
    def __init__(self, image, position=(10, 10), speed=(5, 5), bounds=(0,)):
        Movable.__init__(self, position=position, speed=speed)
        Sprite.__init__(self, image)
        self.freeze = False
        self.bounds = bounds if len(bounds) < 4 else \
            (bounds[0], bounds[1], bounds[2] - self.image.get_width(), bounds[3] - self.image.get_height())

    def moveOn(self, chart):
        # css like
        if len(self.bounds) == 1:
            self.bounds = (self.bounds[0], self.bounds[0],
                           chart.get_width() - self.bounds[0] - self.image.get_width(),
                           chart.get_height() - self.bounds[0] - self.image.get_height())
        elif len(self.bounds) == 2:
            self.bounds = (self.bounds[0], self.bounds[1],
                           chart.get_width() - self.bounds[0] - self.image.get_width(),
                           chart.get_height() - self.bounds[1] - self.image.get_height())
        elif len(self.bounds) == 3:
            self.bounds = (self.bounds[0], self.bounds[1],
                           chart.get_width() - self.bounds[0] - self.image.get_width(),
                           chart.get_height() - self.bounds[2] - self.image.get_height())
        else:
            self.bounds = (self.bounds[0], self.bounds[1],
                           chart.get_width() - self.bounds[2] - self.image.get_width(),
                           chart.get_height() - self.bounds[3] - self.image.get_height())

        return Movable.moveOn(self, chart)

    def get_rect(self):
        return pygame.Rect(self.position, (self.image.get_width(), self.image.get_height()))

    def onXBounce(self):
        pass

    def onYBounce(self):
        pass

    def update_position(self, delta=(0, 0)):
        bounce = False
        if self.position[0] + delta[0] < self.bounds[0]:
            self.position[0] = self.bounds[0]
            self.onXBounce()
            bounce = True
        elif self.position[0] + delta[0] > self.bounds[2]:
            self.position[0] = self.bounds[2]
            self.onXBounce()
            bounce = True
        else:
            self.position[0] = self.position[0] + delta[0]

        if self.position[1] + delta[1] < self.bounds[1]:
            self.position[1] = self.bounds[1]
            self.onYBounce()
            bounce = True
        elif self.position[1] + delta[1] > self.bounds[3]:
            self.position[1] = self.bounds[3]
            self.onYBounce()
            bounce = True
        else:
            self.position[1] = self.position[1] + delta[1]
        return bounce
