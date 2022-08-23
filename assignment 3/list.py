import random

numbers = []
list = []

for i in range (20):
    num = random.randint(0, 99)
    numbers.append(num)

print(numbers)

for i in range (20):
    numbers[i] = numbers[i] * numbers[i]
    list.append(numbers[i])

print(list)