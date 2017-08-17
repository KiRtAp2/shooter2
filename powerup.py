import random
from pygame.image import load as image
import base_class
import constants
import utils

powerup_types = (
    #'null',
    #'speed',
    #'tripleshot',
    #'bulletspeed',
    'points',
    #'ignorewalls',
)

powerup_textures = {
    'null' : image("textures/powerup/null.png"),
    'speed' : image("textures/powerup/speed.png"),
    'tripleshot' : image("textures/powerup/tripleshot.png"),
    'bulletspeed' : image("textures/powerup/ammospeed.png"),
    'points' : image("textures/powerup/points.png"),
    'ignorewalls' : image("textures/powerup/ignorewalls.png"),
}

class Powerup(base_class.Base):

    type = "null"
    # "null" = debug. No effect
    # "speed" = speed buff
    # "tripleshot" = triple shot
    # "blletspeed" = bullet speed buff
    # "points" = double points
    # "ignorewalls" = bullets ignore walls

    time_remaining = constants.framerate*10 # ticks

    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type
        self.sx = self.sy = 50

    def __init__(self):

        # random init
        self.x, self.y = utils.random_position()
        self.type = random.choice(powerup_types)
        self.sx = self.sy = 50

    @staticmethod
    def spawn(pos=(-1,-1), type=''):
        if pos[0]==-1:
            spawned_powerup = Powerup()
        else:
            spawned_powerup = Powerup(x,y = pos, type=type)

        return spawned_powerup

    def show(self, window):
        try:
            window.blit(powerup_textures[self.type], (self.x, self.y))
        except KeyError:
            super().show(window)

    def tick(self):
        """Returns true if it's time to destroy the object"""
        self.time_remaining -= 1
        if self.time_remaining <= 0:
            return True
