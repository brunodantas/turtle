from turtle import *
setup(width=1., height=1., startx=None, starty=None)
hideturtle()
speed(10)

begin_fill()

i = 1
step = .00001
inc = .0001
angle = 5
for _ in range(10 ** 3):
    forward(step)
    right(angle)
    i += 1
    step += inc
    inc += .0001
done()
