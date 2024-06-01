from turtle import Turtle

class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("yellow")
        self.penup()
        with open("highscore.txt") as highscore:
            self.high_score = int(highscore.read())
        self.goto(0, 180)
        self.hideturtle()
        self.update_score()
    
  
    
    def update_score(self):
        self.clear()
        
        self.write(f"Score: {self.score} High Score : {self.high_score}", align="center", font=("Retro Gaming", 20, "normal"))


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscore.txt") as data:
                data.write(f"{self.high_score}")
            
        self.score = 0
        self.update_score()
    
    
    def inc_score(self):
        self.score += 1
        
        self.update_score()

        
   