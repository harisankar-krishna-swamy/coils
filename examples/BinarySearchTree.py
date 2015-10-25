'''
Created on Oct 25, 2015
@author: hari
'''
from coils.trees.BST import BinarySearchTree

def print_tree_inorder_using_stack(tree):
    traversed  = []
    for key, value in tree.inorder_traversal_with_stack():
        traversed.append((key, value))
    print 'Tree stack based preorder traversal (key, value) pairs:'
    print traversed


def print_tree_preorder(tree):
    traversed  = []
    for key, value in tree.traversal(want_pre_order = True):
        traversed.append((key, value))
    print 'Tree preorder traversal (key, value) pairs:'
    print traversed

def print_tree_postorder(tree):
    traversed  = []
    for key, value in tree.traversal(want_post_order = True):
        traversed.append((key, value))
    print 'Tree postorder traversal (key, value) pairs:'
    print traversed

def print_tree_inorder(tree):
    traversed  = []
    for key, value in tree.traversal(want_in_order = True):
        traversed.append((key, value))
    print 'Tree inorder traversal (key, value) pairs:'
    print traversed
    
if __name__ == '__main__':
    bst = BinarySearchTree()
    print 'Node count is %s' % str(bst.node_count)
    print 'Adding key value pairs (1, 1), (2, 2), .... (6, 6)'
    kvpairs = [(5, 5), (2, 2), (7, 7), (1, 1), (3, 3), (9, 9), (8, 8), (4, 4), (6, 6)]
    
    for kvpair in kvpairs:
        bst.insert(key = kvpair[0], obj = kvpair[1])
    
    print_tree_inorder(bst)
    print_tree_preorder(bst)
    print_tree_postorder(bst)
    
    #remove
    element_to_remove = 9
    print 'removing element %s' % str(element_to_remove) 
    bst.remove(key = element_to_remove)
    print_tree_inorder_using_stack(bst)
    
    #replace obj for a key
    key_to_replace = 1
    new_object_for_Key = 111
    
    bst.replace(key = key_to_replace, obj = new_object_for_Key)
    print_tree_inorder_using_stack(bst)
    
    
    