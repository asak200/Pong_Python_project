from turtle import Screen, Turtle
from time import sleep

screen = Screen()

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.player_score = 0
        self.bot_score = 0

    def draw_screen(self):
        self.hideturtle()
        self.pencolor('#FFFFFF')
        self.penup()
        self.goto(-400, 250)
        self.pendown()
        for i in range(0, 2):
            self.seth(180 * i)
            self.fd(800)
            self.right(90)
            self.fd(500)
        self.goto(0, 250)
        self.seth(-90)
        self.pensize(3)
        while self.ycor() > -250:
            self.pendown()
            self.fd(20)
            self.penup()
            self.fd(20)

        screen.update()

    def write_scores(self, playerscore, botscore):
        self.clear()
        self.draw_screen()
        self.goto(-100, 250)
        self.write(playerscore, align='center', font=('Courier', 50, 'normal'))
        self.goto(100, 250)
        self.write(botscore, align='center', font=('Courier', 50, 'normal'))

    def counter(self):
        for i in range(3,0,-1):
            self.goto(0, 0)
            self.clear()
            self.write(i, align='center', font=('Courier', 80, 'normal'))
            sleep(1)
