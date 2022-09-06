number = int(input('How many name do you have? '))
list = []
new_list = []
counter = 1
for i in range(number):
    print('Enter your names' ,counter, ': ')
    name = str(input())
    list.append(name)
    counter += 1

for name in list:
    if name in new_list:
        continue
    else:
        new_list.append(name)

for name in new_list:
    x = list.count(name)
    print(name, "  " ,x)