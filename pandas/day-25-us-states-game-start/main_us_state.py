import turtle 
import numpy as np
import pandas as pd

screen = turtle.Screen()
screen.title("us state game - sk")

image = r"D:\sankhu codes and stuff\angela yu course\python\pandas\day-25-us-states-game-start\blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

def get_mouse(x,y):
    print(x,y)
    
turtle.onscreenclick(get_mouse)

answer_state = screen.textinput(title="guess the state's name", prompt="what is the state's name ?")

screen.mainloop()






