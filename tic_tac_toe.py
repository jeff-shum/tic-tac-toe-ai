#tic_tac_toe.py

print("Welcome to tic tac toe!")

def generate_board():
    board = [
            [ 0, 0, 0],
            [ 0, 0, 0],
            [ 0, 0, 0]
            ]
    return board

def display_grid(board_state):
    for row in board_state:
        for item in row:
            print(item, end='')

def elicit_player_choice:
    choice = input("Enter the number corresponding to the square you'd like to choose as your first move.")
    
