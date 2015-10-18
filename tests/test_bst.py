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

class BST_Test_Tree_Delete_Element_With_10_Sorted_Elements(TestCase):
    
    def setUp(self):
        self._bst = BinarySearchTree()
        self._bst.addElement(1)
        self._bst.addElement(2)
        self._bst.addElement(3)
        self._bst.addElement(4)
        self._bst.addElement(5)
        self._bst.addElement(6)
        self._bst.addElement(7)
        self._bst.addElement(8)
        self._bst.addElement(9)
        self._bst.addElement(10)
        
        self._bst_node_count = 10
        
    def test_delete_element_of_tree_non_existing_element(self):
         self._bst.deleteElement(11)
         self.assertEquals(self._bst.node_count, self._bst_node_count, 'Tree node count must be 10')
    
    def test_delete_element_of_tree_with_10_node(self):
        elements_to_delete = [10, 1, 7, 3, 5, 8, 2, 6, 9, 4]
        for element in elements_to_delete:
            print 'Deleting %d from tree' % element 
            self._bst.deleteElement(element)
            self.assertEquals(self._bst.findElement(element), None, 'Element found in BST after deleting it!')
            self._bst_node_count = self._bst_node_count - 1
            self.assertEquals(self._bst.node_count, self._bst_node_count, 'Tree node count must tally after deletion')
    
    def tearDown(self):
        self._bst = None

class BST_Test_Tree_Delete_Element_With_10_Reverse_Sorted_Elements(TestCase):
    
    def setUp(self):
        self._bst = BinarySearchTree()
        self._bst.addElement(10)
        self._bst.addElement(9)
        self._bst.addElement(8)
        self._bst.addElement(7)
        self._bst.addElement(6)
        self._bst.addElement(5)
        self._bst.addElement(4)
        self._bst.addElement(3)
        self._bst.addElement(2)
        self._bst.addElement(1)
        
        self._bst_node_count = 10
        
    def test_delete_element_of_tree_non_existing_element(self):
         self._bst.deleteElement(11)
         self.assertEquals(self._bst.node_count, self._bst_node_count, 'Tree node count must be 10')
    
    def test_delete_element_of_tree_with_10_node(self):
        elements_to_delete = [10, 1, 7, 3, 5, 8, 2, 6, 9, 4]
        for element in elements_to_delete:
            print 'Deleting %d from tree' % element 
            self._bst.deleteElement(element)
            self.assertEquals(self._bst.findElement(element), None, 'Element found in BST after deleting it!')
            self._bst_node_count = self._bst_node_count - 1
            self.assertEquals(self._bst.node_count, self._bst_node_count, 'Tree node count must tally after deletion')
    
    def tearDown(self):
        self._bst = None
        
# Preorder traversal
class BST_Test_Preorder_Traversal_with_empty_Tree(TestCase):
    def setUp(self):
        self._bst = BinarySearchTree()
    
    def test_preorder_traversal_with_empty_tree(self):
        pre_order_elements = []
        for element in self._bst.traversal(want_pre_order = True, want_in_order = False, want_post_order = False):
            pre_order_elements.append(element)
        print 'Pre order traversal of empty tree %s' % pre_order_elements
        self.assertEquals(0, len(pre_order_elements), 'Pre order traversal on empty tree must yield no elements')
    
    def tearDown(self):
        self._bst = None

class BST_Test_Preorder_Traversal_with_Single_Node_Tree(TestCase):
    def setUp(self):
        self._bst = BinarySearchTree()
        self._bst.addElement(10)
    
    def test_preorder_traversal_with_single_node_tree(self):
        pre_order_elements = []
        for element in self._bst.traversal(want_pre_order = True, want_in_order = False, want_post_order = False):
            pre_order_elements.append(element)
        print 'Pre order traversal of single node tree %s' % pre_order_elements
        self.assertEquals(1, len(pre_order_elements), 'Pre order traversal on single node tree must yield no elements')
        self.assertEquals(pre_order_elements, [10], 'Pre order traversal did not yield expected elements in order')
    
    def tearDown(self):
        self._bst = None

class BST_Test_Preorder_Traversal_with_10_Node_Tree(TestCase):
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
    
    def test_preorder_traversal_with_10_node_tree(self):
        pre_order_elements = []
        for element in self._bst.traversal(want_pre_order = True, want_in_order = False, want_post_order = False):
            pre_order_elements.append(element)
        print 'Pre order traversal of 10 node tree %s' % pre_order_elements
        self.assertEquals(10, len(pre_order_elements), 'Pre order traversal on 10 node tree must yield 10 elements')
        self.assertEquals(pre_order_elements, [5, 2, 1, 3, 4, 8, 7, 6, 9, 10], 'Pre order traversal did not yield expected elements in order')
    
    def tearDown(self):
        self._bst = None        

# Postorder traversal
class BST_Test_Postorder_Traversal_with_empty_Tree(TestCase):
    def setUp(self):
        self._bst = BinarySearchTree()
    
    def test_postorder_traversal_with_empty_tree(self):
        post_order_elements = []
        for element in self._bst.traversal(want_pre_order = False, want_in_order = False, want_post_order = True):
            post_order_elements.append(element)
        print 'Post order traversal of empty tree %s' % post_order_elements
        self.assertEquals(0, len(post_order_elements), 'Post order traversal on empty tree must yield no elements')
    
    def tearDown(self):
        self._bst = None

