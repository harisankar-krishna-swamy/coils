'''
Created on Oct 28, 2015
@author: hari
'''
from coils.hashtables.hashbuckets import SplayedHashBucket
from coils.hashtables.HashTables import SeperateChainHashTable
from coils.trees.uptree import UpTreeNode

class DisjointSetWithUnion(object):
    '''
    A disjoint set forest has disjoint sets where each set is represented by an uptree.
    
    A disjoint set DJS has a number of elements from a fixed Universe U. DJS knows all the elements in it.
    The elements in DJS may themselves form subsets. i.e U = { a, b, c, d, r, f, g}. DJS can be
    { {a, g}, {b}, {d}, {c, r, f} }. Disjoint set allows 3 operations.
    
    1) make_set(x) returns a new set {x}
    2) find(x) return R such that x is in set R. for example {c, r, f} be identified by c. then find(r) = c
    3) union(s, t): merges the smaller set into the larger. {c} U {r, f} = {c, r, f}
    for more info please refer Datastructures and their algorithms by Harry Lewis and Larry Denenberg
    
    uptree nodes are used to represent the individual items of the set.
    1) Each item needs to be known just like that in the set. We use a hash tabe where table[item] = UpTree Node for the item
    2) make_set(item) just creates an uptree node with item. Each node starts off as a tree rooted at node.   
    '''
    def __init__(self):
        self._table_of_uptrees = SeperateChainHashTable(bucket_type_class = SplayedHashBucket)
    
    def make_set(self, item = None):
        if item == None:
            return None
        uptree_node = UpTreeNode(node_element = item)#single node tree
        self._table_of_uptrees[item] = uptree_node
        return uptree_node
    
    def _uptree_find_with_path_compression(self, item = None):
        '''
        Return the root of the uptree to which item belongs. Compress the path before leaving.
        '''
        uptree_node_with_item = self._table_of_uptrees.get(item, None)
        if uptree_node_with_item == None:
            raise KeyError('Key Error: %s ' % repr(item))
        #before returning the root node element, we set the parent of the original node to the parent.
        current_node = uptree_node_with_item
        while current_node.parent_node != None:
            current_node = current_node.parent_node
        #we have root node
        root_of_uptree = current_node
        #compress path
        current_node = uptree_node_with_item
        parent_of_current_node = current_node.parent_node 
        while current_node != root_of_uptree:
            parent_of_current_node = current_node.parent_node
            current_node.parent_node = root_of_uptree
            current_node = parent_of_current_node
            
        return root_of_uptree
        
    def find(self, item):
        '''
        returns the set to which this item belongs.
        '''
        try:
            root_node = self._uptree_find_with_path_compression(item)
        except KeyError:
            return  None
        return root_node.node_element
        
    def union(self, item_1 = None, item_2 = None):
        '''
        Finds the set for item_1 and item_2. Merges the two and returns the larger set.
        '''
        if item_1 == None or item_2 == None:
            return None
        
        uptree_1 = self._uptree_find_with_path_compression(item = item_1)#root actually
        uptree_2 = self._uptree_find_with_path_compression(item = item_2)#root actually
        
        #return the remaining dominating tree as first element of the tuple
        if uptree_1.node_count >= uptree_2.node_count:
            uptree_2.parent_node = uptree_1
            uptree_1.node_count = uptree_1.node_count + uptree_2.node_count
            return uptree_1.node_element
        else:
            uptree_1.parent_node = uptree_2
            uptree_2.node_count = uptree_2.node_count + uptree_1.node_count
            return uptree_2