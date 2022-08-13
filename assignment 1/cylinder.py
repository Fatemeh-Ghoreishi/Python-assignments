radius = int(input("please enter radius of the cylinder: "))
height = int(input("please enter height of the cylinder: "))
pi = 3.14

side_area = (2*pi*radius*height)
total_area = ((side_area)+(2*pi*radius*radius))
volume = (pi*radius*radius*height)

print("side_area:",side_area)
print("total_area:" ,total_area)
print("volume:",volume)
