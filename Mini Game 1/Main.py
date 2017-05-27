import pygame
import sys

from classes import *
from process import process


# ****************
# ***** INIT *****
# ****************

pygame.init()

# *****
# ***** DATA *****
# *****

# SCREEN
# ------

SCREENWIDTH, SCREENHEIGHT = 640, 360
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT), 0, 32)

# CLOCK
# -----

clock = pygame.time.Clock()
FPS = 24
fives_second_interval = FPS * 5
total_frames = 0

# GRAPHIC
# -------

clr1 = (22, 122, 211)
clr2 = (240, 44, 166)
clr3 = (34, 55, 245)

# COUNT
# -----

i = 0

# OBJECTS
# -------

bug = Bug(0, SCREENHEIGHT - 40, 45, 36, "assets/img/fly-001.png")

# ****************************************
# ****************************************

# *********************
# ***** MAIN LOOP *****
# *********************

while True:

    # *********************
    # ***** PROCESSES *****
    # *********************

    process(bug)

    # ****************************************
    # ****************************************

    # *****************
    # ***** LOGIC *****
    # *****************

    bug.motion()

    # ****************************************
    # ****************************************

    # ****************
    # ***** DRAW *****
    # ****************

    screen.fill((0, 0, 0))
    BaseClass.allsprites.draw(screen)

    # ****************************************
    # ****************************************

    # *******************
    # ***** DISPLAY *****
    # *******************

    pygame.display.flip()

    # ****************************************
    # ****************************************

    # ****************
    # ***** TICK *****
    # ****************

    clock.tick(FPS)
