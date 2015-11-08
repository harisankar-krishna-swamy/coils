'''
Created on Nov 8, 2015

@author: hari
'''
from functools import total_ordering

class WrappedString(object):
    '''
    This class simply wraps around python string.
    '''
    def __init__(self, string = 'default string'):
        self._string = string
    
    @property
    def wrapped_string(self):
        return self._string
    
    def __eq__(self, other):
        if other == None or type(other) != type(self):
            return False
        
        return self._string == other.wrapped_string
    
    def __lt__(self, other):
        if other == None or type(other) != type(self):
            return False
        
        return self._string < other.wrapped_string
    
    def __str__(self, *args, **kwargs):
        return self._string
    
    def __hash__(self, *args, **kwargs):
        return hash(self._string)