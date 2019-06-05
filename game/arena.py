from game.actives import Vaus


class Arena:
    def __init__(self, chart):
        self.chart = chart
        self.player = Vaus(bounds=(20,)).moveOn(self.chart)

    def ProcessInput(self, events, pressed_keys):
        self.player.events(pressed_keys)

    def Render(self, screen):
        screen.fill((20, 20, 20))
        self.player.output(screen)

    def Update(self):
        pass
