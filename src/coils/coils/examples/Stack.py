'''
Created on Oct 25, 2015
@author: hari
'''
from __future__ import print_function
from builtins import str
from coils.stackNqueues.stack import Stack

if __name__ == '__main__':
    stack = Stack()
    # count items
    print('stack items count: %s' % str(stack.size))
    #Push items
    stack.push(item = 1)
    stack.push(item = 2)
    stack.push(item = 3)
    stack.push(item = 4)
    stack.push(item = 5)
    stack.push(item = 6)
    #top
    print('stack top is %s' % str(stack.top))
    #pop
    popped = stack.pop()
    print('Popped item is %s' % str(popped))
    #iterate over the stack popping items one by one
    print('Iterate over stack popping items')
    for item in stack:
        print('item %s' % str(item))
        
