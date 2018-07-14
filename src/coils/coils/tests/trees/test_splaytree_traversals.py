'''
Created on Oct 19, 2015
@author: hari
'''
from __future__ import print_function
import unittest
from coils.trees.splaytree import SplayTree
#        
# Preorder traversal
#
class Splay_Tree_Test_Preorder_Traversal_with_empty_Tree(unittest.TestCase):
    def setUp(self):
        self._splay_tree = SplayTree()
    
    def test_preorder_traversal_with_empty_tree(self):
        pre_order_elements = []
        for key, element in self._splay_tree.traversal(want_pre_order = True, want_in_order = False, want_post_order = False):
            pre_order_elements.append(element)
        self.assertEqual(0, len(pre_order_elements), 'Pre order traversal on empty tree must yield no elements')
    
    def tearDown(self):
        self._splay_tree = None

class Splay_Tree_Test_Preorder_Traversal_with_Single_Node_Tree(unittest.TestCase):
    def setUp(self):
        self._splay_tree = SplayTree()
        self._splay_tree.insert(key = 10, obj = 10)
    
    def test_preorder_traversal_with_single_node_tree(self):
        pre_order_elements = []
        for key, element in self._splay_tree.traversal(want_pre_order = True, want_in_order = False, want_post_order = False):
            pre_order_elements.append(element)
        self.assertEqual(1, len(pre_order_elements), 'Pre order traversal on single node tree must yield no elements')
        self.assertEqual(pre_order_elements, [10], 'Pre order traversal did not yield expected elements in order')
    
    def tearDown(self):
        self._splay_tree = None

class Splay_Tree_Test_Preorder_Traversal_with_10_Node_Tree(unittest.TestCase):
    def setUp(self):
        self._splay_tree = SplayTree()
        self._splay_tree.insert(key = 5, obj = 5)
        self._splay_tree.insert(key = 8, obj = 8)
        self._splay_tree.insert(key = 7, obj = 7)
        self._splay_tree.insert(key = 9, obj = 9)
        self._splay_tree.insert(key = 10, obj = 10)
        self._splay_tree.insert(key = 2, obj = 2)
        self._splay_tree.insert(key = 1, obj = 1)
        self._splay_tree.insert(key = 3, obj = 3)
        self._splay_tree.insert(key = 4, obj = 4)
        self._splay_tree.insert(key = 6, obj = 6)
        
    def test_preorder_traversal_with_10_node_tree(self):
        pre_order_elements = []
        for key, element in self._splay_tree.traversal(want_pre_order = True, want_in_order = False, want_post_order = False):
            pre_order_elements.append(element)
        self.assertEqual(10, len(pre_order_elements), 'Pre order traversal on 10 node tree must yield 10 elements')
        self.assertEqual(pre_order_elements, [6, 4, 3, 1, 2, 5, 10, 7, 8, 9], 'Pre order traversal did not yield expected elements in order')
    
    def tearDown(self):
        self._splay_tree = None        
#
# Postorder traversal
#
class Splay_Tree_Test_Postorder_Traversal_with_empty_Tree(unittest.TestCase):
    
    def setUp(self):
        self._splay_tree = SplayTree()
    
    def test_postorder_traversal_with_empty_tree(self):
        post_order_elements = []
        for key, element in self._splay_tree.traversal(want_pre_order = False, want_in_order = False, want_post_order = True):
            post_order_elements.append(element)
        self.assertEqual(0, len(post_order_elements), 'Post order traversal on empty tree must yield no elements')
    
    def tearDown(self):
        self._splay_tree = None

class Splay_Tree_Test_Postorder_Traversal_with_Single_Node_Tree(unittest.TestCase):
    def setUp(self):
        self._splay_tree = SplayTree()
        self._splay_tree.insert(key = 10, obj = 10)
    
    def test_postorder_traversal_with_single_node_tree(self):
        post_order_elements = []
        for key, element in self._splay_tree.traversal(want_pre_order = False, want_in_order = False, want_post_order = True):
            post_order_elements.append(element)
        self.assertEqual(1, len(post_order_elements), 'Post order traversal on single node tree must yield one elements')
        self.assertEqual(post_order_elements, [10], 'Post order traversal did not yield expected elements in order')
    
    def tearDown(self):
        self._splay_tree = None

