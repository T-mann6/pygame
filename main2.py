import pygame as pg
from random import randint

pg.init()

WHITE = (255,255,255)
BLUE = (0,0,255)

screen = pg.display.set_mode((1000,1000))
player_img = pg.image.load("Idle2.png")
player_img = pg.transform.scale(player_img, (100,100))

x = 0
y = 0

speed = 5

direction_x = 1
direction_y = 1
color = (randint(0,255),randint(0,255),randint(0,255))

FPS = 120
clock = pg.time.Clock()
playing = True
while playing: # game loop
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False
    
    screen.fill(BLUE)# tegner bakgrunn
    screen.blit(player_img, (x,y))
    
    
    keys = pg.key.get_pressed()

    if keys[pg.K_w]:
        y -= speed
    if keys[pg.K_s]:
        y += speed
    if keys[pg.K_a]:
        x -= speed
    if keys[pg.K_d]:
        x += speed




    if x > 900:
        x = 900
        
    if x < 0:
        x = 0
        
    if y > 900:
        y = 900
        
    if y < 0:
        y = 0
    pg.display.update()
