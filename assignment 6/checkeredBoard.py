n = int(input('Enter row: '))
m = int(input('Enter column: '))
list , new_list = [] , []
y = int(m / 2)
x = y + 1
if m % 2 != 0:
    j = 0
    k = 1
    for i in range(x):
        list.insert(j, '$')
        j += 2
    for i in range(y):
        list.insert(k, '&')
        k += 2
    j = 0
    k = 1
    for i in range(x):
        new_list.insert(j, '&')
        j += 2
    for i in range(y):
        new_list.insert(k, '$')
        k += 2
else:
    h = 0
    p = 1
    for i in range(y):
        list.insert(h, '$')
        h += 2
    for i in range(y):
        list.insert(p, '&')
        p += 2
    h = 0
    p = 1
    for i in range(y):
        new_list.insert(h, '&')
        h += 2
    for i in range(y):
        new_list.insert(p, '$')
        p += 2
new_list = ''.join(new_list)
list = ''.join(list)
if n % 2 == 0:
    b = int(n/2)
    for i in range(b):            
        print(list)
        print(new_list)
else:
    if n == 1:
        print(list)
    else:
        b = int(n/2)
        for i in range(b):
            print(list)
            print(new_list)
        print(list)