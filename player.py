from turtle import Turtle

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.color('Black')
        self.setheading(90)
        self.goto(0, -260)

    def ahead(self):
        self.forward(20)
        
    def behind(self):
        self.back(20)