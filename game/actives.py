import pygame
from game.live import LiveItem
from game.sprite import Sprite


class Vaus(LiveItem):
    def __init__(self, bounds=(0,)):
        super().__init__('vaus-static.png', position=(400, 550), speed=(12, 0), bounds=bounds)

    def events(self, pressed):
        if self.freeze:
            return
        dx = 0
        if pressed[pygame.K_LEFT]:
            dx -= self.speed[0]
        elif pressed[pygame.K_RIGHT]:
            dx += self.speed[0]
        self.move(dx, 0)

    def event(self, event):
        pass

    def output(self, screen):
        self.render(screen, Sprite.update(self))
