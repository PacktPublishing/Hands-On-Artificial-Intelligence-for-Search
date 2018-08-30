'''
@author: Devangini Patel
'''
import pydot 
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

class TreePlot:
    """
    This class creates tree plot for search tree
    """
    
    def __init__(self):
        """
        Constructor
        """
        self.graph = pydot.Dot(graph_type='graph', dpi = 300)
        self.index = 0
        
    
    def createGraph(self, node, currentNode):
        """
        This method creates pydot graph from search tree
        Similar to printTree() of Node class
        """
        
        if node.state.place == currentNode.state.place:
            color = "#ee0011"
        elif node.fringe:
            color = "#0011ee"
        else:
            color = "#00ee11"
            
        #create node
        parentGraphNode = pydot.Node(str(self.index) + " " + \
            node.state.place, style="filled", \
            fillcolor = color, xlabel = node.heuristic)
        self.index += 1
        
        #add node
        self.graph.add_node(parentGraphNode)
        
        #call this method for child nodes
        for childNode in node.children:
            childGraphNode = self.createGraph(childNode, currentNode)
            
            #create edge
            edge = pydot.Edge(parentGraphNode, childGraphNode)
            
            #add edge
            self.graph.add_edge(edge)
            
        return parentGraphNode
        
    
    def generateDiagram(self, rootNode, currentNode):
        """
        This method generates diagram
        """
        self.createGraph(rootNode, currentNode)
        
        #show the diagram
        self.graph.write_png('graph.png')
        img=mpimg.imread('graph.png')
        plt.imshow(img)
        plt.axis('off')
        mng = plt.get_current_fig_manager()
        mng.window.state('zoomed')
        plt.show()
