'''
Created on Aug 14, 2015
@author: topcat
'''
class Stack(object):
    """
    A stack implementation in Python. Uses Python list to hold stack elements.
    """
    def __init__(self):
        self._list = []
    
    def push(self, element):
        self._list.append(element)
    
    def pop(self):
        if len(self._list) == 0:
            return None
            
        index = len(self._list) - 1
        element = self._list[index]
        del self._list[index]
        return element
    
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
    
    def __str__(self):
        return '%s size [%s] elements %s' % (self.__class__.__name__, len(self), self._list)