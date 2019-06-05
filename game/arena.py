import pygame
from game.actives import Vaus, Ball


class Arena:
    def __init__(self, chart):
        self.chart = chart
        self.player = Vaus(bounds=(20,)).moveOn(self.chart)
        self.ball = Ball(bounds=(20,)).moveOn(self.chart)

    def ProcessInput(self, events, pressed_keys):
        self.player.events(pressed_keys)

    def Render(self, screen):
        screen.fill((20, 20, 20))
        self.player.output(screen)
        self.ball.output(screen)

        shape_ball = self.emboss(self.ball.get_shape())
        if self.player.get_rect().colliderect(shape_ball):
            self.player.bounceEffect(self.ball)

    def Update(self):
        self.ball.run()

    def emboss(self, rect):
        return pygame.Rect((rect.left -1, rect.top -1), (rect.width +2, rect.height +2))