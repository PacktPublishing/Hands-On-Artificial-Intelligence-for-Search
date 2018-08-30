'''
@author: Devangini Patel

https://docs.python.org/2/tutorial/datastructures.html#using-lists-as-stacks
'''

#create a empty stack
stack = []

print "stack", stack

#add items to the stack
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)

print "stack", stack

#pop all the items out
while len(stack) > 0:
    item = stack.pop()
    print item
    
print "stack", stack