"""My happiest place! A Tennis court. The scene is a tennis court with a nice crowd, and a beutiful sky.

I attemppted a couple things to obtain the extra 15 point: 
1. Look at net_drawer function where I created two separate functions that simplified the net drawing.
2. I made use of a function call uniform imported from random 
to define an area where players and the ball are randomly drawn!
3. I also made used of a couple functions from Turtle that were not taught like Circle and x.cord or y.cord!
"""

__author__ = "730442926"

from turtle import Turtle, colormode, done
from random import uniform

colormode(255)

RECT_SIDES: int = 4
RECT_SIDE1: int = 0
RECT_SIDE3: int = 2
RECT_ANGLE: int = 90
TWO_SIDES_NET: int = 2
NET_SIDE1: int = 0
NET_SIDE2: int = 1
VERTICAL_NET: int = 21
SPACE_VERT_NET_LIN: int = 20
START_PT_CHANGE: int = 20
NUM_FANS: int = 66
ROW1_FANS: int = 21
ROWS_1_2_FANS: int = 44
X_SPACES_BY_FANS: int = 840
Y_SPACES_BY_FANS: int = 30
FANS_DISTANCING: int = 40
NUM_SKY_LINES: int = 15
Y_DISTANCING_SKY: int = 10
SKY_TONECOLOR_CHANGE: float = 5
SUN_LENGTH: float = 180
LEFT_X_COURTCORD: float = -400
RIGHT_X_COURTCORD: float = 500
TOP_Y_COURTCORD: float = 250
BOT_Y_COURTCORD: float = -300
TOP_Y_SINGLES_COURTCORD: float = 175
BOT_Y_SINGLES_COURTCORD: float = -225
X_MID_COURT: float = 50
X_LEFT_SERVICE: float = -150
X_RIGHT_SRVICE: float = 250
COURT_LENGTH: float = 900
COURT_WIDTH: float = 550
SINGLE_COURT_WIDTH: float = 400


def main() -> None:
    """The Tennis Court Builder!"""
    gabe: Turtle = Turtle()
    gabe.speed(1000)
    gabe.fillcolor(32, 192, 211)
    gabe.begin_fill()
    draw_court(gabe, LEFT_X_COURTCORD, TOP_Y_COURTCORD, COURT_LENGTH, COURT_WIDTH, 0.0)
    gabe.end_fill()
    gabe.pensize(5)
    gabe.color(255, 255, 255)
    draw_court(gabe, LEFT_X_COURTCORD, TOP_Y_COURTCORD, COURT_LENGTH, COURT_WIDTH, 0.0)
    line_drawer(gabe, LEFT_X_COURTCORD, TOP_Y_SINGLES_COURTCORD, COURT_LENGTH, 0.0)
    line_drawer(gabe, LEFT_X_COURTCORD, BOT_Y_SINGLES_COURTCORD, COURT_LENGTH, 0.0)
    line_drawer(gabe, X_LEFT_SERVICE, TOP_Y_SINGLES_COURTCORD, SINGLE_COURT_WIDTH, -90)
    line_drawer(gabe, X_RIGHT_SRVICE, TOP_Y_SINGLES_COURTCORD, SINGLE_COURT_WIDTH, -90)
    line_drawer(gabe, TOP_Y_COURTCORD, -25, SINGLE_COURT_WIDTH, 180)
    gabe.color(0, 0, 0)
    gabe.pensize(3)
    net_drawer(gabe, X_MID_COURT, TOP_Y_SINGLES_COURTCORD, SINGLE_COURT_WIDTH + 10, 50, 60)
    line_drawer(gabe, LEFT_X_COURTCORD, BOT_Y_COURTCORD, 100, -60)
    line_drawer(gabe, gabe.xcor(), gabe.ycor(), COURT_LENGTH, 0.0)
    line_drawer(gabe, gabe.xcor(), gabe.ycor(), 100, 120)
    crowd_heads(gabe, LEFT_X_COURTCORD + 50, BOT_Y_COURTCORD, 15)
    gabe.pencolor(255, 255, 255)
    gabe.fillcolor(20, 52, 97)
    gabe.begin_fill()
    draw_court(gabe, LEFT_X_COURTCORD - 5, TOP_Y_COURTCORD, COURT_WIDTH, SINGLE_COURT_WIDTH, -90)
    gabe.end_fill()
    gabe.begin_fill()
    draw_court(gabe, RIGHT_X_COURTCORD + 5, TOP_Y_COURTCORD, SINGLE_COURT_WIDTH, COURT_WIDTH, 0.0)
    gabe.end_fill()
    gabe.color(187, 146, 94)
    players(gabe, 1, 15)
    players(gabe, 2, 15)
    sky_draw(gabe, -715, 253, 15, 1500, 255, 131, 0)
    tennis_ball(gabe, 2)
    gabe.pensize(1)
    sun(gabe, TOP_Y_COURTCORD, 250, 200, 90)
    done()


