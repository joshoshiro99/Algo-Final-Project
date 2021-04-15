#!/usr/bin/env python3
# -----imports-----
import time
import platform
from os import system
from random import choice
from math import inf as infinity

# -----notes-----
# the terminal output window is 13x7
# 
# right now the ai does not select the winning move
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

    #default the moves value and provide a dict of numpad -> coords
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

# -----AI functions-----

# computer turn code
# *look inside for further info*
def comp_turn(a_choice, p_choice):
    #check depth of game tree
    depth = len(empty_cells(board))
    if depth == 0 or game_ends(board):
        return

    clean()
    print(f'Computer turn [{a_choice}]')
    render(board, a_choice, p_choice)

    # random start
    if depth == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
    else: # subsequent turns will be determined with minimax
        move = minimax(board, depth, AI)
        x, y = move[0], move[1]

    make_move(x, y, AI)
    time.sleep(1)

# returns scoring for the current board
# returns +1, -1, 0 
def evaluate(state):
    if wins(state, AI):
        score = +1
    elif wins(state, HUMAN):
        score = -1
    else:
        score = 0
    return score

# minimax code 
# minimax is a decision rule for:
#   minimizing the loss for a maximum loss scenario
#                       or
#   maximizing the gain for a minimum gain scenario
def minimax(state, depth, player):
    if player == AI:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    if depth == 0 or game_ends(state):
        score = evaluate(state)
        return [-1, -1, score]

    for cell in empty_cells(state):
        # get coords for next available space
        x, y = cell[0], cell[1]
        # insert player to the grid
        state[x][y] = player
        # get the state to play, next turn, and alternate min/max player
        score = minimax(state, depth -1 , -player)

        #reset board position
        state[x][y] = 0
        #save result of minimax
        score[0], score[1] = x, y

        if player == AI:
            if score[2] > best[2]:
                best = score # highest value
        else:
                if score[2] < best[2]:
                    best = score # min value

        return best

# -----driver code-----
def main():
    a_choice = 'X'
    p_choice = 'O'
    #gameloop
    while(not game_ends(board)):
        #game loop outline:
        # 1)render the current board
        clean()
        render(board, a_choice, p_choice)

        # 2)get player input
        player_turn(a_choice,p_choice)

        # 3)get AI input
        comp_turn(a_choice,p_choice)

        # 4)repeat until win/draw/lose
        
    # render final board
    render(board,a_choice,p_choice)


if __name__ == "__main__":
    main()