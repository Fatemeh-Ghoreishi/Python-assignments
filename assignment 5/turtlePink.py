import turtle
t = turtle.Turtle()
x = turtle.Screen()
x.bgcolor('black')
t.pensize(2)
t.speed(150)
color = ['plum','pink', 'crimson', 'blueviolet']
for i in range(133):
    t.fd(i + 1)
    t.right(50)
    t.pencolor(color[i%4])
t.hideturtle()
turtle.done()