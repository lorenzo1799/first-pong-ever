# First PONG ever
# by @Lorenzo
# part 1: start

import turtle

# Schermo #  
wn = turtle.Screen()
wn.title("First Pong Ever")
wn.bgcolor("black")
wn.setup(width=800, height=600)
# velocizza,
wn.tracer(0)
# fine schermo #
# score
Pietro = 0
Lorenzo = 0

# Paddle A
# Creo un oggetto
paddle_a = turtle.Turtle()
# non è la velocità del paddle ma permette di arrivare al massimo della velocità
paddle_a.speed(0)
paddle_a.shape("square") #20 pixel * 20 pixel
paddle_a.color("white")
paddle_a.penup()
# starting point x, y
paddle_a.goto(-350, 0)
paddle_a.shapesize(stretch_wid=5, stretch_len=1)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(+350, 0)

# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.goto(0, 0)
ball.penup()
# separare ball movment in 2 parti = (x, y)
ball.dx = 2 #ogni volta che si muove, si muove di 2 pixel
ball.dy = 2

pen = turtle.Turtle()
pen.color("white")
pen.speed(0)
pen.penup()
pen.hideturtle()
pen.goto(0, 260)


# FUNZIONI # (MOVIMENTO)
# definire funzione per paddle_a
def paddle_a_up():
    y = paddle_a.ycor()      # (ritorna le coordinate Y)
    y += 20
    paddle_a.sety(y)
    

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# La funzione è stata definita ma bisogna chiamarla
wn.listen()
wn.onkeypress(paddle_a_up, "w")  # Attiva paddle_a_up quando clicco "w"
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_down, "Down")
# FINE FUNZIONI


# Every game need a loop
# main game loop
while True:
    wn.update()

    # Move the ball
    # ball start-->ball.xcor() e aggiunge ball.dy\dx (posizione attuale)
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Bordi
    if paddle_a.ycor()  > 300:
        paddle_a.clear()
        paddle_a.sety(250)

    if paddle_a.ycor()  < -300:
        paddle_a.clear()
        paddle_a.sety(-250)

    if paddle_b.ycor()  > 300:
        paddle_b.clear()
        paddle_b.sety(250)

    if paddle_b.ycor()  < -300:
        paddle_b.clear()
        paddle_b.sety(-250)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 #reverse direction
        
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        Pietro += 1
        pen.clear()
        pen.write("Pietro: {} Lorenzo: {}".format(Pietro, Lorenzo), align="center", font=("Courier", 24, "normal"))
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        Lorenzo += 1
        pen.clear()
        pen.write("Pietro: {} Lorenzo: {}".format(Pietro, Lorenzo), align="center", font=("Courier", 24, "normal"))
        # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() -50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() -50):
        ball.setx(-340)
        ball.dx *= -1
    
