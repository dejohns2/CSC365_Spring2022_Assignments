#!/usr/bin/env python3

import globals

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
    global x, y

    globals.t.clear()            # clear the screen
    globals.t.pensize(5)         # how wide the outline will be
    globals.t.pencolor('white')  # color of the outline

    globals.t.penup()            # don't want to see icon moving on the screen
    globals.t.goto(-350, 350)    # from the current position which is center after clear, move left 350 up 350
    globals.t.write("Use arrows to move, or press 'h' for home", font=("Verdana", 12, "bold"))

    globals.t.goto(x, y)
    globals.t.pendown()          # start drawing the outline of the circle
    globals.t.fillcolor('pink')  # fill color of the circle
    globals.t.begin_fill()       # start the fill of whatever is being drawn
    globals.t.circle(50)         # diameter of the circle
    globals.t.end_fill()         # done drawing the object to complete the fill


def main():
    """
    The main function, used to test drawing a square using the turtle library.

    Args:
        no value
    Returns:
        no value
    """

    globals.wn.tracer(False)           # turn animation off which causes screen flickering as the circle gets redrawn
    globals.wn.title("Moving Circle")  # title the title bar of the window
    globals.wn.bgcolor('black')        # set the window's background color
    globals.wn.setup(800, 900)         # se the size of the window

    # t.shape("turtle") this is how you can change what the turtle cursor looks like, but I don't want a cursor
    globals.t.hideturtle()      # don't show the icon
    globals.t.speed('fastest')  # draw quickly

    draw_circle()  # draw the initial shape

    # set up the keys to listen to and what function should be called
    globals.wn.onkeypress(move_home, "h")
    globals.wn.onkeypress(move_up, "Up")
    globals.wn.onkeypress(move_down, "Down")
    globals.wn.onkeypress(move_right, "Right")
    globals.wn.onkeypress(move_left, "Left")
    globals.wn.listen()    # start listening for keys being pressed

    globals.wn.mainloop()


# if this is the program starting module, then run the main function
if __name__ == '__main__':
    main()
