#!/usr/bin/env python3

import turtle
# import globals

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


def draw_square(t, length=100):
    """
    the draw_square_shape function is use to draw a square

    Args:
        t (turtle): turtle object
        length (int): the square's side length - default value 100
    Returns:
        no value
    """

    t.hideturtle()  # make the turtle invisible
    t.color("red")
    t.width(50)  # line width
    t.shape("turtle")
    t.penup()  # don't draw when turtle moves
    t.goto(-250, 50)  # move the turtle to a location
    t.showturtle()  # make the turtle visible
    t.pendown()  # draw when the turtle moves

    t.color("green", "yellow")  # blue is the fill color

    t.begin_fill()

    # draw square
    for _ in range(0, 4):
        t.forward(length)  # Forward turtle by l units
        t.left(90)  # Turn turtle by 90 degree

    t.end_fill()


def main():
    """
    The main function, used to test drawing a square using the turtle library.

    Args:
        no value
    Returns:
        no value
    """
    wn = turtle.Screen()  # used to control the window
    t = turtle.Turtle()   # basically this is your cursor that you used to draw with

    wn.bgcolor("lightblue")
    wn.title("SQUARE")
    #wn.exitonclick()

    draw_square(t, 100)



# if this is the program starting module, then run the main function
if __name__ == '__main__':
    main()
