import constants
import base_class

character_default_move_speed = 5 # pixels/tick
character_default_wall_cooldown = constants.framerate*15
character_boosted_move_speed = 8 # pixels/tick

default_effect_durations = {
    'speed' : 10*constants.framerate,
    'tripleshot' : 10*constants.framerate,
    'bulletspeed' : 10*constants.framerate,
    'points' : 10*constants.framerate,
    'ignorewalls' : 10*constants.framerate,
}

class Character(base_class.Base):

    image = constants.default_image
    sx = sy = 49
    wall_timer = 0 #ticks/frames
    current_move_speed = character_default_move_speed

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

        self.effect_durations = {
            "speed": -1,
            "tripleshot": -1,
            "bulletspeed": -1,
            "points": -1,
            "ignorewalls": -1,
        }

    def show(self, window):
        window.blit(self.image, (self.x, self.y))

    def set_cooldown(self):
        self.wall_timer = character_default_wall_cooldown

    def tick(self):
        self.wall_timer -= 1
        if self.effect_durations["speed"] > -1: self.effect_durations["speed"] -= 1
        if self.effect_durations["tripleshot"] > -1: self.effect_durations["tripleshot"] -= 1
        if self.effect_durations["bulletspeed"] > -1: self.effect_durations["bulletspeed"] -= 1
        if self.effect_durations["points"] > -1: self.effect_durations["points"] -= 1
        if self.effect_durations["speed"] < 1 and self.current_move_speed==character_boosted_move_speed:
            self.unboost_speed()

    def start_movement(self, direction):
        if direction == -1:
            self.dy = -self.current_move_speed
        if direction == 1:
            self.dy = self.current_move_speed

    def boost_speed(self):
        self.current_move_speed = character_boosted_move_speed
        self.effect_durations["speed"] = constants.framerate*10

    def unboost_speed(self):
        self.current_move_speed = character_default_move_speed

    def shoot(self, bullet_class, pos):
        if self.orientation == 0:
            orientation = 1
        else:
            orientation = 0

        vel_coeff = constants.bullet_default_velocity
        if self.effect_durations["bulletspeed"] > -1:
            vel_coeff = constants.bullet_boosted_velocity

        bullets = [
            bullet_class(orientation, pos, vel_coeff),
        ]

        if self.effect_durations["tripleshot"]>-1:
            bullets.append(
                bullet_class(orientation, (pos[0], pos[1]+40), vel_coeff)
            )
            bullets.append(
                bullet_class(orientation, (pos[0], pos[1] - 40), vel_coeff)
            )

        return bullets

    def boost_general(self, effect):
        self.effect_durations[effect] = default_effect_durations[effect]


    def score_multiplier(self):
        if self.effect_durations["points"] > -1: return 2
        else: return 1
