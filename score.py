import turtle
from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(0, 265)
        self.score=0
        with open("data.txt") as data:
           self.high_score=int(data.read())
        self.write(f"Score : {self.score}  highest_score={self.high_score}",False,"center",("Arial",24,"normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.clear()
        self.write(f"Score : {self.score}  highest_score={self.high_score}", False, "center", ("Arial", 24, "normal"))


    def score_count(self):
        self.clear()
        self.score+=1
        self.goto(0, 265)
        self.write(f"Score : {self.score} High_score :{self.high_score}", False, "center", ("Arial", 24, "normal"))



