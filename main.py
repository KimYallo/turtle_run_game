import time
import random
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

MAKE_CAR = [True, False, False, False, False]
car_list = []

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
screen.onkey(fun=player.turtle_move, key="Up")

scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)

    # Create and move cars
    if random.choice(MAKE_CAR):
        car_manager = CarManager()
        car_list.append(car_manager)
    for car in car_list:
        car.car_move()

    # if the turtle pass the finish line -> go back to the start_position and level UP
    if player.ycor() > FINISH_LINE_Y:
        player.is_finish()
        scoreboard.level += 1
        scoreboard.show_level()
        for car in car_list:
            car.speed_up()
    # if the turtle hits the car -> game over
    for car in car_list:
        x_distance = abs(player.xcor() - car.xcor())
        y_distance = abs(player.ycor() - car.ycor())
        if x_distance < 28 and y_distance < 23:
            scoreboard.game_over()
            game_is_on = False

    screen.update()

screen.exitonclick()
