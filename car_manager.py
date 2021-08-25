from turtle import Turtle
import random
from time import sleep

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.cars = []
        self.counter = 0
        self.speed = 10

    def create_car(self):
        if self.counter % self.speed == 0:
            new_car = Turtle('square')
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            y = random.randint(-200,250)
            new_car.goto(300,y)
            while len(self.cars) > 0 and new_car.distance(self.cars[-1]) < 70:
                y = random.randint(-200, 250)
            new_car.goto(300, y)
            self.cars.append(new_car)
            self.move_cars()
        else:
            self.move_cars()
        self.counter += 1

    def move_cars(self):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE)

