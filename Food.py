import random
from turtle import Turtle



# Turtle is superclass

class Food(Turtle):

    def __init__(self, ):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color('beige')
        self.speed("fastest")
        self.food_generator()

    def food_generator(self):
        x_axis = random.randint(-280, 280)
        y_axis = random.randint(-280, 280)
        self.goto(x_axis,y_axis)