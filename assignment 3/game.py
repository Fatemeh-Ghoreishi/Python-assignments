import random
first = count = x = 0
end = 99
while x == 0:
    guess = random.randint(first, end)
    count += 1
    print('\n',guess)

    while True:
        reply = input('Is the guess correct? (yes / no)\n')
        if reply == 'yes':
            print('Hoora, you have won :) Answer is',guess)
            print('The number of all guesses:' ,count)
            x += 1
            break
        elif reply == 'no':
            while True:
                reply_1 = int(input('1. The desired number is smaller \n2. The desired number is bigger\n'))
                if reply_1 == 1:
                    end = guess
                    break
                elif reply_1 == 2:
                    first = guess
                    break
                else:
                    print('Select 1 or 2 !')
                    continue
            break
        else:
            print('Select yes or no!')