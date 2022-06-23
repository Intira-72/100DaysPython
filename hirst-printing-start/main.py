from itertools import count
from turtle import Turtle, Screen
import colorgram
import random

def colors_set():
    colors = colorgram.extract('pic.jpg', 6)
    rgb_color = []

    for c in colors:
        r = c.rgb.r
        g = c.rgb.g
        b = c.rgb.b

        new_color = (r, g, b)
        rgb_color.append(new_color)

    return rgb_color

tim = Turtle()
tim.speed('fastest')
tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)

screen = Screen()
screen.colormode(255)

colors = colors_set()
count_dot = 0

for _ in range(10):    
    for _ in range(10): 
        tim.dot(20, random.choice(colors))        
        tim.forward(50) 
        count_dot += 1 

    if count_dot % 10 == 0:  
        tim.left(90)
        tim.forward(50)
        tim.left(90)
        tim.forward(500)
        tim.right(180)


screen.exitonclick()
 