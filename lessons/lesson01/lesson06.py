import turtle

def draw01():
    pen = turtle.Turtle()
    for i in range(50,100):
        for j in range(50,100):
            for k in range(50,100):
                pen.forward(i)
                pen.left(j)
                pen.backward(k)
                pen.left(i+k)


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
    draw01()
    turtle.Screen().exitonclick()

if __name__ == '__main__':
    main()