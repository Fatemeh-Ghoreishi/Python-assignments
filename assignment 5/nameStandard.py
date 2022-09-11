list = []
for i in range(1, 11):
    name = input(f'Enter your name {i}:')
    new_name = name.capitalize()
    list.append(new_name)
print(list)