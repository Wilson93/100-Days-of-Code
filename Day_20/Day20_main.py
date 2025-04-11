from turtle import Screen
import time
from Snake_class import Snake
from food_class import Food
from scoreboard_class import Scoreboard

# Settings
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Create snake body
snake = Snake()

# Create Food
food = Food()

# scoreboard
scoreboard = Scoreboard()

# Create keybinds
screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")

# Move snake forward
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect wall collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    # detect tail collision
    for segment in snake.all_turtles[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()























# Exit
screen.exitonclick()