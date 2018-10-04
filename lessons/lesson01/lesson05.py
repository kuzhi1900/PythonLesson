import turtle

def draw01():
    pen = turtle.Turtle()
    for i in range(5):
        pen.forward(200)
        pen.left(144)

def draw02():
    pen = turtle.Turtle()
    for i in range(5):
        pen.forward(200)
        pen.left(72+144)


def draw03():
    pen = turtle.Turtle()
    for i in range(5):
        pen.forward(200)
        pen.left(144*3)


def draw04():
    pen = turtle.Turtle()
    for i in range(36):
        for i in range(5):
            pen.forward(200)
            pen.left(72+144)
        pen.left(10)


def main():
    draw04()
    # draw02()
    turtle.Screen().exitonclick()

if __name__ == '__main__':
    main()