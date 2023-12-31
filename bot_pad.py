from turtle import Screen, Turtle
DIFFICULTY = 3

screen = Screen()


class BotPaddle:
    def __init__(self):
        self.create_paddle()
        self.score = 0

    def create_paddle(self):
        self.paddle = Turtle('square')
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        self.paddle.color('white')
        self.paddle.goto(350, 00)

    def defend(self, ball_pos, moves):
        if moves % DIFFICULTY == 0:
            if ball_pos > self.paddle.ycor()+20 and 200 > self.paddle.ycor():
                self.paddle.sety(self.paddle.ycor()+20)
            elif ball_pos < self.paddle.ycor()-20 and self.paddle.ycor() > -200:
                self.paddle.sety(self.paddle.ycor()-20)


