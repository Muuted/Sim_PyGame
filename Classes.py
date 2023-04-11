import pygame


class WaterDrops(pygame.sprite.Sprite):

    def _init_(self, color, width, height, xv, yv, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.colors = color
        self.width = width
        self.height = height
        self.xv = xv
        self.yv = yv
        self.x = x
        self.y = y


    pass


class Board(pygame.sprite.Sprite):
    def _init_(self, color, width, height, xv, yv, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.colors = color
        self.width = width
        self.height = height
        self.xv = xv
        self.yv = yv
        self.x = x
        self.y = y


    pass


if __name__ == "__main__":
    pass
