import turtle

"""
Objects & methods that all shapes uses to share one global turtle and window screen.
"""

__author__ = 'Debbie Johnson'
__version__ = '1.0'
__copyright__ = "Copyright 2022.02.17, Chapter 4 Assignment"
__github__ = "https://github.com/dejohns2/CSC365_Spring2022_Code_Examples"

wn = None  # the global window screen that all shapes will share
t = None   # the global turtle that all shapes will share


def turtle_setup():
    """
    All shape need to share the same window screen & turtle objects
    Also, sets the newly open window screen on top of other windows

    Returns:
        None
    """
    global wn, t
    wn = turtle.Screen()  # used to control the window
    t = turtle.Turtle()  # basically this is your cursor that you used to draw with

    # make sure the turtle window screen displays on top of other open windows
    root_window = wn.getcanvas().winfo_toplevel()  # get the top level turtle screen canvas
    root_window.call('wm', 'attributes', '.', '-topmost', '1')  # and make it have the top focus


def screen_recreation():
    """
    After the user closes the turtle window, force the recreation of the turtle screen window
    in prep for the next shape that might be displayed

    Returns:
        None
    """

    turtle.Turtle._screen = None  # force recreation of singleton Screen object
    turtle.TurtleScreen._RUNNING = True  # only set upon TurtleScreen() definition

