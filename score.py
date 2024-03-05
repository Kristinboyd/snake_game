# Libraries
from turtle import Turtle
import random
# Constants
from constants import *


# Score class
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highest_score_file.txt") as highest_score:
            self.high_score = int(highest_score.read())
        self.penup()
        self.clear()
        self.color(random.choice(COLOR_LIST))
        self.goto(0, 270)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}, High Score: {self.high_score}", move=False, align=ALIGN_SCORE, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highest_score_file.txt", mode='w') as highest_score:
                highest_score.write(f"{self.high_score}")

        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
