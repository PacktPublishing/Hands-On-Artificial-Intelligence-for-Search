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
        #self.parent
        self.setParent(parentNode)
        self.fringe = True
        #self.costFromRoot
        self.computeCost()
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
        
        
    def computeDistance(self, location1, location2):
        """
        This method computes distance between two places
        """
        #difference in x coordinates
        dx = location1[0] - location2[0]
        #difference in y coordinates
        dy = location1[1] - location2[1]
        #distance
        distance = math.sqrt(dx ** 2 + dy ** 2)
        return distance
    
        
    def computeCost(self):
        """
        This method computes distance of current node from root node
        """
        
        if self.parent != None:
            #find distance from current node to parent
            distance = self.computeDistance(location[self.state.place], \
                location[self.parent.state.place])
            #cost = parent cost + distance
            self.costFromRoot = self.parent.costFromRoot + distance
        else:
            self.costFromRoot = 0
    
        
    def computeHeuristic(self):
        """
        This function computes the heuristic value of node
        """
        
        #find the distance of this state from goal state
        goalLocation = location["AI Lab"]
        currentLocation = location[self.state.place]
        distanceFromGoal = self.computeDistance(goalLocation, currentLocation)
        
        #add them up to form heuristic value
        heuristic = self.costFromRoot + distanceFromGoal
        
        print "heuristic for", self.state.place, "=", self.costFromRoot, distanceFromGoal, heuristic
        self.heuristic = heuristic
