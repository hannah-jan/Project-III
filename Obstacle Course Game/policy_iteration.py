#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 16:18:02 2019

@author: hannahjanmo
"""

from policy_eval import policy_eval, r_policy, print_grid, print_policy
from policy_improv import greedy
import numpy as np


def policy_it(initial_policy, state_val_initial = np.zeros((5,5)), discount=1, epsilon = 0.00001):
    m = 0
    policy = initial_policy
    while True:
        
        value = policy_eval(policy, discount=discount, epsilon=epsilon)
        #print_grid(value)
        
        policy_new = greedy(value[0])
        #print_policy(policy_new)
        
        if np.array_equal(policy_eval(policy_new)[0], value[0]) == True:
            break
    
        policy = policy_new 
        m = m + 1 + value[1] #include iterations for policy evaluation in computational cost
        
    return(policy, m)


# Tests-> 

"""
trial_1 = policy_it(r_policy, discount=1, epsilon=0.01)
print(trial_1[1])

trial_2 = policy_it(r_policy, discount=1, epsilon=0.0001)
print(trial_2[1])

trial_3 = policy_it(r_policy, discount=1, epsilon=0.000001)
print(trial_3[1])

trial_4 = policy_it(r_policy, discount=1, epsilon=0.00000001)
print(trial_4[1])
"""

# alter discounting



trial_1_1 = policy_it(r_policy, discount=0.8, epsilon=0.01)
print(trial_1_1[1])


