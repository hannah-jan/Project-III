#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 14:50:55 2019

@author: hannahjanmo
"""

from policy_eval import step, policy_eval, print_grid, r_policy
import numpy as np


def lookahead(i,j, state_val):
    
    (north_i, north_j) = step([i,j], np.array([-1,0]))
    (south_i, south_j) = step([i,j], np.array([1,0]))
    (east_i, east_j) = step([i,j], np.array([0,1]))
    (west_i, west_j) = step([i,j], np.array([0,-1]))
    
    action_values = [state_val[north_i][north_j], state_val[south_i][south_j],
                     state_val[east_i][east_j], state_val[west_i][west_j]]
    
    return(action_values)


def greedy(state_val):
    
    greedy_policy = [[[0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]],
                     [[0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]],
                     [[0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]],
                     [[0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]],
                     [[0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]]]
    for i in range(5):
        for j in range(5):
            greedy_action = np.argmax(lookahead(i, j, state_val))
            greedy_policy[i][j][greedy_action] = 1
            
    greedy_policy[0][4] = [0, 0, 0, 0, 0, 0, 1] # always goal
    greedy_policy[1][1] = [0, 0, 0, 0, 1, 0, 0] # always snake
    greedy_policy[1][3] = [0, 0, 0, 0, 1, 0, 0] # always snake
    greedy_policy[3][2] = [0, 0, 0, 0, 1, 0, 0] # always snake
    greedy_policy[4][4] = [0, 0, 0, 0, 1, 0, 0] # always snake
    greedy_policy[3][4] = [0, 0, 0, 0, 0, 1, 0] # always ladder
    
    return(greedy_policy)
        
    
# TEST WITH RANDOM POLICY

"""
val0 = np.zeros((5,5))

r_policy_eval = policy_eval(r_policy)[0]
print_grid(r_policy_eval)    

print_policy(greedy(r_policy_eval)) #check to see optimal policy

value_optimal = policy_eval(greedy(r_policy_eval))[0]


def print_policy(policy):
    for state_pols in policy:
        for probs in state_pols:
            print(probs),       
        print  
        
print_grid(value_optimal)


"""