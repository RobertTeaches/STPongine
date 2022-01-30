from main import *
class Scoreboard:
  left_player_score = 0
  right_player_score = 0

  #THIS IS THE FUNCTION YOU NEED TO WRITE
  def playerScored(self, leftPlayer = True):
    pass

#utility/display functions
  def __init__(self, screen): 
    self.screen = screen


  def write_score(self):
    pass
  
  def player_won(self, leftPlayer = True):
    main.player_won(leftPlayer)
  