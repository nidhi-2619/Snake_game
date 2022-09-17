from turtle import Turtle
class Snake:
    snake = [(0, 0), (-20, 0), (-40, 0)]
    snake_body = []
    UP = 90
    DOWN = 270
    LEFT = 180
    RIGHT = 0
    def __init__(self):
        for i in self.snake:
            self.segment(i)
        self.head = self.snake_body[0]

    def segment(self,i):
        self.snake = Turtle(shape='square')
        self.snake.color('white')
        self.snake.penup()
        self.snake.goto(i)
        self.snake_body.append(self.snake)

    def snake_body_extend(self):
        self.segment(self.snake_body[-1].position())
    def move(self):
        for segment in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[segment - 1].xcor()
            new_y = self.snake_body[segment - 1].ycor()
            self.snake_body[segment].goto(new_x, new_y)
        self.head.forward(20)

    def right(self):
        if self.head.heading()!= self.LEFT:
            self.head.setheading(self.RIGHT)

    def left(self):
        if self.head.heading()!= self.RIGHT:
            self.head.setheading(self.LEFT)

    def down(self):
        if self.head.heading()!= self.UP:
            self.head.setheading(self.DOWN)

    def up(self):
        if self.head.heading()!= self.DOWN:
            self.head.setheading(self.UP)
