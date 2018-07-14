'''
Created on Oct 28, 2015
@author: hari
'''
from coils.hashtables.HashTables import SeperateChainHashTable
from coils.hashtables.hashbuckets import SplayedHashBucket

class UpTreeNode(object):
    '''
    Uptrees: Every node in the tree holds a reference to a parent node. Every node also holds the 
    number of nodes in the tree rooted at that node. This is used in disjoint set union find operations.
    '''
    __slots__ = 'node_element', 'node_count', 'parent_node' #attribute properties are already added by python slots
    def __init__(self, node_element = None, node_count = 1, parent_node = None):
        self.node_element = node_element
        self.node_count = node_count
        self.parent_node = parent_node
