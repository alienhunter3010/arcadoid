import pygame
from game.actives import Vaus, Ball
from game.bricks import Brick, BricksFactory
from shapely.geometry import LineString


class Arena:
    def __init__(self, chart):
        self.chart = chart
        self.player = Vaus(bounds=(20,)).moveOn(self.chart)
        self.ball = Ball(bounds=(20,)).moveOn(self.chart)
        self.ball_origin = self.ball.get_shape().center

        factory = BricksFactory()
        self.bricks = []
        self.wall(factory)
        self.wall(factory, 160)

    def wall(self, factory, start=64):
        for i in range(0, 20):
            self.bricks.append(Brick(factory.getBrick(factory.BLUE), position=(64+i*32, start)))
        for i in range(0, 20):
            self.bricks.append(Brick(factory.getBrick(factory.GREEN), position=(64 + i * 32, start+16)))
        for i in range(0, 20):
            self.bricks.append(Brick(factory.getBrick(factory.MAGENTA), position=(64 + i * 32, start+32)))
        for i in range(0, 20):
            self.bricks.append(Brick(factory.getBrick(factory.GREEN), position=(64 + i * 32, start+48)))
        for i in range(0, 20):
            self.bricks.append(Brick(factory.getBrick(factory.BLUE), position=(64 + i * 32, start+64)))

    def ProcessInput(self, events, pressed_keys):
        self.player.events(pressed_keys)

    def Render(self, screen):
        screen.fill((20, 20, 20))
        self.player.output(screen)
        self.ball.output(screen)

        shape_ball = self.emboss(self.ball.get_shape())
        if self.player.get_rect().colliderect(shape_ball):
            self.player.bounceEffect(self.ball)

        drop = []
        for brick in self.bricks:
            if self.bounce(shape_ball, brick.shape):
                drop.append(brick)
                continue
            screen.blit(brick.image, brick.get_position())

        for brick in drop:
            self.bricks.remove(brick)
        self.ball_origin = (shape_ball.center[0] - self.ball.speed[0], shape_ball.center[1] - self.ball.speed[1])

    def Update(self):
        self.ball.run()

    def emboss(self, rect):
        return pygame.Rect((rect.left -1, rect.top -1), (rect.width +2, rect.height +2))

    def bounce(self, shape_ball, shape):
        strike = LineString([self.ball_origin, shape_ball.center])
        # going down
        if self.ball.speed[1] > 0:
            top = LineString([shape.topleft, shape.topright])
            if strike.crosses(top):
                self.ball.onYBounce()
                return True
        # going up
        else:
            bottom = LineString([shape.bottomleft, shape.bottomright])
            if strike.crosses(bottom):
                self.ball.onYBounce()
                return True
        # going right
        if self.ball.speed[0] > 0:
            left = LineString([shape.topleft, shape.bottomleft])
            if strike.crosses(left):
                self.ball.onXBounce()
                return True
        # going left
        else:
            right = LineString([shape.topright, shape.bottomright])
            if strike.crosses(right):
                self.ball.onXBounce()
                return True
        return False