from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#15202b")
screen.title("3310 Snake Game.")
screen.tracer(0)

# Create a snake body
starting_pos = [(0, 0), (-20, 0), (-40, 0)]

segnents = []

for s in starting_pos:
    squ = Turtle('square')
    squ.color('#8899A6')
    squ.penup()
    squ.goto(s)
    segnents.append(squ)

# Snake Segments on Screen
game_is_no = True

while game_is_no:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(segnents) - 1, 0, -1):
        new_x = segnents[seg_num - 1].xcor()
        new_y = segnents[seg_num - 1].ycor()
        segnents[seg_num].goto(new_x, new_y)
    segnents[0].forward(20)        
        

screen.exitonclick()