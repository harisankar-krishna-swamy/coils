'''
Created on Oct 23, 2015
@author: hari
'''
from datastructures.lists.LinkedList import LinkedList
from datastructures.common import KeyValuePair

class LinkedListHashBucket(object):
    '''
    A hash bucket is used to hold objects that hash to the same value in a hash table. This is hash bucket
    using a list. This masquerades as a python dict in code where it is used.
    
    Note: HASHBUCKET ITERATION YIELDS KEYS. not the key value pairs in the bucket. 
    '''
    def __init__(self):
        self._list_of_kv_pairs = LinkedList() #we use our linked list!
    
    def __len__(self):
        return self._list_of_kv_pairs.length
    
    def get(self, key, default = None):
        '''
        Get object associated with a key and on key miss return specified default. This is there in Python dict and this class
        masquerades as dict, we implement it.
        '''
        try:
            value = self[key]
            return value
        except KeyError:
            return default            
    
    def __getitem__(self, key):
        for kv_pair in self._list_of_kv_pairs:
            if kv_pair.key == key:
                return kv_pair.value
        raise KeyError('Key Error: %s ' % repr(key))
    
    def __delitem__(self, key):
        for kv_pair in self._list_of_kv_pairs:
            if kv_pair.key == key:
                self._list_of_kv_pairs.remove(kv_pair)
                return    
        raise KeyError('Key Error: %s ' % repr(key))
    
    def __setitem__(self, key, obj):
        for kv_pair in self._list_of_kv_pairs:
            if kv_pair.key == key:
                kv_pair.value = obj
                return    
        self._list_of_kv_pairs.append(KeyValuePair(key = key, value = obj))
  
    def __iter__(self):
        for kvpair in self._list_of_kv_pairs:
            yield kvpair.key