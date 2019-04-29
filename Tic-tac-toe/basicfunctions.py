import functools

win_locations = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # horizontal
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # vertical
    (0, 4, 8), (2, 4, 6)              # diagonal
    ]

# Middle first, then corners then elsewhere
def enumerate2(state):
    return [(loc, state[loc]) for loc in (4, 0, 2, 6, 8, 1, 3, 5, 7)]

# Returns all possible next states for player in order of enumerate2
def next_states(player, state):
    return [
        tuple((value if location != next_location else player)
              for location, value in enumerate(state))
        for next_location, value2 in enumerate2(state)
        if value2 == 0]

# Checks if player is a winner in state
def is_winner(player, state):
    return any(all(state[location] == player for location in locations)
               for locations in win_locations)

# Checks if grid is full
def is_finished(state):
    return all(value != 0 for value in state)

# Converts numbers into noughts and crosses   
def value_str(val):
    return ' xo'[val]

# Converts string to grid
def state_str(state):
    rows = [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
    return '\n'.join(' '.join([value_str(state[i]) for i in row])
                     for row in rows)


# return (score, best_move) where
# score  = 1 if the state leads to a win for player
#          0 if the state leads to a draw for player
#         -1 if the state leads to a loss for player
# best_moves = tuple of all moves the player can take to achieve this score
#              (empty if the state is a final state)
    
@functools.lru_cache(maxsize=10000)
def get_never_lose_score(player, state):
    moves = next_states(player, state)
    otherplayer = 3 - player
    if is_winner(otherplayer, state):
        return (-1, ())
    elif not moves:
        return (0, ())
    else:
        # find all moves that minimize the score for the other player
        scores = [(get_never_lose_score(otherplayer, move)[0], move)
                  for move in moves]
        min_score = min(score for (score, _) in scores)
        return (-min_score, tuple(best_move for (score, best_move) in scores
                                  if score == min_score))