def draw_court(gabe_turtle: Turtle, x: float, y: float, width: float, length: float, angle: float) -> None:
    """Draw a rectangualar court with x,y being top_left corner!"""
    gabe_turtle.penup()
    gabe_turtle.goto(x, y)
    gabe_turtle.setheading(angle)
    gabe_turtle.pendown()
    i: int = 0
    while i < RECT_SIDES:
        if i == RECT_SIDE1 or i == RECT_SIDE3:
            gabe_turtle.forward(width)
            gabe_turtle.right(RECT_ANGLE)
        else:
            gabe_turtle.forward(length)
            gabe_turtle.right(RECT_ANGLE)
        i += 1


def line_drawer(gabe_turtle: Turtle, x: float, y: float, length: float, angle: float) -> None:
    """Draw lines for the tennis court and delimitations of other aspects of the paint!"""
    gabe_turtle.penup()
    gabe_turtle.goto(x, y)
    gabe_turtle.setheading(angle)
    gabe_turtle.pendown()
    gabe_turtle.forward(length)


def net_drawer(gabe_turtle: Turtle, x: float, y: float, width: float, length1: float, angle: float) -> None:
    """A code that draws a tennis net with the aid of other two functions defined lower in this program!

    I am attempting to fulfill the requirement for 10 points that asks to simplified one of my functions.
    I did so by creating a two separate functions that draw the vertical lines and the horizontal lines!
    """
    gabe_turtle.penup()
    gabe_turtle.goto(x, y)
    gabe_turtle.setheading(angle)
    gabe_turtle.pendown()
    i: int = 0
    while i < TWO_SIDES_NET:
        if i == NET_SIDE1: 
            gabe_turtle.forward(length1)
            gabe_turtle.right(150)
        if i == NET_SIDE2:
            gabe_turtle.forward(width)
            gabe_turtle.right(45)
        i += 1
    net_mesh(gabe_turtle, x, y, length1, 60) 
    net_mesh_h(gabe_turtle, x, y, width - 5, 15, 60, -90) 


def net_mesh(gabe_turtle: Turtle, x: float, y: float, z: float, angle: float) -> None:
    """Vertical lines for Tennis net! FUnction used to simplified net_drawer!"""
    gabe_turtle.penup()
    gabe_turtle.goto(x, y)
    gabe_turtle.setheading(angle)
    gabe_turtle.pendown()
    i: int = 0
    while i < VERTICAL_NET:
        y -= SPACE_VERT_NET_LIN
        gabe_turtle.forward(z)
        gabe_turtle.penup()
        gabe_turtle.goto(x, y)
        gabe_turtle.pendown()
        i += 1


def net_mesh_h(gabe_turtle: Turtle, x: float, y: float, z: float, start_pt: int, angle1: float, angle2: float) -> None:
    """Horizontal lines ofr the Tennis Net. Function used to simplified Net_drawer!"""
    i: int = 0
    start_pt = start_pt
    while i < 2:
        gabe_turtle.penup()
        gabe_turtle.goto(x, y)
        gabe_turtle.setheading(angle1)
        gabe_turtle.forward(start_pt)
        gabe_turtle.pendown()
        gabe_turtle.setheading(angle2)
        gabe_turtle.forward(z)
        start_pt += START_PT_CHANGE
        i += 1


