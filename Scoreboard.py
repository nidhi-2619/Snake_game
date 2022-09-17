from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)  # we keep it here because using it after write won't make any diference
        self.write(f"Score:{self.score}", align='center', font={'Arial', 25, 'normal'})
        self.hideturtle()  # to hide the turtle arrow

    def record_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score:{self.score}", align='center', font={'Arial', 25, 'normal'})

    def game_over(self):
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0,0)
        self.write(f"GAME OVER",align = "center",font={'Raleway', 40, 'normal'})