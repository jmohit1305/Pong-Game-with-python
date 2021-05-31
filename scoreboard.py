from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.penup()
        self.shape("classic")
        self.goto(pos)
        self.color("white")
        self.print_score()

    def print_score(self):
        self.write(f'{self.score}', align="center", font=("Courier", 80, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.print_score()
