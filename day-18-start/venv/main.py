from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape('turtle')
timmy.color('#088F8F')

def random_rgb():
    return(random.random(), random.random(), random.random())


def spirograph(size_of_gap):
    round_move = int(360 / size_of_gap) + 1    

    for i in range(1, round_move):
        rand_color = random_rgb()
        timmy.color(rand_color)
        timmy.pencolor(rand_color)
        timmy.speed('fastest')

        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)


def draw_a_random_walk():
    directions = [0, 90, 180, 270, 360]
    timmy.pensize(10)
    timmy.speed('fastest')

    for _ in range(200):
        timmy.color(random_rgb())
        timmy.pencolor(random_rgb())

        timmy.setheading(random.choice(directions))
        timmy.forward(30)


def draw_shape():
    for i in range(3, 11):
        timmy.color(random_rgb())
        timmy.pencolor(random_rgb())
        for a in range(i):
            timmy.fd(100)
            timmy.right(360/i)

# for i in range(10):
#     if i % 2:
#         timmy.pendown()
#     else:
#         timmy.penup()
#     timmy.forward(10)

# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)

if __name__=='__main__':
    spirograph(2)


screen = Screen()
screen.exitonclick()