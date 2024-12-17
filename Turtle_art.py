import turtle #imports turtle
import random as r #imports random
#instantiates 2 turtles
leo = turtle.Turtle()
don = turtle.Turtle()

leo.shape('turtle') #leo now looks like turtle
#list of my colors
colors = ["orange","red","blue","purple"]

def size_circle(inc):
    leo.hideturtle()
    r.shuffle(colors)    

    leo.fillcolor(colors[0])
    leo.begin_fill()

    for i in range(72):
        leo.forward(inc)
        leo.left(5)
    leo.showturtle()

    for i in range(72):
        leo.forward(inc+1)
        leo.left(5)
    leo.showturtle()

    for i in range(72):
        leo.forward(inc+2)
        leo.left(5)
    leo.end_fill()
    leo.showturtle()

    if colors[0] == "blue":
        leo.fillcolor("green")#Leo is happy
    else:
        leo.fillcolor("red")#leo is mad

size_circle(5)
leo.penup()
leo.forward(100)
leo.pendown()
size_circle(6)



 
