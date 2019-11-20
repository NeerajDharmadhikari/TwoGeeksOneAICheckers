from random import randint
from BoardClasses import Move
from BoardClasses import Board
import copy
# The following part should be completed by students.
# Students can modify anything except the class name and existing functions and variables.
# python3 AI_Runner.py 7 7 2 l ../src/checkers-python/main.py Sample_AIs/Random_AI/main.py
# python3 AI_Runner.py 7 7 2 l Sample_AIs/Random_AI/main.py ../src/checkers-python/main.py

class StudentAI():

    def __init__(self, col, row, p):
        self.col = col
        self.row = row
        self.p = p
        self.board = Board(col, row, p)
        self.board.initialize_game()
        self.color = ''
        self.opponent = {1: 2, 2: 1}
        self.color = 2

    def get_heuristic_score(self, currentBoard):
        # Iterate through entire board to count B/W pieces
        our_score = 0
        opponent_score = 0

        our_color = ''
        num_our_pieces = 0
        opponent_color = ''
        num_opp_pieces = 0

        # 1 is color black
        if (self.color == 1):
            our_color = 'B'
            opponent_color = 'W'
        else:
            our_color = 'W'
            opponent_color = 'B'
        
        if our_color == 'B':
            for x in range(len(currentBoard.board)):
                for y in range(len(currentBoard.board[x])):
                    
                    # Check if it's our checker piece
                    if (currentBoard.board[x][y].get_color() == our_color):
                        num_our_pieces += 1
                        # Check if it's a king
                        if(currentBoard.board[x][y].is_king == True):
                            our_score += 2
                        else:
                            our_score += 1
                        # Check if it's a corner piece either (0, 0), (0, n), (n, 0), or (n, n)
                        cp = currentBoard.board[x][y].get_location()
                        
                        # Check if it's an edge piece row 0, row n, col 0, col n
                        if (cp[0] == 0 or cp[0] == currentBoard.row -1):
                            our_score += 1
                        if (cp[1] == 0 or cp[1] == currentBoard.col -1):
                            our_score += 1
                        
                        # If checker piece is not an edge piece
                        if (cp[0] != 0 and cp[0] != currentBoard.row -1):
                            if (cp[1] != 0 and cp[1] != currentBoard.col -1):
                                if(currentBoard.board[x + 1][y - 1].get_color() == opponent_color):
                                    if(currentBoard.board[x - 1][y + 1].get_color() == '.'):
                                        our_score -= 3
                                if(currentBoard.board[x + 1][y + 1].get_color() == opponent_color):
                                    if(currentBoard.board[x - 1][y - 1].get_color() == '.'):
                                        our_score -= 3
                                if(currentBoard.board[x - 1][y + 1].get_color() == opponent_color and currentBoard.board[x - 1][y + 1].is_king):
                                    if(currentBoard.board[x + 1][y-1].get_color() == '.'):
                                        our_score -= 3
                                if(currentBoard.board[x - 1][y - 1].get_color() == opponent_color and currentBoard.board[x - 1][y - 1].is_king):
                                    if(currentBoard.board[x + 1][y + 1].get_color() == '.'):
                                        our_score -= 3
                                # Check if checker piece is able to become king
                                if (cp[0] == currentBoard.row - 2):
                                    if(currentBoard.board[x + 1][y - 1].get_color() == '.' and currentBoard.board[x + 1][y + 1].get_color() == '.'):
                                        our_score += 5
                                    if(currentBoard.board[x + 1][y - 1].get_color() == opponent_color):
                                        if(currentBoard.board[x - 1][y + 1].get_color() != '.'):
                                            our_score += 5
                                        else:
                                            our_score -= 3
                                    if(currentBoard.board[x + 1][y + 1].get_color() == opponent_color):
                                        if(currentBoard.board[x - 1][y - 1].get_color() != '.'):
                                            our_score += 5
                                        else:
                                            our_score -= 3
                                    if(currentBoard.board[x + 1][y + 1].get_color() == '.'):
                                        our_score += 5
                                    if(currentBoard.board[x + 1][y - 1].get_color() == '.'):
                                        our_score += 5
                            else:
                                if(currentBoard.board[x][y].is_king == True):
                                    if(cp[1] == 0):
                                        if(cp[0] != 0 and cp[0] != currentBoard.row - 1):
                                            if(currentBoard.board[x + 1][y + 1].get_color() == opponent_color):
                                                our_score += 3
                                            if(currentBoard.board[x - 1][y + 1].get_color() == opponent_color):
                                                our_score += 3
                                    if(cp[1] == currentBoard.col - 1):
                                        if(cp[0] != 0 and cp[0] != currentBoard.row - 1):
                                            if(currentBoard.board[x + 1][y - 1].get_color() == opponent_color):
                                                our_score += 3
                                            if(currentBoard.board[x - 1][y - 1].get_color() == opponent_color):
                                                our_score += 3
                                    if(cp[0] == 0):
                                        if(cp[1] != 0 and cp[1] != currentBoard.col - 1):
                                            if(currentBoard.board[x + 1][y - 1].get_color() == opponent_color):
                                                our_score += 3
                                            if(currentBoard.board[x + 1][y + 1].get_color() == opponent_color):
                                                our_score += 3
                                    if(cp[0] == currentBoard.row - 1):
                                        if(cp[1] != 0 and cp[1] != currentBoard.col - 1):
                                            if(currentBoard.board[x - 1][y + 1].get_color() == opponent_color):
                                                our_score += 3
                                            if(currentBoard.board[x - 1][y - 1].get_color() == opponent_color):
                                                our_score += 3
                                else: # It's a pawn
                                    if(cp[1] == 0):
                                        if(cp[0] != 0 and cp[0] != currentBoard.row - 1):
                                            if(currentBoard.board[x + 1][y + 1].get_color() == opponent_color):
                                                our_score += 3
                                    if(cp[1] == currentBoard.col - 1):
                                        if(cp[0] != 0 and cp[0] != currentBoard.row - 1):
                                            if(currentBoard.board[x + 1][y - 1].get_color() == opponent_color):
                                                our_score += 3

                    elif (currentBoard.board[x][y].get_color() == '.'):
                        # ignore since this location doesn't have a checkerpiece
                        continue
                    else:
                        num_opp_pieces += 1
                        # Check if it's king
                        if(currentBoard.board[x][y].is_king == True):
                            opponent_score += 2
                        else:
                            opponent_score += 1
                        
                        cp = currentBoard.board[x][y].get_location()
                        # Check if it's an edge piece row 0, row n, col 0, col n
                        if (cp[0] == 0 or cp[0] == currentBoard.row -1):
                            opponent_score += 1
                        if (cp[1] == 0 or cp[1] == currentBoard.col -1):
                            opponent_score += 1
        else: # our_color == 'W'
            for x in range(len(currentBoard.board) -1, -1, -1):
                for y in range(len(currentBoard.board[x]) -1, -1, -1):
                    
                    # Check if it's our checker piece
                    if (currentBoard.board[x][y].get_color() == our_color):
                        num_our_pieces += 1
                        # Check if it's a king
                        if(currentBoard.board[x][y].is_king == True):
                            our_score += 2
                        else:
                            our_score += 1
                        # Check if it's a corner piece either (0, 0), (0, n), (n, 0), or (n, n)
                        cp = currentBoard.board[x][y].get_location()
                        
                        # Check if it's an edge piece row 0, row n, col 0, col n
                        if (cp[0] == 0 or cp[0] == currentBoard.row -1):
                            our_score += 1
                        if (cp[1] == 0 or cp[1] == currentBoard.col -1):
                            our_score += 1
                        
                        # If checker piece is not an edge piece
                        if (cp[0] != 0 and cp[0] != currentBoard.row -1):
                            if (cp[1] != 0 and cp[1] != currentBoard.col -1):
                                if(currentBoard.board[x - 1][y - 1].get_color() == opponent_color):
                                    if(currentBoard.board[x + 1][y + 1].get_color() == '.'):
                                        our_score -= 3
                                if(currentBoard.board[x - 1][y + 1].get_color() == opponent_color):
                                    if(currentBoard.board[x + 1][y - 1].get_color() == '.'):
                                        our_score -= 3
                                if(currentBoard.board[x + 1][y + 1].get_color() == opponent_color and currentBoard.board[x + 1][y + 1].is_king):
                                    if(currentBoard.board[x - 1][y - 1].get_color() == '.'):
                                        our_score -= 3
                                if(currentBoard.board[x + 1][y - 1].get_color() == opponent_color and currentBoard.board[x + 1][y - 1].is_king):
                                    if(currentBoard.board[x - 1][y + 1].get_color() == '.'):
                                        our_score -= 3
                                # Check if checker piece is able to become king
                                if (cp[0] == 1):
                                    if(currentBoard.board[x - 1][y - 1].get_color() == '.' and currentBoard.board[x - 1][y + 1].get_color() == '.'):
                                        our_score += 5
                                    if(currentBoard.board[x - 1][y - 1].get_color() == opponent_color):
                                        if(currentBoard.board[x + 1][y + 1].get_color() != '.'):
                                            our_score += 5
                                        else:
                                            our_score -= 3
                                    if(currentBoard.board[x - 1][y + 1].get_color() == opponent_color):
                                        if(currentBoard.board[x + 1][y - 1].get_color() != '.'):
                                            our_score += 5
                                        else:
                                            our_score -= 3
                                    if(currentBoard.board[x - 1][y + 1].get_color() == '.'):
                                        our_score += 5
                                    if(currentBoard.board[x - 1][y - 1].get_color() == '.'):
                                        our_score += 5
                            else:
                                if(currentBoard.board[x][y].is_king == True):
                                    if(cp[1] == 0):
                                        if(cp[0] != 0 and cp[0] != currentBoard.row - 1):
                                            if(currentBoard.board[x + 1][y + 1].get_color() == opponent_color):
                                                our_score += 3
                                            if(currentBoard.board[x - 1][y + 1].get_color() == opponent_color):
                                                our_score += 3
                                    if(cp[1] == currentBoard.col - 1):
                                        if(cp[0] != 0 and cp[0] != currentBoard.row - 1):
                                            if(currentBoard.board[x + 1][y - 1].get_color() == opponent_color):
                                                our_score += 3
                                            if(currentBoard.board[x - 1][y - 1].get_color() == opponent_color):
                                                our_score += 3
                                    if(cp[0] == 0):
                                        if(cp[1] != 0 and cp[1] != currentBoard.col - 1):
                                            if(currentBoard.board[x + 1][y - 1].get_color() == opponent_color):
                                                our_score += 3
                                            if(currentBoard.board[x + 1][y + 1].get_color() == opponent_color):
                                                our_score += 3
                                    if(cp[0] == currentBoard.row - 1):
                                        if(cp[1] != 0 and cp[1] != currentBoard.col - 1):
                                            if(currentBoard.board[x - 1][y + 1].get_color() == opponent_color):
                                                our_score += 3
                                            if(currentBoard.board[x - 1][y - 1].get_color() == opponent_color):
                                                our_score += 3
                                else: # It's a pawn
                                    if(cp[1] == 0):
                                        if(cp[0] != 0 and cp[0] != currentBoard.row - 1):
                                            if(currentBoard.board[x - 1][y + 1].get_color() == opponent_color):
                                                our_score += 3
                                    if(cp[1] == currentBoard.col - 1):
                                        if(cp[0] != 0 and cp[0] != currentBoard.row - 1):
                                            if(currentBoard.board[x - 1][y - 1].get_color() == opponent_color):
                                                our_score += 3
                            

                    elif (currentBoard.board[x][y].get_color() == '.'):
                        # ignore since this location doesn't have a checkerpiece
                        continue
                    else:
                        num_opp_pieces += 1
                        # Check if it's king
                        if(currentBoard.board[x][y].is_king == True):
                            opponent_score += 2
                        else:
                            opponent_score += 1
                        
                        cp = currentBoard.board[x][y].get_location()
                        # Check if it's an edge piece row 0, row n, col 0, col n
                        if (cp[0] == 0 or cp[0] == currentBoard.row -1):
                            opponent_score += 1
                        if (cp[1] == 0 or cp[1] == currentBoard.col -1):
                            opponent_score += 1
                 
        return our_score - opponent_score

    def get_move(self, move):
        if len(move) != 0:  # If the opponent started first
            self.board.make_move(move, self.opponent[self.color])
        else:
            self.color = 1

        # Make a copy of the current board
        copyBoard = copy.deepcopy(self.board)

        # Make a list of all possible moves that our AI can make
        our_moves = copyBoard.get_all_possible_moves(self.color)


        # Build local list to store heuristic scores
        heuristic_scores = []
        our_moves_1D = []

        # Iterate through list of all our moves
        for x in range(len(our_moves)):
            for y in range(len(our_moves[x])):
                # Make a move on the copy/theoretical board
                copyBoard.make_move(our_moves[x][y], self.color)
                # Find heuristic score of that move with current state of board
                heuristic_scores.append(self.get_heuristic_score(copyBoard))
                our_moves_1D.append(our_moves[x][y])
                copyBoard.undo()

        # Go through all the moves and pick the highest scoring move
        max_score = -1
        index = 0
        for x in range(len(heuristic_scores)):
            # Update max score if current value is greater than max
            if (heuristic_scores[x] > max_score):
                max_score = heuristic_scores[x]
                index = x
        move = our_moves_1D[index]
        self.board.make_move(move, self.color)
        return move
