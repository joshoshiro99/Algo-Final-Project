#!/usr/bin/env python3
import MiniMaxTicTacToe

# testing file for Minimax:
#   - this file will create an environment that will enable the AI 
#   to play against itself
#   - the AI will record the performance of Minimax adding
#   it to a file with the following fomat:
#
#          | First call |   Second   | . . . | Final Call |
#   -------|------------|------------|-------|------------|
#   Game 1 | 0.12345678 | 0.12345678 | . . . | 0.12345678 |
#   -------|------------|------------|-------|------------|
#   Game 2 | 0.12345678 | 0.12345678 | . . . | 0.12345678 |
#   -------|------------|------------|-------|------------| 
#     .    |            |            |       |            |
#     .    |            |            |       |            |
#     .    |            |            |       |            |
#   -------|------------|------------|-------|------------| 
#   Game N | 0.12345678 | 0.12345678 | . . . | 0.12345678 |
#   -------|------------|------------|-------|------------| 

def comp_turn(a_choice, p_choice, current):
    #check depth of game tree
    board = MiniMaxTicTacToe.board
    depth = len(MiniMaxTicTacToe.empty_cells(board))
    if depth == 0 or MiniMaxTicTacToe.game_ends(board):
        return


    MiniMaxTicTacToe.clean()
    print(f'Computer turn [{a_choice}]')
    MiniMaxTicTacToe.render(board, a_choice, p_choice)

    # random start
    
    if depth == 9:
        x = MiniMaxTicTacToe.choice([0, 1, 2])
        y = MiniMaxTicTacToe.choice([0, 1, 2])
    else: # subsequent turns will be determined with minimax
        time_minimax = 0
        minimax_start = MiniMaxTicTacToe.time.time()

        move = MiniMaxTicTacToe.minimax(board, depth, current)
        x, y = move[0], move[1]

        print('Minimax time:')
        print(MiniMaxTicTacToe.time.time() - minimax_start)

    MiniMaxTicTacToe.make_move(x, y, current)

    print()
    MiniMaxTicTacToe.time.sleep(1)

def main():
    p1_choice = 'X'
    p2_choice = 'O'

    debug = True

    #gameloop
    board = MiniMaxTicTacToe.board
    while(not MiniMaxTicTacToe.game_ends(board)):
         #output to ensure ai can play itself
        if debug:
            
            MiniMaxTicTacToe.clean()
            MiniMaxTicTacToe.render(board, p1_choice, p2_choice)

            comp_turn(p1_choice, p2_choice, +1)

            MiniMaxTicTacToe.render(board, p1_choice, p2_choice)

            comp_turn(p1_choice, p2_choice, -1)

            MiniMaxTicTacToe.render(board, p1_choice, p2_choice)
        else:
            comp_turn(board, p1_choice, p2_choice)
            comp_turn(board, p2_choice, p1_choice)

if __name__ == "__main__":
    main()