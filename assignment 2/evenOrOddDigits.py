number = int(input('Enter your number: '))
even = 0
odd = 0

while number != 0 :
    new_number = int(number % 10)
    number = int(number / 10)
    if (new_number % 2 == 0):
        even = even + 1
    elif (new_number % 2 != 0):
        odd = odd + 1
    else:
        break

if (even > odd):
    print('The number of even digits is more.')
elif (even < odd):
    print('The number of odd digits is more.')
else:
    print('The number of even and odd digits is equal.')
