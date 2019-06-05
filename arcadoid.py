import pygame
import time
from etc.setup import Setup
from game.arena import Arena


class Arcadoid:

    def __init__(self, fps, screen_dim=(800, 600)):
        self.fps = fps
        pygame.init()
        pygame.display.set_caption('Arcadoid')
        pygame.display.set_icon(pygame.image.load(Setup.images + 'icon.png' ))
        self.screen = pygame.display.set_mode(screen_dim, pygame.SRCALPHA)
        self.clock = pygame.time.Clock()
        self.scene = Arena(self.screen)

    def events(self, pressed_keys):
        filtered_events = []
        for event in pygame.event.get():
            quit_attempt = False
            if event.type == pygame.QUIT:
                quit_attempt = True
            elif event.type == pygame.KEYDOWN:
                alt_pressed = pressed_keys[pygame.K_LALT] or \
                              pressed_keys[pygame.K_RALT]
                if event.key == pygame.K_ESCAPE:
                    quit_attempt = True
                elif event.key == pygame.K_F4 and alt_pressed:
                    quit_attempt = True

            if quit_attempt:
                exit(0)
            else:
                filtered_events.append(event)
        return filtered_events

    def run(self):
        while True:
            pressed_keys = pygame.key.get_pressed()
            filtered_events = self.events(pressed_keys)

            self.scene.ProcessInput(filtered_events, pressed_keys)
            self.scene.Update()
            self.scene.Render(self.screen)

            pygame.display.flip()
            self.clock.tick(self.fps)


if __name__ == "__main__":
    app = Arcadoid(48)
    app.run()
