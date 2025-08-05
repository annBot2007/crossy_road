from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.level = 1
        self.hideturtle()

    def display_score(self):
        self.clear()
        self.penup()
        self.goto(-215, 255)
        self.write(f"LEVEL: {self.level}", align="center", font=FONT)
        self.goto(215, 255)
        self.write(f"SCORE: {self.score}", align="center", font=FONT)

    def losing_sequence(self):
        self.penup()
        self.goto(0, 0)
        self.write("***GAME OVER**", align="center", font=("Courier", 30, "italic bold"))
        self.goto(0, -50)
        self.write(f"FINAL SCORE: {self.score}", align="center", font=("Courier", 30, "italic bold"))
