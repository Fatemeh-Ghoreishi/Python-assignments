import random
first = 0
end = 9
number = []
while True:
    x = int(input('Enter your desired integer number: '))
    if (x < 0):
        print('Enter a integer number !')
        continue
    else:
        break

for i in range(x):
    numbers = random.randint(first, end)
    number.append(numbers)
    first += 10
    end += 10

print (number)
