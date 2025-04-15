from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
# Settings
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

#create scoreboard
scoreboard = Scoreboard()

# create ball
ball = Ball()

# create paddles
l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)

# movement keys
screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    #detect collision with top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #detect collision with right wall
    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.l_scored()

    # detect collision with right wall
    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.r_scored()






# Exit
screen.exitonclick()

# need:
# paddles
# ball
# scoreboard
# table line