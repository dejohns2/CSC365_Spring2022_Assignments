#!/usr/bin/env python3

"""
This module contains functions related to drawing and moving a circle around the screen
"""

__author__ = 'Debbie Johnson'
__version__ = '1.0'
__copyright__ = "Copyright 2022.02.17, Chapter 4 Assignment"
__github__ = "https://github.com/dejohns2/CSC365_Spring2022_Code_Examples"

import turtle
import random
import validation

s = None  # used to control the window
t = None  # basically this is your cursor that you used to draw with

num_moves = 0

# set the difficulty of the game by the size of the circles
circle_size = 50
move_size = 20

# position where the turtle will be drawn at
# these values will change by plus/minus 20 as arrows are pressed
previous_x = 0
previous_y = 0
x = 0  # center of screen moving right or left
y = 0  # center of screen moving up or down
fill_color = 'blue'  # the color of the circle

# used to control the hidden circle location
hidden_x = 0
hidden_y = 0
hidden_color = 'black'

def setup_window():
    """
    Controls how the window looks.

    Args:
        bg_color (str): the background color of the window (default white)

    Returns:
        None
    """

    s.tracer(False)  # turn animation off which causes screen flickering as the circle gets redrawn
    s.title('Moving Circle')  # title the title bar of the window
    s.bgcolor('black')       # set the window's background color
    # s.setup(800, 900)         # the size of the window

    # set up the keys to listen to and what function should be called
    s.onkeypress(debug, 'd')
    s.onkeypress(reset, 'r')
    s.onkeypress(move_home, 'h')
    s.onkeypress(move_up, 'Up')
    s.onkeypress(move_down, 'Down')
    s.onkeypress(move_right, 'Right')
    s.onkeypress(move_left, 'Left')
    s.listen()  # start listening for keys being pressed


def set_random_location():
    global hidden_x, hidden_y, circle_size

    while True:
        hidden_x = random.randint(-420, 420)
        hidden_y = random.randint(-300, 300)

        if abs(hidden_x) > (circle_size) and abs(hidden_y) > (circle_size):
            break


def reset():
    global s, x, y, num_moves, hidden_color

    num_moves = 0
    x = 0  # center of screen moving right or left
    y = 0  # center of screen moving up or down
    hidden_color = 'black'
    s.reset()
    main()
    # get_size()
    # set_random_location()
    # display_game()


def debug():
    global hidden_color
    if hidden_color == 'black':
        hidden_color = 'white'
    else:
        hidden_color = 'black'
    display_game()


def move_home():
    """
    Reset the x and y back to zero coordinate which will be used position the circle in the center
    then call draw_circle to clear & redraw the circle is on the screen based on its new location

    Returns:
        None
    """

    global x, y
    x = 0  # center of screen moving right or left
    y = 0  # center of screen moving up or down
    display_game()


def move_left():
    """
    Subtract 20 from the x coordinate which will be used move the circle to the left
    then call draw_circle to clear & redraw the circle is on the screen based on its new location

    Returns:
        None
    """

    global x, num_moves
    x -= move_size  # move to the left of center
    num_moves += 1
    display_game()


def move_right():
    """
    Add 20 to the x coordinate which will be used move the circle to the right
    then call draw_circle to clear & redraw the circle is on the screen based on its new location

    Returns:
        None
    """

    global x, num_moves

    x += move_size  # move to the right of center
    num_moves += 1
    display_game()


def move_up():
    """
    Add 20 to the y coordinate which will be used move the circle up
    then call draw_circle to clear & redraw the circle is on the screen based on its new location

    Returns:
        None
    """

    global y, num_moves

    y += move_size  # move top of center
    num_moves += 1
    display_game()


def move_down():
    """
    Subtract 20 from y coordinate which will be used move the circle to the down
    then call draw_circle to clear & redraw the circle is on the screen based on its new location
    Returns:
        None
    """

    global y, num_moves

    y -= move_size  # move down of center
    num_moves += 1
    display_game()


