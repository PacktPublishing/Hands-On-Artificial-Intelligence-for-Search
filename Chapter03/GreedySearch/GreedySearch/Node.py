'''
@author: Devangini Patel
'''

from NavigationData import *
import math

class Node:
    '''
    This class represents a node in the search tree
    '''
    
    def __init__(self, state, parentNode):
        """
        Constructor
        """
        self.state = state
        self.depth = 0
        self.children = []
        #self.parent = None
        self.setParent(parentNode)
        self.fringe = True
        #self.heuristic
        self.computeHeuristic()
        
        
    def setParent(self, parentNode):
        """
        This method adds a node under another node
        """
        if parentNode != None:
            parentNode.children.append(self)
            self.parent = parentNode
            self.depth = parentNode.depth + 1
        else:
            self.parent = None
        
    
    def printTree(self):
        """
        This method prints the tree
        """
        print self.depth , " - " , self.state.place
        for child in self.children:
            child.printTree()
            
            
    def printPath(self):
        """
        This method prints the path from initial state to goal state
        """
        if self.parent != None:
            self.parent.printPath()
        print "-> ", self.state.place
        
        
    def computeHeuristic(self):
        """
        This function computes the heuristic value of node
        """
        #find the distance of this state to goal state
        
        #goal location
        goalLocation = location["AI Lab"]
        #current location
        currentLocation = location[self.state.place]
        #difference in x coordinates
        dx = goalLocation[0] - currentLocation[0]
        #difference in y coordinates
        dy = goalLocation[1] - currentLocation[1]
        #distance
        distance = math.sqrt(dx ** 2 + dy ** 2)
        print "heuristic for", self.state.place, "=", distance
        self.heuristic = distance