'''
Created on Aug 14, 2015
@author: topcat
'''
from builtins import object
class Stack(object):
    """
    A stack implementation in Python. Uses Python list to hold stack items.
    """
    def __init__(self):
        self._list = []
    
    def push(self, item):
        self._list.append(item)
    
    def pop(self):
        if len(self._list) == 0:
            return None
            
        index = len(self._list) - 1
        item = self._list[index]
        del self._list[index]
        return item
    
    def __len__(self):
        return len(self._list)
    
    @property
    def top(self):
        if len(self._list) > 0:
            return self._list[len(self._list) - 1]
        else:
            return None
    @property
    def size(self):
        return len(self._list)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        stack_item = self.pop()
        if stack_item == None:
            raise StopIteration
        return stack_item 
    
    def __str__(self):
        return '%s size [%s] items %s' % (self.__class__.__name__, len(self), self._list)