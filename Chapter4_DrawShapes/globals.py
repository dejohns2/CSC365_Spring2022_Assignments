import turtle

wn = None
t = None


def turtle_setup():
    global wn, t
    wn = turtle.Screen()  # used to control the window
    t = turtle.Turtle()  # basically this is your cursor that you used to draw with

    root_window = wn.getcanvas().winfo_toplevel()  # get the top level turtle screen canvas
    root_window.call('wm', 'attributes', '.', '-topmost', '1')  # and make it have the top focus


def turtle_recreation():
    turtle.Turtle._screen = None  # force recreation of singleton Screen object
    turtle.TurtleScreen._RUNNING = True  # only set upon TurtleScreen() definition
