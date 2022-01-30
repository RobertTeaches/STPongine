import pygame
from pygame import key
from pygame.event import pump
from pygame.locals import *
import numpy
import random
from ball import Ball
from player import Player
from scoreboard import Scoreboard

#CONSTS
W_KEY = pygame.K_w
S_KEY = pygame.K_s
UP_KEY = pygame.K_UP
DOWN_KEY = pygame.K_DOWN

pygame.init()

def player_won(leftPlayer):
    pass




surface = pygame.display.set_mode((400,400))
leftPlayer = Player(surface, (155,0,0), surface.get_width() * .1)
rightPlayer = Player(surface, (0,0,155), surface.get_width() * .9)
scoreboard = Scoreboard(surface, player_won)
ball = Ball(surface)
keep_playing = True
clock = pygame.time.Clock()
deltaTime = 0


    

while(keep_playing):
    deltaTime = clock.tick(144) / 1000
    #base events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           keep_playing = False
           pygame.quit()
           break
    if not keep_playing: break
    #clearing screen
    surface.fill((0,0,0))

    #input
    keys = pygame.key.get_pressed()

    #moving lPlayer
    if(keys[W_KEY]):
        leftPlayer.move("up", deltaTime)
    elif keys[S_KEY] and not keys[W_KEY]:
        leftPlayer.move("down", deltaTime)
    
    #moving rPlayer
    if keys[UP_KEY] and not keys[DOWN_KEY]: rightPlayer.move("up", deltaTime)
    elif not keys[UP_KEY] and keys[DOWN_KEY]: rightPlayer.move("down", deltaTime)

    ball.update(deltaTime)
    ball.draw()
    leftPlayer.draw()
    rightPlayer.draw()
    scoreboard.write_score()
    #Collisions
    if(ball.collision_check(leftPlayer.pos, leftPlayer.size)):
       ball.velocity = (((abs(ball.velocity[0]) + 50)), ball.velocity[1] + (random.randint(-50, 50) * numpy.sign(ball.velocity[1])))

    elif ball.collision_check(rightPlayer.pos, rightPlayer.size):
       ball.velocity = (-(abs(ball.velocity[0]) + 50), ball.velocity[1]+ (random.randint(-50, 50) * numpy.sign(ball.velocity[1])))
    print(ball.velocity)
    if ball.pos[0] < 1:
        selfleftPlayer = Player(surface, (155,0,0), surface.get_width() * .1)
        rightPlayer = Player(surface, (0,0,155), surface.get_width() * .9)
        ball = Ball(surface)
        scoreboard.playerScored(True)
    elif ball.pos[0] + ball.size >= surface.get_width():
        selfleftPlayer = Player(surface, (155,0,0), surface.get_width() * .1)
        rightPlayer = Player(surface, (0,0,155), surface.get_width() * .9)
        ball = Ball(surface)
        scoreboard.playerScored(False)

    pygame.display.flip()
