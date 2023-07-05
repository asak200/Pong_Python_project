from turtle import Screen, Turtle
HARDNESS = 5

screen = Screen()

class BotPaddle:
    def __init__(self):
        self.creat_paddle()
        self.score = 0

    def creat_paddle(self):
        self.paddle = Turtle('square')
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        self.paddle.color('white')
        self.paddle.goto(350, 00)

    def defend(self, ball_pos, moves):
        if 220 > ball_pos > -220 and moves % HARDNESS == 0:
            if ball_pos > self.paddle.ycor()+20:
                self.paddle.sety(self.paddle.ycor()+20)
            elif ball_pos < self.paddle.ycor()-20:
                self.paddle.sety(self.paddle.ycor()-20)


