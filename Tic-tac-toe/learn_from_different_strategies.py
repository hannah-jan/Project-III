import matplotlib.pyplot as plt
from strategies import player_move_random, player_move_never_lose, player_move_learner, player_move_good
from basicfunctions import is_finished, is_winner

"""
Simulating the game of tic-tac-toe a reinforcement learner vs other strategies
 and comparing the average wins against a random player for a reinforcement learner who has 
learned through each different strategy
"""

value_map_1 = {}
value_map_2 = {}
value_map_3 = {}
    
# Runs the game once with player 1 with specified strategy and player 2 moving as learner    
def play_versus_learner(strategy, value_map, verbose = True, explore=0.1, update=True):
    state0 = (0, 0, 0, 0, 0, 0, 0, 0, 0)
    alpha = 0.5
    while True:
        state1 = strategy(1, state0)
        if is_winner(1, state1):
            value_map[state0] = 0
            if verbose: print("\033[1;31;40m player 1 wins \n")
            return -1
        if is_finished(state1):
            value_map[state0] = 0.5
            if verbose: print("\033[1;33;40m draw \n")
            return 0
        state2 = player_move_learner(2, state1,value_map, False, explore)
        #update after every player 2 move=>
        if update == True:
            value_map[state0] = (
                value_map.get(state0, 0.5)
                + alpha * (value_map.get(state2, 0.5) - value_map.get(state0, explore))
                )
        if is_winner(2, state2):
            value_map[state2] = 1
            if verbose: print("\033[1;34;40m player 2 wins \n")
            return 1
        if is_finished(state2):
            value_map[state2] = 0.5
            if verbose: print("\033[1;33;40m draw \n")
            return 0
        # reset to iterate again
        state0 = state2
  
# iterate to get a value map (get a different value map depending on oponents strategy)

for i in range(20000):
    play_versus_learner(player_move_random, value_map_1, verbose = False, explore = 0.1)
    play_versus_learner(player_move_good, value_map_2, verbose = False, explore = 0.1)
    play_versus_learner(player_move_never_lose, value_map_3, verbose = False, explore = 0.1)


learner_wins_1 = []
learner_wins_2 = []
learner_wins_3 = []


for i in range(1000):
    learner_win_1 = play_versus_learner(player_move_random, value_map_1, verbose = False, explore = -1, update=False)
    learner_win_2 = play_versus_learner(player_move_random, value_map_2, verbose = False, explore = -1, update=False)
    learner_win_3 = play_versus_learner(player_move_random, value_map_3, verbose = False, explore = -1, update=False)
    learner_wins_1.append(learner_win_1)
    learner_wins_2.append(learner_win_2)
    learner_wins_3.append(learner_win_3)



learner_totals_1 = [sum(learner_wins_1[0:i]) for i in range (1, len(learner_wins_1)+1)]
learner_averages_1 = [learner_totals_1[i]/(i+1) for i in range(len(learner_totals_1))] 
learner_averages_1.pop(0)

learner_totals_2 = [sum(learner_wins_2[0:i]) for i in range (1, len(learner_wins_2)+1)]
learner_averages_2 = [learner_totals_2[i]/(i+1) for i in range(len(learner_totals_2))] 
learner_averages_2.pop(0)

learner_totals_3 = [sum(learner_wins_3[0:i]) for i in range (1, len(learner_wins_3)+1)]
learner_averages_3 = [learner_totals_3[i]/(i+1) for i in range(len(learner_totals_3))] 
learner_averages_3.pop(0)


plt.plot(learner_averages_1)
plt.plot(learner_averages_2)
plt.plot(learner_averages_3)

plt.ylabel('Average Score')
plt.xlabel('Iteration')
plt.gca().legend(('Vs. Random','Vs. Good', 'Vs. Never-lose'))
plt.suptitle('Average scores against a random player over time')
plt.savefig('learning_from_different_strategies.pdf', bbox_inches='tight', type = 'pdf' )
plt.show()

