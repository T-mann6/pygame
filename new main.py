import pygame as pg
from sprites import *

class Game():
    def __init__(self): # kjører når vi starter spillet
       pg.init()
       self.WHITE = (255,255,255)
       self.BLACK = (0,0,0)
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
        self.pokemon = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.red = Player()
        self.mewtwo = Mewtwo()
        self.giovanni = Giovanni()
        self.all_sprites.add(self.red, self.mewtwo, self.giovanni)
        self.pokemon.add(self.mewtwo)
        self.enemies.add(self.giovanni)
        self.i=0
        self.red.caught = 0
        self.giovanni.caught = 0
        self.red_caught = self.comic_sans30.render("You caught: " + str(self.red.caught), False, self.WHITE)
        self.enemy_caught = self.comic_sans30.render("Enemy caught: " + str(self.giovanni.caught), False, self.WHITE)
        self.game_over = False
        if self.game_over:
            self.game_over_loop()
        self.You_Won = False
        if self.You_Won:
            self.You_Won_loop()
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
            hero_hits = pg.sprite.spritecollide(self.red, self.pokemon, True)
            if hero_hits:
                self.red.caught += 1
                self.red_caught = self.comic_sans30.render("You caught: " + str(self.red.caught), False, self.WHITE)
                if self.red.caught >= 150:
                    self.You_Won_loop()
            
            giovanni_hits = pg.sprite.spritecollide(self.giovanni, self.pokemon, True)
            if giovanni_hits:
                self.giovanni.caught += 1
                self.enemy_caught = self.comic_sans30.render("Enemy caught: " + str(self.giovanni.caught), False, self.WHITE)
                if self.giovanni.caught >= 150:
                    self.game_over_loop()

            if len(self.pokemon) < 1:
                self.mewtwo = Mewtwo()
                self.all_sprites.add(self.mewtwo)
                self.pokemon.add(self.mewtwo)
            self.screen.blit(self.red_caught,(10,10))
            self.screen.blit(self.enemy_caught,(700,10))
            self.all_sprites.draw(self.screen)
            pg.display.update()
        
    def game_over_loop(self):
        self.game_over = True
        while self.game_over:
            self.clock.tick(self.FPS)
            self.game_over_text=self.comic_sans30.render("GAME OVER, Too bad", False, self.WHITE)
            self.game_restart_text=self.comic_sans30.render("Want to try again, Press Ctrl R to restart", False, self.WHITE)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.game_over = False

                if event.type == pg.KEYDOWN: 
                    if event.key == pg.K_r and pg.key.get_mods() & pg.KMOD_LCTRL:
                        self.game_over = False

            self.screen.blit(self.game_over_text, (self.WIDTH/2 - self.game_over_text.get_width()/2, 400))
            self.screen.blit(self.game_restart_text, (self.WIDTH/2 - self.game_restart_text.get_width()/2, self.HEIGHT/2))
            pg.display.update()

        self.new()
    
    def You_Won_loop(self):
        self.You_Won = True
        while self.You_Won:
            self.clock.tick(self.FPS)
            self.game_over_text=self.comic_sans30.render("You beat Team Rocket, Congratulations", False, self.WHITE)
            self.game_restart_text=self.comic_sans30.render("Want to try again, Press Ctrl R to restart", False, self.WHITE)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.You_Won = False
                if event.type == pg.KEYDOWN: 
                    if event.key == pg.K_r and pg.key.get_mods() & pg.KMOD_LCTRL:
                        self.You_Won = False

            self.screen.blit(self.game_over_text, (self.WIDTH/2 - self.game_over_text.get_width()/2, 400))
            self.screen.blit(self.game_restart_text, (self.WIDTH/2 - self.game_restart_text.get_width()/2, self.HEIGHT/2))
            pg.display.update()

        self.new()

g = Game()