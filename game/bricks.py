import pygame
from game.sprite import Set


class Brick:
    def __init__(self, image, unbreakable=False, position=(0, 0)):
        self.image = image
        self.unbreakable = unbreakable
        self.shape = pygame.Rect((position[0] - 2, position[1] - 2), (self.image.get_width() + 4, self.image.get_height() + 4))

    def get_position(self):
        return self.shape.left, self.shape.top

    def collision(self, position):
        return self.shape.collidepoint(position)


class BricksFactory(Set):
    WHITE = 0
    ORANGE = 1
    CYAN = 2
    GREEN = 3
    MAGENTA = 4
    BLUE = 5
    PINK = 6
    GRAY = 7

    def __init__(self):
        super().__init__(image='blocks.png', cells=(1, 9))

    def getBrick(self, idx):
        return self.sprites[idx][0]
