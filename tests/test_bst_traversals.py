'''
Created on Oct 19, 2015
@author: hari
'''
from unittest import TestCase
from datastructures.BST import BinarySearchTree        
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
        self._bst.insert(key = 10, obj = 10)
    
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
        self._bst.insert(key = 10, obj = 10)
    
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
        self._bst.insert(key = 10, obj = 10)
    
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
