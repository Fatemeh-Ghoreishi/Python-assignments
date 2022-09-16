row = int(input('Enter number of rows: '))
col = int(input('Enter number of columns: '))
list = []
a , b = 1 , 1
for r in range(row):
    list.append([])
    for i in range(col):
        new_list = list[r]
        new_list.append([])
for i in range(row):
    for j in range(col):
        x = a * b
        list[i][j] = x
        b += 1
    a += 1
    b = 1
for i in range(row):
    for c in range(col):
        print(list[i][c], end='\t')
    print()