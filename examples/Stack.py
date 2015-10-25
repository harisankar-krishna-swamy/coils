'''
Created on Oct 25, 2015
@author: hari
'''
from coils.stackNqueues.Stack import Stack

if __name__ == '__main__':
    stack = Stack()
    # count items
    print 'Stack items count: %s' % str(stack.size)
    #Push items
    stack.push(element = 1)
    stack.push(element = 2)
    stack.push(element = 3)
    stack.push(element = 4)
    stack.push(element = 5)
    stack.push(element = 6)
    #top
    print 'Stack top is %s' % str(stack.top)
    #pop
    popped = stack.pop()
    print 'Popped item is %s' % str(popped)
    #iterate over the stack popping items one by one
    print 'Iterate over stack popping items'
    for item in stack:
        print 'item %s' % str(item)
        
