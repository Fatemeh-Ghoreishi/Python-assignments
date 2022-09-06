list = []
control = 0
for i in range(10):
    number = int(input('Eter your numbers:'))
    list.append(number)

for i in range(1, len(list)):
    if (list[i - 1] < list[i]) or (list[i - 1] > list[i]):
        control = True
        continue
    else:
        control = False
        break

if control == True:
    print('Yes')
else:
    print('No')==