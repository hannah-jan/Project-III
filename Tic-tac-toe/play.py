import itertools
from strategies import player_move_random, player_move_good, player_move_never_lose, player_move_learner
from basicfunctions import is_finished, is_winner, state_str
value_map = {}

# Let player make a move using either random, good or never_lose strategy (not learner)

def next_play(player, state, strategy, verbose=False):
    next_state = strategy(player, state)
    if verbose: print(state_str(next_state) + "\n-----")
    if is_winner(player, next_state):
        if verbose: print("player %i wins" % player)
        return (player, None)
    elif is_finished(next_state):
        if verbose: print("draw")
        return (0, None)
    else:
        return (None, next_state)



# Play a game of two strategies against each other
# returns 1 if first player wins, -1 if second player wins, 0 if draw
def play(strategy1, strategy2, verbose=False):
    state0 = (0, 0, 0, 0, 0, 0, 0, 0, 0)
    while True:
        outcome1, state1 = next_play(1, state0, strategy1, verbose)
        if outcome1 is not None:
            return outcome1
        outcome2, state2 = next_play(2, state1, strategy2, verbose)
        if outcome2 is not None:
            return outcome2
        state0 = state2
        
        
# random can beat good if random starts
def test_random_good():
    assert(any(play(player_move_random, player_move_good, verbose=True) == 1
               for i in itertools.count()))


# random can beat good if random starts
def test_random_never_lose():
    assert(all(play(player_move_never_lose, player_move_never_lose, verbose=True) != 1
               for i in itertools.count()))


# never_lose can beat good if never_lose starts
def test_never_lose_good():
    assert(any(play(player_move_never_lose, player_move_good, verbose=True) == 1
               for i in itertools.count()))


# never_lose cannot beat good if good starts
def test_good_never_lose():
    assert(all(play(player_move_good, player_move_never_lose) == 0
               for i in range(1000)))


# random cannot beat good if good starts
def test_good_random():
    assert(all(play(player_move_good, player_move_random) != 2
               for i in range(1000)))

# never_lose players always draw
def test_never_lose():
    assert(all(play(player_move_never_lose, player_move_never_lose) == 0
               for i in range(1000)))



#test_random_never_lose()
#test_random_good()
#test_never_lose_good()
#test_good_never_lose()
#test_good_random()


