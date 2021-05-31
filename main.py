from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()

screen.onkeypress(key="Up", fun=r_paddle.go_up)
screen.onkeypress(key="Down", fun=r_paddle.go_down)

screen.onkeypress(key="w", fun=l_paddle.go_up)
screen.onkeypress(key="s", fun=l_paddle.go_down)

game_is_on = True

l_scoreboard = ScoreBoard((-100, 200))
r_scoreboard = ScoreBoard((100, 200))

while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    if ball.ycor() >= 270 or ball.ycor() <= -270:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.distance(r_paddle) > 50 and ball.xcor() > 320:
        l_scoreboard.increase_score()
        ball.reset_position()

    elif ball.distance(l_paddle) > 50 and ball.xcor() < -320:
        r_scoreboard.increase_score()
        ball.reset_position()

screen.exitonclick()
