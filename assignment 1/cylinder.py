radius = int(input("please enter radius of the cylinder: "))
height = int(input("please enter height of the cylinder: "))
pi = 3.14
area_of_circle = (pi*radius*radius)
perimeter_of_circle = (2*pi*radius)

side_area = (perimeter_of_circle*height)
total_area = ((side_area)+(2*area_of_circle))
volume = (area_of_circle*height)

print("side_area:",side_area)
print("total_area:" ,total_area)
print("volume:",volume)