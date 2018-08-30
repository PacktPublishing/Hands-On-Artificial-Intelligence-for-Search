'''
@author: Devangini Patel
'''
from State import State
import os
import pprint

initialState = State()
print "initialState", initialState.path

interState = State(os.path.join(initialState.path, "d2", "d21"))
goalState = State(os.path.join(initialState.path, "d2", "d21", "f211.txt"))

print "interState", interState.path
print "goalState", goalState.path

pp = pprint.PrettyPrinter(indent=4)
print "successor of ", initialState.path, ":" 
pp.pprint(initialState.successorFunction())
print "successor of ", interState.path, ":"
pp.pprint(interState.successorFunction())

print initialState.path , "is goal state =", initialState.checkGoalState()
print interState.path, "is goal state =", interState.checkGoalState()
print goalState.path, "is goal state =", goalState.checkGoalState()

