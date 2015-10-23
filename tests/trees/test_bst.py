'''
Created on Oct 17, 2015
@author: hari
'''
from unittest import TestCase
from datastructures.trees.BST import BinarySearchTree

class BST_Test_Empty_Tree(TestCase):    
    def setUp(self):
        self._bst = BinarySearchTree()
    
    def test_node_count_of_empty_tree(self):
        self.assertEquals(self._bst.node_count, 0, 'Empty tree node count must be 0')
        
    def test_find_key_empty_tree(self):
        self.assertEquals(self._bst.find(20), None, 'Empty tree find operation must return None')
    
    def test_delete_element_empty_tree(self):
        self._bst.remove(20)
    
    def tearDown(self):
        self._bst = None

class BST_Test_Tree_With_1_Element(TestCase):
    
    def setUp(self):
        self._bst = BinarySearchTree()
        self._bst.insert(key = 10, obj = 10)
    
    def test_node_count_of_tree_with_1_node(self):
        self.assertEquals(self._bst.node_count, 1, 'Tree node count must be 1')
        
    def test_find_key_of_tree_with_1_node(self):
        self.assertEquals(self._bst.find(10), 10, 'Find operation failed on tree with 1 node')
    
    def test_delete_element_of_tree_with_1_node(self):
        self._bst.remove(10)
        self.assertEquals(self._bst.node_count, 0, 'Empty tree node count must be 0')
        self.assertEquals(self._bst.find(20), None, 'Empty tree find operation must return None')
            
    def tearDown(self):
        self._bst = None

class BST_Test_Tree_Count_Find_Element_With_10_Elements(TestCase):
    
    def setUp(self):
        self._bst = BinarySearchTree()
        self._bst.insert(key = 5, obj = 5)
        self._bst.insert(key = 8, obj = 8)
        self._bst.insert(key = 7, obj = 7)
        self._bst.insert(key = 9, obj = 9)
        self._bst.insert(key = 10, obj = 10)
        self._bst.insert(key = 2, obj = 2)
        self._bst.insert(key = 1, obj = 1)
        self._bst.insert(key = 3, obj = 3)
        self._bst.insert(key = 4, obj = 4)
        self._bst.insert(key = 6, obj = 6)
        
        self._bst_node_count = 10
    
    def test_node_count_of_tree_with_10_node(self):
        print 'Bst node count %d' % self._bst.node_count
        self.assertEquals(self._bst.node_count, self._bst_node_count, 'Tree node count must be 10')
        
    def test_find_element_of_tree_with_10_node(self):
        for i in range(1, 11): # 1 to 10
            tree_element = self._bst.find(i)
            self.assertNotEqual(tree_element, None, 'BST findElement did not return existing element')
            print 'Bst findElement(%d) = %d' % (i, tree_element)
            self.assertEquals(tree_element, i, 'Find operation failed on tree with 1 node')
    
    def tearDown(self):
        self._bst = None
        
class BST_Test_Tree_Delete_Element_With_10_Elements(TestCase):
    
    def setUp(self):
        self._bst = BinarySearchTree()
        self._bst.insert(key = 5, obj = 5)
        self._bst.insert(key = 8, obj = 8)
        self._bst.insert(key = 7, obj = 7)
        self._bst.insert(key = 9, obj = 9)
        self._bst.insert(key = 10, obj = 10)
        self._bst.insert(key = 2, obj = 2)
        self._bst.insert(key = 1, obj = 1)
        self._bst.insert(key = 3, obj = 3)
        self._bst.insert(key = 4, obj = 4)
        self._bst.insert(key = 6, obj = 6)
        
        self._bst_node_count = 10
        
    def test_delete_element_of_tree_non_existing_element(self):
         self._bst.remove(11)
         self.assertEquals(self._bst.node_count, self._bst_node_count, 'Tree node count must be 10')
    
    def test_delete_element_of_tree_with_10_node(self):
        elements_to_delete = [10, 1, 7, 3, 5, 8, 2, 6, 9]
        for element in elements_to_delete:
            print 'Deleting %d from tree' % element 
            self._bst.remove(element)
            self.assertEquals(self._bst.find(element), None, 'Element found in BST after deleting it!')
            self._bst_node_count = self._bst_node_count - 1
            self.assertEquals(self._bst.node_count, self._bst_node_count, 'Tree node count must tally after deletion')
    
    def tearDown(self):
        self._bst = None

