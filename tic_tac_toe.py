#tic_tac_toe.py

print("Welcome to tic tac toe!")

initial_grid = [
    [ "   ", "   ", "   "],
    [ "   ", "   ", "   "],
    [ "   ", "   ", "   "]
    ]

def display_grid(grid_state):
    '''
    Prints the grid state that is passed to it.
    '''
    first = True
    for row in grid_state:
        if first:
            first = False
        else:
            print("-"*11)
        print(row[0]  + '|', end="")
        print(row[1]  + '|', end="")
        print(row[2])
    print("Next player's turn...")

def elicit_player_choice():
    '''
    Elicits player for which numerical spot they would like to choose as their next move. Returns an integer.
    '''
    #TODO: find a way to account for which player's turn it currently is
#    while True:
#        choice = input("Enter the number corresponding to the square you'd like to choose as your first move.")
#        #TODO: display the current board state
#        try:
#            choice = int(choice)
#            break
#        except ValueError:
#            print("Invalid response. Enter a number from 1 to 9. Careful not to choose a spot that's already occupied!")
#            continue
#    return choice
        
def update_grid_state(previous_grid_state, player_choice):
    #TODO: make indexes to access the different spaces in the grid
#    previous_grid_state[#index1][#index2] = player_choice
#    return previous_grid_state
    return


def check_win_condition(grid_state):
    '''
    Checks whether the grid state passed to it has fulfilled the win condition for either player.
    '''
        #TODO: statements to check for win condition
        #TODO: display appropriate message if any player has won and restart new game

if __name__ == "__main__":
    display_grid(initial_grid)
    grid_state = initial_grid
    player_choice = elicit_player_choice()
#    while True:
#        grid_state = update_grid_state(grid_state, player_choice)
#        display_grid(grid_state)
#        if check_win_condition(grid_state) == True:
#            if turn_counter % 2 == 0:
#                print("Congratulations player 'X', you've won!")
#                break
#            else:
#                print("Congratulations player 'O', you've won!")
#                break
#        else:
#            turn_counter += 1
#            continue
