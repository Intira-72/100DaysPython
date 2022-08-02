import time
from turtle import Screen
from player import Player
from car_manager import CarManager


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#15202b")
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
cars = CarManager()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.car_move()

screen.exitonclick()