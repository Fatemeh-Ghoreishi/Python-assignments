import time
import random
import colorama
from colorama import Fore, Back
colorama.init(autoreset=True)
start = time.time()
def final():
    introdu()
    board = create_board()
    printStyle(board)
    symbol_1, symbol_2 = symbol()
    isFull(board, symbol_1, symbol_2)
def introdu():
    print(Back.MAGENTA + "Hello! Welcome to Tic Tac Toe game!")
def create_board():
    print("\nStart the game :)")
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]        
    return board
def symbol():
    symbol_1 = input("Player 1, do you want to be X or O? ")
    symbol_1 = symbol_1.upper()
    symbol_1 = (Fore.RED + symbol_1)
    if symbol_1 == (Fore.RED + "X"):
        symbol_2 = (Fore.GREEN + "O")
        print("Player 2, you are O.")
    else:
        symbol_2 = (Fore.GREEN + "X")
        print("Player 2, you are X.")
    return (symbol_1, symbol_2)
def startgame(board, symbol_1, symbol_2, count):
    row11 = ['1', '2', '3']
    col12 = ['1', '2', '3']
    if count % 2 == 0:
        player = symbol_1
    elif count % 2 == 1:
        player = symbol_2
    print(Fore.BLACK + Back.CYAN + "Player "+ player + Fore.BLACK + Back.CYAN + ", it is your turn.")

    if playering == 1:
        if player == symbol_2:
            row = int(random.choice(row11)) - 1
            column = int(random.choice(col12)) - 1
        else:
            row = int(input("Pick a row[upper row:[enter 1, middle row: enter 2, bottom row: enter 3]: ")) - 1
            column = int(input("Pick a column:[left column: enter 1, middle column: enter 2, right column enter 3]: ")) - 1
    else:
        row = int(input("Pick a row:[upper row: enter 1, middle row: enter 2, bottom row: enter 3]: ")) - 1
        column = int(input("Pick a column:[left column: enter 1, middle column: enter 2, right column enter 3]: ")) - 1
    while (row > 2 or row < 0) or (column > 2 or column < 0):
        outOfRange()
        if playering == 1:
            if player == symbol_2:
                row = int(random.choice(row11)) - 1
                column = int(random.choice(col12)) - 1
            else:
                row = int(input("Pick a row[upper row:[enter 1, middle row: enter 2, bottom row: enter 3]: ")) - 1
                column = int(input("Pick a column:[left column: enter 1, middle column: enter 2, right column enter 3]: ")) - 1
        else:
            row = int(input("Pick a row:[upper row: enter 1, middle row: enter 2, bottom row: enter 3]: ")) - 1
            column = int(input("Pick a column:[left column: enter 1, middle column: enter 2, right column enter 3]: ")) - 1
    while (board[row][column] == symbol_1) or (board[row][column] == symbol_2):
        if playering == 1:
            if player == symbol_2:
                row = int(random.choice(row11)) - 1
                column = int(random.choice(col12)) - 1
            else:
                wrong()
                row = int(input("Pick a row[upper row:[enter 1, middle row: enter 2, bottom row: enter 3]: ")) - 1
                column = int(input("Pick a column:[left column: enter 1, middle column: enter 2, right column enter 3]: ")) - 1
        else:
            wrong()
            row = int(input("Pick a row:[upper row: enter 1, middle row: enter 2, bottom row: enter 3]: ")) - 1
            column = int(input("Pick a column:[left column: enter 1, middle column: enter 2, right column enter 3]: ")) - 1
    if player == symbol_1:
        board[row][column] = symbol_1
    else:
        board[row][column] = symbol_2
    return (board)
def isFull(board, symbol_1, symbol_2):
    count = 1
    winner = True
    while count < 10 and winner == True:
        startgame(board, symbol_1, symbol_2, count)
        printStyle(board)
        winner = isWinner(board, symbol_1, symbol_2)
        if count == 9:
            print("The board is full. Game over.")
            if winner == True:
                print(Fore.YELLOW + "Result : Nobody won.")
        count += 1
    report(count, winner, symbol_1, symbol_2)
def outOfRange():
    print("This house is out of range, please choose another one.")
def printStyle(board):
    rows = len(board)
    print("---*---*---")
    for r in range(rows):
        print(board[r][0], " |", board[r][1], "|", board[r][2])
        print("---*---*---")
    return board
def isWinner(board, symbol_1, symbol_2):
    winner = True
    for row in range (0, 3):
        if (board[row][0] == board[row][1] == board[row][2] == symbol_1):
            winner = False
            print("Player " + symbol_1 + Fore.RESET + ", you won!")
        elif (board[row][0] == board[row][1] == board[row][2] == symbol_2):
            winner = False
            print("Player " + symbol_2 + Fore.RESET + ", you won!")
    for col in range (0, 3):
        if (board[0][col] == board[1][col] == board[2][col] == symbol_1):
            winner = False
            print("Player " + symbol_1 + Fore.RESET + ", you won!")
        elif (board[0][col] == board[1][col] == board[2][col] == symbol_2):
            winner = False
            print("Player " + symbol_2 + Fore.RESET + ", you won!")
    if board[0][0] == board[1][1] == board[2][2] == symbol_1:
        winner = False 
        print("Player " + symbol_1 + Fore.RESET + ", you won!")
    elif board[0][0] == board[1][1] == board[2][2] == symbol_2:
        winner = False
        print("Player " + symbol_2 + Fore.RESET + ", you won!")
    elif board[0][2] == board[1][1] == board[2][0] == symbol_1:
        winner = False
        print("Player " + symbol_1 + Fore.RESET + ", you won!")
    elif board[0][2] == board[1][1] == board[2][0] == symbol_2:
        winner = False
        print("Player " + symbol_2 + Fore.RESET + ", you won!")
    return winner
def wrong():
    print("This house is full, please choose another one.")
def report(count, winner, symbol_1, symbol_2):
    if (winner == False) and (count % 2 == 1 ):
        print("Winner : Player " + symbol_1 + ".")
    elif (winner == False) and (count % 2 == 0 ):
        print("Winner : Player " + symbol_2 + ".")
while True:
    playering = int(input('Choose on of them:\n1.Single player\n2.Two player\n'))
    if playering == 1 or playering == 2:
        break
    else:
        continue
final()
result = time.time() - start
print(Fore.MAGENTA + Back.BLACK + f'Run time: {result:.2f} second')