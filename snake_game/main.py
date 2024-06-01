from turtle import Screen
from snake import Snake
import time
from food import Food
from score import Score


screen = Screen()
screen.setup(width=600, height = 600)
screen.bgcolor("black")
screen.title("made with ❤️‍🔥 by sanskar bhai")
screen.tracer(0)


scoreboard = Score()
snake = Snake()
food=Food()



screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")




game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    
#detect collision
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.inc_score()
        snake.extend()
        
        
        
# detect colide with bhaal

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset(
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            33
        )
    

#detect head tail collisiuon

    for segment in snake.segments[1:]:  
        if snake.head.distance(segment) < 10:  
           scoreboard.reset() 
           snake.reset()
    
screen.exitonclick()
        

  
screen.mainloop()