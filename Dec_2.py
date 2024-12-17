def x2_minus3x4(x):
    return (x**2)-(3*x)+4

print((x2_minus3x4(2)))

def quad(b,c,x, a = 1):
    return a*(x**2)+b*x+c

print(quad(4,7,5))

import turtle

world = turtle.Screen()
world.screensize(400,400)
world.setup(400,400)

turtle.teleport(0,400)
turtle.goto(0,-400)

turtle.teleport(-400,0)
turtle.goto(400,0)

turtle.teleport(-30,x2_minus3x4(-30))

for i in range(-30,30):
    turtle.goto(i, x2_minus3x4(i))
