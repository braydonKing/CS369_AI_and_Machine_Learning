INITIAL_STATE = '.........'

def successor(state, index, player):
    # ls = list(state)
    # ls[index] = player
    #
    # return ''.join(ls)
    return state[:index] + player + state[index+1:]

def legal_moves(state):
    return [i for i in range(len(state)) if state[i] == '.']

def winner(state):
    lines = [[0,1,2], [3,4,5], [6,7,8],
             [0,3,6] ,[1,4,7],[2,5,8],
             [0,4,5],[2,4,6]]
    for line in lines:
       if state[line[0]] == state[line[1]] == state[line[2]]:
           player = state[line[0]]
           if player=='X':
               return 1
           if player=='O':
                return -1
    return 0

def min_value(state):
    """
    Returns the value of state if it is min (O)'s turn.
    """
    if winner(state) != 0:
        return winner(state)
    if not legal_moves(state):
        return winner(state)
    best_value = 2
    for m in legal_moves(state):
        s = successor(state, m, 'O')
        value = max_value(s)
        if value < best_value:
            best_value = value
    return best_value

def max_value(state):
    """
    Returns the value of state if it is max (X)'s turn.
    """
    if winner(state) != 0:
        return winner(state)
    if not legal_moves(state):
        return winner(state)
    best_value = -2
    for m in legal_moves(state):
        s = successor(state, m, 'X')
        value = min_value(s)
        if value > best_value:
            best_value = value
    return best_value

def value(state,player,better,bad):
    """
    Returns the value of state if it is player's turn.
    :param player:
    :param better: takes two value and returns True if the first is better
    :param bad: value worse than anything we will see
    """
    if winner(state) != 0:
        return winner(state)
    if not legal_moves(state):
        return winner(state)
    best_value = bad
    for m in legal_moves(state):
        s = successor(state, m, player)
        if player == 'X':
            v = value(s,'O', lambda a, b: a<b, 2)
        else:
            v = value(s,'X', lambda a, b: a>b, 2)
        if better(value, best_value):
            best_value = value
    return best_value
