import random
sum = 0
while True:
    dice = random.randint(1, 6)
    if dice == 6:
        print(dice)
        print('You are lucky :)')
        sum += dice
        continue
    else:
        sum += dice
        print(dice)
        print('sum of number: ',sum)
        break