class BST_Test_Postorder_Traversal_with_Single_Node_Tree(TestCase):
    def setUp(self):
        self._bst = BinarySearchTree()
        self._bst.addElement(10)
    
    def test_postorder_traversal_with_single_node_tree(self):
        post_order_elements = []
        for element in self._bst.traversal(want_pre_order = False, want_in_order = False, want_post_order = True):
            post_order_elements.append(element)
        print 'Post order traversal of single node tree %s' % post_order_elements
        self.assertEquals(1, len(post_order_elements), 'Post order traversal on single node tree must yield one elements')
        self.assertEquals(post_order_elements, [10], 'Post order traversal did not yield expected elements in order')
    
    def tearDown(self):
        self._bst = None

class BST_Test_Postorder_Traversal_with_10_Node_Tree(TestCase):
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
    
    def test_postorder_traversal_with_10_node_tree(self):
        post_order_elements = []
        for element in self._bst.traversal(want_pre_order = False, want_in_order = False, want_post_order = True):
            post_order_elements.append(element)
        print 'Post order traversal of 10 node tree %s' % post_order_elements
        self.assertEquals(10, len(post_order_elements), 'Post order traversal on 10 node tree must yield 10 elements')
        self.assertEquals(post_order_elements, [1, 4, 3, 2, 6, 7, 10, 9, 8, 5], 'Post order traversal did not yield expected elements in order')
    
    def tearDown(self):
        self._bst = None

# Inorder traversal
class BST_Test_Inorder_Traversal_with_empty_Tree(TestCase):
    def setUp(self):
        self._bst = BinarySearchTree()
    
    def test_inorder_traversal_with_empty_tree(self):
        in_order_elements = []
        for element in self._bst.traversal(want_pre_order = False, want_in_order = True, want_post_order = False):
            in_order_elements.append(element)
        print 'In order traversal of empty tree %s' % in_order_elements
        self.assertEquals(0, len(in_order_elements), 'In order traversal on empty tree must yield no elements')
    
    def tearDown(self):
        self._bst = None

class BST_Test_Inorder_Traversal_with_Single_Node_Tree(TestCase):
    def setUp(self):
        self._bst = BinarySearchTree()
        self._bst.addElement(10)
    
    def test_inorder_traversal_with_single_node_tree(self):
        in_order_elements = []
        for element in self._bst.traversal(want_pre_order = False, want_in_order = True, want_post_order = False):
            in_order_elements.append(element)
        print 'In order traversal of single node tree %s' % in_order_elements
        self.assertEquals(1, len(in_order_elements), 'In order traversal on single node tree must yield one elements')
        self.assertEquals(in_order_elements, [10], 'In order traversal did not yield expected elements in order')
    
    def tearDown(self):
        self._bst = None

class BST_Test_Inorder_Traversal_with_10_Node_Tree(TestCase):
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
    
    def test_inorder_traversal_with_10_node_tree(self):
        in_order_elements = []
        for element in self._bst.traversal(want_pre_order = False, want_in_order = True, want_post_order = False):
            in_order_elements.append(element)
        print 'In order traversal of 10 node tree %s' % in_order_elements
        self.assertEquals(10, len(in_order_elements), 'In order traversal on 10 node tree must yield 10 elements')
        self.assertEquals(in_order_elements, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'In order traversal did not yield expected elements in order')
    
    def tearDown(self):
        self._bst = None
        
class BST_Test_All_Traversals_Consecutively_For_Tree_Integirty_With_10_Node_Tree(TestCase):
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
    
    def test_traversal_consecutively_with_10_node_tree(self):
        #inorder
        in_order_elements = []
        for element in self._bst.traversal(want_pre_order = False, want_in_order = True, want_post_order = False):
            in_order_elements.append(element)
        print 'In order traversal of 10 node tree %s' % in_order_elements
        self.assertEquals(10, len(in_order_elements), 'In order traversal on 10 node tree must yield 10 elements')
        self.assertEquals(in_order_elements, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'In order traversal did not yield expected elements in order')
        
        #postorder
        post_order_elements = []
        for element in self._bst.traversal(want_pre_order = False, want_in_order = False, want_post_order = True):
            post_order_elements.append(element)
        print 'Post order traversal of 10 node tree %s' % post_order_elements
        self.assertEquals(10, len(post_order_elements), 'Post order traversal on 10 node tree must yield 10 elements')
        self.assertEquals(post_order_elements, [1, 4, 3, 2, 6, 7, 10, 9, 8, 5], 'Post order traversal did not yield expected elements in order')
    
        pre_order_elements = []
        for element in self._bst.traversal(want_pre_order = True, want_in_order = False, want_post_order = False):
            pre_order_elements.append(element)
        print 'Pre order traversal of 10 node tree %s' % pre_order_elements
        self.assertEquals(10, len(pre_order_elements), 'Pre order traversal on 10 node tree must yield 10 elements')
        self.assertEquals(pre_order_elements, [5, 2, 1, 3, 4, 8, 7, 6, 9, 10], 'Pre order traversal did not yield expected elements in order')
    
    
    def tearDown(self):
        self._bst = None                