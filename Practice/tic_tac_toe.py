from operator import truediv


board = [" " for _ in range(9)]

def display_board():
    print()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

# display_board()

def check_winner(player):
    win_condition = [[0,1,2] , [3,4,5] , [6,7,8] , [0,3,6] , [1,4,7] ,
                      [2,5,8] , [0,4,8] , [2,4,6]]
    
    for match in win_condition:
        if all(board[i] == player for i in match):
            return True
    return False

def check_draw():
    return " " not in board


current_player = 'X'

while True:
    display_board()

    move = input(f"player{current_player}, choose a position from 1 to 9:-")

    if not move.isdigit() or int(move) not in range (1, 10):
        print("enter a valid input")
        continue
    #changed to index
    move = int(move) -1 

    if board[move] != " ":
        print("spot already taken")
        continue
    board[move] = current_player

    if check_winner(current_player):
        display_board()
        print(f"player {current_player} wins!")
        break
    if check_draw():
        display_board()
        print("its a draw")
        break

    current_player = "O" if current_player == "X" else "X"