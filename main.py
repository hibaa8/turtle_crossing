import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, 'Up')
screen.onkey(player.down, 'Down')

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()

    for car in car_manager.cars:
        if car.distance(player) < 27:
            player.reset()
            car.hideturtle()
            scoreboard.increment()

    car_manager.create_car()

    if scoreboard.lives == 0:
        scoreboard.game_over()
        game_on = False

    if player.ycor() >= 260:
        if car_manager.speed > 2:
            car_manager.speed -= 2
            print(car_manager.speed)
        scoreboard.reset()
        player.reset()

screen.exitonclick()

