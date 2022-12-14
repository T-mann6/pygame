import pygame as pg
from random import randint

vec = pg.math.Vector2

player_img = pg.image.load("red.png")
player_img = pg.transform.scale(player_img, (100,150))
mewtwo_img = pg.image.load("mewtwo enemy.png")
mewtwo_img = pg.transform.scale(mewtwo_img, (200,200))
team_rocket_boss_img = pg.image.load("giovanni.png")
giovanni_img = pg.transform.scale(team_rocket_boss_img, (100,150))

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = player_img
        self.rect = self.image.get_rect()
        self.pos = vec(100,100)
        self.rect.center = self.pos
        self.caught = 0
        self.speed = 5
    def update(self):
        self.rect.center = self.pos
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.pos.y -= self.speed
        if keys[pg.K_s]:
            self.pos.y += self.speed
        if keys[pg.K_d]:
            self.pos.x += self.speed
            self.image = pg.transform.flip(player_img, True, False)
        if keys[pg.K_a]:
            self.pos.x -= self.speed
            self.image = pg.transform.flip(player_img, False, False)
class Mewtwo(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = mewtwo_img
        self.rect = self.image.get_rect()
        self.pos = vec(-1100,randint(0,900))
        self.rect.center = self.pos
        self.speed = 5
    def update(self):
        self.rect.center = self.pos
        self.pos.x -= self.speed
        if self.pos.x < -100:
            self.pos.x = 1100
            self.pos.y = randint(0,900)
class Giovanni(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = giovanni_img
        self.rect = self.image.get_rect()
        self.pos = vec(10,10)
        self.rect.center = self.pos
        self.speed = 10
        self.caught = 0
    def update(self):
        self.rect.center = self.pos
        self.pos.y -= self.speed
        if self.pos.y < -100:
            self.pos.y = 1100
            self.pos.x = randint(0,900)
        self.pos.x -= self.speed
        if self.pos.x < -100:
            self.pos.x = 1100
            self.pos.y = randint(0,900)