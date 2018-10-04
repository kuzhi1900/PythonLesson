import turtle


def draw01():
    pen = turtle.Turtle()
    pen.pensize(3)
    for i in range(100):
        pen.forward(i*3)
        pen.left(90)

def draw02():
    pen = turtle.Turtle()
    pen.pensize(3)
    for i in range(500):
        pen.forward(i/50)
        pen.left(6)

def draw03():
    pen = turtle.Turtle()
    pen.pensize(3)
    for i in range(100):
        pen.forward(i*3)
        pen.left(89)

def drawRect(pen):
    pen.color("red")
    pen.pensize(1)
    for i in range(4):
        pen.forward(200)
        pen.left(90)

def draw04():
    pen = turtle.Turtle()
    for i in range(36):
        drawRect(pen)
        pen.left(10)

def main():
    turtle.Screen().bgcolor("#303030")
    draw04()
    turtle.Screen().exitonclick()

if __name__ == '__main__':
    main()