#!/usr/bin/env python3
# -----imports-----
import platform
from os import system

# -----notes-----
# the terminal output window is 13x7
# 
#
#

# -----global variables-----
HUMAN = -1 
AI = +1
board = [
    [0,0,0],
    [0,0,0],
    [0,0,0],
]

# -----TicTacToe Functions-----
# takes current board state and displays it
def render(state, a_choice, p_choice):
    chars = { #char dict
        -1: p_choice,
        +1: a_choice,
        0: ''
        }

    str_line = '------------'

    print('\n' + str_line)
    for row in state:
        for cell in row:
            symbol = chars[cell]
            print(f'| {symbol} |', end='')
        print('\n' + str_line)

# clears the screen
def clean(): 
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')

# creates a list of empty cells??
def empty_cells(state): 
    cells = []

    for x, row in enumerate(state):
        for y, cell in enumerate(row):
            if cell == 0:
                cells.append([x,y])
           
    return cells

# using our empty cell list, checks to see if x,y is in
def check_if_valid(x,y): 
    if [x, y] in empty_cells(board):
        return True
    else:
        return False

# checks validity and then applies to board
def make_move(x, y, human):
    if check_if_valid(x, y):
        board[x][y] = human
        return True
    else:
        return False

# takes in the current state + player variable and checks all win configurations for player value
# RETURN: BOOL
def wins(state, player):
    win_state = [
        [state[0][0], state[0][1], state[0][2]], #top straight
        [state[1][0], state[1][1], state[1][2]], #middle straight
        [state[2][0], state[2][1], state[2][2]], #bottom straight
        [state[0][0], state[1][0], state[2][0]], #left vertical
        [state[0][1], state[1][1], state[2][1]], #middle vertical
        [state[0][2], state[1][2], state[2][2]], #right vertical
        [state[0][0], state[1][1], state[2][2]], #l-r diagonal
        [state[2][0], state[1][1], state[0][2]], #r-l diagonal
    ]
    if [player, player, player] in win_state:
        return True
    else:
        return False

# ensures the game has not been won
# RETURN: BOOL
def game_ends(state):
    return wins(state,HUMAN) or wins(state, AI)

# player turn code 
# *look inside for further info*
#question does triggering not can_move will cause AI to take turn after
def player_turn(a_choice, p_choice):
    # determine depth of game tree from board state
    depth = len(empty_cells(board))
    if depth == 0 or game_ends(board):
        return

    #defaul the moves value and provide a dict of numpad -> coords
    move = -1
    moves = {
        1: [0, 0], 
        2: [0, 1], 
        3: [0, 2],
        4: [1, 0], 
        5: [1, 1], 
        6: [1, 2],
        7: [2, 0], 
        8: [2, 1], 
        9: [2, 2],
    }

    #Player input
    clean()
    print(f'Human turn [{p_choice}]')
    render(board, a_choice, p_choice)
    while move < 1 or move > 9:
        try: #error checking
            move = int(input('Use numpad (1..9): ')) #ask for input
            coord = moves[move]
            can_move = make_move(coord[0], coord[1], HUMAN)

            if not can_move: #check if valid move
                print('Bad move')
                move = -1
        #error output
        except (EOFError, KeyboardInterrupt): 
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')



# -----driver code-----
def main():
    a_choice = 'X'
    p_choice = 'O'
    #gameloop
    while(not game_ends(board)):
        #game loop outline:
        # 1)render the current board
        # 2)get player input
        # 3)get AI input
        # 4)repeat until win/draw/lose
        clean()
        render(board, a_choice, p_choice)
        player_turn(a_choice,p_choice)

        
        
    # render final board
    render(board,a_choice,p_choice)


if __name__ == "__main__":
    main()