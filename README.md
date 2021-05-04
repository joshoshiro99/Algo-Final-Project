# Algo-Final-Project
Implementation of MiniMax AI in TicTacToe
By Alex Kennedy and Josh Oshiro

*pictures not shown*

# Explaining the Algorithm:
This project was implementing the minimax algorithm in python for use with tic-tac-toe. The minimax algorithm is a theory used by artificial intelligence. A scenario is created where artificial intelligence wants to minimize possible loss while maximizing possible gains. Minimax uses a recursive algorithm to determine the most optimal move for a given scenario. Minimax starts with a terminal node. Going up the tree, the next layer is run through a maximizer. This results in the highest numbers for these specific nodes. The next set of values is run through a minimizer. This results in the lowest value being selected for this set of nodes. The program generally runs once again through a maximizer. The end result will show a path that has the most efficient path, taking into factors both gains and losses. Minimax algorithms are commonly used in games such as chess, checkers or any other game that factors must be weighed between gains and losses.

# Implementation and Code:
In our specific example, the code for the minimax algorithm is stated below. The minimax takes in the current game state, the depth of the tree and the move from the player. The algorithm first starts off by seeing if the game is over, by evaluating the end state. The algorithm then checks all available board positions. The current score of the player is compared to the best possible lowest value score and the best possible highest value score.  

# Testing Strategy and Results:
For testing purposes, the algorithm was set to run against itself. This was so we could acquire our data without the need to constantly participate with the AI. We simulated 2000 games and the data can be found in the screenshots below.  The code starts by building the standard Tic Tac Toe board, like the main code. The time that it took for the AI to select their path was recorded into data and shown in the three tables below. As expected, as the algorithm started to traverse up the tree, the runtime got significantly shorter. 

The first runtime averaged between .16s and 20s, with a majority of games sitting around .18s. 

Second round was between .02s and .03s. For this, .027s was about the most consistent.

Turn Three goes between .003 and .009s, with the most consistent time being around .008s. At turn 7-9, the program started to run into microseconds, around 10-5 s. 
The below image details the specific code used to output the timing of each turn onto a Minimax file. 

# Complexity Theory in Practice:
Minimax algorithm follows the same path as Depth - First - Search algorithm and both are recursive algorithms. Both algorithms traverse through the game state space searching for the first terminal node. Once minimax has passed all terminal node values up to the root it will have traversed through the entire state space. Traveling through the entire tree will be based on the maximum depth m and branching factor b of the tree. The time complexity of this will therefore be O ( bm ). 


# Worked Example of Minimax: 
The below example details the strategy from an initial position starting from the MAX player. In the first turn we can see the minimax algorithm generate a bunch of possible moves. The MAX player will seek the move with the highest score, that move will be the one with a win state for the MAX player. As the algorithm continues to deepen into another call, the MIN player will search for the win state for the MIN player. This process will continue to alternate each player  until all nodes possible from the initial state have been generated. 
