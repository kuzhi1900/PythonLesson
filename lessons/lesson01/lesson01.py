import turtle

def main():
    turtle.Screen().bgcolor("#303030")
    pen = turtle.Turtle()
    pen.speed(10)
    pen.pensize(3)
    pen.forward(200)
    pen.left(90)
    pen.forward(200)
    pen.left(90)
    pen.forward(200)
    pen.left(90)
    pen.forward(200)

    drawRect()
    drawArc()
    draw6s()
    drawCircle()
    pen.circle(200)

    turtle.Screen().exitonclick()

def drawRect():
    pen = turtle.Turtle()
    pen.color("red")
    pen.pensize(3)
    for i in range(4):
        pen.forward(200)
        pen.left(90)

def drawArc():
    pen = turtle.Turtle()
    pen.color("blue")
    pen.pensize(3)
    for i in range(3):
        pen.forward(200)
        pen.left(120)

def draw6s():
    pen = turtle.Turtle()
    pen.color("blue")
    pen.pensize(3)
    for i in range(6):
        pen.forward(200)
        pen.left(60)

def drawCircle():
    pen = turtle.Turtle()
    pen.color("green")
    pen.pensize(3)
    for i in range(60):
        pen.forward(20)
        pen.left(6)

main()