class Splay_Tree_Test_Postorder_Traversal_with_10_Node_Tree(unittest.TestCase):
    def setUp(self):
        self._splay_tree = SplayTree()
        self._splay_tree.insert(key = 5, obj = 5)
        self._splay_tree.insert(key = 8, obj = 8)
        self._splay_tree.insert(key = 7, obj = 7)
        self._splay_tree.insert(key = 9, obj = 9)
        self._splay_tree.insert(key = 10, obj = 10)
        self._splay_tree.insert(key = 2, obj = 2)
        self._splay_tree.insert(key = 1, obj = 1)
        self._splay_tree.insert(key = 3, obj = 3)
        self._splay_tree.insert(key = 4, obj = 4)
        self._splay_tree.insert(key = 6, obj = 6)
        
    def test_postorder_traversal_with_10_node_tree(self):
        post_order_elements = []
        for key, element in self._splay_tree.traversal(want_pre_order = False, want_in_order = False, want_post_order = True):
            post_order_elements.append(element)
        self.assertEqual(10, len(post_order_elements), 'Post order traversal on 10 node tree must yield 10 elements')
        self.assertEqual(post_order_elements, [2, 1, 3, 5, 4, 9, 8, 7, 10, 6], 'Post order traversal did not yield expected elements in order')
    
    def tearDown(self):
        self._splay_tree = None
#
# Inorder traversal
#
class Splay_Tree_Test_Inorder_Traversal_with_empty_Tree(unittest.TestCase):
    def setUp(self):
        self._splay_tree = SplayTree()
    
    def test_inorder_traversal_with_empty_tree(self):
        in_order_elements = []
        for key, element in self._splay_tree.traversal(want_pre_order = False, want_in_order = True, want_post_order = False):
            in_order_elements.append(element)
        self.assertEqual(0, len(in_order_elements), 'In order traversal on empty tree must yield no elements')
    
    def tearDown(self):
        self._splay_tree = None

class Splay_Tree_Test_Inorder_Traversal_with_Single_Node_Tree(unittest.TestCase):
    def setUp(self):
        self._splay_tree = SplayTree()
        self._splay_tree.insert(key = 10, obj = 10)
    
    def test_inorder_traversal_with_single_node_tree(self):
        in_order_elements = []
        for key, element in self._splay_tree.traversal(want_pre_order = False, want_in_order = True, want_post_order = False):
            in_order_elements.append(element)
        self.assertEqual(1, len(in_order_elements), 'In order traversal on single node tree must yield one elements')
        self.assertEqual(in_order_elements, [10], 'In order traversal did not yield expected elements in order')
    
    def tearDown(self):
        self._splay_tree = None

class Splay_Tree_Test_Inorder_Traversal_with_10_Node_Tree(unittest.TestCase):
    def setUp(self):
        self._splay_tree = SplayTree()
        self._splay_tree.insert(key = 5, obj = 5)
        self._splay_tree.insert(key = 8, obj = 8)
        self._splay_tree.insert(key = 7, obj = 7)
        self._splay_tree.insert(key = 9, obj = 9)
        self._splay_tree.insert(key = 10, obj = 10)
        self._splay_tree.insert(key = 2, obj = 2)
        self._splay_tree.insert(key = 1, obj = 1)
        self._splay_tree.insert(key = 3, obj = 3)
        self._splay_tree.insert(key = 4, obj = 4)
        self._splay_tree.insert(key = 6, obj = 6)
    
    def test_inorder_traversal_with_10_node_tree(self):
        in_order_elements = []
        for key, element in self._splay_tree.traversal(want_pre_order = False, want_in_order = True, want_post_order = False):
            in_order_elements.append(element)
        self.assertEqual(10, len(in_order_elements), 'In order traversal on 10 node tree must yield 10 elements')
        self.assertEqual(in_order_elements, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'In order traversal did not yield expected elements in order')
    
    def tearDown(self):
        self._splay_tree = None
        
