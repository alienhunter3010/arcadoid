import pygame
from etc.setup import Setup
from game.sprite import Sprite
from game.text import Write


class Hud(Sprite):

    def __init__(self, stats):
        super().__init__(pygame.image.load(Setup.images + 'vaus-static.png'))
        self.stats = stats
        self.lifeIconPos = ((60, 12))

        self.lifesBox = Write(). \
            withFont("kenpixel", 16). \
            withAlign((Write.LEFT, Write.TOP)). \
            withMargin((120, -20)). \
            withColor((250, 250, 250))

        self.scoreBox = Write(). \
            withFont("kenpixel", 16). \
            withAlign((Write.RIGHT, Write.TOP)). \
            withMargin((40, -20)). \
            withColor((250, 250, 250))

    def Render(self, screen):
        screen.blit(self.image, self.lifeIconPos)
        self.lifesBox.withText('x {}'.format(self.stats.lifes)).onScreen(screen).render()
        self.scoreBox.withText(self.stats.score).onScreen(screen).render()