def crowd_heads(gabe_turtle: Turtle, x: float, y: float, rad: float) -> None:
    """Drawing machine for the tennis fans in this court!"""
    x = x
    y = y
    i: int = 0
    gabe_turtle.fillcolor(187, 146, 94)
    while i <= NUM_FANS:
        if i == ROW1_FANS or i == ROWS_1_2_FANS:
            gabe_turtle.penup()
            gabe_turtle.goto(x, y)
            gabe_turtle.pendown()
            gabe_turtle.begin_fill
            gabe_turtle.circle(rad)
            gabe_turtle.end_fill
            x -= X_SPACES_BY_FANS
            y -= Y_SPACES_BY_FANS
            
        else:
            gabe_turtle.penup()
            gabe_turtle.goto(x, y)
            gabe_turtle.pendown()
            gabe_turtle.begin_fill
            gabe_turtle.circle(rad)
            gabe_turtle.end_fill
            x += FANS_DISTANCING
        i += 1
        

def players(gabe_turtle: Turtle, player_number: int, head: float) -> None:
    """A machine that draws tennis players anywhere within a defined area.

    It makes use of a random function called uniform that helps me defined the area! 
    With this I am attempting to fulfill the last 5 points from the instructions!
    """
    y: float = uniform(BOT_Y_SINGLES_COURTCORD, TOP_Y_SINGLES_COURTCORD)
    if player_number == 1 or player_number == 3:
        x: float = uniform(LEFT_X_COURTCORD, X_MID_COURT - 20)
    else: 
        x = uniform(X_MID_COURT + 20, RIGHT_X_COURTCORD)
    line_drawer(gabe_turtle, x, y, 40, 90)
    new_x: float = gabe_turtle.xcor()
    new_y: float = gabe_turtle.ycor()
    line_drawer(gabe_turtle, new_x, new_y, 35, 210)
    line_drawer(gabe_turtle, new_x, new_y, 35, -30)
    line_drawer(gabe_turtle, x, y, 45, 240)
    line_drawer(gabe_turtle, x, y, 45, -60)
    gabe_turtle.penup()
    gabe_turtle.goto(new_x, new_y)
    gabe_turtle.pendown()
    gabe_turtle.setheading(0.0)
    gabe_turtle.circle(head)


def sky_draw(gabe_turtle: Turtle, x: float, y: float, psize: int, lenght: float, r: float, g: float, b: float) -> None:
    """A code that draws lines of defined thickness and incrasing color tones, used for the sky in this picture!"""
    i: int = 0
    x = x
    y = y
    g = g
    b = b
    while i < NUM_SKY_LINES:
        gabe_turtle.penup()
        gabe_turtle.goto(x, y)
        gabe_turtle.pencolor(r, g, b)
        gabe_turtle.pendown()
        gabe_turtle.pensize(psize)
        gabe_turtle.forward(lenght)
        y += Y_DISTANCING_SKY
        i += 1
        g += SKY_TONECOLOR_CHANGE
        b += SKY_TONECOLOR_CHANGE


def sun(gabe_turtle: Turtle, x: float, y: float, rad: float, angle: float) -> None:
    """Sun drawer!"""
    gabe_turtle.penup()
    gabe_turtle.goto(x, y)
    gabe_turtle.pendown()
    gabe_turtle.setheading(angle)
    gabe_turtle.color(255, 224, 0)
    gabe_turtle.begin_fill()
    gabe_turtle.circle(rad, SUN_LENGTH)
    gabe_turtle.end_fill()
    

def tennis_ball(gabe_turtle: Turtle, rad: float) -> None:
    """Code that draws a tennis ball anywhere in the court. It uses a function imported from random called uniform!"""
    y: float = uniform(BOT_Y_SINGLES_COURTCORD, TOP_Y_SINGLES_COURTCORD)
    x: float = uniform(LEFT_X_COURTCORD, RIGHT_X_COURTCORD)
    gabe_turtle.penup()
    gabe_turtle.goto(x, y)
    gabe_turtle.pendown()
    gabe_turtle.fillcolor(209, 255, 0)
    gabe_turtle.begin_fill()
    gabe_turtle.circle(rad)
    gabe_turtle.end_fill()


if __name__ == "__main__":
    main()