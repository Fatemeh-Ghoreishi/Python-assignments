while True:
    number = int(input('Enter your desired integer number: '))
    if number >= 0 :
        break
    else:
        print('Please enter a positive number!')
        continue
x , result = 1 , 1
if number == 1:
    print('Your number is a factorial of 1 or 0')
else:
    while True:
        if result <= number:
            result = result * x
            x += 1
            if result == number:
                print('Your number is a factorial of ' ,x-1)
                break
            else:
                continue
        else:
            print('Your number is not factorail of other number.')
            break