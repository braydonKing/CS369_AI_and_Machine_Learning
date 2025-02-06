from vacuum import *
import random


directions = ["east", "west", "north", "south"]
last_square_status = True
last_movement = None
switch = 1
count = 0

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
    #allowed to remember:
    # what it has seen (dirty or clean square)
    # what it has done (which direction it has moved)
    global last_movement,last_square_status,switch,count

    if percept:
        action = 'clean'
        last_square_status = percept
    elif not percept and switch == 1:
        action = 'north'
    elif not percept and switch == -1:
        action = 'south'

    if last_square_status == False and percept == False:
        if count>100:
            action = 'west'
            switch = switch * -1
        else:
            action = 'east'
            switch = switch * -1
        if count>150:
            count = 0
        count += 1
        #print(count)

    last_square_status = percept
    #print(last_square_status)
    #print(count)
    return action


#run(20,5000,state_agent)
print(many_runs(20, 50000, 3, state_agent))