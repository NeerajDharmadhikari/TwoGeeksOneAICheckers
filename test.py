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
                    # Helper Function 1: START
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
                       # Helper Function 1: END
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
                                # HELPER Function 2: START
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

                                # HELPER FUNCTION 2: END
                                else: # It's a black pawn
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
                    # HELPER FUNCTION 1 : START
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
                    # HELPER FUNCTION 1 : END
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
                                # HELPER FUNCTION 2: START
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
                                # HELPER FUNCTION 2: END
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
