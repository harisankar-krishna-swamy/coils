'''
Created on Aug 15, 2015
@author: hari
'''
from datastructures.common import KeyValuePair

class BSTTreeNode(object):
    '''
    A binary search tree node. For example, key can be a unique employee id and value is a python object for employee.
    '''    
    def __init__(self, key = None, value = None, left_child = None, right_child = None):
        self._kvpair = KeyValuePair(key = key, value = value)
        self._right_child = right_child
        self._left_child = left_child
        self._link_inversion_traversal_tag = False #used for constant space traversal using link inversion.
    
    @property
    def kvpair(self):
        return self._kvpair
    
    @kvpair.setter
    def kvpair(self, new_kv_pair):#for replacing data in a node. this is used in node removal.
        self._kvpair = new_kv_pair
        
    @property
    def key(self):
        return self._kvpair.key
    
    @property
    def value(self):
        return self._kvpair.value
    
    @value.setter
    def value(self, new_value):
        self._kvpair.value = new_value
    
    @property
    def left_child(self):
        return self._left_child
        
    @left_child.setter
    def left_child(self, new_left_child):
        self._left_child = new_left_child
    
    @property
    def right_child(self):
        return self._right_child
    
    @right_child.setter
    def right_child(self, new_right_child):
        self._right_child = new_right_child
    
    @property
    def has_left_child(self):
        if self._left_child != None:
            return True
        return False
    
    @property
    def has_right_child(self):
        if self._right_child != None:
            return True
        return False
    
    @property
    def is_leaf_node(self):
        return not self.has_left_child and not self.has_right_child
    
    @property
    def has_only_left_child(self):
        return not self.has_right_child and self.has_left_child
    
    @property
    def has_only_right_child(self):
        return not self.has_left_child and self.has_right_child
    
    @property
    def link_inversion_traversal_tag(self):
        return self._link_inversion_traversal_tag
    
    @link_inversion_traversal_tag.setter
    def link_inversion_traversal_tag(self, new_link_inversion_traversal_tag):
        self._link_inversion_traversal_tag = new_link_inversion_traversal_tag
    
    def __str__(self):
        return '%s key[%s] value[%s]' % (self.__class__.__name__, str(self._kvpair.key), str(self._kvpair.value))

