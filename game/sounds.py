import os

import pygame
from etc.setup import Setup


class Effects:
    abspath = '.'

    @staticmethod
    def init(abspath):
        if pygame.get_sdl_version()[0] == 2:
            pygame.mixer.pre_init(22100, -16, 2, 16)
        else:
            pygame.mixer.init(22100, -16, 2, 16)
        Effects.abspath = abspath

    def __init__(self):
        self.bases = {}

    def withMusic(self, music):
        pygame.mixer.music.load(os.path.join(Setup.sounds, music))
        return self

    def withSound(self, key, sound):
        self.bases[key] = pygame.mixer.Sound(os.path.join(Effects.abspath, Setup.sounds, sound))
        return self

    def withVolume(self, volume):
        pygame.mixer.music.set_volume(volume)
        return self

    def playMusic(self, times):
        pygame.mixer.music.play(times)
        return self

    def playSound(self, key):
        if key in self.bases:
            self.bases[key].play()
        return self