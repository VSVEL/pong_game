import turtle as t
import paddle as p
from ball import Ball
from scoreboard import ScoreBoard
import time


screen = t.Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

right_paddle = p.Paddle((350,0))
left_paddle = p.Paddle((-350,0))
ball = Ball()
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(right_paddle.go_up,"Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up,"w")
screen.onkey(left_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_point()

    if scoreboard.right_score == 10 or scoreboard.left_score == 10:
        game_is_on = False
        screen.exitonclick()



