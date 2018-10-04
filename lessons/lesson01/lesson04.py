import turtle

def main():
    pen = turtle.Turtle()
    pen.color("black")
    pen.fillcolor("green")
    pen.begin_fill()
    pen.forward(80)
    pen.left(120)
    pen.forward(100)
    pen.left(200)
    pen.forward(50)
    pen.left(150)
    pen.forward(100)
    pen.left(220)
    pen.forward(40)
    pen.left(150)
    pen.forward(160)

    pen.left(120)
    pen.forward(160)
    pen.left(140)
    pen.forward(40)
    pen.left(220)
    pen.forward(100)
    pen.left(150)
    pen.forward(50)
    pen.left(220)
    pen.forward(100)
    pen.end_fill()
    turtle.Screen().exitonclick()

if __name__ == '__main__':
    main()