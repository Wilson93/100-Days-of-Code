from turtle import Turtle
UP = 90
DOWN = 270
class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.paddle(x, y)

    def paddle(self, x, y):
        self.shape("square")
        self.color("white")
        self.setheading(UP)
        self.turtlesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.setpos(x, y)

    # create movement methods
    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)