class BST_Test_Tree_Delete_Element_With_10_Sorted_Elements(TestCase):
    
    def setUp(self):
        self._bst = BinarySearchTree()
        self._bst.insert(key = 1, obj = 1)
        self._bst.insert(key = 2, obj = 2)
        self._bst.insert(key = 3, obj = 3)
        self._bst.insert(key = 4, obj = 4)
        self._bst.insert(key = 5, obj = 5)
        self._bst.insert(key = 6, obj = 6)
        self._bst.insert(key = 7, obj = 7)
        self._bst.insert(key = 8, obj = 8)
        self._bst.insert(key = 9, obj = 9)
        self._bst.insert(key = 10, obj = 10)
        
        self._bst_node_count = 10
        
    def test_delete_element_of_tree_non_existing_element(self):
         self._bst.remove(11)
         self.assertEquals(self._bst.node_count, self._bst_node_count, 'Tree node count must be 10')
    
    def test_delete_element_of_tree_with_10_node(self):
        elements_to_delete = [10, 1, 7, 3, 5, 8, 2, 6, 9, 4]
        for element in elements_to_delete:
            print 'Deleting %d from tree' % element 
            self._bst.remove(element)
            self.assertEquals(self._bst.find(element), None, 'Element found in BST after deleting it!')
            self._bst_node_count = self._bst_node_count - 1
            self.assertEquals(self._bst.node_count, self._bst_node_count, 'Tree node count must tally after deletion')
    
    def tearDown(self):
        self._bst = None

class BST_Test_Tree_Delete_Element_With_10_Reverse_Sorted_Elements(TestCase):
    
    def setUp(self):
        self._bst = BinarySearchTree()
        self._bst.insert(key = 10, obj = 10)
        self._bst.insert(key = 9, obj = 9)
        self._bst.insert(key = 8, obj = 8)
        self._bst.insert(key = 7, obj = 7)
        self._bst.insert(key = 6, obj = 6)
        self._bst.insert(key = 5, obj = 5)
        self._bst.insert(key = 4, obj = 4)
        self._bst.insert(key = 3, obj = 3)
        self._bst.insert(key = 2, obj = 2)
        self._bst.insert(key = 1, obj = 1)
        
        self._bst_node_count = 10
        
    def test_delete_element_of_tree_non_existing_element(self):
        self._bst.remove(11)
        self.assertEquals(self._bst.node_count, self._bst_node_count, 'Tree node count must be 10')
    
    def test_delete_element_of_tree_with_10_node(self):
        elements_to_delete = [10, 1, 7, 3, 5, 8, 2, 6, 9, 4]
        for element in elements_to_delete:
            print 'Deleting %d from tree' % element 
            self._bst.remove(element)
            self.assertEquals(self._bst.find(element), None, 'Element found in BST after deleting it!')
            self._bst_node_count = self._bst_node_count - 1
            self.assertEquals(self._bst.node_count, self._bst_node_count, 'Tree node count must tally after deletion')
    def tearDown(self):
        self._bst = None
        
class BST_Test_Has_Key_with_Empty_Tree(TestCase):    
    def setUp(self):
        self._bst = BinarySearchTree()
    
    def test_has_key_empty_tree(self):
        self.assertEquals(self._bst.has_key(20), False, 'Empty tree has_key operation must return False')
    
    def tearDown(self):
        self._bst = None

class BST_Test_Has_Key_with_Single_Node_Tree(TestCase):    
    def setUp(self):
        self._bst = BinarySearchTree()
        self._bst.insert(key = 10, obj = 'Object value')
    
    def test_has_key_empty_tree(self):
        self.assertEquals(self._bst.has_key(10), True, 'Tree has_key operation must return True for existing key')
    
    def tearDown(self):
        self._bst = None

class BST_Test_Has_Key_With_10_Elements(TestCase):
    
    def setUp(self):
        self._bst = BinarySearchTree()
        self._bst.insert(key = 5, obj = 5)
        self._bst.insert(key = 8, obj = 8)
        self._bst.insert(key = 7, obj = 7)
        self._bst.insert(key = 9, obj = 9)
        self._bst.insert(key = 10, obj = 10)
        self._bst.insert(key = 2, obj = 2)
        self._bst.insert(key = 1, obj = 1)
        self._bst.insert(key = 3, obj = 3)
        self._bst.insert(key = 4, obj = 4)
        self._bst.insert(key = 6, obj = 6)
        
        self._bst_node_count = 10
    
    def test_has_key_with_10_node(self):
        for i in range(1, 11): # 1 to 10
            self.assertEquals(self._bst.has_key(i), True, 'has_key operation must return True for existing key.')
    
    def tearDown(self):
        self._bst = None