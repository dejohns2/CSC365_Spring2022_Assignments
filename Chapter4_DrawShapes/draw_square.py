#!/usr/bin/env python3

import turtle
import globals

"""
This module contains functions related to drawing a square using turtle

Helpful reference: 
https://www.techwithtim.net/tutorials/python-module-walk-throughs/turtle-module/shapes-and-fills/
https://www.geeksforgeeks.org/draw-square-and-rectangle-in-turtle-python/
"""

__author__ = 'Debbie Johnson'
__version__ = '1.0'
__copyright__ = "Copyright 2022.02.10, Chapter 4 Assignment"
__github__ = "https://github.com/dejohns2/CSC365_Spring2022_Code_Examples"


def draw_square(length=100):
    """
    the draw_square_shape function is use to draw a square

    Args:
        t (turtle): turtle object
        length (int): the square's side length - default value 100
    Returns:
        no value
    """

    globals.t.hideturtle()  # make the turtle invisible
    globals.t.color("red")
    globals.t.width(50)  # line width
    globals.t.shape("turtle")
    globals.t.penup()  # don't draw when turtle moves
    globals.t.goto(-250, 50)  # move the turtle to a location
    globals.t.showturtle()  # make the turtle visible
    globals.t.pendown()  # draw when the turtle moves

    globals.t.color("green", "yellow")  # blue is the fill color

    globals.t.begin_fill()

    # draw square
    for _ in range(0, 4):
        globals.t.forward(length)  # Forward turtle by l units
        globals.t.left(90)  # Turn turtle by 90 degree

    globals.t.end_fill()

    # tim.reset() would clear the screen
    # tim.home() would return to the home position


def main():
    """
    The main function, used to test drawing a square using the turtle library.

    Args:
        no value
    Returns:
        no value
    """

    globals.wn.bgcolor("lightblue")
    globals.wn.title("SQUARE")

    draw_square()


# if this is the program starting module, then run the main function
if __name__ == '__main__':
    globals.initialize()
    main()
