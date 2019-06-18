import pygame
from game.actives import Vaus, Ball
from game.background import Fence
from game.bricks import Brick, BricksFactory
from shapely.geometry import LineString
from game.sounds import Effects
from game.logic import Stats
from game.hud import Hud


class Arena(Stats):
    def __init__(self, screen):
        super().__init__()
        self.chart = screen
        self.fence = Fence('voidframe.tmx')
        self.player = Vaus(bounds=(20,)).moveOn(self.chart)
        self.ball = Ball().moveOn(self.chart)
        self.ball_origin = self.ball.get_shape().center

        factory = BricksFactory()
        self.bricks = []
        self.wall(factory)
        self.wall(factory, 160)

        self.hud = Hud(self)
        self.effects = Effects(). \
            withSound('bounce', 'UI04.ogg'). \
            withSound('racket', 'UI01.ogg'). \
            withSound('break', 'Damage01.ogg'). \
            withSound('lost', 'Explosion3.ogg'). \
            withVolume(1)

    def wall(self, factory, start=64):
        for i in range(0, 21):
            self.bricks.append(Brick(factory.getBrick(factory.BLUE), position=(64+i*32, start)))
        for i in range(0, 21):
            self.bricks.append(Brick(factory.getBrick(factory.GREEN), position=(64 + i * 32, start+16)))
        for i in range(0, 21):
            self.bricks.append(Brick(factory.getBrick(factory.MAGENTA), position=(64 + i * 32, start+32)))
        for i in range(0, 21):
            self.bricks.append(Brick(factory.getBrick(factory.GREEN), position=(64 + i * 32, start+48)))
        for i in range(0, 21):
            self.bricks.append(Brick(factory.getBrick(factory.BLUE), position=(64 + i * 32, start+64)))

    def ProcessInput(self, events, pressed_keys):
        self.player.events(pressed_keys)

    def Render(self, screen):
        screen.fill((20, 20, 20))
        self.fence.render(screen, limit=1)
        self.player.output(screen)
        self.ball.output(screen)
        self.fence.render(screen, start=1)

        for brick in self.bricks:
            screen.blit(brick.image, brick.get_position())
        self.hud.Render(screen)

    def kill(self):
        self.effects.playSound('lost')
        if self.scaleLifes() > 0:
            self.ball = Ball(position=(self.player.position[0] + 40, self.player.position[1] - 5)). \
                moveOn(self.chart)
            self.ball_origin = self.ball.get_shape().center
            return True
        return False # Game over!

    def Update(self):
        if self.ball.run():
            if self.ball.position[1] > self.player.position[1] + self.player.image.get_height():
                self.kill()
            else:
                self.effects.playSound('bounce')

        shape_ball = self.emboss(self.ball.get_shape())
        if self.player.get_rect().colliderect(shape_ball):
            self.player.bounceEffect(self.ball)
            self.effects.playSound('racket')

        drop = []
        for brick in self.bricks:
            if self.bounce(shape_ball, brick.shape):
                drop.append(brick)

        for brick in drop:
            self.bricks.remove(brick)
            self.addScore(100)
            self.effects.playSound('break')
        self.ball_origin = (shape_ball.center[0] - self.ball.speed[0], shape_ball.center[1] - self.ball.speed[1])

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