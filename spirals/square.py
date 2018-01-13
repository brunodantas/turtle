from turtle import *
setup(width=1., height=1., startx=None, starty=None)
hideturtle()
# speed(0)

begin_fill()

points = [(10,0), (10,10), (0,10), (0,0)]

step = 10
inc = .1
for _ in range(10 ** 3):
    p = points.pop(0)
    setheading(towards(p))
    forward(step)
    points.append(pos())
    step += inc
    inc += .1

done()
