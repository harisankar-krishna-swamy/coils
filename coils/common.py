'''
Created on Oct 21, 2015
@author: hari
'''
from functools import total_ordering

@total_ordering
class KeyValuePair:# Save space in key value pair by using slots for all client programs using this?! 
    __slots__ = 'key', 'value'# python created descriptors for the slots

    def __init__(self, key = None, value = None):
        self.key = key
        self.value = value
            
    def __eq__(self, other_kv_pair):
        if other_kv_pair is None:
            return False
        
        return self.key == other_kv_pair.key 
    
    def __lt__(self, other_kv_pair):
        if other_kv_pair is None:
            return False
        return self.key < other_kv_pair.key
    
    def __str__(self):
        return '%s key[%s] value[%s]' % (self.__class__.__name__,
                                         str(self.key), str(self.value))