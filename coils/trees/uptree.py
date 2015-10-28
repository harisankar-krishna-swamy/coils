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

class UpTree(object):
    '''
    TODO: items in nodes must be hashable.
    '''
    __slots__ = 'root_node', 'hash_table_of_nodes'
    def __init__(self, root_node = None):
        if self.root_node == None:
            raise ValueError('UpTree root node cannot be None')
        self.root_node = root_node    
        self.hash_table_of_nodes = SeperateChainHashTable(bucket_type_class = SplayedHashBucket)
    @property
    def node_count(self):#wire this to the node's node count
        return self.root_node.node_count
    @node_count.setter
    def node_count(self, new_node_count):
        self.root_node.node_count = new_node_count 
    
    def iter(self):
        '''
        Iterating over an up tree gives us all the nodes in the tree
        '''
        for key in self.hash_table_of_nodes:
            yield self.hash_table_of_nodes[key]
    
    def _uptree_find_with_path_compression(self, item_to_find):
        '''
        lookup to hash table returns None?
        '''
        node_with_obj = self.hash_table_of_nodes.get(item_to_find, None)
        if node_with_obj == None:
            raise KeyError('Key Error: %s ' % repr(item_to_find))
        #before returning the root node element, we set the parent of the original node to the parent.
        #TODO do we just point all the nodes visited to the root instead of just the node to find?
        #TODO does this not make the node_count inconsistent except for root nodes?
        node_with_obj.parent = self.root_node
        return self.root_node.node_element
        
    def uptree_find(self, item_to_find):
        '''
        item_to_find: a hashable application object that is in the uptree.
        returns the set(root item) to which this item belongs.
        For example:tree be  
        '''
        return self._uptree_find_with_path_compression(item_to_find)
        
    def uptree_union(self, some_other_uptree = None):
        '''
        Takes some other uptree and merge small tree to larger tree. 
        Return (larger tree, smaller tree)
        '''
        if some_other_uptree == None:
            return (None, None)
        #return the remaining dominating tree as first element of the tuple
        if self.node_count >= some_other_uptree.node_count:
            some_other_uptree.root_node.parent = self.root_node
            self.node_count = self.node_count + some_other_uptree.node_count
            return (self, some_other_uptree)
        else:
            self.root_node.parent = some_other_uptree.root_node
            some_other_uptree.node_count = some_other_uptree.node_count + self.node_count
            return (some_other_uptree, self)