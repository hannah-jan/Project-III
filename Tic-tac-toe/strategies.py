import random
from basicfunctions import next_states, is_winner, get_never_lose_score

# Player moves randomly into next state
def player_move_random(player, state):
    return random.choice(next_states(player, state))


# A good strategy: player first sees if they can win, then they block their opponent
# from winning and then if not they move in the order of enumerate2
def player_move_good(player, state):
    otherplayer = 3 - player
    moves = next_states(player, state)
    winning_states = [next_state for next_state in moves
                      if is_winner(player, next_state)]
    if winning_states:
        return random.choice(winning_states)
    moves_other = next_states(otherplayer, state)
    blocking_states = [
        next_state for (next_state, next_state_other)
        in zip(moves, moves_other)
        if is_winner(otherplayer, next_state_other)]
    if blocking_states:
        return random.choice(blocking_states)
    return moves[0]


# never_lose play, assuming opponent also plays never_lose
def player_move_never_lose(player, state):
    score, best_moves = get_never_lose_score(player, state)
    return random.choice(best_moves)      


# Learner play
def player_move_learner(player, state, value_map, verbose = True, explore = 0.1):
    # List all possible next moves
    next_moves = next_states(player, state)
    # List probabilities of winning corresponding to possible next moves 
    #(or 0.5 if no value assigned)
    next_moves_values = [value_map.get(i, 0.5) for i in next_moves]
    # Find the index of the move corresponding to the maximum value
    maxpos =  [i for i, v in enumerate(next_moves_values) if v == max(next_moves_values)]
    rand = random.random()
    # Randomly explore sometimes
    if rand < explore:
        if verbose: print("\033[1;32;40m expoloratory move \n")
        return random.choice(next_moves)
    # Otherwise return best move
    else:
        return next_moves[maxpos[0]]
    



