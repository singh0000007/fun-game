from turtle import Turtle

move_dist = 20
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for position in starting_positions:
            self.add_segment(position)


    def add_segment(self , position):
        t = Turtle("square")
        t.color("white")
        t.penup()
        t.goto(position)
        self.segment.append(t)


    def extend(self):
        self.add_segment(self.segment[-1].position())


    def move(self):
        for i in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[i - 1].xcor()
            new_y = self.segment[i - 1].ycor()
            self.segment[i].goto(new_x, new_y)
        self.head.forward(move_dist)

    def up(self):

        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):

        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):

        if  self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):

        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
