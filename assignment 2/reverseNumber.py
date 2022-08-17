new_number = number= int(input('Enter your number: '))
while True:
    if number < 0:
        print('Please enter a positive and integer number.')
        new_number = number= int(input('Enter your number: '))
    else:
        break

rev = 0
while new_number != 0:
    if new_number >= 0:
        x = new_number % 10
        rev  = (rev*10) + x
        new_number = int(new_number / 10)
print(rev)
if (rev == number):
    print('The number is equal to its inverse.')
elif (rev != number):
    print('The number is not equal to its inverse.')