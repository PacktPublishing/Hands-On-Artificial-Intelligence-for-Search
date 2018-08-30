'''
@author: Devangini Patel
'''

from Node import Node
from State import State

initialState = State()
root = Node(initialState)

childStates = initialState.successorFunction()
for childState in childStates:
    childNode = Node(State(childState))
    root.addChild(childNode)
    
root.printTree()