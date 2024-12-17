import turtle
import random
turtle.penup()
turtle.forward(100)
turtle.pendown()
turtle.left(90)
colors = ["black", "blue", "brown", "cyan", "dark blue", "dark cyan", "dark gray", "dark green",
"dark magenta", "dark red", "dark salmon", "dark sea green", "dark slate blue",
"dark violet", "firebrick", "gray", "green", "green yellow", "indian red", "indigo",
"ivory", "khaki", "light blue", "light coral", "light cyan", "light goldenrod yellow",
"light green", "light gray", "light pink", "light salmon", "light sea green",
"light sky blue", "light slate gray", "light steel blue", "light yellow", "lime",
"lime green", "magenta", "maroon", "midnight blue", "navy", "olive", "orange",
"orange red", "orchid", "pink", "plum", "purple", "red", "rosy brown", "royal blue",
"saddle brown", "salmon", "sandy brown", "sea green", "seashell", "sienna",
"sky blue", "slate blue", "slate gray", "snow", "spring green", "steel blue",
"tan", "teal", "thistle", "tomato", "turquoise", "violet", "wheat", "white",
"yellow", "yellow green"]


for i in range(72):
    num= random.randint(1,31)
    turtle.forward(5)
    turtle.left(5)
    turtle.pencolor(colors[num])

turtle.left(90)
turtle.forward(125)


