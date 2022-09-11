word = input('Enter your word: ')

for i in range(len(word)):
    if word[i] == 'a' or word[i] == 'A':
        word = word.replace('a', '?').replace('A', '?')
    elif word[i] == 'e' or word[i] == 'E':
        word = word.replace('e', '?').replace('E', '?')
    elif word[i] == 'o' or word[i] == 'O':
        word = word.replace('o', '?').replace('O', '?')
    elif word[i] == 'u' or word[i] == 'U':
        word = word.replace('u', '?').replace('U', '?')
    elif word[i] == 'i' or word[i] == 'I':
        word = word.replace('i', '?').replace('I', '?')
print(word)