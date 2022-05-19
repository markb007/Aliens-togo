import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, ai_game):
        # initialise bullet object and set location to the middle of the
        #  top of the ship
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        # create bullet rect 0,0 then set to correct location. Bullet is
        #  not from an image so we have to create the rect from scratch
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        # draw the bullet to the screen
        pygame.draw.rect(self.screen, self.color, self.rect)
        