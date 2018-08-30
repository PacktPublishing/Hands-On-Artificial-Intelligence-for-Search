'''
@author: Devangini Patel
'''

from Node import Node
from State import State


def performStackDFS():
    """
    This function performs DFS search using a stack
    """
    #create stack
    stack = []
    
    #create root node and add to stack 
    initialState = State()
    root = Node(initialState)
    stack.append(root)
    
    # check if there is something in stack to pop
    while len(stack) > 0:
        
        #pop top node
        currentNode = stack.pop()
        
        print "-- pop --", currentNode.state.path
        
        #check if this is goal state
        if currentNode.state.checkGoalState():
            print "reached goal state"
            break
            
        #get the child nodes 
        childStates = currentNode.state.successorFunction()
        for childState in childStates:
            childNode = Node(State(childState))
            currentNode.addChild(childNode)
        
        #in reverse order add node to stack
        for index in range(len(currentNode.children) - 1, -1, -1):
            stack.append(currentNode.children[index])
    
    
    #print tree
    print "----------------------"
    root.printTree()
    
performStackDFS()