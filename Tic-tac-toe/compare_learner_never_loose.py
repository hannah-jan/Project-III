import matplotlib.pyplot as plt
from strategies import player_move_random, player_move_never_lose, player_move_learner
from basicfunctions import is_finished, is_winner

"""
Simulating the game of tic-tac-toe for a player who never loses vs a random player and 
a reinforcement learner vs a random player and comparing the average wins

"""

value_map = {}

    
# Runs the game once with player 1 with specified strategy and player 2 moving as learner    
def play_versus_learner(strategy, value_map, verbose = True, explore=0.1):
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

for i in range(10000):
    play_versus_learner(player_move_random, value_map, verbose = False)


learner_wins = []

for i in range(10000):
    learner_win = play_versus_learner(player_move_random, value_map, verbose = False, explore = -1)
    learner_wins.append(learner_win)

learner_totals = [sum(learner_wins[0:i]) for i in range (1, len(learner_wins)+1)]
learner_averages = [learner_totals[i]/(i+1) for i in range(len(learner_totals))] 
learner_averages.pop(0)

        
# Runs the game once with player 1 random and player 2 never-lose
def random_versus_never_lose(verbose = True):
    state0 = (0, 0, 0, 0, 0, 0, 0, 0, 0)
    while True:
        state1 = player_move_random(1, state0)
        if is_winner(1, state1):
            if verbose: print("\033[1;31;40m player 1 wins \n")
            return -1
        if is_finished(state1):
            if verbose: print("\033[1;33;40m draw \n")
            return 0
        state2 = player_move_never_lose(2, state1)
        if is_winner(2, state2):
            if verbose: print("\033[1;34;40m player 2 wins \n")
            return 1
        if is_finished(state2):
            if verbose: print("\033[1;33;40m draw \n")
            return 0
        # reset to iterate again
        state0 = state2
  

# iterate to get a value map (get a different value map depending on oponents strategy)
never_lose_wins = []

for i in range(10000):
    never_lose_win = random_versus_never_lose(False)
    never_lose_wins.append(never_lose_win)

never_lose_totals = [sum(never_lose_wins[0:i]) for i in range (1, len(never_lose_wins)+1)]
never_lose_averages = [never_lose_totals[i]/(i+1) for i in range(len(never_lose_totals))]
never_lose_averages.pop(0)

plt.plot(learner_averages, label = 'Average learner score')
plt.plot(never_lose_averages, label = 'Average never_lose player score')
plt.ylabel('Average Score')
plt.xlabel('Iteration')
plt.gca().legend(('Learner','Never-lose'))
plt.suptitle('Average scores against a random player over time')
plt.savefig('graphneverloselearner.pdf', bbox_inches='tight', type = 'pdf' )
plt.show()
