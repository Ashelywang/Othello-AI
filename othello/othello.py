# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 10:58:30 2017

@author: Anshu.Wang
"""
import numpy as np
from config.config import BLACK, WHITE, EMPTY, BOARDSIZE
from config.config import IS_IN_RANGE

class othello:
    def __init__(self):
        self.board = np.zeros((BOARDSIZE,BOARDSIZE), dtype = np.integer)
        self.board[int(BOARDSIZE/2 -1)][int(BOARDSIZE/2)] = BLACK
        self.board[int(BOARDSIZE/2)][int(BOARDSIZE/2 -1)] = BLACK
        self.board[int(BOARDSIZE/2 -1)][int(BOARDSIZE/2 -1)] = WHITE
        self.board[int(BOARDSIZE/2)][int(BOARDSIZE/2)] = WHITE
        
        self.white_count = 2
        self.black_count = 2
        
        self.turn = BLACK
    
    def _get_possible_moves(self, row, col, player):
        """
        get all possible moves
        
        For AI
        """
        pass
        
    def _is_possible_move(self, row, col, player):
        """
        return whether current move is possible 
        
        for checking before move
         1 | 2 | 3   
        ----------    has 8 directions to search !
         4 |   | 6
        ----------
         7 | 8 | 9
        
        ------
        """
        if player == BLACK:
            anti_player = WHITE
        else:
            anti_player = BLACK
            
        # If it is not empty, you can not put it on the board
        if self.board[row,col] != EMPTY:
            return False
        
        place_p = np.array([row,col])
        a = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
        directions = np.array(a)
        
        for i in range(len(directions)):
            tmp_p = place_p
            flip_num = 0 # how many can be flipped
            #can_end = False # is there a same color at end that can make me flip
            
            while IS_IN_RANGE(tmp_p + directions[i]):
                tmp_p = tmp_p + directions[i]
                if self.board[tmp_p[0],tmp_p[1]] == anti_player:
                    flip_num += 1
                elif self.board[tmp_p[0],tmp_p[1]] == player:
                    if flip_num > 0 :
                        return True
                elif self.board[tmp_p[0],tmp_p[1]] == EMPTY:
                    break
        return False
                    
        
        
    def move(self, row, col, player):
        
        
        if player == BLACK:
            anti_player = WHITE
        else:
            anti_player = BLACK
            
            
        # IF I can not put at this place
        if not self._is_possible_move( row, col, player):
            print("This place can not be placed!")
            return 
        
        # Else put it down
        self.board[row,col] = player
        
        
        # Then flip!
        
        a = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
        directions = np.array(a)
        place_p = np.array([row,col])
        
        for i in range(len(directions)):
            tmp_p = place_p 
            flip_num = 0
            
            while IS_IN_RANGE(tmp_p + directions[i]):
                tmp_p = tmp_p + directions[i]
                if self.board[tmp_p[0],tmp_p[1]] == anti_player:
                    flip_num += 1
                elif self.board[tmp_p[0],tmp_p[1]] == player:
                    if flip_num == 0:
                        break
                    elif flip_num >0:
                        tmp_p = place_p
                        for j in range(flip_num):
                            print(flip_num,tmp_p,directions[i])
                            tmp_p = tmp_p + directions[i]
                            print(flip_num,tmp_p)
                            self.board[tmp_p[0],tmp_p[1]] = player
                        break
                elif self.board[tmp_p[0],tmp_p[1]] == EMPTY:
                    break
        self.display()
            
        
        
        # If I can, I'll put and revert
        
    def display(self):
        print('  ',end=' ')
        for i in range(8):
            print('', i,end='')
        print()
        for i in range(8):
            print(i, ' |',end='')
            for j in range(8):
                if self.board[i][j] == BLACK:
                    print('B',end='')
                elif self.board[i][j] == WHITE:
                    print('W',end='')
                else:
                    print(' ',end='')
                print('|',end='')
            print()
        
        
        
        
        
    
        