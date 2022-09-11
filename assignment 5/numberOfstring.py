st = input('Enter your text: ')
let = 0
word = 0
for letter in st:
    if 'a' <= letter <= 'z' or 'A' <= letter <= 'Z':
        let += 1
word = st.split()
word = '\n'.join(word)
word = word.split('\n')
word = '\t'.join(word)
word = word.split('\t')
word = len(word)
char = len(st)
space = st.count(' ')
enter = st.count('\n')
point = st.count('.')
comma = st.count(',')
print(f'number of letter: {let}\nnumber of word: {word}\nnumber of character: {char}')
print(f'number of space and enter: {space + enter}\nnumber of point and comma: {comma + point}')