import turtle

squary = turtle.Turtle()
squary.speed(0)

for i in range(500):
    for i in range(500):
        squary.forward(i)
        squary.right(91)
    squary.forward(i)
    squary.left(91)
