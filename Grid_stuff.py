import pygame.sprite

from Variables import *

pygame.init()


# Vertical lines
class Vertical(pygame.sprite.Sprite):
    def __init__(self, x):
        super(Vertical, self).__init__()
        self.surf = pygame.Surface((1, s_height))
        self.rect = self.surf.get_rect(center=(x, s_height/2))
        self.surf.fill((255, 255, 255))


# Horizontal lines
class Horizontal(pygame.sprite.Sprite):
    def __init__(self, y):
        super(Horizontal, self).__init__()
        self.surf = pygame.Surface((s_width, 1))
        self.rect = self.surf.get_rect(center=(s_width/2, y))
        self.surf.fill((255, 255, 255))


# Groups
vert_lines = pygame.sprite.Group()
vert_start = pygame.sprite.Group()
vert_end = pygame.sprite.Group()
hor_lines = pygame.sprite.Group()
hor_top = pygame.sprite.Group()
hor_bottom = pygame.sprite.Group()

# Creation of vertical lines
for ind, x in enumerate(range(0, s_width+1, block_len), 1):
    line = Vertical(x)
    vert_lines.add(line)
    if ind == 1:
        vert_start.add(line)

for q, w in enumerate(vert_lines, 1):
    if q == len(vert_lines):
        vert_end.add(w)

# Creation of horizontal lines
for ind, y in enumerate(range(0, s_height+1, block_len), 1):
    h_line = Horizontal(y)
    hor_lines.add(h_line)
    if ind == 1:
        hor_top.add(h_line)

for q, w in enumerate(hor_lines, 1):
    if q == len(vert_lines):
        hor_bottom.add(w)


def grid():
    global vert_lines, vert_start, vert_end, hor_lines, hor_top, hor_bottom
    # # Vertical lines stuff
    # Add to start
    for y in vert_end:
        if y.rect.centerx > s_width:
            new_start = Vertical(y.rect.centerx - s_width)
            vert_lines.add(new_start)
            vert_start = pygame.sprite.Group(new_start)
            y.kill()
            for n in vert_lines:
                if n.rect.centerx > (s_width - block_len):
                    vert_end.add(n)
    # Adding to end
    for z in vert_start:
        if z.rect.centerx < 0:
            new_end = Vertical(z.rect.centerx + s_width)
            vert_lines.add(new_end)
            vert_end = pygame.sprite.Group(new_end)
            z.kill()
            for n in vert_lines:
                if n.rect.centerx < block_len:
                    vert_start.add(n)

    # Horizontal line stuff
    # Add to top
    for p in hor_bottom:
        if p.rect.centery > s_height:
            new_top = Horizontal(p.rect.centery - s_height)
            hor_lines.add(new_top)
            hor_top = pygame.sprite.Group(new_top)
            p.kill()
            for n in hor_lines:
                if n.rect.centery > (s_height - block_len):
                    hor_bottom.add(n)

    # Adding to bottom
    # Adding to end
    for q in hor_top:
        if q.rect.centery < 0:
            new_bottom = Horizontal(q.rect.centery + s_height)
            hor_lines.add(new_bottom)
            hor_bottom = pygame.sprite.Group(new_bottom)
            q.kill()
            for n in hor_lines:
                if n.rect.centery < block_len:
                    hor_top.add(n)