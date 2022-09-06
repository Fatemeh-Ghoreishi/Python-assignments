names = ['ali', 'atefe', 'reza', 'homa', 'amir', 'fateme']
new_list , numbers = [] , []
count = 1
for i in range(1, 4):
    print(f'Enter your name {count} :')
    name = input()
    new_list.append(name)
    print(f'Enter your number {count} :')
    number = int(input())-1
    new_list.append(number)
    numbers.append(number)
    count += 1

numbers.sort()

for i in range (0, 3):
    n = 0
    num = 1
    if numbers[i] == new_list[num]:
        names.insert(new_list[num], new_list[n])
    n += 2
    num += 2
    if numbers[i] == new_list[num]:
        names.insert(new_list[num], new_list[n])
    n += 2
    num += 2
    if numbers[i] == new_list[num]:
        names.insert(new_list[num], new_list[n])
print(names)