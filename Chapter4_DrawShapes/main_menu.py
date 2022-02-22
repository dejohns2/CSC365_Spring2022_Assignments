#!/usr/bin/env python3

import validation
import moving_circle
import draw_square

"""
This script has the menu controls for displaying shapes

Helpful reference: 
https://www.techwithtim.net/tutorials/python-module-walk-throughs/turtle-module/shapes-and-fills/
https://www.geeksforgeeks.org/draw-square-and-rectangle-in-turtle-python/
"""

__author__ = 'Debbie Johnson'
__version__ = '1.0'
__copyright__ = "Copyright 2022.02.17, Chapter 4 Assignment"
__github__ = "https://github.com/dejohns2/CSC365_Spring2022_Code_Examples"


def display_menu():
    print("Draw Shapes")
    print()
    print("MENU")
    print("1. Square")
    print("2. Moving Circle")
    print("0. Exit")
    print()


def main():

    while True:
        display_menu()
        option = validation.get_int('Enter a menu option: ', 0, 2)
        if option == 1:
            draw_square.main()
        elif option == 2:
            moving_circle.main()
        elif option == 0:
            break
        else:
            print("You must enter a valid menu number.")


if __name__ == "__main__":
    main()
