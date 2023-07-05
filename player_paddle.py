from turtle import Screen, Turtle

screen = Screen()


class PlayerPaddle:
    def __init__(self):
        self.creat_paddle()
        self.score = 0

    def creat_paddle(self):
        self.paddle = Turtle('square')
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        self.paddle.color('white')
        self.paddle.goto(-350, 00)

    def up(self):
        if self.paddle.ycor() >= 199:
            return
        self.paddle.sety(self.paddle.ycor() + 20)

    def down(self):
        if self.paddle.ycor() <= -199:
            return
        self.paddle.sety(self.paddle.ycor() - 20)


