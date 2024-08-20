import pygame

run = True
s_width = 1000
s_height = 600
screen_xdir = 0
screen_ydir = 0
vel_list = [5, 7, 9, 11]
block_len = 40
dragging = False
current_sprite = None
bl_img_list = ["pl_tile1.png", "pl_tile2.png",
               "rect_tile1.png",
               "sm_tile1.png", "sm_tle2.png",
               "sq_tile1.png", "sq_tile2.png", "sq_tile3.png", "sq_tile4.png",
               "gen.png",
               'lava_1.png',
               'spike_3.png',
               'fire_3.png']
id_list = ['pl1', 'pl2', 'rc', 'sm1', 'sm2', 'sq1', 'sq2', 'sq3', 'sq4', 'gem', 'lava', 'spike', 'fire']
ins_list = [True, True, True, True, True, True, True, True, True, True, True, True, True]

# Screen
screen = pygame.display.set_mode((s_width + 300, s_height))