def math(st):
    op = ['+','-' ,'*','/']
    oprs = []
    for i in st:
        for j in range(4):
            if i == op[j]:
                oprs.append(i)
    for i in range(4):
        math = st.split(op[i])
        st = ' '.join(math)
    math = st.split(' ')
    while '' in math:
        math.remove('')
    for i in range(len(math)):
        math[i] = int(math[i])
    count = 0
    while '*' in oprs or '/' in oprs:
        if oprs[count] == '*':
            math[count] = math[count] * math[count+1]
            math.pop(count+1)
            oprs.pop(count)
            count -= 1
        elif oprs[count] == '/':
            math[count] = math[count] / math[count+1]
            math.pop(count+1)
            oprs.pop(count)
            count -= 1
        count += 1
    count = 0
    while '+' in oprs or '-' in oprs:
        if oprs[count] == '+':
            math[count] = math[count] + math[count+1]
            math.pop(count+1)
            oprs.pop(count)
            count -= 1
        elif oprs[count] == '-':
            math[count] = math[count] - math[count+1]
            math.pop(count+1)
            oprs.pop(count)
            count -= 1
        count += 1
    print(math[0])
st = input('Enter your math expression: ')
math(st)
