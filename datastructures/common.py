'''
Created on Oct 21, 2015
@author: hari
'''
from functools import total_ordering

@total_ordering
class KeyValuePair:# Save space in key value pair by using slots? python created descriptors for the slots
    __slots__ = 'key', 'value'
    
    def __init__(self, key = None, value = None):
        self.key = key
        self.value = value
            
    def __eq__(self, other_kv_pair):
        return self.key == other_kv_pair.key 
    def __lt__(self, other_kv_pair):
        return self.key < other_kv_pair.key