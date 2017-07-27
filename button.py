import base_class

class Button(base_class.Base):

    sreen_on_which_located = "menu"

    def __init__(self, position, size, screen="menu"):

        self.screen_on_which_located = screen
        self.x = position[0]
        self.y = position[1]
        self.sx = size[0]
        self.sy = size[1]


    @staticmethod
    def show_all(blist, screen):
        for b in blist:
            if b.sreen_on_which_located == screen:
                b.show()