import pygame
from etc.setup import Setup


class Write:
    CENTER = 0
    TOP = 1
    LEFT = 1
    BOTTOM = -1
    RIGHT = -1
    margin = 10
    align = (0, -1)
    color = (200, 200, 200)
    shadow = False

    def withFont(self, font, size=18):
        self.font = pygame.font.Font("{}/{}.ttf".format(Setup.fonts, font), size)
        return self

    def withMargin(self, margin):
        self.margin = tuple(margin) if isinstance(margin, list) else margin
        return self

    def withAlign(self, align):
        self.align = align
        return self

    def withColor(self, color):
        self.color = color
        return self

    def withText(self, text):
        self.text = text
        return self

    def withShadow(self, offset):
        self.shadow = offset
        return self

    def onScreen(self, screen):
        self.screen = screen
        return self

    def withAbsolutePosition(self, xy):
        self.xy = xy
        return self

    def positionByAlign(self, canvasLen, itemLen, align=0, margin=0):
        if align == 0:
            return canvasLen // 2 - itemLen // 2
        p = margin * align
        if align < 0:
            p += canvasLen - itemLen
        return p

    def render(self):
        rows = self.text.split("\n") if isinstance(self.text, str) else (self.text, )
        height = -1

        for row in rows:
            text = self.font.render(str(row), True, self.color)

            try:
                x = self.xy[0]
            except AttributeError:
                x = self.positionByAlign(self.screen.get_width(), text.get_width(),
                                         align=self.align[0],
                                         margin=(self.margin[0] if isinstance(self.margin, tuple) else self.margin))

            if height < 0:
                height = text.get_height() * len(rows) + 10 * (len(rows) - 1)
                try:
                    y = self.xy[1]
                except AttributeError:
                    y = self.positionByAlign(self.screen.get_height(), height,
                                             align=self.align[1],
                                             margin=(self.margin[1] if isinstance(self.margin, tuple) else self.margin))
                    y += text.get_height() * self.align[1]
            else:
                y += text.get_height() + 10
            self.output(text, (x, y), rawText=row)

    def output(self, text, xy, rawText=''):
        if self.shadow:
            shadow = self.font.render(rawText, True, self.shadow[2] if len(self.shadow) > 2 else
                (self.color[0]-50, self.color[1]-50, self.color[2]-50))
            self.screen.blit(shadow, (xy[0] + self.shadow[0], xy[1] + self.shadow[1]))

        self.screen.blit(text, xy)
