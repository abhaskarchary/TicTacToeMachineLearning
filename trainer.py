#!/usr/bin/python

import copy,os,random
import numpy as np

states = {}

exploration_rate = 0.1


def calculate_states(nmat,t):

    for i in range(3):
        for j in range(3):
            turn = t
            if nmat[i][j] == 0:
                temp_mat = copy.deepcopy(nmat)
                temp_mat[i][j] = turn
                states[str(encode(temp_mat))] = 0
                turn = turn%2+1
                if win(temp_mat) == 0:
                    calculate_states(temp_mat,turn)



def encode(mat):
    encoded = 0
    for i in range(3):
        for j in range(3):
            encoded = (encoded + mat[i][j])*3

    encoded/=3
    return encoded

    
def win(board):
    
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != 0:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != 0:
            return board[0][i]
    
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != 0:
        return board[0][2]

    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return 0

    return -1


def play_game(turn,mat):
    (state,(i,j)) = choose_best(turn, mat)
    nmat = copy.deepcopy(mat)
    nmat[i][j] = turn
    if turn == 1:
        cross_moves.append(state)
        if win(nmat) == 1:
            feed_cross_reward(1)
            feed_knot_reward(-1)
            return
    else:
        knot_moves.append(state)
        if win(nmat) == 2:
            feed_knot_reward(1)
            feed_cross_reward(-1)
            return
    if win(nmat) == -1:
        feed_cross_reward(0)
        feed_knot_reward(0)
        return

    play_game(turn%2+1, nmat)

def feed_cross_reward(rew):
    for i in cross_moves:
        states[i] = states[i] + 0.1*(rew - states[i])


def feed_knot_reward(rew):
    for i in knot_moves:
        states[i] = states[i] + 0.1*(rew - states[i])

def choose_best(turn, nmat):
    available_moves = []
    max_prob,min_prob = -2,2
    for i in range(3):
        for j in range(3):
            if nmat[i][j] == 0:
                new_nmat = copy.deepcopy(nmat)
                new_nmat[i][j] = turn
                available_moves.append((str(encode(new_nmat)),(i,j)))

    exploration = random.random()
    if exploration <= exploration_rate:
        best_move = available_moves[random.randint(0,len(available_moves)-1)]
    else:
        for (state, move) in available_moves:
            if states[state] >= max_prob:
                best_move = (state,move)
                max_prob = states[state]
            if states[state] <= min_prob:
                min_prob = states[state]

        if max_prob == min_prob == 0:
            best_move = available_moves[random.randint(0,len(available_moves)-1)]

    return best_move
                
        
if not os.path.exists("optimal_strategy.npy"):
    calculate_states([[0,0,0],[0,0,0],[0,0,0]], 1)
    np.save("optimal_strategy.npy",states)
else:
    states = np.load("optimal_strategy.npy").item()

trainer_count = int(raw_input("Enter the number of times to train: "))

for i in range(trainer_count):
    cross_moves = []
    knot_moves = []
    play_game(1,[[0,0,0],[0,0,0],[0,0,0]])
    print "training", (i+1)

np.save("optimal_strategy.npy",states)
print "exiting.."









