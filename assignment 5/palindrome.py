word = input('Enter your word: ')
st = word.split()
st = ''.join(st)
st = st.split(',')
st = ''.join(st)
st = st.split(';')
st = ''.join(st)
st = st.split("'")
st = ''.join(st)
st = st.upper()
print(st)
x = len(st)
j = -1
count = 0
c = int(x/2)
if x % 2 != 0:
    y = (x / 2) + 1
    for i in range(c):
        if st[i] == st[j]:
            j -= 1
            count += 1
            continue
        else:
            break
    if c == count:
        print('Your word is palindrome :)')
    else:
        print('Your word is not palindrome.')
elif x % 2 == 0:
    print('Your word is not palindrome.')