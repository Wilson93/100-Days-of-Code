import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# settings
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# create object
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # create car
    car_manager.create_car()

    # move cars
    car_manager.move_cars()

    # detect car collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.scored()

    # movement keys
    screen.listen()
    screen.onkeypress(player.up, "Up")
    screen.onkeypress(player.down, "Down")

screen.exitonclick()