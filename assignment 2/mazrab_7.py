number = int(input('Give me a number: '))
new_number = number % 7

if (new_number == 0):
    print('Your number is divisible by 7.')
elif (1 <= new_number <= 6):
    next_number = ((number - new_number ) + 7)
    print("Your number is not divisible by 7, next number is " ,next_number)