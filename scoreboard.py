from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto(-250, 250)
        self.write_text()

    def write_text(self):
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def update_score(self):
        self.clear()
        self.level += 1
        self.write_text()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)



