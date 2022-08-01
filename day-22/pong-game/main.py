from turtle import Screen
from paddle import Paddle
from ball import Ball
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("#15202b")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((380, 0))
l_paddle = Paddle((-387, 0))

ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    ball.b_move()

    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.bounce_y()

    if (ball.distance(r_paddle) < 50 and ball.xcor() > 350) or (ball.distance(l_paddle) < 60 and ball.xcor() < -360):
        ball.bounce_x()

    if ball.xcor() > 380 or ball.xcor() < -390:
        ball.home()


screen.exitonclick()