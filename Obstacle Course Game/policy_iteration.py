from policy_eval import policy_eval, r_policy, print_grid
from policy_improv import greedy, print_policy
import numpy as np


# Policy iteration

def policy_it(initial_policy, state_val_initial = np.zeros((5,5)), discount=1, epsilon = 0.00001):
    m = 0
    policy = initial_policy
    while True:
        
        # Evaluate policy and then find greedy policy with respect to value function.
        value = policy_eval(policy, discount=discount, epsilon=epsilon)
        policy_new = greedy(value[0])
        
        # Stop iterating if value of the two policies are the same, i.e. if improvement stops
        if np.array_equal(policy_eval(policy_new)[0], value[0]) == True:
            break
    
        policy = policy_new 
        m = m + 1 + value[1] # include iterations for policy evaluation in computational cost
        
    return(policy, m)



# TESTING EPSILON 

trial_1 = policy_it(r_policy, discount=1, epsilon=0.01)
print(trial_1[1])

trial_2 = policy_it(r_policy, discount=1, epsilon=0.0001)
print(trial_2[1])

trial_3 = policy_it(r_policy, discount=1, epsilon=0.000001)
print(trial_3[1])

trial_4 = policy_it(r_policy, discount=1, epsilon=0.00000001)
print(trial_4[1])



