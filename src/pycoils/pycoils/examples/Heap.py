'''
Created on Oct 25, 2015

@author: hari
'''
from __future__ import print_function
from builtins import str
from pycoils.trees.heap import Heap

if __name__ == '__main__':
    # A max heap. for a min heap use minHeap = True (is default)
    max_heap = Heap(min_heap = False)
    
    elements = [0, 4, 3, 2, 5, 1, 6]
    print('Adding elements to heap: %s' % elements)
    for element in elements:
        max_heap.add_item(element)
        
    print('Getting element from max heap')
    element = max_heap.get()
    print('Top element from heap is %s' % str(element))
    
    print('Iterating through heap') 
    for element in max_heap:
        print('heap popped %s' % str(element))
    
      