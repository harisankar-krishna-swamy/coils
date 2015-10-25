'''
Created on Oct 19, 2015
@author: hari
'''
from coils.trees.BST import BinarySearchTree

class BinarySplayTree(BinarySearchTree):
    '''
    Splay tree is a binary search tree with splay operations to keep it balanced. Balanced search tree!
    '''
    def __init__(self, root_node=None):
        super(BinarySplayTree, self).__init__(root_node = root_node)
    
    def _find_node_with_key_for_splay(self, key):
        '''
        Returns the node with key and its parent node too as (node, parent, grandparent). Splay tree rotation is acheved by knowing 
        parent and grand parent of a node. So when searching for  
        '''
        if self._root_node == None or key == None:
            return (None, None, None)
        current_node = self._root_node
        parent_node = None
        grand_parent_node = None
        
        while (current_node != None):
            if current_node.key == key:
                return (current_node, parent_node, grand_parent_node)
            grand_parent_node = parent_node
            parent_node = current_node
            if key > current_node.key:
                current_node = current_node.right_child
            else:    
                current_node = current_node.left_child
        #while
        #failed to find node but we fell off the tree at some point
        return (None, parent_node, grand_parent_node)
    
    def _rotate_right_for(self, aNode):
        aNode, parent, grandparent = self._find_node_with_key_for_splay(aNode.key)
        
        if grandparent != None:
            if parent == grandparent.left_child:
                grandparent.left_child = aNode
            else:
                grandparent.right_child = aNode
        else:
            self._root_node = aNode
        
        right_of_aNode = aNode.right_child
        parent.left_child = right_of_aNode
        aNode.right_child = parent
    
    def _rotate_left_for(self, aNode):
        aNode, parent, grandparent = self._find_node_with_key_for_splay(aNode.key)
        
        if grandparent != None:
            if parent == grandparent.left_child:
                grandparent.left_child = aNode
            else:
                grandparent.right_child = aNode
        else:
            self._root_node = aNode
        
        left_of_aNode = aNode.left_child
        parent.right_child = left_of_aNode
        aNode.left_child = parent
        
    def _splay_node_with_key(self, key):
        '''
        Splay operation
        '''
        node_to_splay = None
        parent = None 
        grand_parent = None
        
        while True:
            #this find operation needs to be done everytime if we do not store extra meta (isroot leftchild etc) on each node.
            #Assuming a billion nodes and the tree is almost balance which is the case, log2 (1 billion) < 25. Compared to that
            #storing meta for 1 billion nodes is too much space? 
            node_to_splay, parent, grand_parent = self._find_node_with_key_for_splay(key)
            if parent == None or (self._root_node.left_child == node_to_splay or self._root_node.right_child == node_to_splay):
                break#if node is root or child of root break
               
            if grand_parent.right_child != None and node_to_splay == grand_parent.right_child.left_child:
                self._rotate_right_for(node_to_splay)
                self._rotate_left_for(node_to_splay)
                continue
            if grand_parent.left_child != None and node_to_splay == grand_parent.left_child.right_child:
                self._rotate_left_for(node_to_splay)
                self._rotate_right_for(node_to_splay)
                continue
            if grand_parent.left_child != None and node_to_splay == grand_parent.left_child.left_child:
                self._rotate_right_for(parent)
                self._rotate_right_for(node_to_splay)
                continue
            if grand_parent.right_child != None and node_to_splay == grand_parent.right_child.right_child:
                self._rotate_left_for(parent)
                self._rotate_left_for(node_to_splay)
        #while
        #node_to_splay is either root or a child of root
        if parent == None:
            return
        if node_to_splay == parent.left_child:
            self._rotate_right_for(node_to_splay)
        else:
            self._rotate_left_for(node_to_splay)
        
    def remove(self, key):
        node_to_remove, parent, grand_parent = self._find_node_with_key_for_splay(key)# need to know to splay
        # remove as in BST
        BinarySearchTree.remove(self, key = key)
        #splay the parent from which we fell off the tree
        if parent != None:
            self._splay_node_with_key(parent.key)
        
    def find(self, key):
        node_with_key, parent, grand_parent = self._find_node_with_key_for_splay(key)# need to know to splay
        value = None
        if node_with_key != None:
            value = node_with_key.value
            self._splay_node_with_key(key)
        else:#node was not found so we splay the parent (node from which we fell off the tree)
            if parent != None:
                self._splay_node_with_key(parent.key)
        return value
    
    def insert(self, key=None, obj=None):
        #add the node.
        BinarySearchTree.insert(self, key=key, obj=obj)
        #then splay it to root
        if key != None and obj != None:
            self._splay_node_with_key(key)