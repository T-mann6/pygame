import pygame as pg
from sprites import *

pg.init()

WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)
BLACK = (0,0,0)

WIDTH = 1000
HEIGHT = 1000

all_sprites = pg.sprite.Group()
enemies = pg.sprite.Group()

hero = Player()
enemy = Enemy()
all_sprites.add(hero, enemy)
enemies.add(enemy)

screen = pg.display.set_mode((WIDTH,HEIGHT))
bg = pg.image.load("background.png").convert_alpha()
bg_img = pg.transform.scale(bg, (WIDTH,HEIGHT))

i=0
FPS = 120
clock = pg.time.Clock()
comic_sans30 = pg.font.SysFont("Comic Sans MS", 30)
hero.life = 50
text_hp = comic_sans30.render("HP:" + str(hero.caught), False, BLACK)

playing = True
while playing: # game loop
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False
    
    screen.blit(bg_img,(i,0))# tegner bakgrunn
    all_sprites.update()
    
    hits = pg.sprite.spritecollide(hero, enemies, True)
    if hits:
        hero.caught += 1
        text_hp = comic_sans30.render("HP:" + str(hero.caught), False, BLACK)
            
    if len(enemies) < 1:
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)

    screen.blit(text_hp,(10,10))
    all_sprites.draw(screen)

    pg.display.update()