import pygame
#from main import *
SPEED = .25

class Player:
  pos = (0,0)
  size = (10,60)
  

  def __init__(self, screen, color, xStart):
    self.screen = screen
    self.color = color
    self.pos = (xStart, screen.get_height() / 2)

  def move(self, direction = "up"):
    print(self.pos)
    if(direction == "up"):
      self.pos = (self.pos[0], self.pos[1] - (SPEED))
    elif direction == "down":
      self.pos = (self.pos[0], self.pos[1] + SPEED)
    print(self.pos)

  def draw(self):
    pygame.draw.rect(self.screen, self.color, pygame.Rect(self.pos, self.size))