# Libraries
from turtle import Turtle
import random
# Constants
from constants import *


# food class
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(random.choice(COLOR_LIST))
        self.refresh()

    def refresh(self):
        random_food_x = random.randint(-280, 280)
        random_food_y = random.randint(-280, 280)
        self.goto(random_food_x, random_food_y)