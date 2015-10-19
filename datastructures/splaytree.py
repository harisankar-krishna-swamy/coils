'''
Created on Oct 19, 2015
@author: hari
'''
from datastructures.BST import BinarySearchTree

class BinarySplayTree(BinarySearchTree):
    '''
    Splay tree is a binary search tree with splay operations to keep it balanced. Balanced search tree!
    '''
    def __init__(self, root_node=None):
        super(BinarySplayTree, self).__init__(root_node = root_node)
    
    def _splay_node_with_key(self, key):
        '''
        Splay the node with key to the root.
        '''
        pass

    def remove(self, key):
        return BinarySearchTree.remove(self, key)
    
    def find(self, key):
        value =  BinarySearchTree.find(self, key)
        if value != None:
            self._splay_node_with_key(key)
        return value
    
    def insert(self, key=None, obj=None):
        #add the node.
        BinarySearchTree.insert(self, key=key, obj=obj)
        #then splay it to root
        if key != None and obj != None:
            self._splay_node_with_key(key)