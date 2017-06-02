import pygame


# **********************
# ***** BASE CLASS *****
# **********************

class BaseClass(pygame.sprite.Sprite):

    # *********************
    # ***** VARIABLES *****
    # *********************

    allsprites = pygame.sprite.Group()

    # ****************************************
    # ****************************************

    # ****************
    # ***** INIT *****
    # ****************

    def __init__(self, x, y, width, height, image_string):
        pygame.sprite.Sprite.__init__(self)
        BaseClass.allsprites.add(self)

        self.image = pygame.image.load(image_string)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height

        # ****************************************
        # ****************************************


# *********************
# ***** BUG CLASS *****
# *********************

class Bug(BaseClass):

    # *********************
    # ***** VARIABLES *****
    # *********************

    List = pygame.sprite.Group()

    # ****************************************
    # ****************************************

    # ****************
    # ***** INIT *****
    # ****************

    def __init__(self, x, y, width, height, image_string):
        BaseClass.__init__(self, x, y, width, height, image_string)
        Bug.List.add(self)
        self.vel_x = 0

    # ****************************************
    # ****************************************

    # ******************
    # ***** MOTION *****
    # ******************

    def motion(self, SCREENWIDTH):

        predicted_location = self.rect.x + self.vel_x

        if predicted_location < 0:
            self.vel_x = 0
        elif predicted_location + self.width > SCREENWIDTH:
            self.vel_x = 0

        self.rect.x += self.vel_x
