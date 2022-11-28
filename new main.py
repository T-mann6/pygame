import pygame as pg
from sprites import *

class Game():
    def __init__(self): # kjører når vi starter spillet
       pg.init()
       self.WHITE = (255,255,255)
       self.WIDTH = 1000
       self.HEIGHT = 1000
       self.screen = pg.display.set_mode((self.WIDTH,self.HEIGHT))
       self.bg = pg.image.load("background.png").convert_alpha()
       self.BG = pg.transform.scale(self.bg, (self.WIDTH,self.HEIGHT))
       self.comic_sans30 = pg.font.SysFont("Comic Sans MS", 30)
       self.FPS = 120
       self.clock = pg.time.Clock()       
       self.new()
    def new(self): # ny runde, kjører f. eks. når vi dør
        self.all_sprites = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.hero = Player()
        self.mewtwo = Mewtwo()
        self.all_sprites.add(self.hero, self.mewtwo)
        self.enemies.add(self.mewtwo)
        self.i=0
        self.hero.caught = 0
        self.Pokemon_caught = self.comic_sans30.render("Pokémon caught: " + str(self.hero.caught), False, self.WHITE)
        self.run()
    def run(self): # mens vi spiller, game loop er her
        playing = True
        while playing: # game loop
            self.clock.tick(self.FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    playing = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_r and pg.key.get_mods() &pg.K_LCTRL:
                        self.new()
            self.screen.blit(self.BG,(self.i,0))# tegner bakgrunn
            self.all_sprites.update()
            hits = pg.sprite.spritecollide(self.hero, self.enemies, True)
            if hits:
                self.hero.caught += 1
                self.Pokemon_caught = self.comic_sans30.render("Pokémon caught: " + str(self.hero.caught), False, self.WHITE)
                if self.hero.caught >= 150:
                    self.new()
            if len(self.enemies) < 1:
                self.mewtwo = Mewtwo()
                self.all_sprites.add(self.mewtwo)
                self.enemies.add(self.mewtwo)
            self.screen.blit(self.Pokemon_caught,(10,10))
            self.all_sprites.draw(self.screen)
            pg.display.update()

g = Game()