class BinarySearchTree(object):
    '''
    A binary search tree. At each node, the key > than keys in left sub-tree and <= keys in right sub-tree.Duplicates are allowed 
    as such. When deletion or find is done, the key encountered first is returned and this depends on the tree structure and 
    as such no guarantees are given on this order.
    
    Note* Tree traversals: pre-order, in-order and post-order are implemented as constant-space link inversion traversals.
    '''
    def __init__(self, root_node = None):
        self._root_node = root_node
        self._node_count = 0
        
        if self._root_node != None:
            self._node_count = 1

    @property    
    def node_count(self):
        return self._node_count
    
    def insert(self, key = None, obj = None):
        '''
        Add a key and its object value to the tree.
        '''
        if key == None or obj == None:
            return
        
        if self._root_node == None:
            self._root_node = BSTTreeNode(key = key, value = obj)
            self._node_count = 1
            return
        
        current_node = self._root_node
        parent_node = current_node
        
        while(current_node != None):
            parent_node = current_node
            if key >= current_node.key:
                current_node = current_node.right_child
            else:
                current_node = current_node.left_child
                
        if key >= parent_node.key:
            parent_node.right_child = BSTTreeNode(key= key, value = obj)
        else:
            parent_node.left_child = BSTTreeNode(key= key, value = obj)
        
        self._node_count = self._node_count + 1
        #    
            
    def _find_node_with_key(self, key):
        '''
        Returns the node with key and its parent node too as (node, parent). We use the parent often in other methods so sending it
        together as a tuple saves a call to find the parent again.
        '''
        if self._root_node == None or key == None:
            return (None, None)
        current_node = self._root_node
        parent_node = None
        while (current_node != None):
            if current_node.key == key:
                return (current_node, parent_node)
            
            parent_node = current_node
            if key > current_node.key:
                current_node = current_node.right_child
            else:    
                current_node = current_node.left_child
        #while
        return (None, None)        
        
    def find(self, key):
        '''
        Find the value associated with key. Returns None if nothing is found.
        '''
        node_with_key, parent_node = self._find_node_with_key(key)
        
        if node_with_key  != None:
            return node_with_key.value
        else:
            return None
            
    def _find_parent_of_node(self, bst_tree_node):
        if bst_tree_node == None:
            return         
        search_key = bst_tree_node.key
        node, parent_of_node = self._find_node_with_key(search_key)
        return parent_of_node
    
    def _find_inorder_successor(self, node):
        if node == None:
            return None
        
        while node.left_child != None:
            node = node.left_child
        return node
        
    def remove(self, key):
        '''
        Remove the node with key.
        '''
        node_to_delete, parent_of_node_to_delete = self._find_node_with_key(key)
        
        if node_to_delete == None:
            return
    
        '''
        if the node to delete is a leaf node and it has a parent, set the parent child reference to None.
        if node to delete does not have a parent, it is root, delete the node.
        update the count and return 
        '''
        if node_to_delete.is_leaf_node:
            if parent_of_node_to_delete != None:
                if parent_of_node_to_delete.left_child == node_to_delete:
                    parent_of_node_to_delete.left_child = None
                else:
                    parent_of_node_to_delete.right_child = None
            else:
                self._root_node = None
            
            self._node_count = self._node_count - 1
            return    
        
        if node_to_delete.has_only_left_child or node_to_delete.has_only_right_child:
            if parent_of_node_to_delete != None:
                if node_to_delete == parent_of_node_to_delete.left_child:
                    if node_to_delete.has_only_left_child :
                        parent_of_node_to_delete.left_child = node_to_delete.left_child
                    elif node_to_delete.has_only_right_child:
                        parent_of_node_to_delete.left_child = node_to_delete.right_child    
                elif node_to_delete == parent_of_node_to_delete.right_child:
                    if node_to_delete.has_only_left_child :
                        parent_of_node_to_delete.right_child = node_to_delete.left_child
                    elif node_to_delete.has_only_right_child:
                        parent_of_node_to_delete.right_child = node_to_delete.right_child
            else:#root with only one child
                if node_to_delete.has_only_left_child :
                    self._root_node = node_to_delete.left_child
                elif node_to_delete.has_only_right_child:
                    self._root_node = node_to_delete.right_child
            self._node_count = self._node_count - 1
            return
    
        #node has left and right children. find inorder successor of the right child of node to delete
        inorder_successor = self._find_inorder_successor(node_to_delete.right_child)
        parent_of_inorder_successor = self._find_parent_of_node(inorder_successor)
        
        right_child_of_inorder_successor = inorder_successor.right_child
        node_to_delete.kvpair = inorder_successor.kvpair
        
        if parent_of_inorder_successor != node_to_delete:
            parent_of_inorder_successor.left_child = right_child_of_inorder_successor
        else:
            parent_of_inorder_successor.right_child = right_child_of_inorder_successor
        self._node_count = self._node_count - 1
        return
    
    def traversal(self, want_pre_order = False, want_post_order = False, want_in_order = False):
        '''
        A yield is used to return the node elements while traversing the tree.
        Code is exact duplicate of link inversion traversal for tree in my Java library. It is available to read/download at
        http://harisankar-krishnaswamy.blogspot.in/2013/10/a-coder-post-link-inversion-traversal.html
        '''
        prev = None
        curr = self._root_node
        temp = None
        
        while 1==1:
            while curr != None: #fall down to left
                curr.link_inversion_traversal_tag = False
                if want_pre_order: 
                    yield curr.value
                temp = curr.left_child
                curr.left_child = prev
                prev = curr
                curr = temp
                
            while prev != None and prev.link_inversion_traversal_tag == True: #Rise from right
                temp = prev.right_child #has our way up
                prev.right_child = curr #Reset pointer
                curr = prev         #Move up
                if want_post_order:
                    yield curr.value 
                prev = temp
            
            if prev == None: 
                return
            else:
                    temp = prev.left_child
                    prev.left_child = curr
                    curr = prev;
                    prev = temp;
                    #We are comparing with pre-order traversal.
                    if want_in_order:
                        yield curr.value 
                    curr.link_inversion_traversal_tag = True
                    temp = curr.right_child
                    curr.right_child = prev
                    prev = curr;
                    curr = temp;    
    #
    def has_key(self, key):
        node_with_key, parent = self._find_node_with_key(key)
        if node_with_key != None:
            return True
        return False
        