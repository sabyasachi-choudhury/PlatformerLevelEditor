# Imports
import pygame.mouse
from pygame.locals import *

from Variables import *

# Main init
pygame.init()


# Square
class Square(pygame.sprite.Sprite):
    def __init__(self, img, y, id):
        super(Square, self).__init__()
        self.surf = pygame.transform.smoothscale(pygame.image.load(img).convert(), (2 * block_len, 2 * block_len))
        self.surf.set_colorkey((0, 0, 0))
        self.rect = self.surf.get_rect(center=(s_width + 100, y))
        self.id = id


# Rectangle
class Rectangle(pygame.sprite.Sprite):
    def __init__(self, img, y, id):
        super(Rectangle, self).__init__()
        self.surf = pygame.transform.smoothscale(pygame.image.load(img).convert(), (2 * block_len, block_len))
        self.rect = self.surf.get_rect(center=(s_width + 100, y))
        self.id = id
        self.img = img


# Small
class Small(pygame.sprite.Sprite):
    def __init__(self, img, x, y, id):
        super(Small, self).__init__()
        self.surf = pygame.transform.smoothscale(pygame.image.load(img).convert(), (block_len, block_len))
        self.surf.set_colorkey((0, 0, 0))
        self.rect = self.surf.get_rect(center=(x, y))
        self.id = id
        self.img = img


# Pillar
class Pillar(pygame.sprite.Sprite):
    def __init__(self, img, x, y, id):
        super(Pillar, self).__init__()
        self.surf = pygame.transform.smoothscale(pygame.image.load(img).convert(), (block_len, 2 * block_len))
        self.rect = self.surf.get_rect(center=(x, y))
        self.id = id
        self.img = img


# Player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.transform.smoothscale(pygame.image.load("player.png").convert(), (int(1.2*block_len), int(1.8*block_len)))
        self.rect = self.surf.get_rect(center=(s_width+100, s_height))
        self.surf.set_colorkey((0, 0, 0))
        self.id = 'player'


# Lava
class Lava(pygame.sprite.Sprite):
    def __init__(self):
        super(Lava, self).__init__()
        self.surf = pygame.transform.smoothscale(pygame.image.load("lava_1.png").convert(), (2*block_len, block_len))
        self.rect = self.surf.get_rect(center=(s_width+200, 180))
        self.surf.set_colorkey((0, 0, 0))
        self.id = 'lava'


# Spike
class Spike(pygame.sprite.Sprite):
    def __init__(self):
        super(Spike, self).__init__()
        self.surf = pygame.transform.smoothscale(pygame.image.load("spike_3.png").convert(), (2*block_len, 2*block_len))
        self.rect = self.surf.get_rect(center=(s_width+200, 270))
        self.surf.set_colorkey((0, 0, 0))
        self.id = 'spike'


# Fire
class Fire(pygame.sprite.Sprite):
    def __init__(self):
        super(Fire, self).__init__()
        self.surf = pygame.transform.smoothscale(pygame.image.load("fire_3.png").convert(), (2*block_len, block_len))
        self.rect = self.surf.get_rect(center=(s_width+200, 350))
        self.id = 'fire'
        self.surf.set_colorkey((0, 0, 0))


# all the needed groups and lists
player = Player()
pal_group = pygame.sprite.Group\
    (
     Pillar("pl_tile1.png", s_width + 70, 45, 'pl1'), Pillar("pl_tile2.png", s_width + 130, 45, 'pl2'),
     Rectangle("rect_tile1.png", 110, 'rc'),
     Square("sq_tile1.png", 175, 'sq1'), Square("sq_tile2.png", 270, 'sq2'),
     Square("sq_tile3.png", 365, 'sq3'), Square("sq_tile4.png", 460, 'sq4'),
     Small("sm_tile1.png", s_width + 70, 525, 'sm1'), Small("sm_tile2.png", s_width + 130, 525, 'sm2'),
     Small("gem.png", s_width+200, 100, 'gem'),
     Lava(),
     Spike(),
     Fire(),
     player
     )

sandbox = pygame.sprite.Group()
all_elem = pygame.sprite.Group()
for block in pal_group:
    all_elem.add(block)

para_list = [
    ("pl_tile1.png", s_width + 70, 45, 'pl1'), ("pl_tile2.png", s_width + 130, 45, 'pl2'),
    ("rect_tile1.png", 110, 'rc'),
    ("sm_tile1.png", s_width + 70, 525, 'sm1'), ("sm_tile2.png", s_width + 130, 525, 'sm2'),
    ("sq_tile1.png", 175, 'sq1'), ("sq_tile2.png", 270, 'sq2'), ("sq_tile3.png", 365, 'sq3'),
    ("sq_tile4.png", 460, 'sq4'),
    ("gem.png", s_width+200, 100, 'gem'),
    (),
    (),
    ()
]
class_list = [Pillar, Pillar, Rectangle, Small, Small, Square, Square, Square, Square, Small, Lava, Spike, Fire]


def drag_drop(event, body, drag_state, c_sprite):
    global rel_x, rel_y
    mouse_pos = pygame.mouse.get_pos()

    if event.type == MOUSEBUTTONDOWN:
        if body.rect.collidepoint(mouse_pos):
            drag_state = True
            c_sprite = body
            rel_x, rel_y = mouse_pos[0] - c_sprite.rect.centerx, mouse_pos[1] - c_sprite.rect.centery

    if event.type == MOUSEBUTTONUP:
        drag_state = False

    if event.type == MOUSEMOTION:
        if drag_state:
            sandbox.add(c_sprite)
            pal_group.remove(c_sprite)
            c_sprite.rect.center = (mouse_pos[0] - rel_x, mouse_pos[1] - rel_y)
            for i in range(len(id_list)):
                if c_sprite.id == id_list[i]:
                    ins_list[i] = False

    return drag_state, c_sprite


def replenish(pos_check_list):
    for ind, bol in enumerate(pos_check_list, 0):
        if not pos_check_list[ind]:
            new = class_list[ind](*para_list[ind])
            pos_check_list[ind] = True
            pal_group.add(new)
            all_elem.add(new)