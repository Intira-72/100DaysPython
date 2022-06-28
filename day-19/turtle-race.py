from random import random
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color:')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink']
turtle_positions = [100, 70, 40, 10, -20, -50, -80]
all_turtles = []
is_race_on = False

for i in range(len(colors)):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=turtle_positions[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 238:
            if turtle.pencolor() == user_bet:
                print(f"You've won! the {turtle.pencolor()} turtle is the winner!!!")
            else:
                print(f"You've lose! the {turtle.pencolor()} turtle is the winner!!!")
            is_race_on = False

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()