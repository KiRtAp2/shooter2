import constants
import base_class

bullet_default_size_x = 8
bullet_default_size_y = 4
bullet_default_velocity = 15 # pixels/tick

class Bullet(base_class.Base):

    sx = bullet_default_size_x
    sy = bullet_default_size_y

    #def show(self):
    # no need to overload

    def __init__(self, direction, position):
        # direction:
        # 0 = moving to the left
        # 1 = moving to the right

        if direction == 0:
            self.dx = -bullet_default_velocity
        elif direction == 1:
            self.dx = bullet_default_velocity

        self.x, self.y = position