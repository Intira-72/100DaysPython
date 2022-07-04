from this import d
from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
H_UP = 90
H_DOWN = 270
H_LEFT = 180
H_RIGHT = 0

class Snake:
    def __init__(self):
        self.segnents = []
        self.create_snake()
        self.head = self.segnents[0]
        
    # Create a snake body
    def create_snake(self):
        for s in STARTING_POSITIONS:
            squ = Turtle('square')
            squ.color('#8899A6')
            squ.penup()
            squ.goto(s)
            self.segnents.append(squ)

    # Snake Segments on Screen
    def move(self):
        for seg_num in range(len(self.segnents) - 1, 0, -1):
            new_x = self.segnents[seg_num - 1].xcor()
            new_y = self.segnents[seg_num - 1].ycor()
            self.segnents[seg_num].goto(new_x, new_y)
        self.head .forward(MOVE_DISTANCE)


    def up(self):
        if self.head.heading() != H_DOWN:
            self.head.setheading(H_UP)

    def down(self):
        if self.head.heading() != H_UP:
            self.head.setheading(H_DOWN)

    def left(self):
        if self.head.heading() != H_RIGHT:
            self.head.setheading(H_LEFT)

    def right(self):
        if self.head.heading() != H_LEFT:
            self.head.setheading(H_RIGHT)