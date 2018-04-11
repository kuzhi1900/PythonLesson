# ColorSpiral.py
import turtle
sum = 0
for x in range(1, 101):
    sum = sum + x
print(sum)

pen = turtle.Pen()
pen.pencolor("yellow")
pen.width(2)
turtle.bgcolor("black")

# sides = 4
for x in range(0, 100):
    pen.forward(x*4)
    pen.left(46)
    pen.forward(x)
    pen.right(180)
# pen.forward(100)
# pen.left(90)
# pen.forward(100)
# pen.left(90)
# pen.forward(100)
# pen.left(90)x
# x = input()



