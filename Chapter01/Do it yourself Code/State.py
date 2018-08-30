'''
@author: Devangini Patel
'''

'''
This script solves the file search application using Depth First Search
'''

import os  

class State:
    '''
    This class retrieves state information for search application
    '''
    
    def __init__(self, path = None):
        if path == None:
            #create initial state
            self.path = self.getInitialState()
        else:
            self.path = path
    
    def getInitialState(self):
        """
        This method returns the current directory
        """
        initialState = os.path.dirname(os.path.realpath(__file__))
        return initialState


    def successorFunction(self):
        """
        This is the successor function. It generates all the possible
         paths that can be reached from current path.
        """
        if os.path.isdir(self.path):
            return [os.path.join(self.path, x) for x in sorted(os.listdir(self.path))]
        else:
            return []
        
        
    def checkGoalState(self):
        """
        This method checks whether the path is goal state 
        """ 
        #check if it is a folder
        if os.path.isdir(self.path):
            return False
        else:
            #check if file contains text
            with open(self.path) as searchFile:
                for line in searchFile:
                    if "dfs notes" in line:
                        return True
            return False
