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
        TODO: Splay the node with key to the root.
        '''
        pass
        '''
        node_to_splay, parent = self._find_node_with_key(key)
        while True:
            if parent == None or (self._root_node.left_child == node_to_splay or self._root_node.right_child == node_to_splay):
               break#if node is root or child of root break
               
            if node_to_splay.isLeftChildOfRightChild:
                self._rotate_right_for(node_to_splay)
                self._rotate_left_for(node_to_splay)
                continue
            if node_to_splay.isRightChildOfLeftChild:
                self._rotate_left_for(node_to_splay)
                self._rotate_right_for(node_to_splay)
                continue
            if node_to_splay.isLeftChildOfLeftChild:
                self._rotate_right_for(parent)
                self._rotate_right_for(node_to_splay)
                continue
            if node_to_splay.isRightChildOfRightChild:
                self._rotate_left_for(parent)
                self._rotate_right_for(node_to_splay)
        #while
        #node_to_splay is either root or a child of root
        if node_to_splay.isRoot:
            return
        if node_to_splay.isLeftChild:
            self._rotate_right_for(node_to_splay)
        else:
            self._rotate_left_for(node_to_splay)
        '''
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