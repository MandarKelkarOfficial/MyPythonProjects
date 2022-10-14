
import colorsys
from operator import lt
from turtle import bgcolor, circle, done, fd, hideturtle, pencolor, pensize, rt, speed

bgcolor("black")
hue=0.0
hideturtle()
pensize(2)
speed(300)

for i in range(500):
    col=colorsys.hsv_to_rgb(hue,1,1)
    pencolor(col)
    hue+=0.005
    fd(i)
    rt(40+2+10)
    lt(20,5)
    circle(10)
done()
    