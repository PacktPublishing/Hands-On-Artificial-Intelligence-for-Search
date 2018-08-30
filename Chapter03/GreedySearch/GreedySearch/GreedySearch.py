'''
@author: Devangini Patel
'''
from State import State
from Node import Node
import Queue
from TreePlot import TreePlot
    

def performGreedySearch():
    """
    This method performs greedy best first search
    """
    
    #create queue
    pqueue = Queue.PriorityQueue()
    
    #create root node
    initialState = State()
    #parent node of root is None
    root = Node(initialState, None)
    
    #show the search tree explored so far
    treeplot = TreePlot()
    treeplot.generateDiagram(root, root)
    
    #add to priority queue
    pqueue.put((root.heuristic, root))
    
    #check if there is something in priority queue 
    while not pqueue.empty(): 
        
        #get front node from the priority queue
        _, currentNode = pqueue.get()
        
        #remove from the fringe
        #currently selected for exploration
        currentNode.fringe = False
        
        print "-- current --", currentNode.state.place
        
        #check if this is goal state
        if currentNode.state.checkGoalState():
            print "reached goal state"
            #print the path
            print "----------------------"
            print "Path"
            currentNode.printPath()
            
            #show the search tree explored so far
            treeplot = TreePlot()
            treeplot.generateDiagram(root, currentNode)
            break
            
        #get the child nodes 
        childStates = currentNode.state.successorFunction()
        for childState in childStates:
            
            #create node 
            #and add to tree
            childNode = Node(State(childState), currentNode)
            
            #add to priority queue
            pqueue.put((childNode.heuristic, childNode))
            
        #show the search tree explored so far
        treeplot = TreePlot()
        treeplot.generateDiagram(root, currentNode)
                
    #print tree
    print "----------------------"
    print "Tree"
    root.printTree()
    
performGreedySearch()