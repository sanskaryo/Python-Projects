from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
      
        self.x_move = 13
        self.y_move = 13

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        
    def bounce_x(self):
        self.x_move *= -1
        
    def reset(self): 
        self.goto(0,0) 
        self.bounce_x()
        self.x_move = 13 
        self.y_move = 13
        

