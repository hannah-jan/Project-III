import matplotlib.pyplot as plt
from strategies import  player_move_learner
from basicfunctions import is_finished, is_winner

"""
Simulating the game of tic-tac-toe a reinforcement learner vs another reinforcement learner
 and comparing the average wins, for various conditions
"""

value_map_1 = {}
value_map_2 = {}

    
# Runs the game once with both players moving as learner    
def two_learners(value_map_1, value_map_2, explore1, explore2, verbose = False):
    state0 = (0, 0, 0, 0, 0, 0, 0, 0, 0)
    state1 = player_move_learner(1, state0, value_map_1, False, explore1)      
    alpha = 0.5
    #print(state_str(state0))
    #print('----')

    while True:

        state2 = player_move_learner(2, state1, value_map_2, False, explore2)
        #print(state_str(state2))
        #print('----')
        #update after every player 2 move=>
        value_map_2[state0] = (
            value_map_2.get(state0, 0.5)
            + alpha * (value_map_2.get(state2, 0.5) - value_map_2.get(state0, explore2))
            )        
        if is_winner(2, state2):
            value_map_2[state2] = 1
            if verbose: print("\033[1;34;40m player 2 wins \n")
            return -1
        if is_finished(state2):
            value_map_2[state2] = 0.5
            if verbose: print("\033[1;33;40m draw \n")
            return 0
       
        state3 = player_move_learner(1, state2, value_map_1, False, explore1)
        #print(state_str(state3))
        #print('----')
        
        value_map_1[state1] = (
                value_map_1.get(state1, 0.5)
            + alpha * (value_map_1.get(state3, 0.5) - value_map_1.get(state1, explore1))) 

        if is_winner(1, state3):
            value_map_1[state0] = 0
            if verbose: print("\033[1;31;40m player 1 wins \n")
            return 1
        if is_finished(state3):
            value_map_1[state0] = 0.5
            if verbose: print("\033[1;33;40m draw \n")
            return 0
        
        # reset to iterate again
        state0 = state2
        state1 = state3
        


"""
# Players take it in turns to start the game
 
learner1_wins = []
learner2_wins = []

for i in range(10000):
    learner_win = two_learners(value_map_1, value_map_2, 0.1, 0.1)
    learner1_wins.append(learner_win)
    learner2_wins.append(-1*learner_win)
    learner_win2 = two_learners(value_map_2, value_map_1, 0.1, 0.1) #each player gets to start
    learner1_wins.append(-1*learner_win2)
    learner2_wins.append(learner_win2)

    
learner1_totals = [sum(learner1_wins[0:i]) for i in range (1, len(learner1_wins)+1)]
learner1_averages = [learner1_totals[i]/(i+1) for i in range(len(learner1_totals))] 
learner1_averages.pop(0)

learner2_totals = [sum(learner2_wins[0:i]) for i in range (1, len(learner2_wins)+1)]
learner2_averages = [learner2_totals[i]/(i+1) for i in range(len(learner2_totals))] 
learner2_averages.pop(0)


plt.plot(learner1_averages, label = 'Average learner 1 score')
plt.plot(learner2_averages, label = 'Average learner 2 score')
plt.ylabel('Average Score')
plt.xlabel('Iteration')
plt.gca().legend(('Learner 1','Learner 2'))
plt.suptitle('Average scores over time')
plt.savefig('both_learner_both_start.pdf', bbox_inches='tight', type = 'pdf' )
plt.show()
"""
"""
# Player 1 always starts the game

learner1_wins = []
learner2_wins = []

for i in range(20000):
    learner_win = two_learners(value_map_1, value_map_2, 0.1, 0.1)
    learner1_wins.append(learner_win)
    learner2_wins.append(-1*learner_win)

    
learner1_totals = [sum(learner1_wins[0:i]) for i in range (1, len(learner1_wins)+1)]
learner1_averages = [learner1_totals[i]/(i+1) for i in range(len(learner1_totals))] 
learner1_averages.pop(0)

learner2_totals = [sum(learner2_wins[0:i]) for i in range (1, len(learner2_wins)+1)]
learner2_averages = [learner2_totals[i]/(i+1) for i in range(len(learner2_totals))] 
learner2_averages.pop(0)


plt.plot(learner1_averages, label = 'Average learner 1 score')
plt.plot(learner2_averages, label = 'Average learner 2 score')
plt.ylabel('Average Score')
plt.xlabel('Iteration')
plt.gca().legend(('Learner 1','Learner 2'))
plt.suptitle('Average scores over time')
plt.savefig('both_learner_player1_start.pdf', bbox_inches='tight', type = 'pdf' )
plt.show()
"""

# Players take it in turns to start the game but player 1 explores twice as often
 
learner1_wins = []
learner2_wins = []

for i in range(10000):
    learner_win = two_learners(value_map_1, value_map_2, 0.2, 0.1)
    learner1_wins.append(learner_win)
    learner2_wins.append(-1*learner_win)
    learner_win2 = two_learners(value_map_2, value_map_1, 0.1, 0.2) #each player gets to start
    learner1_wins.append(-1*learner_win2)
    learner2_wins.append(learner_win2)

    
learner1_totals = [sum(learner1_wins[0:i]) for i in range (1, len(learner1_wins)+1)]
learner1_averages = [learner1_totals[i]/(i+1) for i in range(len(learner1_totals))] 
learner1_averages.pop(0)

learner2_totals = [sum(learner2_wins[0:i]) for i in range (1, len(learner2_wins)+1)]
learner2_averages = [learner2_totals[i]/(i+1) for i in range(len(learner2_totals))] 
learner2_averages.pop(0)


plt.plot(learner1_averages, label = 'Average learner 1 score')
plt.plot(learner2_averages, label = 'Average learner 2 score')
plt.ylabel('Average Score')
plt.xlabel('Iteration')
plt.gca().legend(('Learner 1','Learner 2'))
plt.suptitle('Average scores over time')
plt.savefig('both_learner_both_start_player1_explore2.pdf', bbox_inches='tight', type = 'pdf' )
plt.show()


# Players take it in turns to start the game but player 1 explores twice as often
 
learner1_wins = []
learner2_wins = []

for i in range(10000):
    learner_win = two_learners(value_map_1, value_map_2, 0.5, 0.1)
    learner1_wins.append(learner_win)
    learner2_wins.append(-1*learner_win)
    learner_win2 = two_learners(value_map_2, value_map_1, 0.1, 0.5) #each player gets to start
    learner1_wins.append(-1*learner_win2)
    learner2_wins.append(learner_win2)

    
learner1_totals = [sum(learner1_wins[0:i]) for i in range (1, len(learner1_wins)+1)]
learner1_averages = [learner1_totals[i]/(i+1) for i in range(len(learner1_totals))] 
learner1_averages.pop(0)

learner2_totals = [sum(learner2_wins[0:i]) for i in range (1, len(learner2_wins)+1)]
learner2_averages = [learner2_totals[i]/(i+1) for i in range(len(learner2_totals))] 
learner2_averages.pop(0)


plt.plot(learner1_averages, label = 'Average learner 1 score')
plt.plot(learner2_averages, label = 'Average learner 2 score')
plt.ylabel('Average Score')
plt.xlabel('Iteration')
plt.gca().legend(('Learner 1','Learner 2'))
plt.suptitle('Average scores over time')
plt.savefig('both_learner_both_start_player1_explore5.pdf', bbox_inches='tight', type = 'pdf' )
plt.show()