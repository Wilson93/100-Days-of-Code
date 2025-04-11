UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
from turtle import Turtle

class Snake:
    def __init__(self):
        self.all_turtles = []
        self.create_snake()
        self.head = self.all_turtles[0]

    # Create snake body
    def create_snake(self):
        for turtle_index in range(0, 2):
            position = (0 + (-20 * turtle_index), 0)
            self.add_segment(position)

    # make turtles follow in-line
    def move(self):
        for turtles in range(len(self.all_turtles) - 1, 0, -1):
            new_x = self.all_turtles[turtles - 1].xcor()
            new_y = self.all_turtles[turtles - 1].ycor()
            self.all_turtles[turtles].goto(new_x, new_y)
        self.head.forward(20)

    # add segments to snake body
    def add_segment(self, position):
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.all_turtles.append(new_turtle)

    # extend snake body
    def extend(self):
        self.add_segment(self.all_turtles[-1].position())

    # reset snake
    def reset(self):
        for turtles in self.all_turtles:
            turtles.goto(1000, 1000)
        self.all_turtles.clear()
        self.create_snake()
        self.head = self.all_turtles[0]

    # create movement methods
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)