import random
import pygame
from settings import *
from sprites import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True


    def new(self):
        self.score = 0
        self.all_sprites = pygame.sprite.Group()
        self.pipes = pygame.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
