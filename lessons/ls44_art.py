

import turtle as t
from random import randint, random

LEFT = 1.0
RIGHT = -1.0
TRUNK = 100.0
UP = 90.0


def tree(x: float, y: float) -> None:
    t.penup()
    t.goto(x, y)
    t.pendown()
    branch(TRUNK, 90.0)
    t.update()


def branch(lenght: float, angle: float) -> None:
    t.setheading(angle)
    t.forward(lenght)
    if lenght < 2:
        ...     
    else:
        branch(lenght * 0.7, angle - randint(20, 60))
        branch(lenght * 0.6, angle + randint(15, 60))
    
    t.setheading(angle + 180)
    t.forward(lenght)

if __name__ == "__main__":
    t.speed(0)
    t.tracer(0, 0)
    t.getscreen().onclick(tree)
    tree(0, 0)
    t.done()
