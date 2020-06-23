import pygame
from settings import *
from pygame.locals import *

vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super(Player, self).__init__()
        self.game = game
        self.rect = pygame.Surface(40, 20)
        self.rect.fill(FLAPPY_ORANGE)
        self.pos = vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
