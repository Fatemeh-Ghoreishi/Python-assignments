def number_of_word (st):
    elements = ["0" , "1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" ,
                "." , "," , "/" , "\\" , "[" , "]" , "{" , "}" , "!" , "#" ,
                "&" , "(" , ")" , "*" , "^" , "<" , ":" , ";" , "\'" , "\"" ,
                ">" , "|" , "$" , "%" ,"~" , "`" , "@" , "?"]
    for i in elements:
        st = st.replace(i, " ")
    words = st.split()
    return(len(words))
st = input('Enter your text: ')
print('Number of words:' ,number_of_word(st) )