import base_class
import constants

default_wall_height = 80
default_wall_width = 20
default_distance_between_char_and_wall = 30
wall_default_despawn_time = 5*constants.framerate # ticks/frames

class Wall(base_class.Base):

    def __init__(self, orientation, char):

        # orientation:
        # 0 = left chracter
        # 1 = right character

        self.y = (char.y + char.sy / 2) - (default_wall_height / 2)

        if orientation == 0:
            self.x = (char.x+default_distance_between_char_and_wall+char.sx)
        elif orientation == 1:
            self.x = (char.x-default_distance_between_char_and_wall)

        self.sx = default_wall_width
        self.sy = default_wall_height

        self.despawn_time = wall_default_despawn_time

    def tick(self):
        """Returns True if wall should dissapear, ticks off time"""
        self.despawn_time -= 1
        if self.despawn_time == 0:
            return True
        return False
