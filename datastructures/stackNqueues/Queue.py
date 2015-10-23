'''
Created on Aug 14, 2015
@author: hari
'''
class Queue(object):
    """
    Implementation of queue in Python using list.
    """
    def __init__(self):
        self._list = []
    
    def enqueue(self, element):
        self._list.append(element)
    
    def dequeue(self):
        if len(self._list) == 0:
            return None
            
        element = self._list[0]
        del self._list[0]
        return element
    
    def __len__(self):
        return len(self._list)
    
    def __iter__(self):
        return self
    
    def next(self):
        if len(self._list) != 0:
            return self.dequeue()
        raise StopIteration
    
    @property
    def front(self):
        if len(self._list) == 0:
            return None
        return self._list[0]
    
    def __str__(self):
        return '%s size %s Q %s' % (self.__class__.__name__, len(self), self._list) 