import turtle
import random

# global definition
# base = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F]
base = [str(x) for x in range(10)] + [ chr(x) for x in range(ord('A'),ord('A')+6)]

def main():
    tList = []
    head = 0
    wn = turtle.Screen()
    wn.bgcolor("#303030")
    # wn.bgcolor("#ffffff")

    pen = turtle.Turtle()
    pen.up()
    pen.goto(-0, -2)
    pen.down()
    pen.pensize(0.005)
    pen.speed(10)

    numTurtles = 8
    for i in range(numTurtles):
        nt = turtle.Turtle()
        nt.setheading(head)
        nt.pensize(0.01)
        nt.pencolor("#"+dec2hex(random.randrange(256))+dec2hex(random.randrange(256))+dec2hex(random.randrange(256)))
        nt.speed(10)
        # nt.tracer(30, 0)
        tList.append(nt)
        head = head + 360 / numTurtles

    for i in range(120):
        moveTurtles(tList, 15, i)
    for i in range(80):
        moveTurtles2(tList, 15, i)
    for i in range(20):
        moveTurtles(tList, 15, i)

    pen.up()
    pen.goto(-220, -260)
    pen.write("HuangXiaobian's Coding Lessons", True, "center", "30px Arial")
    pen.goto(-140, 230)
    pen.write("Hello World!", True, "center", "50px Arial")

    wn.exitonclick()


def moveTurtles(turtleList, dist, angle):
    for turtle in turtleList:
        turtle.forward(dist * 0.7)
        turtle.left(angle / 2)
        turtle.pensize(angle * 0.02)


def moveTurtles2(turtleList, dist, angle):
    for turtle in turtleList:
        turtle.forward(dist * 0.3)
        turtle.right(angle / 2)
        turtle.pensize(angle * 0.02)
def dec2hex(string_num):
    num = int(string_num)
    mid = []
    while True:
        if num == 0: break
        num,rem = divmod(num, 16)
        mid.append(base[rem])
    return ''.join([str(x) for x in mid[::-1]])

main()
