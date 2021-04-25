#!/usr/bin/env python3

# Todo:
#  -see "TESTING TO FILE OUTPUT"
#

# testing file for Minimax:
#   - this file will create an environment that will enable the AI 
#   to play against itself
#   - the AI will record the performance of Minimax adding
#   it to a file with the following fomat:
#   Game 0:\tFirst\tSecond\tThird\tFourth\tFifth\tSixth\tSeventh\tEighth\tNinth
import MiniMaxTicTacToe

#----------AI ALGORITHM----------#
def comp_turn(a_choice, p_choice, current):
    # retrieve current board
    board = MiniMaxTicTacToe.board
    
    # check depth of game tree
    depth = len(MiniMaxTicTacToe.empty_cells(board))
    if depth == 0 or MiniMaxTicTacToe.game_ends(board):
        return

    # render
    MiniMaxTicTacToe.clean()
    print(f'Computer turn [{a_choice}]')
    MiniMaxTicTacToe.render(board, a_choice, p_choice)

    if depth == 9:
        # random start
        x = MiniMaxTicTacToe.choice([0, 1, 2])
        y = MiniMaxTicTacToe.choice([0, 1, 2])
    else: 
        # subsequent turns will be determined with minimax
        # record initial time
        time_minimax = 0
        minimax_start = MiniMaxTicTacToe.time.time()

        # get the Minimax recommended move to make
        move = MiniMaxTicTacToe.minimax(board, depth, current)

        # output minimax performance
        print('Minimax time:')
        print(MiniMaxTicTacToe.time.time() - minimax_start)
        
        # save the move coordinates
        x, y = move[0], move[1]

    # apply the move to the board
    MiniMaxTicTacToe.make_move(x, y, current)

    print()
    MiniMaxTicTacToe.time.sleep(1)

#------------MAIN------------------#
def main():
    p1_choice = 'X'
    p2_choice = 'O'

    # debug flag
    debug = True
    board = MiniMaxTicTacToe.board
    if debug:
        #-------DEBUG GAMELOOP--------#
        while(not MiniMaxTicTacToe.game_ends(board)):
            # render the board
            MiniMaxTicTacToe.clean()
            MiniMaxTicTacToe.render(board, p1_choice, p2_choice)

            # player 1 (maximizer)
            comp_turn(p1_choice, p2_choice, +1)

            # render results of player 1
            MiniMaxTicTacToe.render(board, p1_choice, p2_choice)

            # player 2 (minimizer)
            comp_turn(p1_choice, p2_choice, -1)

            # render results of player 2
            MiniMaxTicTacToe.render(board, p1_choice, p2_choice)
        else:
            #-----------TESTING TO FILE OUTPUT-------#
            # Todo:
            #  -read in previous game number
            #  -take in requested number of games
            #  -game management system
            #       -start a game
            #       -record each turns input
            #       -aggregate data into file append
            #       -restart game
            #  

            # for reference, here is the table format:
            # Game 0:\tFirst\tSecond\tThird\tFourth\tFifth\tSixth\tSeventh\tEighth\tNinth

            # record each turn's performance, add to performance array
            # output performance in above format
            # maximizer
            comp_turn(board, p1_choice, p2_choice)
            # minimizer
            comp_turn(board, p2_choice, p1_choice)

if __name__ == "__main__":
    main()