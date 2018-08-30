'''
@author: Devangini Patel
'''
from NavigationData import *
import matplotlib.pyplot as plt
import pylab

#extract x, y, labels array from location dict
x = []
y = []
labels = []
areas = []
for key, value in location.iteritems():
    labels.append(key)
    x.append(value[0])
    y.append(value[1])
    areas.append(100)

#plot the places with labels
fig, ax = plt.subplots()
ax.scatter(x, y, areas)
"""
for i in range(len(x)):
    ax.annotate(labels[i], (x[i] - 2,y[i] - 0.2), horizontalalignment='left', \
        verticalalignment='top', fontsize=24) 
"""

#plot the connections between places
for key in connections.iterkeys():
    for value in connections[key]:
        x = []
        y = []
        x.append(location[key][0])
        x.append(location[value][0])
        y.append(location[key][1])
        y.append(location[value][1])
        plt.plot(x, y)

pylab.xlim([0,8])   
pylab.ylim([-1,9]) 

mng = plt.get_current_fig_manager()
mng.window.state('zoomed')
plt.axis('equal')
plt.show()