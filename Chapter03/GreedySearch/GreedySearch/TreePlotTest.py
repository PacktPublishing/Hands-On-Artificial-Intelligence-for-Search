'''
@author: Devangini Patel

Reference http://www.graphviz.org/content/attrs

use ctrl + w is to close the current open window
'''
import pydot 
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

#create graph object
graph = pydot.Dot(graph_type='graph', dpi = 300)


#create and add root node
rootNode = pydot.Node("0 Root", style="filled", fillcolor = "#00ee11", xlabel = "0")
graph.add_node(rootNode)

for i in range(3):
    #create node and add node
    childNode = pydot.Node("Child" , style="filled", \
        fillcolor = "#ee0011", xlabel = "1")
    graph.add_node(childNode)
    
    #create edge between two nodes
    edge = pydot.Edge(rootNode, childNode)
    #add the edge to graph
    graph.add_edge(edge)

#show the diagram
graph.write_png('graph.png')
img=mpimg.imread('graph.png')
plt.imshow(img)
plt.axis('off')
mng = plt.get_current_fig_manager()
mng.window.state('zoomed')
plt.show()
