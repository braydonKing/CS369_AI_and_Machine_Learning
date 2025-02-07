from html.parser import commentclose

from vacuum import *
import random

"""
Author: <Braydon King>

Simple vacuum AI's. No specific algorithm used
"""


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
    # counters okay??

    global last_movement,last_square_status,switch,count,side_direction

    if percept: #if dirty, clean square. Otherwise, move 'north' or 'south'.
        action = 'clean'
        last_square_status = percept
    elif not percept and switch == 1:
        action = 'north'
    elif not percept and switch == -1:
        action = 'south'

    if last_square_status == False and percept == False: #if last square status was clean and the current square status is clean, the bot is essentially stuck on a wall.
        if count<15:  #assume bot gets in "lucky" position with less walls and chooses a predictable direction 'west'.
            action = 'west'
        else: #FAILSAFE creates random action if bot is stuck/cant find dirt.
            action = random.choice(directions)

        if count>500: #reset counter so it can keep trying horizontal direction 'west' on occasion.
            count = 0

        switch = switch * -1 #switch for vertical directions
        count += 1 #count to track random or predictable movement

    last_square_status = percept #set last square status

    return action


#run(20,5000,state_agent)
print(many_runs(20, 50000, 10, state_agent))