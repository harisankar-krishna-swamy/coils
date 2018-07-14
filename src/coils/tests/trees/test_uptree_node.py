'''
Created on Oct 28, 2015
@author: hari
'''
from __future__ import print_function
import unittest
from coils.trees.uptree import UpTreeNode

class UpTreeNode_Test_Default_Attributes(unittest.TestCase):
    def setUp(self):
        self._uptree_node = UpTreeNode()
    
    def test_default_attributes(self):
        self.assertEqual(self._uptree_node.node_count, 1, 'UpTree node default node count was not correct')
        self.assertEqual(self._uptree_node.parent_node, None, 'UpTree node default parent must be None')
        self.assertEqual(self._uptree_node.node_element, None, 'UpTree node default element must be None')
    def tearDown(self):
        self._uptree_node = None
    
class UpTreeNode_Test_Attributes_With_Predefined_Values(unittest.TestCase):
    def setUp(self):
        self._element = 2
        self._parent_node = UpTreeNode(node_element = 1)
        self._uptree_node = UpTreeNode(node_element = self._element, node_count = 1, 
                                                                     parent_node = self._parent_node)
    def test_default_attributes(self):
        self.assertEqual(self._uptree_node.node_count, 1, 'UpTree node node count was not correct')
        self.assertEqual(self._uptree_node.parent_node, self._parent_node, 'UpTree node parent did not add up')
        self.assertEqual(self._uptree_node.node_element, self._element, 'UpTree node element does not matchup')
        
    def tearDown(self):
        self._uptree_node = None

if __name__ == '__main__':
    print('UpTreeNode tests')
    unittest.main()