from turtle import Turtle 
import time


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.player_a_score = 0
        self.player_b_score = 0
        self.color("yellow")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Player A: {self.player_a_score}  Player B: {self.player_b_score}", align="center", font=("Retro Gaming", 20, "normal"))

  
    def a_win(self):
        self.clear()
        self.write(F"Player A won the game 🏆🔥"  , align="center", font=("Retro Gaming", 20, "normal"))
   
    def b_win(self):
        self.clear()
        self.write(F"Player B won the game 🏆🔥"  , align="center", font=("Retro Gaming", 20, "normal"))
   

    
    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over - Press r to restart", align="center", font=("Retro Gaming", 20, "normal"))
        


    
    
    def increase_score_a(self):
        self.player_a_score += 1
        self.update_score()

    def increase_score_b(self):
        self.player_b_score += 1
        self.update_score()
        
        
    