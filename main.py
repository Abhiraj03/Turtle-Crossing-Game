from turtle import Screen
from player import Player
from cars import Cars
import time
import random
from scoreboard import Scoreboard
screen = Screen()
screen.bgcolor('white')
screen.title('Turtle Crossing')
screen.setup(600,600)
screen.tracer(0)
screen.listen()

cars = []

for obstacle in range(30):
    car = Cars()
    car.goto(random.randint(-270,270),random.randint(-200,200))
    cars.append(car)

turtle = Player()
levels = Scoreboard()

screen.onkey(turtle.ahead,'Up')
screen.onkey(turtle.behind,'Down')


game_is_on = True
game_speed = 0.1

while game_is_on:
    time.sleep(game_speed)
    screen.update()
    for _ in cars:
        if _.distance(turtle) < 20:
            levels.game_over()
            game_is_on = False
        _.move()
    if turtle.ycor() > 280:
        levels.update()
        turtle.goto(0, -260)
        game_speed -= 0.01


































screen.exitonclick()