'''
Created on Oct 21, 2015
@author: hari
'''
from functools import total_ordering

@total_ordering
class KeyValuePair:# Save space in key value pair by using slots? 
    __slots__ = '_key', '_value'
    def __init__(self, key = None, value = None):
        self._key = key
        self._value = value
    @property
    def key(self):
        return self._key
    @property
    def value(self):
        return self._value
    @key.setter
    def key(self, new_key):
        self._key = new_key
    @value.setter
    def value(self, new_value):
        self._value = new_value
    def __eq__(self, other_kv_pair):
        return self._key == other_kv_pair.key 
    def __lt__(self, other_kv_pair):
        return self._key < other_kv_pair.key