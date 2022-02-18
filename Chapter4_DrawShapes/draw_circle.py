#!/usr/bin/env python3

import turtle

"""
This module contains functions related to drawing a circle using turtle

Helpful reference: 
https://www.techwithtim.net/tutorials/python-module-walk-throughs/turtle-module/shapes-and-fills/
https://www.geeksforgeeks.org/draw-square-and-rectangle-in-turtle-python/
"""

__author__ = 'Debbie Johnson'
__version__ = '1.0'
__copyright__ = "Copyright 2022.02.10, Chapter 4 Assignment"
__github__ = "https://github.com/dejohns2/CSC365_Spring2022_Code_Examples"


screen = turtle.Screen()
# screen.bgcolor("black")  # this matches the pen color so you won't see the outline of the drawing ;)

t = turtle.Turtle()


def draw_circle(x, y, pensize, color, rad):
    t.shape("turtle")
    t.up()
    t.pensize(pensize)
    t.goto(x, y)
    t.down()
    t.begin_fill()
    t.fillcolor(color)
    t.circle(rad)
    t.end_fill()
    t.up()
    t.home()

def main():
    """
    The main function, used to test drawing a square using the turtle library.

    Args:
        no value
    Returns:
        no value
    """
    draw_circle(-50, -150, 5, "green", 50)
    draw_circle(0, 100, 10, "orange", 75)
    draw_circle(-200, 150, 20, "blue", 100)
    turtle.done()


# if this is the program starting module, then run the main function
if __name__ == '__main__':
    main()

