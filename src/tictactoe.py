INITIAL_STATE = '.........'

def successor(state, index, player):
    # ls = list(state)
    # ls[index] = player
    #
    # return ''.join(ls)
    return state[:index] + player + state[index+1:]

def legal_moves(state):
    return [i for i in range(len(state)) if state[i] == '.']

