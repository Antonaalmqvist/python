import random

game_board = ["-", "-", "-",
              "-", "-", "-",
              "-", "-", "-",]
current_player = "X"
winner = None
game_active = True

def print_board(game_board):
    print(game_board[0] + " | " + game_board[1] + " | " + game_board[2])
    print("---------")
    print(game_board[3] + " | " + game_board[4] + " | " + game_board[5])
    print("---------")
    print(game_board[6] + " | " + game_board[7] + " | " + game_board[8])

def player_move(game_board):
    while True:
        inp = int(input("Please enter a number 1-9: "))
        if inp >= 1 and inp <= 9:
            if game_board[inp-1] == "-":
                game_board[inp-1] = current_player
                break  
            else:
                print("Ooops, that spot is already occupied! Try again.")
        else:
            print("Invalid input! Please enter a number between 1 and 9.")

def check_row(game_board):
    global winner
    if game_board[0] == game_board[1] == game_board[2] and game_board[1] != "-":
        winner = game_board[0]
        return True
    elif game_board[3] == game_board[4] == game_board[5] and game_board[3] != "-":
        winner = game_board[3]
        return True
    elif game_board[6] == game_board[7] == game_board[8] and game_board[6] != "-":
        winner = game_board[6]
        return True

def check_column(game_board):
    global winner
    if game_board[0] == game_board[3] == game_board[6] and game_board[0] != "-":
        winner = game_board[0]
        return True
    elif game_board[1] == game_board[4] == game_board[7] and game_board[1] != "-":
        winner = game_board[1]
        return True
    elif game_board[2] == game_board[5] == game_board[8] and game_board[2] != "-":
        winner = game_board[2]
        return True

def check_diagonal(game_board):
    global winner
    if game_board[0] == game_board[4] == game_board[8] and game_board[0] != "-":
        winner = game_board[0]
        return True
    if game_board[2] == game_board[4] == game_board[6] and game_board[2] != "-":
        winner = game_board[2]
        return True

def check_tie(game_board):
    global game_active
    if "-" not in game_board:
        print_board(game_board)
        print("It is a tie!")
        game_active = False

def check_win():
    global game_active
    if check_diagonal(game_board) or check_column(game_board) or check_row(game_board):
        print_board(game_board)
        print(f"The winner is {winner}")
        game_active = False
        exit()

def toggle_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

def computer(game_board):
    while current_player == "O":
        position = random.randint(0, 8)
        if game_board[position] == "-":
            game_board[position] = "O"
            toggle_player()


while game_active:
    print_board(game_board)
    player_move(game_board)
    check_win()
    check_tie(game_board)
    toggle_player()
    computer(game_board)
    check_win()
    check_tie(game_board)
