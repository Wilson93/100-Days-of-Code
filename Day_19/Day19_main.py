from turtle import Turtle, Screen
import random

# Screen Settings
screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False

# Turtles
all_turtles = []
colors = ["red", "orange", "yellow", "blue", "green", "purple"]
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[0 + turtle_index])
    new_turtle.penup()
    new_turtle.goto(x = -230, y =-75 + (30 * turtle_index))
    all_turtles.append(new_turtle)

# Bets
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: " )

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You win! The {winning_color} turtle is the winner")
            else:
                print(f"You loose! The {winning_color} turtle is the winner")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)



# Movement Functions
def forwards():
    new_turtle.forward(10)

def backwards():
    new_turtle.back(10)

def right():
    new_turtle.right(10)

def left():
    new_turtle.left(10)

def reset():
    screen.reset()

# Controls
screen.listen()
screen.onkeypress(fun=forwards, key="w")
screen.onkeypress(fun=backwards, key="s")
screen.onkeypress(fun=right, key="d")
screen.onkeypress(fun=left, key="a")
screen.onkeypress(fun=reset, key="c")








screen.exitonclick()
