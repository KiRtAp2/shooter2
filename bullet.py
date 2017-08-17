import constants
import base_class

bullet_default_size_x = 8
bullet_default_size_y = 4

class Bullet(base_class.Base):

    sx = bullet_default_size_x
    sy = bullet_default_size_y

    #def show(self):
    # no need to overload

    def __init__(self, direction, position, velocity=constants.bullet_default_velocity, ignorewalls=False):
        # direction:
        # 0 = moving to the left, owner=right
        # 1 = moving to the right, owner=left
        self.owner = direction

        if direction == 0:
            self.dx = -velocity
        elif direction == 1:
            self.dx = velocity

        self.x, self.y = position

        self.ignorewalls = ignorewalls