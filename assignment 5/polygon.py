import turtle
number = int(input('Enter the number of sides: '))
color = input('Enter your desired color: ')
b = turtle.Screen()
b.bgcolor('peachpuff')
turtle.pencolor(color)
for i in range(number):
    turtle.fd(80)
    turtle.right(360/number)
turtle.done()