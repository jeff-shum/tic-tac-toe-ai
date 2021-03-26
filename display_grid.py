
def display_grid():
    '''
    Prints the grid state that is passed to it.
    '''
    initial_grid = [
            [ "   ", "   ", "   "],
            [ "   ", "   ", "   "],
            [ "   ", "   ", "   "]
            ]
    first = True
    for row in initial_grid:
        if first:
            first = False
        else:
            print("-"*15)
        print(row[0]  + ' | ', end="")
        print(row[1]  + ' | ', end="")
        print(row[2])

if __name__ == "__main__":
    display_grid()
