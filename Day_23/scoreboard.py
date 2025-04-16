FONT = ("Courier", 16, "bold")


from turtle import Turtle

class Scoreboard(Turtle):

        def __init__(self):
            super().__init__()
            self.score = 0
            self.r_score = 0
            self.color("black")
            self.penup()
            self.hideturtle()
            self.update_score()

        def update_score(self):
            self.clear()
            self.goto(-290, 270)
            self.write(arg=f"Score:{self.score}", move=False, align="left", font=FONT)

        def scored(self):
            self.score += 1
            self.update_score()

        def game_over(self):
            self.goto(0, 0)
            self.write(arg="GAME OVER", move=False, align="center", font=("Arial", 24, "bold"))
