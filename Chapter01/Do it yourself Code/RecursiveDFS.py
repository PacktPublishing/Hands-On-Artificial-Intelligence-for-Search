'''
@author: Devangini Patel
'''

from State import State
from Node import Node


class RecursiveDFS():
    """
    This performs DFS search
    """
    def __init__(self):
        self.found = False
        
    
    def search(self):
        """
        This method performs the search
        """
        #get the initial state
        initialState = State()
        
        #create root node
        rootNode = Node(initialState)
        
        #perform search from root node
        self.DFS(rootNode)
        
        rootNode.printTree()
        
    
    def DFS(self, node):
        """
        This creates the search tree
        """
        if not self.found:
            print "-- proc --", node.state.path
            
            #check if we have reached goal state
            if node.state.checkGoalState():
                print "reached goal state"
                self.found = True
                
            else:
                #find the successor states from current state 
                childStates = node.state.successorFunction()
                
                #add these states as children nodes of current node
                for childState in childStates:
                    childNode = Node(State(childState))
                    node.addChild(childNode)
                    
                    self.DFS(childNode)
        
        
dfs = RecursiveDFS()
dfs.search()    