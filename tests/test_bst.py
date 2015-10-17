'''
Created on Oct 17, 2015
@author: hari
'''
from unittest import TestCase
from datastructures.BST import BinarySearchTree

class BST_Test_Empty_Tree(TestCase):
    
    def setUp(self):
        self._bst = BinarySearchTree()
    
    def test_node_count_of_empty_tree(self):
        self.assertEquals(self._bst.node_count, 0, 'Empty tree node count must be 0')
        
    def test_find_element_empty_tree(self):
        self.assertEquals(self._bst.findElement(20), None, 'Empty tree find operation must return None')
    
    def test_delete_element_empty_tree(self):
        self._bst.deleteElement(20)
    
    def tearDown(self):
        self._linkedList = None

class BST_Test_Tree_With_1_Element(TestCase):
    
    def setUp(self):
        self._bst = BinarySearchTree()
        self._bst.addElement(10)
    
    def test_node_count_of_tree_with_1_node(self):
        self.assertEquals(self._bst.node_count, 1, 'Tree node count must be 1')
        
    def test_find_element_of_tree_with_1_node(self):
        self.assertEquals(self._bst.findElement(10), 10, 'Find operation failed on tree with 1 node')
    
    def test_delete_element_of_tree_with_1_node(self):
        self._bst.deleteElement(10)
        self.assertEquals(self._bst.node_count, 0, 'Empty tree node count must be 0')
        self.assertEquals(self._bst.findElement(20), None, 'Empty tree find operation must return None')
        
    
    def tearDown(self):
        self._linkedList = None

