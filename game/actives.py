import pygame
from game.live import LiveItem
from game.sprite import Sprite


class Vaus(LiveItem):
    def __init__(self, bounds=(0,)):
        super().__init__('vaus-static.png', position=(400, 550), speed=(12, 0), bounds=bounds)

    def bounce_here(self, position, shape):
        return shape.collidepoint((position[0], shape.y + 2))

    def bounceEffect(self, ball):
        if self.bounce_here(ball.position,
                            pygame.Rect(self.position, (10, self.image.get_height()))):
            ball.speed = list(ball.ONO)
        elif self.bounce_here(ball.position,
                              pygame.Rect((self.position[0] + 10, self.position[1]), (10, self.image.get_height()))):
            ball.speed = list(ball.NNO)
        elif self.bounce_here(ball.position,
                              pygame.Rect((self.position[0] + self.image.get_width() - 10, self.position[1]),
                                          (10, self.image.get_height()))):
            ball.speed = list(ball.ENE)
        elif self.bounce_here(ball.position,
                              pygame.Rect((self.position[0] + self.image.get_width() - 20, self.position[1]),
                                          (10, self.image.get_height()))):
            ball.speed = list(ball.NNE)
        else:
            ball.onYBounce()

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


class Ball(LiveItem):
    NNE = (2, -4)
    ENE = (4, -2)
    NNO = (-2, -4)
    ONO = (-4, -2)
    SSE = (2, 4)
    ESE = (4, 2)
    SSO = (-2, 4)
    OSO = (-4, 2)

    def __init__(self, bounds=(0,)):
        super().__init__('ball.png', position=(414, 446), speed=[2, -4], bounds=bounds)

    def get_shape(self):
        return pygame.Rect(self.position, (self.image.get_width(), self.image.get_height()))

    def onXBounce(self):
        self.speed[0] *= -1

    def onYBounce(self):
        self.speed[1] *= -1

    def run(self):
        dx = self.speed[0]
        dy = self.speed[1]
        return self.move(dx, dy)

    def output(self, screen):
        self.render(screen, Sprite.update(self))
