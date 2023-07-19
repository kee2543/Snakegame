from random import randint
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("skyblue")
        self.penup()
        self.speed("fastest")
        self.food_position()

    def food_position(self):
        x = randint(-250, 250)
        y = randint(-250, 250)
        self.goto(x, y)