import turtle
turtle.bgcolor("Red")
turtle.pensize(2.5)
turtle.speed(15)
color = ['Blue','Yellow']
for a in range(18):
    for i in color:
        turtle.color(i)
        turtle.circle(100)
        turtle.right(10)
turtle.mainloop