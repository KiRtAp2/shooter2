import colors
import constants
from pygame.draw import rect as draw_rect

class Base(object):

    x, y = 0, 0
    dx, dy = 0, 0
    sx, sy = constants.unknown_object_size

    def move(self, border_hit_event=0):
        """ Moves object, reutrns True if it goes out of bounds"""

        # border_hit_event:
        # 0 = don't allow
        # 1 = go through

        self.x += self.dx
        self.y += self.dy

        if border_hit_event == 0:

            # if position is out of bounds, correct it

            if self.x + self.sx > constants.frame_width: # too far right
                self.x = constants.frame_width - self.sx
                return True

            if self.x < 0: # too far left
                self.x = 0
                return True

            if self.y + self.sy > constants.frame_height: # too far down
                self.y = constants.frame_height - self.sy
                return True

            if self.y < 0: # too far up
                self.y = 0
                return True

        elif border_hit_event == 1:
            if self.x + self.sx > constants.frame_width or self.x < 0 or self.y + self.sy > constants.frame_height or self.y < 0:
                return True

        return False

    def is_hit(self, list_of_objects):
        """ Returns True if objetc is hit by an objects in list_of_objects. elements in list_of_objects must have x, y, sx, sy!"""
        for o in list_of_objects:
            if self.x < o.x+o.sx and self.x+self.sx > o.x:
                if self.y < o.y+o.sy and self.y+self.sy > o.y:
                    return True

        return False

    def show(self, window):
        """Paints a black box at x, y to sx, sy"""
        # probably needs to be overloaded, just paints a black box
        draw_rect(window, colors.black, (self.x, self.y, self.sx, self.sy))

    def is_hit_by_object(self, o):
        """Returns True if self is hit by o"""
        if self.x < o.x + o.sx and self.x + self.sx > o.x:
            if self.y < o.y + o.sy and self.y + self.sy > o.y:
                return True

        return False


