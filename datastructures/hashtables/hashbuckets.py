'''
Created on Oct 23, 2015
@author: hari
'''
from datastructures.lists.singly_linked_list import LinkedList
from datastructures.common import KeyValuePair
from datastructures.trees.BST import BinarySearchTree
from datastructures.trees import splaytree
from datastructures.trees.splaytree import BinarySplayTree
import collections

class LinkedListHashBucket(collections.MutableMapping):
    '''
    A hash bucket is used to hold objects that 'hash to the same value' (collision) in a hash table. 
    This is hash a bucket using a LIST. This masquerades as a python dict in code where it is used.
    
    Note: HASHBUCKET ITERATION YIELDS KEYS. not the key value pairs in the bucket. 
    '''
    def __init__(self):
        self._list_of_kv_pairs = LinkedList() #we use our linked list!
    
    def __len__(self):
        '''
        The number of entries in the bucket!
        '''
        return self._list_of_kv_pairs.length
    
    def get(self, key, default = None):
        '''
        Get object associated with a key and on key miss return specified default. This is there in 
        Python dict and this class masquerades as dict, so we implement it.
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

class BSTHashBucket(collections.MutableMapping):
    '''
    A hash bucket is used to hold objects that hash to the same value in a hash table. This is hash 
    bucket using a binary search tree. This masquerades as a python dict in code where it is used.
    Since bst is used as bucket datastructure, searches take O log(n) rather than O n
    
    Note: HASHBUCKET ITERATION YIELDS KEYS. not the key value pairs in the bucket. 
    '''
    def __init__(self):
        self._bst = BinarySearchTree()
    
    def __len__(self):
        '''
        The number of elements in the hash bucket
        '''
        return self._bst.node_count
    
    def get(self, key, default = None):
        '''
        Get object associated with a key and on key miss return specified default. This is 
        there in Python dict and this class masquerades as dict, we implement it.
        '''
        try:
            value = self[key]
            return value
        except KeyError:
            return default            
    
    def __getitem__(self, key):
        value = self._bst.find(key)
        if value == None:
            raise KeyError('Key Error: %s ' % repr(key))
        return value
        
    def __delitem__(self, key):
        if self._bst.has_key(key):
            self._bst.remove(key)
        else:
            raise KeyError('Key Error: %s ' % repr(key))
        
    def __setitem__(self, key, obj):
        if self._bst.has_key(key):
            self._bst.replace(key, obj)
        else:
            self._bst.insert(key, obj)
            
    def __iter__(self):
        for key, value in self._bst.inorder_traversal_with_stack():
            yield key

class SplayedHashBucket(collections.MutableMapping):
    '''
    A hash bucket is used to hold objects that hash to the same value in a hash table. 
    This is hash bucket using a splay tree. This masquerades as a python dict in code 
    where it is used. Since splat tree is used lookups on avg take Olog(n)
    
    Note: HASHBUCKET ITERATION YIELDS KEYS. not the key value pairs in the bucket. 
    '''
    def __init__(self):
        self._st = BinarySplayTree()
    
    def __len__(self):
        return self._st.node_count
    
    def get(self, key, default = None):
        '''
        Get object associated with a key and on key miss return specified default. This is 
        there in Python dict and this class masquerades as dict, we implement it.
        '''
        try:
            value = self[key]
            return value
        except KeyError:
            return default            
    
    def __getitem__(self, key):
        value = self._st.find(key)
        if value == None:
            raise KeyError('Key Error: %s ' % repr(key))
        return value
        
    def __delitem__(self, key):
        if self._st.has_key(key):
            self._st.remove(key)
        else:
            raise KeyError('Key Error: %s ' % repr(key))
        
    def __setitem__(self, key, obj):
        if self._st.has_key(key):
            self._st.replace(key, obj)
        else:
            self._st.insert(key, obj)
            
    def __iter__(self):
        for key, value in self._st.inorder_traversal_with_stack():
            yield key