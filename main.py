import pygame
from pygame import key
from pygame.event import pump
from pygame.locals import *
from ball import Ball
from player import Player
import scoreboard

#CONSTS
W_KEY = pygame.K_w
S_KEY = pygame.K_s
UP_KEY = pygame.K_UP
DOWN_KEY = pygame.K_DOWN


surface = pygame.display.set_mode((400,400))
leftPlayer = Player(surface, (155,0,0), surface.get_width() * .1)
rightPlayer = Player(surface, (155,0,0), surface.get_width() * .9)
ball = Ball(surface)
keep_playing = True


while(keep_playing):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           keep_playing = False
           pygame.quit()
           break
    surface.fill((0,0,0))
    print("test")
    keys = pygame.key.get_pressed()
    for k in keys: 
        if k: 
            print(k)
    if(keys[W_KEY]):
        leftPlayer.move("up")
    elif keys[S_KEY] and not keys[W_KEY]:
        leftPlayer.move("down")
    
    if keys[UP_KEY] and not keys[DOWN_KEY]: rightPlayer.move("up")
    elif not keys[UP_KEY] and keys[DOWN_KEY]: rightPlayer.move("down")


    leftPlayer.draw()
    rightPlayer.draw()
    pygame.display.flip()
