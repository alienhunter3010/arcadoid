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


class Set(Sprite):
    def __init__(self, image=None, cells=(3, 4)):
        self.image = None
        self.sprites = {}
        if image is None:
            super().__init__()
        else:
            self.loadSet(image=image, cells=cells)
            super().__init__(image=self.sprites[0][0])

    def addImage(self, img, key=0):
        if key in self.sprites:
            self.sprites[key].append(img)
        else:
            self.sprites[key] = [img]

    def addSprite(self, imageChart, origin=(0, 0), size=(32, 32), row=0):
        sprite = imageChart.subsurface(pygame.Rect(origin, size))
        self.addImage(sprite, row)
        if self.image is None:
            self.image = sprite

    def loadSet(self, image=None, cells=(3, 4)):
        imageChart = self.loadImage(image)
        frameWidth = imageChart.get_width() // cells[0]
        frameHeight = imageChart.get_height() // cells[1]
        for y in range(0, cells[1]):
            for x in range(0, cells[0]):
                self.addSprite(imageChart, origin=(x*frameWidth, y*frameHeight), size=(frameWidth, frameHeight), row=y)
