'''
Created on Aug 5, 2015
@author: topcat
'''
import unittest

def assert_min_heap_property(heap_list):
    """
    Tests a list representation of a heap for heap property.
    """ 
    count = len(heap_list) - 1
    index = 1
    limit = count / 2

    while index <= limit:
        if heap_list[index] > heap_list[index *2]:
            return False
    
        if (index * 2 + 1) < count:
            if heap_list[2 * index + 1] > heap_list[index]:
                return False 
        
    return True
  
