password = 1234
count = 0
while True:
    code = int(input('\nEnter your password: '))
    r = int(code/1000)
    if (0 < r <= 9):
        count +=1
        if code == 4321:
            print('\nWarning! The police were informed.')
            break
        elif code == password:
            print('\nYoyr password is correct, Welcome!')
            break
        elif count < 3:
            print('\nYour password is wrong, Please try again!')
        elif count == 3:
            print('\nYour account is locked!')
            break
    else:
        print('\nTry again!')