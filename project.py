#WAP to play ping pong game through Python
#Made by Divyansh Pal
#divyanshnet.w3spaces.com
#The New Best

from tkinter import font
import turtle
import os

#Window
wn = turtle.Screen()
wn.title("Ping pong game by Divyansh")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Score
score_a = 0
score_b = 0

#Paddle A (Orange)
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("orange")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#Paddle B (Green)
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("green")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(+350, 0)

#Ball
ball_b = turtle.Turtle()
ball_b.speed(0)
ball_b.shape("square")
ball_b.color("white")
ball_b.shapesize(stretch_wid=1, stretch_len=1)
ball_b.penup()
ball_b.goto(0, 0)
ball_b.dx = 0.4
ball_b.dy = -0.4

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Orange: 0 Green: 0", align="center", font=("Courier", 24, "normal"))

#Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)    

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)        

#Keyboard binding
wn.listen()     
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

#Main Game loop
while True:
    wn.update()

    #Move the ball
    ball_b.setx(ball_b.xcor() + ball_b.dx)
    ball_b.sety(ball_b.ycor() + ball_b.dy)

    #Border check
    if ball_b.ycor() > 290:
        ball_b.sety(290)
        ball_b.dy *= -1
        os.system("play bounce.wav&")

    if ball_b.ycor() < -290:
        ball_b.sety(-290)
        ball_b.dy *= -1
        os.system("play bounce.wav&")

    if ball_b.xcor() > 390:
        ball_b.goto(0, 0)
        ball_b.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Orange: {} Green: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball_b.xcor() < -390:
        ball_b.goto(0, 0)
        ball_b.dx *= -1 
        score_b += 1
        pen.clear()   
        pen.write("Orange: {} Green: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    if (ball_b.xcor() > 340 and ball_b.xcor() < 350) and (ball_b.ycor() < paddle_b.ycor() + 40 and ball_b.ycor() > paddle_b.ycor() -40):
        ball_b.setx(340)
        ball_b.dx *= -1
        os.system("play bounce.wav")

    if (ball_b.xcor() < -340 and ball_b.xcor() > -350) and (ball_b.ycor() < paddle_a.ycor() + 40 and ball_b.ycor() > paddle_a.ycor() -40):
        ball_b.setx(-340)
        ball_b.dx *= -1   
        os.system("play bounce.wav") 