class Splay_Tree_Test_All_Traversals_Consecutively_For_Tree_Integirty_With_10_Node_Tree(unittest.TestCase):
    def setUp(self):
        self._splay_tree = SplayTree()
        self._splay_tree.insert(key = 5, obj = 5)
        self._splay_tree.insert(key = 8, obj = 8)
        self._splay_tree.insert(key = 7, obj = 7)
        self._splay_tree.insert(key = 9, obj = 9)
        self._splay_tree.insert(key = 10, obj = 10)
        self._splay_tree.insert(key = 2, obj = 2)
        self._splay_tree.insert(key = 1, obj = 1)
        self._splay_tree.insert(key = 3, obj = 3)
        self._splay_tree.insert(key = 4, obj = 4)
        self._splay_tree.insert(key = 6, obj = 6)
        
    def test_traversal_consecutively_with_10_node_tree(self):
        #inorder
        in_order_elements = []
        for key, element in self._splay_tree.traversal(want_pre_order = False, want_in_order = True, want_post_order = False):
            in_order_elements.append(element)
        self.assertEqual(10, len(in_order_elements), 'In order traversal on 10 node tree must yield 10 elements')
        self.assertEqual(in_order_elements, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'In order traversal did not yield expected elements in order')
        
        #postorder
        post_order_elements = []
        for key, element in self._splay_tree.traversal(want_pre_order = False, want_in_order = False, want_post_order = True):
            post_order_elements.append(element)
        
        self.assertEqual(10, len(post_order_elements), 'Post order traversal on 10 node tree must yield 10 elements')
        self.assertEqual(post_order_elements, [2, 1, 3, 5, 4, 9, 8, 7, 10, 6], 'Post order traversal did not yield expected elements in order')
    
        pre_order_elements = []
        for key, element in self._splay_tree.traversal(want_pre_order = True, want_in_order = False, want_post_order = False):
            pre_order_elements.append(element)
        
        self.assertEqual(10, len(pre_order_elements), 'Pre order traversal on 10 node tree must yield 10 elements')
        self.assertEqual(pre_order_elements, [6, 4, 3, 1, 2, 5, 10, 7, 8, 9], 'Pre order traversal did not yield expected elements in order')
    
    def tearDown(self):
        self._splay_tree = None                
#
# Inorder traversal with stack
#
class Splay_Tree__Test_Inorder_Traversal_Using_Stack_with_empty_Tree(unittest.TestCase):
    def setUp(self):
        self._splaytree = SplayTree()
    
    def test_inorder_traversal_with_empty_tree(self):
        in_order_elements = []
        for key, element in self._splaytree.inorder_traversal_with_stack():
            in_order_elements.append(element)
        self.assertEqual(0, len(in_order_elements), 'In order traversal on empty tree must yield no elements')
    
    def tearDown(self):
        self._splaytree = None

class Splay_Tree__Test_Inorder_Traversal_with_Stack_On_Single_Node_Tree(unittest.TestCase):
    def setUp(self):
        self._splaytree = SplayTree()
        self._splaytree.insert(key = 10, obj = 10)
    
    def test_inorder_traversal_with_single_node_tree(self):
        in_order_elements = []
        for key, element in self._splaytree.inorder_traversal_with_stack():
            in_order_elements.append(element)
        self.assertEqual(1, len(in_order_elements), 'In order traversal on single node tree must yield one elements')
        self.assertEqual(in_order_elements, [10], 'In order traversal did not yield expected elements in order')
    
    def tearDown(self):
        self._splaytree = None

class Splay_Tree__Test_Inorder_Traversal_with_Stack_on_10_Node_Tree(unittest.TestCase):
    def setUp(self):
        self._splaytree = SplayTree()
        self._splaytree.insert(key = 5, obj = 5)
        self._splaytree.insert(key = 8, obj = 8)
        self._splaytree.insert(key = 7, obj = 7)
        self._splaytree.insert(key = 9, obj = 9)
        self._splaytree.insert(key = 10, obj = 10)
        self._splaytree.insert(key = 2, obj = 2)
        self._splaytree.insert(key = 1, obj = 1)
        self._splaytree.insert(key = 3, obj = 3)
        self._splaytree.insert(key = 4, obj = 4)
        self._splaytree.insert(key = 6, obj = 6)
    
    def test_inorder_traversal_with_10_node_tree(self):
        in_order_elements = []
        for key, element in self._splaytree.inorder_traversal_with_stack():
            in_order_elements.append(element)
        self.assertEqual(10, len(in_order_elements), 'In order traversal on 10 node tree must yield 10 elements')
        self.assertEqual(in_order_elements, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'In order traversal did not yield expected elements in order')
    
    def tearDown(self):
        self._splaytree = None
if __name__ == '__main__':
    #splay tree traversal
    print('SplayTree traversal tests')
    unittest.main()