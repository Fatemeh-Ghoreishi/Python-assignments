import random
import pyfiglet
from colorama import Fore,Back,Style
text = pyfiglet.figlet_format(text = 'Welcome to the game', font = 'digital')
print(Fore.LIGHTYELLOW_EX+Back.LIGHTBLUE_EX+text+Style.RESET_ALL)
list_letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r',
                's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
names = ['sara', 'ali', 'mersana', 'parsa', 'amirshahan', 'liyana']
animals = ['elephant', 'butterfly', 'dolphin', 'tiger', 'swan', 'cat']
colors = ['pink', 'orange', 'red', 'cyan', 'azure', 'green']
fruits = ['banana', 'peach', 'mango', 'apple', 'cherry', 'avocado']
foods = ['pasta', 'bacon', 'sandwich', 'pizza', 'soup', 'shrimp']
countries = ['iran', 'malaysia', 'singapore', 'netherlands', 'austria', 'toronto']
things = ['table', 'carpet', 'ball', 'bed', 'broom', 'scissor']
while True:
    type = int(input('Choose: 1.Hard 2.Easy\n'))
    if type == 1:
        while True:
            selection = int(input('Choose your item\n1.names\n2.animals\n3.colors\n4.fruits\n5.foods\n6.countries\n7.things\n'))
            if selection == 1:
                final_answer = random.choice(names)
                break
            elif selection == 2:
                final_answer = random.choice(animals)
                break
            elif selection == 3:
                final_answer = random.choice(colors)
                break
            elif selection == 4:
                final_answer = random.choice(fruits)
                break
            elif selection == 5:
                final_answer = random.choice(foods)
                break
            elif selection == 6:
                final_answer = random.choice(countries)
                break
            elif selection == 7:
                final_answer = random.choice(things)
                break
            else:
                print('Please enter one number between 1 to 7 !!\n')
                continue
        show_list , wrong_list = [] , []
        for i in range (len(final_answer)):
            show_list.append('_')
        print(' '.join(show_list))
        while True:
            while True:
                print(list_letter)
                letter_user = input('Enter one letter: ')
                if ('a' <= letter_user <= 'z') or ('A' <= letter_user <= 'Z'):
                    break
                else:
                    print('Please just enter one letter!')
                    continue
            letter_user = letter_user.lower()
            if letter_user == final_answer:
                print('Hoora, you won :)')
                break
            if len(letter_user) >= 2:
                letter_user = letter_user[0]
            if letter_user in wrong_list or letter_user in show_list:
                print('This is a duplicate letter, please try again.')
                continue
            if letter_user in list_letter:
                list_letter.remove(letter_user)
            count = len(final_answer)
            if final_answer.find(letter_user) == -1:
                wrong_list.append(letter_user)
            else:
                for i in range (len(final_answer)):
                    if final_answer[i] == letter_user:
                        show_list[i] = letter_user
                    else:
                        continue
            print('wrong =',wrong_list)
            print(' '.join(show_list))
            if len(wrong_list) == len(final_answer) + 1:
                print('Game over :(')
                break
            for i in show_list:
                if i != '_':
                    count -= 1
            if count == 0:
                print('Hoora, you won :)')
                break
            print('\n')
        break
    elif type == 2:
        while True:
            selection = int(input('Choose your item\n1.names\n2.animals\n3.colors\n4.fruits\n5.foods\n6.countries\n7.things\n'))
            if selection == 1:
                print(names)
                final_answer = random.choice(names)
                break
            elif selection == 2:
                print(animals)
                final_answer = random.choice(animals)
                break
            elif selection == 3:
                print(colors)
                final_answer = random.choice(colors)
                break
            elif selection == 4:
                print(fruits)
                final_answer = random.choice(fruits)
                break
            elif selection == 5:
                print(foods)
                final_answer = random.choice(foods)
                break
            elif selection == 6:
                print(countries)
                final_answer = random.choice(countries)
                break
            elif selection == 7:
                print(things)
                final_answer = random.choice(things)
                break
            else:
                print('Please enter one number between 1 to 7 !!\n')
                continue
        show_list , wrong_list = [] , []
        for i in range (len(final_answer)):
            show_list.append('_')
        print(' '.join(show_list))
        while True:
            while True:
                print(list_letter)
                letter_user = input('Enter one letter: ')
                if ('a' <= letter_user <= 'z') or ('A' <= letter_user <= 'Z'):
                    break
                else:
                    print('Please just enter one letter!')
                    continue
            letter_user = letter_user.lower()
            if letter_user == final_answer:
                print('Hoora, you won :)')
                break
            if len(letter_user) >= 2:
                letter_user = letter_user[0]
            if letter_user in wrong_list or letter_user in show_list:
                print('This is a duplicate letter, please try again.')
                continue
            if letter_user in list_letter:
                list_letter.remove(letter_user)
            count = len(final_answer)
            if final_answer.find(letter_user) == -1:
                wrong_list.append(letter_user)
            else:
                for i in range (len(final_answer)):
                    if final_answer[i] == letter_user:
                        show_list[i] = letter_user
                    else:
                        continue
            print('wrong =',wrong_list)
            print(' '.join(show_list))
            if len(wrong_list) == len(final_answer) + 1:
                print('Game over :(')
                break
            for i in show_list:
                if i != '_':
                    count -= 1
            if count == 0:
                print('Hoora, you won :)')
                break
            print('\n')
        break
    else:
        print('Choose 1 or 2 !!')
        continue
