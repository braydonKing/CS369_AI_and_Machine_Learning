from vacuum import *
import random


directions = ["east", "west", "north", "south"]
last_square_status = True
last_movement = None
switch = 1
count = 0
side_direction = 1
steps = 50000

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
    global last_movement,last_square_status,switch,count,side_direction

    if percept:
        action = 'clean'
        last_square_status = percept
    elif not percept and switch == 1:
        action = 'north'
    elif not percept and switch == -1:
        action = 'south'

    if last_square_status == False and percept == False:
        if count<250:
            action = 'west'

        else:
            action = 'east'

        if count>15:
            action = random.choice(directions)

        if count>500:
            count = 0

        switch = switch * -1
        count += 1
        #print(count)

    last_square_status = percept
    #print(last_square_status)
    #print(count)
    return action


#run(20,5000,state_agent)
print(many_runs(20, steps, 10, state_agent))