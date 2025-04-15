from turtle import Turtle

class Scoreboard(Turtle):

        def __init__(self):
            super().__init__()
            self.l_score = 0
            self.r_score = 0
            self.color("white")
            self.penup()
            self.hideturtle()
            self.update_score()

        # create scoreboard
        def update_score(self):
            self.clear()
            self.goto(-100, 190)
            self.write(arg=self.l_score, move=False, align="center", font=("Courier", 60, "bold"))
            self.goto(100, 190)
            self.write(arg=self.r_score, move=False, align="center", font=("Courier", 60, "bold"))

        def l_scored(self):
            self.l_score += 1
            self.update_score()

        def r_scored(self):
            self.r_score += 1
            self.update_score()

        def game_over(self):
            self.goto(0, 0)
            self.write(arg="GAME OVER", move=False, align="center", font=("Arial", 12, "normal"))