'''
@author: Devangini Patel
'''

class Node:
    '''
    This class represents a node in the search tree
    '''
    
    def __init__(self, state):
        """
        Constructor
        """
        self.state = state
        self.depth = 0
        self.children = []
        self.parent = None
        
        
    def addChild(self, childNode):
        """
        This method adds a node under another node
        """
        self.children.append(childNode)
        childNode.parent = self
        childNode.depth = self.depth + 1
        
    
    def printTree(self):
        """
        This method prints the tree
        """
        print self.depth , " - " , self.state.name
        for child in self.children:
            child.printTree()
 
    
    def printPath(self):
        """
        This method prints the path from initial state to goal state
        """
        if self.parent != None:
            self.parent.printPath()
        print "-> ", self.state.name