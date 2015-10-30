'''
Created on Oct 29, 2015
@author: hari
'''
from coils.trees.heap import Heap
from functools import total_ordering

@total_ordering
class PriorityQueueEntry(object):
    '''
    An entry in the priority Q is made up of an item and its priority. priority can be anything but must
    be comparable. 
    '''
    __slots__ = 'item', 'priority'
    def __init__(self, item = None, priority = None):
        if item == None:#cannot waste slots
            raise ValueError('Priority Q entry item cannot be None')
        if priority == None:
            raise ValueError('Priority Q entry priority cannot be None')
        
        self.item = item
        self.priority = priority
    
    def __eq__(self, other_entry):
        if other_entry is None:
            return False
            
        return self.priority == other_entry.priority
            
    def __lt__(self, other_entry): 
        if other_entry is None:
            return False
        
        return self.priority < other_entry.priority

class PriorityQueue(object):
    '''
    Priority Q based on Heaps. You can set min heap of max heap. Default is Max Heap.
    1) Iterating yields (item, priority) tuples
    '''
    
    def __init__(self, reverse_priority = False):
        '''
        creates a priority queue such that priority 10 is processed first than priority 2. If you want
        to reverse this set reverse_priority so that item with priority 2 is processed first 
        '''
        self._heap = Heap(min_heap =  reverse_priority)#create the heap as needed. Default Max heap
    
    def add_item(self, item = None, priority = None):
        if item == None:
            return #we are not wasting time
        
        self._heap.add_item(PriorityQueueEntry(item = item, priority = priority))
    
    def get(self):
        priority_q_entry = self._heap.get()
        if priority_q_entry == None:
            return None
        return priority_q_entry.item
    
    def __len__(self):
        return self._heap.heap_size
    
    def __iter__(self):
        for priority_q_entry in self._heap:
            yield (priority_q_entry.item, priority_q_entry.priority)