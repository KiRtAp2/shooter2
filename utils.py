import pygame
import random

import constants


def show_text(text, font, position, color, window):
    text_field = font.render(text, True, color)
    window.blit(text_field, position)

def random_position():
    return (random.randrange(constants.frame_start_x, constants.frame_width), random.randrange(constants.frame_start_y, constants.frame_height))