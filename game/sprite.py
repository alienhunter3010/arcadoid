import pygame
from etc.setup import Setup


class Sprite:
    def __init__(self, image=None):
        self.image = self.loadImage(image)

    def loadImage(self, image):
        return None if image is None else \
            image if isinstance(image, pygame.Surface) else \
            pygame.transform.scale2x(pygame.image.load(Setup.images + image))

    def update(self):
        return self.image
