import pygame

class Scoreboard:
  left_player_score = 0
  right_player_score = 0
  WINNING_SCORE = 5
  #THIS IS THE FUNCTION YOU NEED TO WRITE
  def playerScored(self, leftPlayer = True):
    print(leftPlayer)


#utility/display functions
  def __init__(self, screen, p_won_func): 
    self.screen = screen
    self.main_p_won = p_won_func
    self.font = pygame.font.SysFont('chalkduster.ttf', 24)

  


  def write_score(self):
    img = self.font.render("P1: " + str(self.left_player_score) + " vs P2: " + str(self.right_player_score), True, (255,255,255))
    self.screen.blit(img, (self.screen.get_width()/2 - 50, self.screen.get_height() * .1))
  
  def player_won(self, leftPlayer = True):
    self.main_p_won(leftPlayer)
  