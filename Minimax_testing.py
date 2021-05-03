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

# reset the board
def reset():
    board = [
    [0,0,0],
    [0,0,0],
    [0,0,0],
    ]
    return board

#----------AI ALGORITHM----------#
def comp_turn(a_choice, p_choice, current):
    # retrieve current board
    board = MiniMaxTicTacToe.board
    performance = 0
    # check depth of game tree
    depth = len(MiniMaxTicTacToe.empty_cells(board))
    if depth == 0 or MiniMaxTicTacToe.game_ends(board):
        return

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

        # save minimax performance
        performance = MiniMaxTicTacToe.time.time() - minimax_start
        
        # save the move coordinates
        x, y = move[0], move[1]

    # apply the move to the board
    MiniMaxTicTacToe.make_move(x, y, current)
    return performance

#------------MAIN------------------#
def main():
    p1_choice = 'X'
    p2_choice = 'O'

    # debug flag
    debug = False
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
        # for reference, here is the table format:
        # Game 0:\tFirst\tSecond\tThird\tFourth\tFifth\tSixth\tSeventh\tEighth\tNinth
            
        #initial file operation
        file_minimax = open("Minimax_data.txt","a")

        #get beginning game number
        starting_game_number = int(input("Game number of first game: "))

        #get number of games to play
        games_to_play = int(input("How many games do you want the AI to simulate? "))

        # Set initial game number
        gamecounter = starting_game_number

        # store clear board state
        reset_board = MiniMaxTicTacToe.board 

        # GAMES loop
        while(gamecounter<starting_game_number+games_to_play):
            #get first half of output string
            gamestring_1  = "Game "+str(gamecounter)+": "

            #  get a clean board
            MiniMaxTicTacToe.board = reset()

            #init performance array
            performance_array = []
            separator = '\t'

            #  gameloop
            while(not MiniMaxTicTacToe.game_ends(board)):

                # record each turn's performance, add to performance array
                #   player 1 (maximizer)
                performance_array.append(str(comp_turn(p1_choice, p2_choice, +1)))

                #   player 2 (minimizer)
                performance_array.append(str(comp_turn(p1_choice, p2_choice, -1)))

            #get second half of output string
            gamestring_2 = separator.join(performance_array)

            #output full output string
            file_minimax.write(str(gamestring_1)+str(gamestring_2)+'\n')

            print("Game "+str(gamecounter)+" simulated!")
            #inc game counter
            gamecounter += 1
        print("Done!")
        print("All games simulated!!")


        


        #close file
        file_minimax.close()

if __name__ == "__main__":
    main()