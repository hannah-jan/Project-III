import numpy as np
import matplotlib.pyplot as plt

# Colours of the grid
colours = [["w","w","w","w","#98e698"], ["w","#ff4d4d","w","#ff4d4d","w"], ["w","w","w","w","w"], 
           ["w","w","#ff4d4d","w","#56b5fd"], ["#F8E71C","w","w","w","#ff4d4d"]]
            

#######################################################################
# The function 'step' is modified from the following authors.         #
# 2016-2018 Shangtong Zhang(zhangshangtong.cpp@gmail.com)             #
# 2016 Kenta Shimada(hyperkentakun@gmail.com)                         #
# Permission given to modify the code as long as you keep this        #
# declaration at the top                                              #
#######################################################################
           

# Returns position of agent after taking an action from any given state.            
def step(position, action):
    position = np.array(position)
    next_position= (position + action).tolist()
    x, y = next_position
    if x < 0 or x >= 5 or y < 0 or y >= 5: # Grid is 5 by 5
        next_position = position.tolist()

    return next_position


# Matrix to define the probability of taking each action from any given state under random policy. 
# Actions are ordered North, South, East, West, Jump to 1 (snake), Ladder, Goal
    
r_policy = [[[0.25, 0.25, 0.25, 0.25, 0, 0, 0], #21
          [0.25, 0.25, 0.25, 0.25, 0, 0, 0], #22
          [0.25, 0.25, 0.25, 0.25, 0, 0, 0], #23
          [0.25, 0.25, 0.25, 0.25, 0, 0, 0], #24
          [0, 0, 0, 0, 0, 0, 1]],            #25
    
          [[0.25, 0.25, 0.25, 0.25, 0, 0, 0], #16
          [0, 0, 0, 0, 1, 0, 0],             #17
          [0.25, 0.25, 0.25, 0.25, 0, 0, 0], #18
          [0, 0, 0, 0, 1, 0, 0],             #19
          [0.25, 0.25, 0.25, 0.25, 0, 0, 0]], #20
          
          [[0.25, 0.25, 0.25, 0.25, 0, 0, 0], #11
          [0.25, 0.25, 0.25, 0.25, 0, 0, 0], #12
          [0.25, 0.25, 0.25, 0.25, 0, 0, 0], #13
          [0.25, 0.25, 0.25, 0.25, 0, 0, 0], #14
          [0.25, 0.25, 0.25, 0.25, 0, 0, 0]], #15


          [[0.25, 0.25, 0.25, 0.25, 0, 0, 0], #6
          [0.25, 0.25, 0.25, 0.25, 0, 0, 0], #7
          [0, 0, 0, 0, 1, 0, 0],             #8
          [0.25, 0.25, 0.25, 0.25, 0, 0, 0], #9
          [0, 0, 0, 0, 0, 1, 0]],             #10

 
          [[0.25, 0.25, 0.25, 0.25, 0, 0, 0], #1
          [0.25, 0.25, 0.25, 0.25, 0, 0, 0], #2
          [0.25, 0.25, 0.25, 0.25, 0, 0, 0], #3
          [0.25, 0.25, 0.25, 0.25, 0, 0, 0], #4
          [0, 0, 0, 0, 1, 0, 0]]]            #5
          

# Function to perform one iteration of policy evaluation.
def iterate_one(state_val, discount, policy):
    new_state_val = state_val.copy()
    for i in range(5):
        for j in range(5):
                (north_i, north_j) = step([i,j], np.array([-1,0]))
                (south_i, south_j) = step([i,j], np.array([1,0]))
                (east_i, east_j) = step([i,j], np.array([0,1]))
                (west_i, west_j) = step([i,j], np.array([0,-1]))
                # Bellman equation as update formula:
                new_state_val[i,j] =discount*(
                                   policy[i][j][0]*(-1 + state_val[north_i, north_j]) +
                                   policy[i][j][1]*(-1 + state_val[south_i, south_j]) +
                                   policy[i][j][2]*(-1 + state_val[east_i, east_j]) +
                                   policy[i][j][3]*(-1 + state_val[west_i, west_j]) +
                                   policy[i][j][4]*(-1 + state_val[4,0]) +
                                   policy[i][j][5]*(-1 + state_val[0,4]) + 
                                   policy[i][j][6]*(0 +  state_val[0,4]))                                       
    return(new_state_val)
            

# Prints value function in grid layout of obstacle course game.
def print_grid(value_fn, name=' ', save = False):
    it_rounded = [['%.2f' % j for j in i] for i in value_fn]
    fig, ax = plt.subplots()
    ax.axis('tight')
    ax.axis('off')
    the_table = ax.table(cellText=it_rounded,cellColours=colours,loc='left')
    the_table.scale(1.5, 8)
    the_table.set_fontsize(24)
    if save == True:
        plt.savefig(name +'.pdf', bbox_inches='tight', type = 'pdf' )
    plt.show()


# Runs policy evaluation until the successive approximations of the value function is less than epsilon.         
def policy_eval(policy, state_val_initial = np.zeros((5,5)), discount=1, epsilon = 0.000001):
    state_val = state_val_initial
    error = []    
    k = 0    
    while True:            
        new_state_val = iterate_one(state_val, discount, policy)
        delta = 0
        k += 1       
        for i in range(5):
            for j in range(5):
                error.append(state_val[i][j] - new_state_val[i][j])                
        difference = max(max(error), -min(error))
        delta = max(delta, difference)        
        state_val = new_state_val
        error = []
        if delta < epsilon:
            break
    # Return the state-value function and the number of iterations taken.
    return state_val, k


r_policy_eval = policy_eval(r_policy)[0]
print(r_policy_eval)

r_policy_eval_k = policy_eval(r_policy)[1]
print(r_policy_eval_k)