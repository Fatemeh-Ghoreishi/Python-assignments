weight = float(input('Enter your weight in Kilograms: '))
height = float(input('Enter your height in meters: '))

new_height = height * height
Bmi = weight / new_height
print(Bmi)
if (16 < Bmi < 18.5):
    print('You are body weight deficit, Be sure to check up on your body and diet.')
elif (18.5 <= Bmi < 24):
    print('You are normal, keep going :)')
elif (24 <= Bmi < 30):
    print('You are weight over, You can reach a normal weight by eating an apple a day.')
elif (30 <= Bmi < 35):
    print('You are obesity first degree, Eat less oil and carbohydrates.')
elif ( 35 <= Bmi < 40):
    print('You are obesity second degree, Use the elevator more so that your knees do not hurt.')
elif ( Bmi >= 40):
    print('You are obesity third weight, I do not have anything to say to you because you have not taken any steps to reduce your weight so far, fat man :(')