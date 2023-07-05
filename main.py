from turtle import Screen
from scoreboard import ScoreBoard
from player_paddle import PlayerPaddle
from bot_pad import BotPaddle
from ball import Ball
from time import sleep


screen = Screen()
screen.setup(1000, 650)
screen.title('Pong')
screen.bgcolor('black')
screen.tracer(0)

player = PlayerPaddle()
bot = BotPaddle()

screen.listen()

score_board = ScoreBoard()
score_board.draw_screen()
score_board.counter()
score_board.write_scores(player.score, bot.score)
ball = Ball()


screen.onkeypress(player.up, "w")
screen.onkeypress(player.down, "s")

game_is_on = True

while game_is_on:
    ball.move()
    ball.detect_collision_wall()
    ball.detect_collision_paddle(player.paddle.ycor(), bot.paddle.ycor())

    bot.defend(ball.ycor(), ball.move_count)

    if ball.xcor() < -400 or ball.xcor() > 400:
        if ball.xcor() < -400:
            bot.score += 1
        elif ball.xcor() > 400:
            player.score += 1
        score_board.write_scores(player.score, bot.score)
        ball.orientation = 0
        ball.goto(0, 0)
        bot.paddle.sety(0)

    if player.score == 7:
        score_board.goto(0, 0)
        score_board.write("You Won!", align='center', font=('Courier', 80, 'normal'))
        game_is_on = False
    elif bot.score == 7:
        score_board.goto(0, 0)
        score_board.write("Game Over", align='center', font=('Courier', 80, 'normal'))
        game_is_on = False

    screen.update()
    sleep(0.0001)

screen.exitonclick()
