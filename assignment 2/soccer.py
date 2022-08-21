win = equal = loss = total_score = counter = 0
while counter < 8:
    vorodi = int(input('Enter the score (win = 3),(equal = 1),(loss = 0): '))
    if ( vorodi != 0 and vorodi != 1 and vorodi != 3):
        print('Your score must be (0 for loss) or (1 for equal) or (3 for win), Please try again. ')
        continue
    if (vorodi == 3):
        win = int(win + 1)
        total_score += vorodi
    elif (vorodi == 1):
        equal = (equal + 1)
        total_score += vorodi
    elif (vorodi == 0):
        loss = int(loss + 1)
    counter += 1

print("win: ",win)
print( "equal: ",equal)
print("loss: ",loss)
print("total_score: ",total_score)
