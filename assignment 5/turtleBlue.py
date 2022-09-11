import turtle
t = turtle.Turtle()
x = turtle.Screen()
x.bgcolor('black')
t.speed(150)
color = ['blue', 'cyan', 'dark blue', 'slategray']
for i in range(202):
    t.fd(i + 1)
    t.right(95)
    t.pencolor(color[i%4])
t.hideturtle()
turtle.done()