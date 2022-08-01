from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
H_UP = 90
H_DOWN = 270
H_LEFT = 180
H_RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        
    # Create a snake body
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        squ = Turtle('square')
        squ.color('#8899A6')
        squ.penup()
        squ.goto(position)
        self.segments.append(squ)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    # Snake Segments on Screen
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
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