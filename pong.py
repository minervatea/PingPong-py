# reference by @TokyoEdTech

import turtle

# constants
board_width = 800
board_height = 600

wn = turtle.Screen()
wn.title("Pong tutorial learnt by @TokyoEdTech")
wn.bgcolor("black")
wn.setup(board_width, board_height)
wn.tracer(0) #stops window from updating. speed up the game.

# Score 
score_a = 0
score_b = 0

# State
game_over = False


# Paddle A
paddle_a = turtle.Turtle() # Turtle object
paddle_a.speed(0) # speed of the animation (maximum)
paddle_a.shape("square") # built-in shape
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup() # don't draw a line when moving
paddle_a.goto(-350,0)


# Paddle B
paddle_b = turtle.Turtle() 
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup() 
paddle_b.goto(350,0)

# Ball
ball = turtle.Turtle() 
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0,0)
ball.dx = 1 # detla(change) - every time the  ball moves, it moves by 2 pixels
ball.dy = 1

# Pen
pen = turtle.Turtle()
pen.speed(0) 
pen.color("white")
pen.penup()
#pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: {}  PlayerB: {}".format(score_a, score_b), align = "center", font=("Courier", 24, "normal"))

# Function
def paddle_a_up():
    y = paddle_a.ycor() # from the turtle module, returns the  y coordinate
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



# Main game loop

while True:
    if not game_over:
        wn.update() # update the screen everytime the loop runs

        # Keyboard binding
        wn.listen()
        wn.onkeypress(paddle_a_up, "w")
        wn.onkeypress(paddle_a_down, "s")
        wn.onkeypress(paddle_b_up, "Up")
        wn.onkeypress(paddle_b_down, "Down")

        # Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border checking
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
        
        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1
        
        if ball.xcor() > 390:
            ball.goto(0,0)
            ball.dx *= -1
            score_a += 1
            pen.clear()
            pen.write("Player A: {}  PlayerB: {}".format(score_a, score_b), align = "center", font=("Courier", 24, "normal"))

        if ball.xcor() < -390:
            ball.goto(0,0)
            ball.dx *= -1
            score_b += 1
            pen.clear()
            pen.write("Player A: {}  PlayerB: {}".format(score_a, score_b), align = "center", font=("Courier", 24, "normal"))


        # Paddle and ball collisions
        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
            ball.setx(340)
            ball.dx *= -1

        if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
            ball.setx(-340)
            ball.dx *= -1    
