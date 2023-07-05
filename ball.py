from turtle import Screen, Turtle
import random

screen = Screen()


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('#ff3200')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.orientation = 0
        self.seth(self.orientation)
        self.move_count = 0

    def move(self):
        self.seth(self.orientation)
        self.fd(9)
        self.move_count += 1

    def detect_collision_wall(self):
        if self.ycor() >= 240 or self.ycor() <= -240:
            self.orientation = -self.orientation
            if self.ycor() > 250:
                self.sety(self.ycor()-25)
            elif self.ycor() < -250:
                self.sety(self.ycor()+25)

    def detect_collision_paddle(self, player_paddle, bot_paddle):
        if -360 <= self.xcor() <= -340 and player_paddle-60 <= self.ycor() <= player_paddle+60:
            self.adjust_angle(player_paddle)
            self.orientation += random.randint(-10, 10)

        elif 360 >= self.xcor() >= 340 and bot_paddle-50 <= self.ycor() <= bot_paddle+50:
            self.adjust_angle(player_paddle)
            self.orientation = 180-self.orientation
            self.orientation += random.randint(-10, 10)

    def adjust_angle(self, player_paddle):
        if player_paddle + 40 <= self.ycor() <= player_paddle + 60:
            self.orientation = 65
        elif player_paddle + 30 <= self.ycor() <= player_paddle + 40:
            self.orientation = 50
        elif player_paddle + 20 <= self.ycor() <= player_paddle + 30:
            self.orientation = 35
        elif player_paddle + 10 <= self.ycor() <= player_paddle + 20:
            self.orientation = 20
        elif player_paddle - 10 <= self.ycor() <= player_paddle + 10:
            self.orientation = 0
        elif player_paddle - 20 <= self.ycor() <= player_paddle - 10:
            self.orientation = -20
        elif player_paddle - 30 <= self.ycor() <= player_paddle - 20:
            self.orientation = -35
        elif player_paddle - 40 <= self.ycor() <= player_paddle - 30:
            self.orientation = -50
        elif player_paddle - 60 <= self.ycor() <= player_paddle - 40:
            self.orientation = -65





