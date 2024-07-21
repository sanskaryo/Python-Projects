from turtle import Screen , Turtle
import turtle
from ball import Ball
import time
from score import Score

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=700)
screen.title("sanskar's pong game")

# paddle A
paddle_a = Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)
paddle_a._tracer(0)


#paddle B
paddle_b = Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)
paddle_b._tracer(0)

max_score = 5
# The baall

ball = Ball()

score = Score()


# go up down paddle a 

# go_up
def paddle_a_go_up():
    new_y = paddle_a.ycor() + 25
    paddle_a.goto(paddle_a.xcor(), new_y)

# go_down
def paddle_a_go_down():
    new_y = paddle_a.ycor() - 25
    paddle_a.goto(paddle_a.xcor(), new_y)

# go up down paddle b

# go_up
def paddle_b_go_up():
    new_y = paddle_b.ycor() + 25
    paddle_b.goto(paddle_b.xcor(), new_y)

# go_down
def paddle_b_go_down():
    new_y = paddle_b.ycor() - 25
    paddle_b.goto(paddle_b.xcor(), new_y)

screen.onkey(paddle_a_go_up, "w")
screen.onkey(paddle_a_go_down, "s")

screen.onkey(paddle_b_go_up, "o")
screen.onkey(paddle_b_go_down, "k")


def restart_game():
    
    score.update_score()
    ball.reset()


screen.onkey(restart_game, "r")


screen.listen()
#mainloop

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    
# detect collision with walls

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

# detecting collesion with paddle a

    if (
        ball.distance(paddle_a) < 50
        and paddle_a.xcor() - 25 < ball.xcor() < paddle_a.xcor() + 25
    ):
        ball.bounce_x()
       

    # detect collision with paddle_b
    if (
        ball.distance(paddle_b) < 50
        and paddle_b.xcor() - 25 < ball.xcor() < paddle_b.xcor() + 25
    ):
        ball.bounce_x()
        
        
        
    #detect when right paddle pad a misses the balll
    
    if ball.xcor() > 380:
        score.increase_score_a()
        
        ball.reset()
        
    #detect when left paddle pad b misses the balll
    
    if ball.xcor() < -380:
        score.increase_score_b()
        ball.reset()
        
    if score.player_a_score == max_score :
        score.game_over()
        score.a_win()
        game_on = False
    
    
    elif score.player_b_score == max_score:
        score.game_over()
        score.b_win()
        game_on = False
    
        
    
    
    def restart_game():
    # Reset scores and any other game variables
       score.update_score()
       ball.reset()
    

# Key binding for restart (customize the key if needed)
    screen.listen()
    screen.onkey(restart_game, "r")
    # detect
    
screen.listen()




screen.exitonclick()
screen.mainloop()