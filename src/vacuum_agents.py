from vacuum import *
import random

def reflex_agent(percept):
    if percept == True:
        action = 'clean'
    if percept == False:
        action = 'east'

    return action

def random_agent(percept):
    directions = ["east", "west", "north", "south"]

    if percept == True:
        action = 'clean'
    if percept == False:
        action =  random.choice(directions)
    return action

def state_agent():
    
    return 0

percept=None
run(20, 5000,random_agent)