from random import gammavariate
import time
from turtle import Screen
from Food import Food
from snake import Snake
from Scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
Food = Food()
score = Score()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# move the snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # detect collision with food
    # distance method is comparing distance between two turtle
    if snake.head.distance(Food) < 20:
        Food.food_generator()
        score.record_score()
        snake.snake_body_extend()
    # detect collision with wall
    if snake.head.xcor()>290 or snake.head.xcor()< -290  or snake.head.ycor()>290 or snake.head.ycor()< -290:
        game_is_on = False

#         detect collision with its own tail
# any segment of the tail
    for part in snake.snake_body[1:]:
        if snake.head.distance(part) <10:
            game_is_on = False
            score.game_over()
score.game_over()
screen.exitonclick()
