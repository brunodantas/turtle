from turtle import *
setup(width=1., height=1., startx=None, starty=None)
hideturtle()
speed(10)

begin_fill()

i = 1
for _ in range(10 ** 3):
    forward(i)
    right(90)
    i += 1
done()
