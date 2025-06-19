import turtle
from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(0, 265)
        self.point=0
        self.write(f"Score : {self.point}",False,"center",("Arial",24,"normal"))

    def score_count(self):
        self.clear()
        self.point+=1
        self.goto(0, 265)
        self.write(f"Score : {self.point}", False, "center", ("Arial", 24, "normal"))



