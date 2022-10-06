import math
use = int(input("How many times do you want to use it ? "))
use_type = input("1 = Basic \n2 = Advanced\n")
if use_type == "1" or use_type == "Basic":
    for i in range(use):
        num1 = float(input("Enter number 1: "))
        num2= float(input("Enter number 2: "))
        op_list = ["Enter operator: ", "+", "-" , "*" , "/"] 
        print('\n'.join( op_list))
        op_list = input('Choose: ')
        if op_list == "+":
            res = num1 + num2
            print ("Answer = ", res)
        elif op_list == "-":
            res = num1 - num2
            print ("Answer = ", res)
        elif op_list == "*":
            res = num1 * num2
            print ("Answer = ", res)
        elif op_list == "/":
            if num2 == 0:
                print('Division by zero (0) is not allowed.')
                print('You used the calculator', i + 1 ,'times.')
                continue
            else:
                res = num1 / num2
                print ("Answer = ", res)
        else:
            print('operator is not correct')
            continue
        print('You used the calculator', i + 1 ,'times.')
elif use_type == "2" or use_type == "Advanced":
    for i in range(use):
        num1 = float(input('Enter number 1: '))
        op_list = ["Enter operator: ", "^2", "^n", "| |", "//", "sin", "cos", "tan", "cot", "√  or  sqrt", "prm  or  number prime"]
        print('\n'.join(op_list))
        op_list = input('Choose: ')
        if op_list == '||':
           res = math.fabs(num1)
           print('ghadre motlaghe =', res)
        elif op_list == '√' or op_list == 'sqrt':
            res = math.sqrt(num1)
            print('sqrt =', res)
        elif op_list == '//':
            num2 = float(input('Enter number 2: '))
            if num2 == 0:
                print('Error')
                continue
            else:
                res = num1 // num2
                print(num1, '//', num2, "=", res)
        elif  op_list == '^2':
            res = math.pow(num1, 2)
            print(num1, "^2 = ", res)
        elif  op_list == '^':
            num2 = float(input('Enter number 2 : '))
            res = math.pow(num1, num2)
            print(num1, '^', num2, " = ", res)
        elif op_list == 'prm' or op_list == 'number prime':
            num1 = int(num1)
            if num1 > 1:
                for i in range(2, num1 // 2):
                    if (num1 % i) == 0:
                        print(num1, "Number is not prime")
                        break
                else:
                    print(num1, "Number is prime")
            else:
                print(num1, "number is not prime and is not not prime")
        elif op_list == 'sin':
            res = math.sin(num1)
            print('Answer = ', res)
        elif op_list == 'cos':
            res = math.cos(num1)
            print('Answer = ', res)
        elif op_list == 'tan':
            res = math.tan(num1)
            print('Answer = ', res)
        elif op_list == 'cot':
            res = math.atan(num1)
            print('Answer = ', res)
        else:
            print('\noperator is wrong')
        continue
    print('You used the calculator', i + 1 ,'times.')
else:
    print('Unexplored operator')