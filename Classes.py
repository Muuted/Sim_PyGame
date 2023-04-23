import pygame
from pygame.math import Vector2
import random

Screen_height = 720
Screen_width = 1280
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
    def _init_(self, vx,vy):
        super(Board,self).__init__()
        pygame.sprite.Sprite.__init__(self)

        pos = random.randint(0, Screen_width),0
        self.pos = Vector2(pos)
        self.velocity = Vector2(vx,vy)

        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(0, SCREEN_WIDTH),
                -a
            )
        )

    def draw(self,window):
        pygame.draw.rect(window,self.color,(self.x, self.y, self.width, self.height))



if __name__ == "__main__":
    pass
