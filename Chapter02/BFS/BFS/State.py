'''
@author: Devangini Patel
'''

from GraphData import *

class State:
    '''
    This class retrieves state information for social connection feature
    '''
    
    def __init__(self, name = None):
        if name == None:
            #create initial state
            self.name = self.getInitialState()
        else:
            self.name = name
    
    def getInitialState(self):
        """
        This method returns me.
        """
        initialState = "Dev"
        return initialState


    def successorFunction(self):
        """
        This is the successor function. It finds all the persons connected to the
        current person
        """
        return connections[self.name]
        
        
    def checkGoalState(self):
        """
        This method checks whether the person is Jill.
        """ 
        #check if the person's name is Jill
        return self.name == "Jill"