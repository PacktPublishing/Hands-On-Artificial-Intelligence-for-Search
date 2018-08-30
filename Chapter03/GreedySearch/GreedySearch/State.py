'''
@author: Devangini Patel
'''

from NavigationData import *

class State:
    '''
    This class retrieves state information for social connection feature
    '''
    
    def __init__(self, place = None):
        if place == None:
            #create initial state
            self.place = self.getInitialState()
        else:
            self.place = place
    
    def getInitialState(self):
        """
        This method returns source place
        """
        initialState = "Bus Stop"
        return initialState


    def successorFunction(self):
        """
        This is the successor function. It finds all the places connected to the
        current place
        """
        return connections[self.place]
        
        
    def checkGoalState(self):
        """
        This method checks whether the current place is AI Lab
        """ 
        #check if the place is AI Lab
        return self.place == "AI Lab"