#!/usr/bin/env python3

import global_turtle

"""
This module contains functions related to drawing a square using turtle
"""

__author__ = 'Debbie Johnson'
__version__ = '1.0'
__copyright__ = "Copyright 2022.02.10, Chapter 4 Assignment"
__github__ = "https://github.com/dejohns2/CSC365_Spring2022_Code_Examples"


def setup_window(bg_color='white'):
    """
    Controls how the window looks.

    Args:
        bg_color (str): the background color of the window

    Returns:
        None
    """

    global_turtle.wn.bgcolor(bg_color)
    global_turtle.wn.title('Square Turtle')
    global_turtle.wn.setup(500, 500)  # the size of the window


def draw_square(length=100, line_color='red', fill_color='yellow'):
    """
    the draw_square_shape function is use to draw a square

    Args:
        length (int): the square's side length (default 100)
        fill_color (str): the inside color of the square
        line_color (str): the outside line color of the square

    Returns:
        None
    """

    global_turtle.t.hideturtle()      # make the turtle invisible
    global_turtle.t.width(50)         # make the line width very fat :)
    global_turtle.t.shape("turtle")   # make the cursor look like a turtle instead of an arrow
    global_turtle.t.penup()           # don't draw when turtle moves
    global_turtle.t.goto(-100, -100)  # move the turtle to a location -100 x (left of center) -100 y (down of center)
    global_turtle.t.showturtle()      # make the turtle visible
    global_turtle.t.pendown()         # draw when the turtle moves

    global_turtle.t.color(line_color, fill_color)

    global_turtle.t.begin_fill()  # start the fill based on the next object being drawn

    # draw square
    for _ in range(0, 4):                # loop for 4 times
        global_turtle.t.forward(length)  # Forward turtle by l units
        global_turtle.t.left(90)         # Turn turtle by 90 degree

    global_turtle.t.end_fill()  # stop the fill based on the last object that was drawn


def main():
    """
    The main function, used to test drawing a square using the turtle library.

    Returns:
        no value
    """

    global_turtle.turtle_setup()       # create the window & turtle objects

    setup_window('lightblue')          # configure how the turtle window screen will look like
    draw_square(200, 'pink', 'black')  # draw the turtle square (length, outline, fill)

    global_turtle.wn.mainloop()        # keep the turtle running until the user closes it

    global_turtle.screen_recreation()  # recreate the window screen after it's been closed


# if this is the program starting module, then run the main function
if __name__ == '__main__':
    main()
