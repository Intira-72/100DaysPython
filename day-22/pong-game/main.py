from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("#15202b")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((370, 0))
l_paddle = Paddle((-380, 0))

ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()    
    ball.b_move()

    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.bounce_y()

    if (ball.distance(r_paddle) < 50 and ball.xcor() > 340) or (ball.distance(l_paddle) < 60 and ball.xcor() < -350):
        ball.bounce_x()

    if ball.xcor() > 380:
        score.l_points()
        ball.reset_position()
        
    elif ball.xcor() < -390:
        score.r_points()
        ball.reset_position()


screen.exitonclick()