numbers = []
w = 1
k = 0
m = True
y = -1
for i in range(10):
    while True:
        print('Enter your number' ,w,':')
        vorodi = int(input())
        if vorodi < 0:
            print('Enter your number again!')
            continue
        else:
            w += 1
            numbers.append(vorodi)
            break

while m:
    m = False
    y += 1
    for i in range(1, len(numbers) - y):
        if numbers[i - 1] > numbers[i]:
            x = numbers[i]
            numbers[i] = numbers[i - 1]
            numbers[i - 1] = x
            m = True
print (numbers)