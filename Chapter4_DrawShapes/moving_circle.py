#!/usr/bin/env python3

import turtle
# import globals

"""
This module contains functions related to drawing and moving a circle around the screen

"""

__author__ = 'Debbie Johnson'
__version__ = '1.0'
__copyright__ = "Copyright 2022.02.17, Chapter 4 Assignment"
__github__ = "https://github.com/dejohns2/CSC365_Spring2022_Code_Examples"


# position where the turtle will be drawn at
# these values will change by plus/minus 20 as arrows are pressed
x = 0
y = 0

wn = turtle.Screen()  # used to control the window
t = turtle.Turtle()  # basically this is your cursor that you used to draw with


def move_home():
    """
    Reset the x and y back to zero coordinate which will be used position the circle in the center
    then call draw_circle to clear & redraw the circle is on the screen based on its new location
    :return: none
    """
    global x, y
    x = 0
    y = 0
    draw_circle()


def move_left():
    """
    Subtract 20 from the x coordinate which will be used move the circle to the left
    then call draw_circle to clear & redraw the circle is on the screen based on its new location
    :return: none
    """
    global x
    x -= 20
    draw_circle()


def move_right():
    """
    Add 20 to the x coordinate which will be used move the circle to the right
    then call draw_circle to clear & redraw the circle is on the screen based on its new location
    :return: none
    """
    global x
    x += 20
    draw_circle()


def move_up():
    """
    Add 20 to the y coordinate which will be used move the circle up
    then call draw_circle to clear & redraw the circle is on the screen based on its new location
    :return: none
    """
    global y
    y += 20
    draw_circle()


def move_down():
    """
    Subtract 20 from y coordinate which will be used move the circle to the down
    then call draw_circle to clear & redraw the circle is on the screen based on its new location
    :return: none
    """
    global y
    y -= 20
    draw_circle()


def draw_circle():
    """
    clear the screen and draw the circle based on the x & y coordinates
    """
    global wn, t, x, y

    t.clear()            # clear the screen
    t.pensize(5)         # how wide the outline will be
    t.pencolor('white')  # color of the outline

    t.penup()            # don't want to see icon moving on the screen
    t.goto(-350, 350)    # from the current position which is center after clear, move left 350 up 350
    t.write("Use arrows to move, or press 'h' for home", font=("Verdana", 12, "bold"))

    t.goto(x, y)
    t.pendown()          # start drawing the outline of the circle
    t.fillcolor('pink')  # fill color of the circle
    t.begin_fill()       # start the fill of whatever is being drawn
    t.circle(50)         # diameter of the circle
    t.end_fill()         # done drawing the object to complete the fill


def main():
    """
    The main function, used to test drawing a square using the turtle library.

    Args:
        no value
    Returns:
        no value
    """

    wn.tracer(False)           # turn animation off which causes screen flickering as the circle gets redrawn
    wn.title("Moving Circle")  # title the title bar of the window
    wn.bgcolor('black')        # set the window's background color
    wn.setup(800, 900)         # se the size of the window

    # t.shape("turtle") this is how you can change what the turtle cursor looks like, but I don't want a cursor
    t.hideturtle()      # don't show the icon
    t.speed('fastest')  # draw quickly

    # set up the keys to listen to and what function should be called
    wn.onkeypress(move_home, "h")
    wn.onkeypress(move_up, "Up")
    wn.onkeypress(move_down, "Down")
    wn.onkeypress(move_right, "Right")
    wn.onkeypress(move_left, "Left")

    wn.listen()    # start listening for keys being pressed
    draw_circle()  # draw the initial shape
    wn.mainloop()


# if this is the program starting module, then run the main function
if __name__ == '__main__':
    main()
