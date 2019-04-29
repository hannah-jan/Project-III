from basicfunctions import next_states, is_winner

"""
Create value maps for each of the three strategies: random, good, never-lose
"""

def update_value_map_good(value_map, player, move):
    otherplayer = 3 - player
    next_moves = next_states(otherplayer, move)
    if is_winner(player, move):
        value_map[player, move] = 1
    elif not next_moves:
        value_map[player, move] = 0
    else:
        if any(is_winner(otherplayer, next_move) for next_move in next_moves):
            # bad score if other player can win in the next move
            value_map[player, move] = -1
        else:
            # heuristic score which prefers center, corners, and edges
            # in that order
            scores = (.01, .001, .01, .001, .1, .001, .01, .001, .01)
            value_map[player, move] = sum(
                score for (val, score) in zip(move, scores) if val == player)
        for next_move in next_moves:
            if (otherplayer, next_move) not in value_map:
                update_value_map_good(value_map, otherplayer, next_move)


# get value of a particular move
# value = 1 if the move can force a win for player
#         0 if the move can force a draw but not a win for player
#        -1 if the move is a guaranteed loss for player
                
def update_value_map_never_lose(value_map, player, move):
    otherplayer = 3 - player
    next_moves = next_states(otherplayer, move)
    if is_winner(player, move):
        value_map[player, move] = 1
    elif not next_moves:
        value_map[player, move] = 0
    else:
        # assume other player tries to maximize their value
        for next_move in next_moves:
            if (otherplayer, next_move) not in value_map:
                update_value_map_never_lose(value_map, otherplayer, next_move)
        max_value = max(value_map[otherplayer, next_move]
                        for next_move in next_moves)
        # if other player wins, we lose, so our value is minus their value
        value_map[player, move] = -max_value


# random player scores all moves equally
def update_value_map_random(value_map, player, move):
    value_map[player, move] = 0
    if not is_winner(player, move):
        otherplayer = 3 - player
        for next_move in next_states(otherplayer, move):
            if (otherplayer, next_move) not in value_map:
                update_value_map_random(value_map, otherplayer, next_move)


def get_value_map(update_func):
    value_map = {}
    initial_state = (0, 0, 0, 0, 0, 0, 0, 0, 0)
    for move in next_states(1, initial_state):
        update_func(value_map, 1, move)
    return value_map


value_map_never_lose = get_value_map(update_value_map_never_lose)
value_map_random = get_value_map(update_value_map_random)
value_map_good = get_value_map(update_value_map_good)

