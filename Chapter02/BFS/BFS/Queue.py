'''
@author: Devangini Patel

Reference: https://docs.python.org/2/tutorial/datastructures.html#using-lists-as-queues
'''

#This script experiments with python queue data structure

from collections import deque

queue = deque([])
print queue

queue.append("1") 
queue.append("2") 
queue.append("3") 
queue.append("4") 

print queue

while len(queue) > 0:
    item = queue.popleft()  
    print item
    
print queue  
    