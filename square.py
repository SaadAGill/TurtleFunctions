#!/usr/bin/env python


import turtle


def square(t, x : int , y: int):
    """draw a square
    parameters :
    t : the turtle
    x : the start x position
    y : the start y position
    """
    t.penup()
    t.goto(x,y)
    t.pendown()
    for i in range(4):
        t.left(90)
        t.forward(100)

def quit():
    turtle.bye()

#create my main turtle
my_turtle = turtle.Turtle()
#tell the screen to listen for key events
turtle.Screen().listen()
#if thje escape key is pressed exit
turtle.onkeypress(quit,key="Escape")
#enter main loop so windows stays inview
square(my_turtle, 10, 10)
turtle.mainloop()

