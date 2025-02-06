from vacuum import *
import random


directions = ["east", "west", "north", "south"]
last_square_status = None
last_movement = None

def reflex_agent(percept):
    if percept:
        action = 'clean'
    else:
        action = 'east'
    return action

def random_agent(percept):
    if percept:
        action = 'clean'
    else:
        action =  random.choice(directions)
    return action

def state_agent(percept):
# allowed to remember:
    # what it has seen (dirty or clean square)
    # what it has done (which direction it has moved)

run(20,5000,state_agent)
print(many_runs(20, 50000, 1, random_agent))