import constants
import base_class

character_default_move_speed = 5 # pixels/tick
character_default_wall_cooldown = constants.framerate*15


class Character(base_class.Base):

    image = constants.default_image
    sx = sy = 49
    wall_timer = 0 #ticks/frames

    def __init__(self, pos):

        self.score = 0

        #pos:
        # 0 = left
        # 1 = right
        if pos==0:
            self.x = constants.frame_width*0.1
            self.y = constants.frame_height*0.45+constants.frame_start_y

        elif pos==1:
            self.x = constants.frame_width*0.85
            self.y = constants.frame_height*0.45+constants.frame_start_y

        self.orientation = pos

    def show(self, window):
        window.blit(self.image, (self.x, self.y))

    def set_cooldown(self):
        self.wall_timer = character_default_wall_cooldown

    def tick(self):
        self.wall_timer -= 1
