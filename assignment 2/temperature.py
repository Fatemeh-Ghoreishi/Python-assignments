convert_type = float(input('Please choose your convert type:\n 1.Celsius to Kelvin \n 2.Kelvin to Celsius \n 3.Fahrenheit to Celsius \n 4.Celsius to Fahrenheit \n 5.Fahrenheit to kelvin \n 6.Kelvin to Fahrenheit \n '))
while True:
    if convert_type != 1 and convert_type != 2 and convert_type != 3 and convert_type != 4 and convert_type != 5 and convert_type != 6:
        print('\nChoose numbers between 1 and 6 !! \n')
        convert_type = float(input('Please choose your convert type:\n 1.Celsius to Kelvin \n 2.Kelvin to Celsius \n 3.Fahrenheit to Celsius \n 4.Celsius to Fahrenheit \n 5.Fahrenheit to kelvin \n 6.Kelvin to Fahrenheit \n '))
    else:
        break

number1 = int(input('Enter your number:'))

if convert_type == 1:
    print(int(number1 + 273.15),'Kelvin')
elif convert_type == 2:
    print(int(number1 - 273.15),'Celsius')
elif convert_type == 3:
    print(int((number1 - 32) *5 / 9),'Celsius')
elif convert_type == 4:
    print(int(number1 *9 / 5 +32),'Fahrenheit')
elif convert_type == 5:
    print(int(((number1 - 32) *5 / 9) + 273.15),'Kelvin')
else:
    print(int(((number1 - 273.15) *9 / 5) + 32),'Fahrenheit')