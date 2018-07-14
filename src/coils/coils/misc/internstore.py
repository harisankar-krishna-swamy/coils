'''
Created on Nov 6, 2015
@author: hari
'''
from builtins import object
from coils.hashtables.HashTables import SeperateChainHashTable
import weakref

class InternStore(object):
    '''
    Several objects of a class can have the same internal state. Holding all these objects 
    in memory is a waste. InternStore holds all these same internal state objects to 
    refer to a single weak reference object. For this to work all the objects you send to the
    intern store must be hashable. Hash of the objects must return the same hash for the 
    same internal states. 
    '''
    def __init__(self):
        self._store = SeperateChainHashTable()
    
    def intern(self, obj):
        '''
        an object obj is checked against the intern store and if there is an existing weakref
        with hash = hash(obj) then that instance is returned. If no entry is found a weak 
        reference to obj is created and stored.
        '''
        if obj == None:
            return None
        
        class_of_obj = type(obj)
        map_of_class_to_weak_refs_of_obj = self._store.get(class_of_obj, default = None)
        if map_of_class_to_weak_refs_of_obj is None:
            map_of_class_to_weak_refs_of_obj = weakref.WeakValueDictionary()
            self._store[class_of_obj] = map_of_class_to_weak_refs_of_obj
        
        weak_ref_to_obj = map_of_class_to_weak_refs_of_obj.get(obj, default = None)
        strong_ref_obj = None 
        
        if weak_ref_to_obj is not None:
            strong_ref_obj = weak_ref_to_obj
            return strong_ref_obj
        else:
            map_of_class_to_weak_refs_of_obj[obj] = obj 
            strong_ref_obj = obj
            return strong_ref_obj