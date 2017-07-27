import pygame

def show_text(text, font, position, color, window):

    text_field = font.render(text, True, color)
    window.blit(text_field, position)
