import pygame
import constants
import utils
from character import Character
import character
import colors
import bullet
import wall
from sys import exit as quit
import powerup

pygame.init()

window = pygame.display.set_mode((constants.window_width, constants.window_height))
pygame.display.set_caption("Shooter v2")
pygame.display.set_icon(pygame.image.load("textures/icon.png"))

char1 = Character(0)  # levo
char2 = Character(1)  # desno

game_clock = pygame.time.Clock()

bullet_list = []
wall_list = []
powerup_list = [powerup.Powerup.spawn()]

monospace_font = pygame.font.SysFont("monospace", constants.font_size)


def clone(x):
    a = x
    return a


def show_score():
    score_chr1 = monospace_font.render(str(char1.score), True, colors.black)
    score_chr2 = monospace_font.render(str(char2.score), True, colors.black)

    window.blit(score_chr1, (constants.window_width*0.2, constants.scoretext_position_y))
    window.blit(score_chr2, (constants.window_width*0.8, constants.scoretext_position_y))


def build(char):
    if char.wall_timer <= 0.0:
        wall_list.append(wall.Wall(char.orientation, char))
        char.set_cooldown()


def show_cooldowns():

    # char1
    if char1.wall_timer <= 0:
        window.blit(constants.wall_image,
                    (constants.distance_between_border_and_wall_cooldown_image_in_pixels, constants.scoretext_position_y))
    else:
        window.blit(constants.wall_crossed,
                    (constants.distance_between_border_and_wall_cooldown_image_in_pixels, constants.scoretext_position_y))

    #char2
    if char2.wall_timer <= 0:
        window.blit(constants.wall_image,
                    (constants.window_width - constants.distance_between_border_and_wall_cooldown_image_in_pixels,constants.scoretext_position_y))
    else:
        window.blit(constants.wall_crossed,
                    (constants.window_width - constants.distance_between_border_and_wall_cooldown_image_in_pixels,constants.scoretext_position_y))

def game_loop():

    game_running = True

    while game_running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
                quit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_w:
                    char1.dy = -character.character_default_move_speed
                if event.key == pygame.K_s:
                    char1.dy = character.character_default_move_speed
                if event.key == pygame.K_UP:
                    char2.dy = -character.character_default_move_speed
                if event.key == pygame.K_DOWN:
                    char2.dy = character.character_default_move_speed

                if event.key == pygame.K_d:
                    bullet_list.append(bullet.Bullet(1, (char1.x+char1.sx+1, char1.y+char1.sy/2)))
                if event.key == pygame.K_RIGHT:
                    bullet_list.append(bullet.Bullet(0, (char2.x-bullet.bullet_default_size_x, char2.y+char2.sy/2)))

                if event.key == pygame.K_a:
                    build(char1)
                if event.key == pygame.K_LEFT:
                    build(char2)


            if event.type == pygame.KEYUP:

                if event.key in (pygame.K_w, pygame.K_s):
                    char1.dy = 0
                if event.key in (pygame.K_UP, pygame.K_DOWN):
                    char2.dy = 0

        window.fill(colors.white)

        char1.move(0)
        char2.move(0)

        char1.show(window)
        char2.show(window)

        char1.tick()
        char2.tick()

        for b in bullet_list:
            if char1.is_hit_by_object(b):
                char2.score += 1
                bullet_list.remove(b)

            if char2.is_hit_by_object(b):
                char1.score += 1
                bullet_list.remove(b)

        for b in bullet_list:
            if b.move(1):
                bullet_list.remove(b)
            b.show(window)

        for w in wall_list:
            for b in bullet_list:
                if w.is_hit_by_object(b):
                    bullet_list.remove(b)

            w.show(window)
            if w.tick():
                wall_list.remove(w)

        for p in powerup_list:
            for b in bullet_list:
                if p.is_hit_by_object(b):
                    powerup_list.remove(p)
                    print("DEBUG: powerup hit by "+str(b.owner))
            p.show(window)

        pygame.draw.rect(window, colors.gray, (0, constants.frame_height,
                                               constants.window_width,
                                               constants.window_height - constants.frame_height))
        show_score()
        show_cooldowns()

        pygame.display.update()

        game_clock.tick(constants.framerate)



def menu_loop():

    while True:
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN or event.type==pygame.KEYDOWN:
                game_loop()
            if event.type==pygame.QUIT:
                quit()


        window.fill(colors.white)

        window.blit(constants.logo_image, (  # blits the logo to the screen
            constants.window_width*0.5-constants.logo_image_dimensions[0]//2,
            constants.window_height*0.1
        ))

        utils.show_text(
            "Press start",
            monospace_font,
            (constants.window_width*0.4, constants.window_height*0.7),
            colors.black,
            window
        )

        pygame.display.update()

        game_clock.tick(constants.framerate)


if __name__ == '__main__':
    menu_loop()
