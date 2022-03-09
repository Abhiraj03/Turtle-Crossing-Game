from turtle import Turtle
import random
car_colors = ["red", "green", "blue", "yellow", "orange", "purple"]
location = [-200, -180, -160, -140, -120, -100, -80, -60, -40, -20, 0, 200, 180, 160, 140, 120, 100, 80, 60, 40, 20]

class Cars(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color(random.choice(car_colors))
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.setheading(180)
        self.rand_start()

    def rand_start(self):
        self.goto(270,random.choice(location))

    def move(self):
        self.forward(3)
        if self.xcor() < -280:
            self.rand_start()
        

        