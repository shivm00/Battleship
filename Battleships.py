from random import *

board = []

for x in range(5):
    board.append(["0"] * 5)

def print_board(a):
    # x is a string content
    for x in a:
        print (" ".join(x))

def random_row(a):
    return randint(0,len(a)-1)

def random_col(a):
    return randint(0,len(a)-1)

ship_row = random_row(board)
ship_col = random_col(board)
turn=1

for turn in range(5):
    print_board(board)
    print("Turn:", turn + 1)
    guess_row = int(input("Guess Row: "))-1
    guess_col = int(input("Guess Col: "))-1
    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations you sunk the Battleship!")
        board[guess_row][guess_col] = "W"
        print_board(board)
        break
    elif guess_row>5 or guess_col>5:
        print("INVALID INPUT. PLEASE TRY AGAIN")
    elif guess_row == ship_row and guess_col!=ship_col:
        print("The row is correct but not the column")
        board[guess_row][guess_col] = "X"
    elif guess_col == ship_col and guess_row!=ship_row:
        print("The column is correct but not the row")
        board[guess_row][guess_col] = "X"
    else:
        print("")
        print("You missed the battleship")
        board[guess_row][guess_col] = "X"
    print("Turn:", turn+1)
    if turn==7:
        print("GAME OVER")
    print("")

