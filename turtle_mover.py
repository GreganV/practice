import turtle
turtle.speed(0) 
I = True
while I == True:
    direct = input("enter w,a,s,d: ")
    if direct== "w":
        turtle.forward(10)
    elif direct== "a":
        turtle.left(90)
        turtle.forward(10)
    if direct== "s":
        turtle.backward(10)
    
    if direct== "d":
        turtle.right(90)
        turtle.forward(50)
    elif direct == "b":
        turtle.teleport(0,0)
    elif direct == "c":
         for i in range(72):
             turtle.forward(4)
             turtle.left(5)
    if direct == "bc":
        for i in range(72):
             turtle.forward(-4)
             turtle.left(5)
