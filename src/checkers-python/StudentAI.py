from random import randint
from BoardClasses import Move
from BoardClasses import Board
import copy
# The following part should be completed by students.
# Students can modify anything except the class name and existing functions and variables.
# python3 AI_Runner.py 7 7 2 l ../src/checkers-python/main.py Sample_AIs/Random_AI/main.py
# python3 AI_Runner.py 7 7 2 l Sample_AIs/Random_AI/main.py ../src/checkers-python/main.py
MAX, MIN = 1000, -1000
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
        # Returns optimal value for current player  
    
    def get_move(self, move):
        alpha = -1000
        value = -1000
        beta = 1000
        bestMove = None

        if len(move) != 0:  # If the opponent started first
            self.board.make_move(move, self.opponent[self.color])
        else:
            self.color = 1

        # Make a list of all possible moves that our AI can make
        our_moves = self.board.get_all_possible_moves(self.color)

        # Iterate through list of all our moves
        for x in range(len(our_moves)):
            for y in range(len(our_moves[x])):
                # Make a move on the copy/theoretical board
                self.board.make_move(our_moves[x][y], self.color)
                currentScore = self.alphaBetaMin(alpha, beta, 1)
                self.board.undo()
                
                if currentScore >= value:
                    value = currentScore
                    bestMove = our_moves[x][y]
                    #print("New bestMove", bestMove, "current best score:", currentScore)
                    alpha = currentScore
        
        #print("Decision?", bestMove)
        self.board.make_move(bestMove, self.color)
        return bestMove

    def alphaBetaMin(self, alpha, beta, depth):
        '''
        # Check if our AI is black and we won
        #if self.color == self.board.is_win(self.color):
        if self.color == self.board.is_win("B"):
            return 1000
        # Check if our AI (black) lost
        #elif self.color == 1 and self.board.is_win(self.color) == 2:
        elif self.color == 1 and self.board.is_win("B") == 2:
            return -1000
        # Check if our AI (white) lost
        #elif self.color == 2 and self.board.is_win(self.color) == 1:
        elif self.color == 2 and self.board.is_win("W") == 1:
            return -1000
        
        # Check if opponent will tie
        #if self.board.is_win(self.color) == -1:
        if self.board.is_win("B") == -1:
            return 0
        '''
        if depth == 3:
            return self.get_heuristic_score2()
        else:
            value = 1000
            # Go through every possible move
            opponent_moves = self.board.get_all_possible_moves(self.opponent[self.color])
            for x in opponent_moves:
                for move in x:
                    # Make move for opponent
                    self.board.make_move(move, self.opponent[self.color])
                    value = min(value, self.alphaBetaMax(alpha, beta, depth+1))
                    self.board.undo()
                    beta = min(beta, value)
                    if alpha >= beta:
                        return value
            return value

    def alphaBetaMax(self, alpha, beta, depth):
        
        '''
        # Check if our AI is black and we won
        #if self.color == self.board.is_win(self.opponent[self.color]):
        if self.color == self.board.is_win("B"):
            return 1000
        # Check if our AI (black) lost
        #elif self.color == 1 and self.board.is_win(self.opponent[self.color]) == 2:
        elif self.color == 1 and self.board.is_win("B") == 2:
            return -1000
        # Check if our AI (white) lost
        #elif self.color == 2 and self.board.is_win(self.opponent[self.color]) == 1:
        elif self.color == 2 and self.board.is_win("W") == 1:
            return -1000
        
        # Check if opponent will tie
        #if self.board.is_win(self.opponent[self.color]) == -1:
        if self.board.is_win("B") == -1:
            return 0
        '''
        if depth == 3:
            return self.get_heuristic_score2()
        else:
            value = -1000
            # Go through every possible move
            our_moves = self.board.get_all_possible_moves(self.color)
            for x in our_moves:
                for move in x:
                    self.board.make_move(move, self.color)
                    value = max(value, self.alphaBetaMin(alpha, beta, depth+1))
                    self.board.undo()
                    alpha = max(alpha, value)
                    if alpha >= beta:
                        return value
            return value
    
    def closeToBecomingKing(self, color, row_position):
        if self.color == 1: # Our color is black
            return row_position
        else: # our color is white
            return (self.board.row - row_position - 1)

    def get_heuristic_score2(self):
        
        num_black_kings = 0
        num_white_kings = 0
        num_safe_piece_black = 0
        num_safe_piece_white = 0
        num_back_black = 0
        num_back_white = 0
        closer_black = 0
        closer_white = 0
        #score = 0
        for x in range(len(self.board.board)):
            for y in range(len(self.board.board[x])):
                # Check if it's our checker piece
                if (self.board.board[x][y].get_color() == 'B'):
                    # Check if it's a king
                    if(self.board.board[x][y].is_king == True):
                        num_black_kings += 1
                    else: # Check how close checker piece is to becoming King
                        closer_black += self.closeToBecomingKing(self.color, x)
                    
                    cp = self.board.board[x][y].get_location()

                    # Check if black checker piece is in the back
                    if(cp[0] == 0):
                        num_back_black += 1
                    
                    # Check if it's an edge piece row 0, row n, col 0, col n
                    if (cp[0] == 0 or cp[0] == self.board.row -1):
                        num_safe_piece_black += 1
                    if (cp[1] == 0 or cp[1] == self.board.col -1):
                        num_safe_piece_black += 1
                    if (cp[0] == 0 and cp[1] == 0):
                        num_safe_piece_black -= 1
                    if (cp[0] == 0 and cp[1] == self.board.col-1):
                        num_safe_piece_black -= 1
                    if (cp[0] == self.board.row -1 and cp[1] == 0):
                        num_safe_piece_black -= 1
                    if (cp[0] == self.board.row-1 and cp[1] == self.board.col-1):
                        num_safe_piece_black -= 1
                    
                    # Check for safe pieces that are not part of the edge
                    if (cp[0] != 0 and cp[0] != self.board.row -1):
                        if (cp[1] != 0 and cp[1] != self.board.col -1):
                            is_safe = True
                            if(self.board.board[x + 1][y - 1].get_color() == 'W'):
                                if(self.board.board[x - 1][y + 1].get_color() == '.'):
                                    is_safe = False
                            if(self.board.board[x + 1][y + 1].get_color() == 'W'):
                                if(self.board.board[x - 1][y - 1].get_color() == '.'):
                                    is_safe = False
                            if(self.board.board[x - 1][y + 1].get_color() == 'W' and self.board.board[x - 1][y + 1].is_king):
                                if(self.board.board[x + 1][y-1].get_color() == '.'):
                                    is_safe = False
                            if(self.board.board[x - 1][y - 1].get_color() == 'W' and self.board.board[x - 1][y - 1].is_king):
                                if(self.board.board[x + 1][y + 1].get_color() == '.'):
                                    is_safe = False
                            if (is_safe == True):
                                #print("safe piece counted")
                                num_safe_piece_black += 1
                            #else:
                                #print(x, y)
                                #print("safe piece not counted")
                                #score -= 2
                        
                    '''
                    # Check for safe pieces that are part of the edges
                    is_safe = True
                    # Check for safe piece on edge (column - 1)
                    if (cp[1] == self.board.col - 1):
                        if(self.board.board[x + 1][y - 1].get_color() == 'W'):
                            is_safe = False
                        # Check for safe piece on edge (0)
                    if (cp[1] == 0):
                        if(self.board.board[x + 1][y + 1].get_color() == 'W'):
                            is_safe = False
                    # check for safe piece on edge (column - 1) when a King
                    if (cp[1] == self.board.col - 1 and ((cp[0] > 0) or (cp[0] < self.board.row - 1))):
                        if(self.board.board[x - 1][y - 1].get_color() == 'W'):
                            is_safe = False
                        if(self.board.board[x + 1][y - 1].get_color() == 'W'):
                            is_safe = False
                        # check for safe piece on edge (0) when a King
                        if (cp[1] == 0 and ((cp[0] > 0) or (cp[0] < self.board.row - 1))):
                            if(self.board.board[x - 1][y + 1].get_color() == 'W'):
                                is_safe = False
                            if(self.board.board[x + 1][y + 1].get_color() == 'W'):
                                is_safe = False
                    
                        if (is_safe == True):
                            num_safe_piece_black += 1
                    '''

                elif(self.board.board[x][y].get_color() == 'W'): 
                    if(self.board.board[x][y].is_king == True):
                        num_white_kings += 1
                    else:
                        closer_white += self.closeToBecomingKing(2, x)

                    # Check if it's a corner piece either (0, 0), (0, n), (n, 0), or (n, n)
                    cp = self.board.board[x][y].get_location()
                    
                    # Check if white checker piece is in the back
                    if(cp[0] == self.board.row - 1):
                        num_back_white += 1
                    # Check if it's an edge piece row 0, row n, col 0, col n
                    if (cp[0] == 0 or cp[0] == self.board.row -1):
                        num_safe_piece_white += 1
                    if (cp[1] == 0 or cp[1] == self.board.col -1):
                        num_safe_piece_white += 1
                    if (cp[0] == 0 and cp[1] == 0):
                        num_safe_piece_white -= 1
                    if (cp[0] == 0 and cp[1] == self.board.col-1):
                        num_safe_piece_white -= 1
                    if (cp[0] == self.board.row -1 and cp[1] == 0):
                        num_safe_piece_white -= 1
                    if (cp[0] == self.board.row-1 and cp[1] == self.board.col-1):
                        num_safe_piece_white -= 1
                    # Check for white safe pieces that are not part of the edge
                    if (cp[0] != 0 and cp[0] != self.board.row -1):
                        if (cp[1] != 0 and cp[1] != self.board.col -1):
                            is_safe = True
                            if(self.board.board[x - 1][y - 1].get_color() == 'B'):
                                if(self.board.board[x + 1][y + 1].get_color() == '.'):
                                    is_safe = False
                            if(self.board.board[x - 1][y + 1].get_color() == 'B'):
                                if(self.board.board[x + 1][y - 1].get_color() == '.'):
                                    is_safe = False
                            if(self.board.board[x + 1][y + 1].get_color() == 'B' and self.board.board[x + 1][y + 1].is_king):
                                if(self.board.board[x - 1][y - 1].get_color() == '.'):
                                    is_safe = False
                            if(self.board.board[x + 1][y - 1].get_color() == 'B' and self.board.board[x + 1][y - 1].is_king):
                                if(self.board.board[x - 1][y + 1].get_color() == '.'):
                                    is_safe = False
                            if (is_safe == True):
                                num_safe_piece_white += 1
        if self.color == 1:      
            score = 10*(self.board.black_count - self.board.white_count)
            #print("Score after diff in counts:", score)
            #print('safe black:', num_safe_piece_black, 'safe white:', num_safe_piece_white, 'safe score:', num_safe_piece_black - num_safe_piece_white)
            score += 5*(num_black_kings - num_white_kings)
            #print("Score after diff in Ks:", score)
            #score += 2*(closer_black - closer_white)
            score += 2*(num_safe_piece_black - num_safe_piece_white)
            #print("Score after diff in safe pieces:", score)
            score += 2*(num_back_black - num_back_white)
            #print("Score after back row pieces:", score)
        elif self.color == 2:
            score = 10*(self.board.white_count - self.board.black_count)
            #print("Score after diff in counts:", score)
            #print('safe black:', num_safe_piece_black, 'safe white:', num_safe_piece_white, 'safe score:', num_safe_piece_black - num_safe_piece_white)
            score += 5*(num_white_kings - num_black_kings)
            #print("Score after diff in Ks:", score)
            #score += 2*(closer_black - closer_white)
            score += 2*(num_safe_piece_white - num_safe_piece_black)
            #print("Score after diff in safe pieces:", score)
            score += 2*(num_back_white - num_back_black)
            #print("Score after back row pieces:", score)
        return score