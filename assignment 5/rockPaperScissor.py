import random
list = [1, 2, 3]
count = 1
count1 = 0
count2 = 0
while True:
    player = int(input('Choose one of option (1.Single player / 2.Two player): '))
    if player == 1 or player == 2:
        break
    else:
        print('Please choose 1 or 2 !!')
        continue
while True:
    number = int(input('Choose the winning score:\n1 : one score\n3 : three score\n5 : five score\n'))
    if number == 1 or number == 3 or number == 5:
        break
    else:
        print('Please choose 1 or 2 or 3 !!')
        continue


if player == 1:
    while True:
        while True:
            first_person = int(input(f'Enter your desired option of User (1.rock, 2.paper, 3.scissor), number{count}: '))
            count += 1
            accidental = random.choice(list)
            print(accidental)
            if first_person == accidental:
                print('Equal! Please continue.')
                count -= 1
                continue
            elif (first_person == 1 and accidental == 3) or (first_person == 3 and accidental == 2) or (first_person == 2 and accidental == 1):
                count1 += 1
                break
            elif (first_person == 3 and accidental == 1) or (first_person == 2 and accidental == 3) or (first_person == 1 and accidental == 2):
                count2 += 1
                break
            else:
                print('Please enter the correct option! (1 or 2 or 3)')
                count -= 1
                continue
        if (count1 == number) or (count2 == number):
            break
    if count1 < count2 :
        print(f'\nWinner = system \nscore User: {count1}\tscore system: {count2}')
    else:
        print(f'\nWinner = User \nscore User: {count1}\tscore system: {count2}')

else:
    while True:
        while True:
            first_guy = int(input(f'Enter your desired option of User 1 (1.rock, 2.paper, 3.scissor), number{count}: '))
            second_guy = int(input(f'Enter your desired option of User 2 (1.rock, 2.paper, 3.scissor), number{count}: '))
            count += 1
            if first_guy == second_guy:
                print('Equal! Please continue.')
                count -=1
                continue
            elif (first_guy == 1 and second_guy == 3) or (first_guy == 3 and second_guy == 2) or (first_guy == 2 and second_guy == 1):
                count1 += 1
                break
            elif (first_guy == 3 and second_guy == 1) or (first_guy == 2 and second_guy == 3) or (first_guy == 1 and second_guy == 2):
                count2 += 1
                break
            else:
                print('Please enter the correct option! (1 or 2 or 3)')
                count -= 1
                continue
        if (count1 == number) or (count2 == number):
            break
    if count1 < count2 :
        print(f'\nWinner = User 2 \nscore User1: {count1}\tscore User2: {count2}')
    else:
        print(f'\nWinner = User 1 \nscore User1: {count1}\tscore User2: {count2}')