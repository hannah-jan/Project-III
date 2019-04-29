from policy_eval import policy_eval, r_policy, print_grid, print_policy, iterate_one
import matplotlib.pyplot as plt

from policy_improv import greedy
import numpy as np

# Value iteration function
def value_it(state_val_initial = np.zeros((5,5)), discount=1, epsilon = 0.00001):
    m = 0
    state_val = state_val_initial
    error = []
    while True:
        delta = 0
        
        # act greedily and then do one sweep of policy evaluation
        new_state_value = iterate_one(state_val, discount, greedy(state_val))
                
        for i in range(5):
            for j in range(5):
                error.append(state_val[i][j] - new_state_value[i][j])
                
        difference = max(max(error), -min(error))
        delta = max(delta, difference)
        # stop when successive approximations are nearly equal
        if delta < epsilon:
            break
    
        state_val = new_state_value
        m += 1
        error = []
        
    return(greedy(state_val), m)


# TEST EPSILON

value_trial_1 = value_it(epsilon= 0.01)
print(value_trial_1[1])

value_trial_2 = value_it(epsilon= 0.0001)
print(value_trial_2[1])

value_trial_3 = value_it(epsilon= 0.000001)
print(value_trial_3[1])

