import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#15202b")
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.car_move()

    for car in cars.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.is_at_finish_line():
        player.go_to_start()
        scoreboard.level_up()        
        cars.level_up()
        

screen.exitonclick()