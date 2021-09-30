import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# 1. A turtle moves forwards when you press the "Up" key. It can only move forwards, not back, left or right.
# 2. Cars are randomly generated along the y-axis and will move from the right edge of the screen to the left edge.
# 3. When the turtle hits the top edge of the screen, it moves back to the original position and the player levels up.
# On the next level, the car speed increases.
# 4. When the turtle collides with a car, it's game over and everything stops.


# Create a turtle player that starts at the bottom of the screen and listen for the "Up" keypress to move the turtle
# north. If you get stuck, check the video walk through in Step 3.
# Create and move the cars
# Detect collision with car
# Detect when turtle reaches the other side
# Create a scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect successful crossing
    if player.check_position():
        player.go_to_start()
        car_manager.increase_speed()
        scoreboard.update_score()

screen.exitonclick()

