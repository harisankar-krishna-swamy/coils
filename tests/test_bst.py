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
        self._bst = None

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
        self._bst = None

class BST_Test_Tree_Count_Find_Element_With_10_Elements(TestCase):
    
    def setUp(self):
        self._bst = BinarySearchTree()
        self._bst.addElement(5)
        self._bst.addElement(8)
        self._bst.addElement(7)
        self._bst.addElement(9)
        self._bst.addElement(10)
        self._bst.addElement(2)
        self._bst.addElement(1)
        self._bst.addElement(3)
        self._bst.addElement(4)
        self._bst.addElement(6)
        
        self._bst_node_count = 10
    
    def test_node_count_of_tree_with_10_node(self):
        print 'Bst node count %d' % self._bst.node_count
        self.assertEquals(self._bst.node_count, self._bst_node_count, 'Tree node count must be 10')
        
    def test_find_element_of_tree_with_10_node(self):
        for i in range(1, 11): # 1 to 10
            tree_element = self._bst.findElement(i)
            self.assertNotEqual(tree_element, None, 'BST findElement did not return existing element')
            print 'Bst findElement(%d) = %d' % (i, tree_element)
            self.assertEquals(tree_element, i, 'Find operation failed on tree with 1 node')
    
    def tearDown(self):
        self._bst = None
        
class BST_Test_Tree_Delete_Element_With_10_Elements(TestCase):
    
    def setUp(self):
        self._bst = BinarySearchTree()
        self._bst.addElement(5)
        self._bst.addElement(8)
        self._bst.addElement(7)
        self._bst.addElement(9)
        self._bst.addElement(10)
        self._bst.addElement(2)
        self._bst.addElement(1)
        self._bst.addElement(3)
        self._bst.addElement(4)
        self._bst.addElement(6)
        
        self._bst_node_count = 10
        
    def test_delete_element_of_tree_non_existing_element(self):
         self._bst.deleteElement(11)
         self.assertEquals(self._bst.node_count, self._bst_node_count, 'Tree node count must be 10')
    
    def test_delete_element_of_tree_with_10_node(self):
        elements_to_delete = [10, 1, 7, 3, 5, 8, 2, 6, 9]
        for element in elements_to_delete:
            print 'Deleting %d from tree' % element 
            self._bst.deleteElement(element)
            self.assertEquals(self._bst.findElement(element), None, 'Element found in BST after deleting it!')
            self._bst_node_count = self._bst_node_count - 1
            self.assertEquals(self._bst.node_count, self._bst_node_count, 'Tree node count must tally after deletion')
    
    def tearDown(self):
        self._bst = None