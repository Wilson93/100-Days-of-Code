from turtle import Turtle

class Scoreboard(Turtle):

        def __init__(self):
            super().__init__()
            self.score = 0

            # read current highscore
            with open("highscore.txt") as file:
                self.high_score = int(file.read())

            self.color("white")
            self.penup()
            self.hideturtle()
            self.goto(0, 260)
            self.update_score()

        # create scoreboard
        def update_score(self):
            self.clear()
            self.write(arg=f"Score: {self.score} High Score: {self.high_score}", move=False, align="center", font=("Arial", 12, "normal"))

        def increase_score(self):
            self.score += 1
            self.update_score()

        def reset(self):
            if self.score > self.high_score:
                self.high_score = self.score

                # write new highscore
                with open("highscore.txt", mode="w") as file:
                    file.write(str(self.score))

            self.score = 0
            self.update_score()

        def game_over(self):
            self.goto(0, 0)
            self.write(arg="GAME OVER", move=False, align="center", font=("Arial", 12, "normal"))