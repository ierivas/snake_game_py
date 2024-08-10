from turtle import Turtle

ALIGN = "center"
FONT = ("Arial",15,"bold")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score =0
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.goto(0,270)
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", False, align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, align=ALIGN, font=FONT)

    def add_score(self):
        self.score +=1
        self.clear()
        self.update_score()