def get_size():
    global circle_size, move_size

    circle_size = int(turtle.numinput('Circle', '"Size of circles', minval=10, maxval=100))
    move_size = int(turtle.numinput('Circle', 'Size of move', minval=10, maxval=100))


def set_fill_color():
    global hidden_color, fill_color, x, y, previous_x, previous_y, hidden_x, hidden_y

    overlap = circle_size / 100
    if abs(x - hidden_x) < (circle_size * 2 - overlap) and abs(y - hidden_y) < (circle_size * 2 - overlap):
        hidden_color = 'green yellow'
        fill_color = 'green yellow'
    else:
        if previous_x != x:
            if abs(previous_x - hidden_x) > abs(x - hidden_x):
                fill_color = 'red'
            else:
                fill_color = 'blue'

        if previous_y != y:
            if abs(previous_y - hidden_y) > abs(y - hidden_y):
                fill_color = 'red'
            else:
                fill_color = 'blue'

    previous_x = x
    previous_y = y


def display_instructions():
    global num_moves

    # write text on the screen
    t.penup()            # don't want to see icon moving on the screen
    t.pencolor('white')  # text color
    t.goto(-450, 370)    # from the current position which is center after clear, move left 350 up 350
    t.write("Total moves = " + str(num_moves), font=("Verdana", 12, "bold"))
    t.goto(-450, 330)    # from the current position which is center after clear, move left 350 up 350
    t.write("Use arrows to move", font=("Verdana", 12, "bold"))
    t.goto(-450, 310)    # from the current position which is center after clear, move left 350 up 350
    t.write("d = debug", font=("Verdana", 12, "bold"))
    t.goto(-450, 290)    # from the current position which is center after clear, move left 350 up 350
    t.write("h = home", font=("Verdana", 12, "bold"))
    t.goto(-450, 270)    # from the current position which is center after clear, move left 350 up 350
    t.write("r = reset", font=("Verdana", 12, "bold"))


def display_hidden_circle():
    global hidden_x, hidden_y, hidden_color, circle_size
    t.penup()
    t.goto(hidden_x, hidden_y)             # move to the updated x (left-right) and y (up-down) location from center
    t.pendown()              # start drawing the outline of the circle
    t.pencolor(hidden_color)
    t.fillcolor(hidden_color)  # fill color of the circle
    t.begin_fill()           # start the fill of whatever is being drawn
    t.circle(circle_size)             # diameter of the circle
    t.end_fill()             # done drawing the object to complete the fill


def display_user_circle():
    global x, y, circle_size, fill_color

    t.penup()
    t.goto(x, y)             # move to the updated x (left-right) and y (up-down) location from center
    t.pendown()              # start drawing the outline of the circle
    t.pencolor(fill_color)
    t.fillcolor(fill_color)  # fill color of the circle
    t.begin_fill()           # start the fill of whatever is being drawn
    t.circle(circle_size)             # diameter of the circle
    t.end_fill()             # done drawing the object to complete the fill


def display_game():
    """
    clear the screen and draw the circle based on the x & y coordinates

    Returns:
        None
    """

    global x, y, fill_color

    t.speed('fastest')  # draw quickly
    t.clear()  # clear the previous screen for the update circle location

    display_instructions()

    set_fill_color()
    display_hidden_circle()
    display_user_circle()


def main():
    """
    The main function, used to test drawing a square

    Returns:
        None
    """

    global s, t, circle_size, move_size

    get_size()
    set_random_location()

    setup_window()  # configure how the turtle window screen will look like

    display_game()  # draw the initial shape based on diameter

    s.mainloop()  # keep the turtle window open until the user closes it

# if this is the program starting module, then run the main function
if __name__ == '__main__':
    s = turtle.Screen()  # used to control the window
    t = turtle.Turtle(visible=False)  # basically this is your cursor that you used to draw with

    main()
