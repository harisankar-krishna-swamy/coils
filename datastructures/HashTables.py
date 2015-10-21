'''
Created on Oct 21, 2015
@author: hari
This borrows MAD hashing and structure from HashTable from DataStructures in Python By GoodRich and Tammasia. 
A hash table takes a key k (you decide for the object) and the object itself. We hash the key and get a bucket 
number B. This is just an index to a table. A bucket can implemented as a list (here) or any other ds you like.
A Bucket, which is a list masquerading as a python dict, holds multiple objects which happened to have
keys k1 and k2 that mapped into the same bucket B.    
'''
from datastructures.LinkedList import LinkedList
from datastructures.common import KeyValuePair

class HashBucketList(object):
    '''
    A hash bucket is used to hold objects that hash to the same value in a hash table. This is hash bucket
    using a list. This masquerades as a python dist in code where it is used.
    '''
    def __init__(self):
        self._list_of_kv_pairs = LinkedList() #we use our linked list!
    
    def __len__(self):
        return self._list_of_kv_pairs.length # TODO: must implement __len__ for LinkedList!
    
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
    #