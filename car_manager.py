from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()

        self.penup()
        self.shape("square")
        self.shapesize(1, 2)
        self.color(random.choice(COLORS))
        self.y_start = random.randrange(-300, 300, 40)
        self.goto(320, self.y_start)
        self.move_distance = STARTING_MOVE_DISTANCE

    def car_move(self):
        new_x = self.xcor() - self.move_distance
        self.goto(new_x, self.y_start)

    def speed_up(self):
        self.move_distance += MOVE_INCREMENT
