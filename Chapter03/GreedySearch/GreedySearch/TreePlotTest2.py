'''
@author: Devangini Patel
'''

from Node import Node
from State import State
from TreePlot import TreePlot

initialState = State()
root = Node(initialState)

childStates = initialState.successorFunction()
for childState in childStates:
    childNode = Node(State(childState))
    root.addChild(childNode)
    

treeplot = TreePlot()
treeplot.generateDiagram(root, root)