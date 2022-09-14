import math

def delta (a, b, c):
    delt = (b ** 2) - (4 * a * c)
    return delt

a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))

Δ = delta(a, b, c)

if Δ < 0:
    print('This equation has not answer.')
elif Δ == 0:
    ans = -1 * b / a
    print('Root: ',ans)
else:
    x1 = ((-1 * b) - math.sqrt(Δ)) / (2 * a)
    x2 = ((-1 * b) + math.sqrt(Δ)) / (2 * a)

    print('First root: ',x1)
    print('Second root: ',x2)