from pygame.image import load as image

window_width = 1200
window_height = window_width//16*9

frame_width = window_width
frame_height = window_height*0.8
frame_start_y = 0
frame_start_x = 0

scoretext_position_y = frame_height+(window_height-frame_height)*0.4

unknown_object_size = (5,5)

default_image = image("textures/orb_default.png")
wall_image = image("textures/wall/wall_default.png")
wall_used_image = image("textures/wall/wall_gray.png")
wall_crossed = image("textures/wall/wall_gray_crossed.png")
logo_image = image("textures/logo.png")

logo_image_dimensions = (800,300)

font_size = 35

framerate = 60

distance_between_border_and_wall_cooldown_image_in_pixels = frame_width*0.1

bullet_boosted_velocity = 30 # pixels/tick
bullet_default_velocity = 15 # pixels/tick

powerup_spawn_delay = 45*1000 # miliseconds
