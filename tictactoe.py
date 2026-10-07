print("Welcome to Tic Tac Toe.")
instruction = input("Do you know how to play? (enter 'yes' or 'no'.): ")

if instruction == 'yes':
    print("Okay then. Let's begin.")
elif instruction == 'no':
    print("The game is played on 3x3 grid.")
    print("Player 1 is X, and Player 2 is O.")
    print("Players take turns putting their marks in empty squares.")
    print("The first to get 3 of their marks in a row (horizontally, vertically, or diagonally) is the winner.")
    print("When all 9 squares are full, the game is over.")
    print("If no player has 3 marks in a row, the game ends in a tie.")
    print("Now let's begin.")

print("Keep in mind that the columns are numbered from left to right, and the rows are numbered from top to bottom.")

row_1=[' ',' ',' ']
row_2=[' ',' ',' ']
row_3=[' ',' ',' ']

def print_board():
    print(row_1)
    print(row_2)
    print(row_3)

def check_board():
    if row_1[0] == row_2[0] == row_3[0] and row_1[0] != ' ':
        return True
    if row_1[1] == row_2[1] == row_3[1] and row_1[1] != ' ':
        return True
    if row_1[2] == row_2[2] == row_3[2] and row_1[2] != ' ':
        return True
    if row_1[0] == row_1[1] == row_1[2] and row_1[0] != ' ':
        return True
    if row_2[0] == row_2[1] == row_2[2] and row_2[0] != ' ':
        return True
    if row_3[0] == row_3[1] == row_3[2] and row_3[0] != ' ':
        return True
    if row_1[0] == row_2[1] == row_3[2] and row_1[0] != ' ':
        return True
    if row_3[0] == row_2[1] == row_1[2] and row_3[0] != ' ':
        return True
    
def input_stuff(play):
    while True:
        print_board()
        try:
            column_num = int(input("Player " + play + ": column number? (1-3): ")) - 1
        except ValueError:
            print("Input a number, please.")
            continue
        try:
            row_num = int(input("Row number? (1-3): ")) - 1
        except ValueError:
            print("Input a number, please.")
            continue
        if column_num <= 2 and column_num >= 0:
            if row_num == 0:
                if row_1[column_num] == ' ':
                    row_1[column_num] = play
                    break
            if row_num == 1:
                if row_2[column_num] == ' ':
                    row_2[column_num] = play
                    break
            if row_num == 2:
                if row_3[column_num] == ' ':
                    row_3[column_num] = play
                    break
        
def check_cat():
    if not(row_1[0] == ' ' or row_1[1] == ' ' or row_1[2] == ' ' or row_2[0] == ' ' or row_2[1] == ' ' or row_2[2] == ' ' or row_3[0] == ' ' or row_3[1] == ' ' or row_3[2] == ' '):
        return True

while True:
    player = 'X'
    input_stuff(player)
    if check_board():
        print_board()
        print("Congratulations Player " + player + ", you've won!")
        break
    if check_cat():
        print_board()
        print("You got a cat. It's a tie.")
        break
    player = '--'
    input_stuff(player)
    if check_board():
        print_board()
        print("Congratulations Player " + player + ", you've won!")
        break
    if check_cat():
        print_board()
        print("You got a cat. It's a tie.")
        break
print("To play again, rerun code.")