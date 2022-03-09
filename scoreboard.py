from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('Black')
        self.penup()
        self.goto(-225,270)
        self.level = 1
        self.scoreboard_refresh()

    def scoreboard_refresh(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=("Courier", 20, "normal"))


    def update(self):
        self.level += 1
        self.scoreboard_refresh()

    def game_over(self):
        self.goto(-25,-5)
        self.write("GAME OVER!", align="center", font=("Courier", 40, "normal"))