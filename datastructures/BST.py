'''
Created on Aug 15, 2015
@author: hari
TODO: 
1) do we call search by element or key. key is something that is unique to an element. For example elmployee id for element employee
2) while searching for node and parent. Can we just sent both in a tuple as return value.
'''
class BSTTreeNode(object):
    '''
    A binary search tree node.
    '''

    def __init__(self, element = None, left_child = None, right_child = None):
        self._element = element
        self._right_child = right_child
        self._left_child = left_child
        
    @property
    def element(self):
        return self._element
    
    @element.setter
    def element(self, value):
        self._element = value
    
    @property
    def left_child(self):
        return self._left_child
        
    @left_child.setter
    def left_child(self, value):
        self._left_child = value
    
    @property
    def right_child(self):
        return self._right_child
    
    @right_child.setter
    def right_child(self, value):
        self._right_child = value
    
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
    
    def __str__(self):
        return '%s element %s' % (self.__class__.__name__, str(self._element))

class BinarySearchTree(object):
    '''
    A binary search tree. Insertion is done such that if new element/key is >= current node we go to the right child. else we go to the
    left child. Duplicates are allowed as such. When deletion or find is done, the element encountered first is returned and this 
    depends on the tree structure and as such no guarantees are given on this order.
    '''
    def __init__(self, root_node = None):
    
        self._root_node = root_node
        self._node_count = 0
        
        if self._root_node != None:
            self._node_count = 1

    @property    
    def node_count(self):
        return self._node_count
    
    def addElement(self, element):
    
        if self._root_node == None:
            self._root_node = BSTTreeNode(element = element)
            self._node_count = 1
            return
        
        current_node = self._root_node
        parent_node = current_node
        
        while(current_node != None):
            parent_node = current_node
            if element >= current_node.element:
                current_node = current_node.right_child
            else:
                current_node = current_node.left_child
                
        if element >= parent_node.element:
            parent_node.right_child = BSTTreeNode(element = element)
        else:
            parent_node.left_child = BSTTreeNode(element = element)
        
        self._node_count = self._node_count + 1
        #    
            
    def _find_node_with_element(self, element):
    
        if self._root_node == None:
            return None
    
        current_node = self._root_node
        while (current_node != None):
            if current_node.element == element:
                return current_node
            
            if element > current_node.element:
                current_node = current_node.right_child
            else:
                current_node = current_node.left_child
        #while
        return None        
        
    def findElement(self, element):
        
        node_with_element = self._find_node_with_element(element)
        
        if node_with_element  != None:
            return node_with_element.element
        else:
            return None
            
    def _find_parent_of_node(self, bst_tree_node):
    
        if self._root_node == None or self._root_node.element == bst_tree_node.element:
            return None
    
        current_node = self._root_node
        
        while (current_node != None):
            
            if current_node.has_left_child and current_node.left_child.element == bst_tree_node.element:
                return current_node
            
            if current_node.has_right_child and current_node.right_child.element == bst_tree_node.element:
                return current_node
                
            if bst_tree_node.element >= current_node.element:
                current_node = current_node.right_child
            else:
                current_node = current_node.left_child
        return None
    
    def _find_inorder_successor(self, node):
        if node == None:
            return None
        
        while node.left_child != None:
            node = node.left_child
        return node
        
    def deleteElement(self, element):

        node_to_delete = self._find_node_with_element(element)
        
        if node_to_delete == None:
            return
        
        parent_of_node_to_delete = self._find_parent_of_node(node_to_delete)        
            
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
        node_to_delete.element = inorder_successor.element #swap elements only.
        
        if parent_of_inorder_successor != node_to_delete:
            parent_of_inorder_successor.left_child = right_child_of_inorder_successor
        else:
            parent_of_inorder_successor.right_child = right_child_of_inorder_successor
        self._node_count = self._node_count - 1
        return