import numpy as np
import copy

class Bot:

    def __init__(self,turn):
        self.states = np.load("optimal_strategy.npy").item()
        self.turn = turn
    
    def make_move(self, mouse, board):
        available_moves = []
        max_prob = -2
        for i in range(3):
            for j in range(3):
                mat = copy.deepcopy(board)
                if mat[i][j] == 0:
                    mat[i][j] = self.turn
                    available_moves.append((self.encode(mat),(i,j)))

        for (state, move) in available_moves:
            if self.states[state] >= max_prob:
                max_prob = self.states[state]
                best_move = move

        return best_move
        

    def encode(self,board):
        encoded = 0
        for i in range(3):
            for j in range(3):
                encoded = (encoded + board[i][j])*3

        encoded/=3
        return str(encoded)
