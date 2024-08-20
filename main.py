# Imports
import pygame.display

from Grid_stuff import *
from background_stuff import *
from Blocks import *
from Variables import *

# Main init
pygame.init()


# Final compile
def gen_result(render):
    global run
    result = []
    lefts = []
    for block in render:
        lefts.append(block.rect.left)
    fin_mo = -min(lefts)
    for sprite in render:
        sprite.rect.move_ip(fin_mo, 0)
        details = [sprite.id, sprite.rect.centerx, sprite.rect.centery]
        result.append(details)
    print(result)
    run = False


# Main loop
while run:
    # Fill
    screen.fill((73, 96, 101))
    # Presses
    presses = pygame.key.get_pressed()
    # Event detection
    for event in pygame.event.get():
        if event.type == QUIT:
            gen_result(sandbox)
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                gen_result(sandbox)
            if event.key == K_BACKSPACE:
                current_sprite.kill()
            if event.key == K_c:
                for ind in range(len(id_list)):
                    if id_list[ind] == current_sprite.id:
                        copy = class_list[ind](*para_list[ind])
                        copy.rect.center = (current_sprite.rect.centerx + current_sprite.rect.width,
                                            current_sprite.rect.centery)
                        all_elem.add(copy)
                        sandbox.add(copy)
                        current_sprite = copy
        for block in all_elem:
            dragging, current_sprite = drag_drop(event, block, dragging, current_sprite)

    # Bg direction
    if presses[K_RIGHT]:
        screen_xdir = -1
    if presses[K_LEFT]:
        screen_xdir = 1
    if presses[K_UP]:
        screen_ydir = 1
    if presses[K_DOWN]:
        screen_ydir = -1

    # Parallax motion
    parallax(screen_xdir, screen_ydir)

    # Replenishment of pallete sprites
    replenish(ins_list)

    # Cave bg motion
    cave_ambiance.rect.move_ip(0, screen_ydir * vel_list[2])

    # Clear common centers in pal_sprites
    for a in pal_group:
        for b in pal_group:
            if a != b and a.rect.center == b.rect.center:
                a.kill()

    # Clear common centers in vert_lines
    for a in vert_lines:
        for b in vert_lines:
            if a != b and a.rect.center == b.rect.center:
                a.kill()

    # Getting relative round degree
    for x in vert_lines:
        if -1 < x.rect.centerx < block_len:
            rel_round = -x.rect.centerx

    # Moving sandbox sprites
    for s in sandbox:
        s.rect.move_ip(vel_list[3] * screen_xdir, vel_list[2] * screen_ydir)
        if not dragging and s.id != 'player':
            for l in vert_lines:
                if l.rect.centerx-8 < s.rect.left < l.rect.centerx+8:
                    s.rect.left = l.rect.centerx
                if l.rect.centerx-8 < s.rect.right < l.rect.centerx+8:
                    s.rect.right = l.rect.centerx
            for l in hor_lines:
                if l.rect.top-8 < s.rect.top < l.rect.top+8:
                    s.rect.top = l.rect.centery
                if l.rect.bottom-8 < s.rect.bottom < l.rect.bottom+8:
                    s.rect.bottom = l.rect.centery

    """-------------------------------------------------BLIT STUFF---------------------------------------------------"""

    # Background renders. Remember to put this before other blit statements
    screen.blit(cave_ambiance.surf, cave_ambiance.rect)
    for x in layer_list:
        for y in x:
            screen.blit(y.surf, y.rect)

    # EVERYTHING ABOUT GRIDS
    # grid stuff
    grid()
    # grid blit and move
    for m in vert_lines:
        screen.blit(m.surf, m.rect)
        m.rect.move_ip(screen_xdir * vel_list[3], 0)
    for b in hor_lines:
        screen.blit(b.surf, b.rect)
        b.rect.move_ip(0, screen_ydir*vel_list[2])

    # Sandbox elements blit
    for elem in sandbox:
        if elem.id == 'lava':
            screen.blit(elem.surf, elem.rect)
        else:
            screen.blit(elem.surf, elem.rect)

    # Drawing board
    pygame.draw.rect(screen, (252, 148, 73), (s_width, 0, 300, s_height))

    # Palette elements blit
    for elem in pal_group:
        screen.blit(elem.surf, elem.rect)

    # Flip
    pygame.display.flip()
    pygame.time.Clock().tick(100)

    # Reset
    screen_xdir = 0
    screen_ydir = 0

# quit
pygame.quit()
# Add lava to para list and modify the stuff