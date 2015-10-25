'''
Created on Oct 25, 2015
@author: hari
'''
from datastructures.lists.doubly_linked_list import DoublyLinkedList

def print_list(double_link_list):
    elements_in_list = []
    #iterate over the list
    for element in double_link_list:
        elements_in_list.append(element)
    print 'List is now %s' % elements_in_list
    #length of the list
    print 'Length of the list is %s' % len(double_link_list)

def print_reverse_list(double_link_list):
    elements_in_list = []
    #iterate over the list
    for element in reversed(double_link_list):
        elements_in_list.append(element)
    print 'Reversed List is now %s' % elements_in_list
    #length of the list
    print 'Length of the list is %s' % len(double_link_list)
    
    
if __name__ == '__main__':
    double_link_list = DoublyLinkedList()
    
    #add one element
    print 'Adding element 1 to list'
    double_link_list.append(1)
    
    #we add the following list (iterable) of elements
    print 'Adding elements 2 ,3 , 4, 5, 6, 7, 8, 9, 10'
    elements = [2 ,3 , 4, 5, 6, 7, 8, 9, 10]
    double_link_list.extend(elements)
    
    #head
    print 'Head of list is: %s' % str(double_link_list.head)
    
    #tail
    print 'Tail of list is: %s' % str(double_link_list.tail)
    print 'Print list by iterating'
    
    #Find an element's index
    element = 4
    element_index = double_link_list.index(element)
    if element_index == -1:
        print 'Element %s was not found on list' % str(element)
    else:
        print 'Element %s found at index %s' % (str(element), str(element_index))
        
    #Lets delete 7
    print 'Deleting 7'
    element_to_remove = 7
    double_link_list.remove(element_to_remove)
    
    #Try to find it.
    print 'Trying to find %s' % str(element_to_remove)
    index_of_deleted = double_link_list.index(element_to_remove)
    print 'Index of deleted element is %s' % str(index_of_deleted)
    #print list again
    print_list(double_link_list)  
    
    #
    #Lets insert 7 at index 5
    print 'Insert 7 into the list at index 4'
    element_to_insert = 7
    index_at = 5
    double_link_list.insert_at(index = index_at, element = element_to_insert)
    print_list(double_link_list)
    
    # Removing duplicates
    print 'Removing duplicates'
    double_link_list = DoublyLinkedList()
    double_link_list.extend([1, 1, 2, 3, 4, 4, 5, 6, 6, 7, 8, 9, 10, 10])
    print_list(double_link_list)
    double_link_list.remove_duplicates()
    print_list(double_link_list)
    
    #Reverse print list using reversed
    print_reverse_list(double_link_list)