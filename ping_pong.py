import turtle
import time

WIDTH = 800
HEIGHT = 600
PADDLE_SPEED = 20
BALL_SPEED = 0.15

screen = turtle.Screen()
screen.title("Ping Pong")
screen.bgcolor("black")
screen.setup(WIDTH, HEIGHT)
screen.tracer(0)

# Score display
pen = turtle.Turtle()
ped = pen
pen.speed(0)
ped.color("white")
ped.penup()
ped.hideturtle()
ped.goto(0, 260)

score_a = 0
score_b = 0


def update_score():
    pen.clear()
    pen.write(
        f"Player A: {score_a}   Player B: {score_b}",
        align="center",
        font=("Courier", 24, "normal"),
    )


update_score()

# Left paddle
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Right paddle
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.18
ball.dy = 0.18


def paddle_a_up():
    y = paddle_a.ycor() + PADDLE_SPEED
    paddle_a.sety(min(250, y))


def paddle_a_down():
    y = paddle_a.ycor() - PADDLE_SPEED
    paddle_a.sety(max(-250, y))


def paddle_b_up():
    y = paddle_b.ycor() + PADDLE_SPEED
    paddle_b.sety(min(250, y))


def paddle_b_down():
    y = paddle_b.ycor() - PADDLE_SPEED
    paddle_b.sety(max(-250, y))


screen.listen()
screen.onkeypress(paddle_a_up, "w")
screen.onkeypress(paddle_a_down, "s")
screen.onkeypress(paddle_b_up, "Up")
screen.onkeypress(paddle_b_down, "Down")


def reset_ball():
    ball.goto(0, 0)
    ball.dx *= -1
    ball.dy = 0.18


def step():
    global score_a, score_b

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1

    if (
        ball.dx > 0
        and 330 > ball.xcor() > 320
        and paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50
    ):
        ball.setx(320)
        ball.dx *= -1
        ball.dx *= 1.05
        ball.dy *= 1.05

    if (
        ball.dx < 0
        and -330 < ball.xcor() < -320
        and paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50
    ):
        ball.setx(-320)
        ball.dx *= -1
        ball.dx *= 1.05
        ball.dy *= 1.05

    if ball.xcor() > 390:
        score_a += 1
        update_score()
        reset_ball()
    elif ball.xcor() < -390:
        score_b += 1
        update_score()
        reset_ball()

    screen.update()
    time.sleep(BALL_SPEED)
    screen.ontimer(step, 10)


step()
screen.mainloop()
