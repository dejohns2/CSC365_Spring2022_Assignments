import turtle

def initialize():
    # you can only have one screen window (wn) and turtle cursor (t)
    # not sure why programmers use wn as a variable name, but it does seem to be the norm
    global wn
    global t

    wn = turtle.Screen()  # used to control the window
    t = turtle.Turtle()   # basically this is your cursor that you used to draw with

    wn.mainloop()  # keep the program looping
