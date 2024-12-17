import turtle as t
t.shape('turtle')
def new_location(turn,deg,lenght):
    if turn == "left":
        t.left(deg)
    if turn == "right":
        t.right(deg)

    else:
        pass
    t.penup()
    t.forward(lenght)
    t.pendown()


t.pencolor("purple")
# makes color purple
#creates square
for i in range(5):
    t.forward(50)
    t.left(90)

#moves to new location
new_location(0,0,100)

t.pencolor("orange")
#makes color orange
#regular hexagon
for i in range(6):
    t.forward(50)
    t.left(60)

#moves to new location 
new_location("left",90,100)

t.pencolor("red")
#makes color red
#makes irregular hexagon
for i in range(3):
    t.forward(50)
    t.left(45)
    t.forward(50)
    t.left(75)

#moves to new location
new_location("left",180,200)

t.pencolor("blue")
#makes color blue
#makes rectangle

for i in range(2):
    t.forward(100)
    t.left(90)
    t.forward(50)
    t.left(90)

new_location("right",90,300)

#makes circle
for i in range(72):
    t.forward(5)
    t.left(5)

#back to center
t.penup()
t.left(90)
t.forward(50)
t.pendown

#new, bigger circle
for i in range(72):
    t.forward(5.2)
    t.left(5)

#back to center
t.penup()
t.left(90)
t.forward(50)
t.pendown

