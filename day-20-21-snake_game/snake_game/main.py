from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#15202b")
screen.title("3310 Snake Game.")

# Create a snake body
starting_pos = [(0, 0), (-20, 0), (-40, 0)]

for s in starting_pos:
    squ = Turtle('square')
    squ.color('#8899A6')
    squ.goto(s)

screen.exitonclick()