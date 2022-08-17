name = 'mersana'
astro = '123456'
count = 0

for i in range (3):
    user = input('Enter your user: ')
    password = input('Enter your password: ')
    if (user == name) and (password == astro):
        print('welcome!')
        break
    elif (user != name) or (password != astro):
        if (count == 2):
            print('Your account has been locked :(')
            break
        print('Your user or password is incorrect. Please try again!')

    count = count + 1