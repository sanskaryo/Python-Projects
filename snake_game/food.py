from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
      
        self.shapesize(stretch_len=.7, stretch_wid=.7)  
        self.color("red")
        self.speed("fast")
        self.refresh()

    def refresh(self):
        self.color(random.choice(["red", "blue", "green", "yellow", "orange"]))
        random_x = random.randint(-260, 270)
        random_y = random.randint(-260, 270)  
        self.goto(random_x, random_y)
