import turtle

def main():
    turtle.Screen().bgcolor("#303030")
    draw01()
    turtle.Screen().exitonclick()

def drawCircle():
    pen = turtle.Turtle()
    pen.circle(100)

def draw01():
    pen = turtle.Turtle()
    pen.speed(10)
    for i in range(36):
        pen.circle(100)
        pen.left(10)

def draw02():
    pen = turtle.Turtle()
    pen.speed(10)
    color = ["red", "blue", "yellow", "green"]
    for i in range(36):
        pen.color(color[i%4])
        pen.circle(100)
        pen.left(10)

if __name__ == '__main__':
    main()