import turtle
import random

def tree(branch_len, pen):
    if branch_len > 5:
        pen.forward(branch_len)
        angle = random.randint(10, 60)
        pen.right(angle)
        tree(branch_len-15, pen)
        pen.left(2*angle)
        tree(branch_len-15, pen)
        pen.right(angle)
        pen.backward(branch_len)

def grow_tree(x, y):
    pen.up()
    pen.goto(x, y)
    pen.down()
    pen.setheading(90)
    pen.color('blue')
    tree(100, pen)

pen = turtle.Turtle()
pen.speed('fastest')
pen.left(90)
pen.up()
pen.backward(200)
pen.down()

turtle.onscreenclick(grow_tree, 1)

turtle.done()
