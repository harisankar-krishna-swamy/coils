'''
Created on Aug 5, 2015
@author: topcat
'''
import unittest
from datastructures.Heap import Heap
from random import random, randint

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
            if heap_list[2 * index + 1] < heap_list[index]:
                return False 
        
        index = index * 2
        
    return True


class MinHeap_TestCase_Create_With_No_Element(unittest.TestCase):
    """
    Create only. No heap modification. No Elements.
    """    
    def setUp(self):
        self._heap = Heap()
        print self.__class__
        print 'Heap in setUp is %s' % str(self._heap)
    
    def test_heap_status(self):
        self.assertTrue(self._heap.isMinHeap(), 'Heap must be a min heap.')
        self.assertTrue(assert_min_heap_property(self._heap._getHeapAsList()), 'heap property must be satisfied.')
        self.assertTrue([None] == self._heap._getHeapAsList(), 'Heap contents are not same as expected.')
    
    def tearDown(self):
        unittest.TestCase.tearDown(self) 

class MinHeap_TestCase_Create_With_One_Element(unittest.TestCase):
    """
    Create only. No heap modification. Only one element.
    """    
    def setUp(self):
        self._heap = Heap()
        self._heap.addElement(3)
        print self.__class__
        print 'Heap in setUp is %s' % str(self._heap)
    
    def test_heap_status(self):
        self.assertTrue(self._heap.isMinHeap(), 'Heap must be a min heap.')
        self.assertTrue(assert_min_heap_property(self._heap._getHeapAsList()), 'heap property must be satisfied.')
        self.assertTrue([None, 3] == self._heap._getHeapAsList(), 'Heap contents are not same as expected.')
    
    def tearDown(self):
        unittest.TestCase.tearDown(self) 

class MinHeap_TestCase_Create_With_Predictable_SmallSet_Of_Elements(unittest.TestCase):
    """
    Create only. No heap modification. Small predictable set of elements.
    """
    def setUp(self):
        self._heap = Heap()
        self._heap.addElements([3, 1, 2])
        print self.__class__
        print 'Heap in setUp is %s' % str(self._heap)
    
    def test_heap_status(self):
        self.assertTrue(self._heap.isMinHeap(), 'Heap must be a min heap.')
        self.assertTrue(assert_min_heap_property(self._heap._getHeapAsList()), 'heap property must be satisfied.')
        self.assertTrue([None, 1, 3, 2] == self._heap._getHeapAsList(), 'Heap contents are not same as expected.')
    
    def tearDown(self):
        unittest.TestCase.tearDown(self)

class MinHeap_TestCase_1_Pop_With_Predictable_SmallSet_Of_Elements(unittest.TestCase):
    """
    Create only. No heap modification. Small predictable set of elements.
    """
    def setUp(self):
        self._heap = Heap()
        self._heap.addElements([3, 1, 2])
        print self.__class__
        print 'Heap in setUp is %s' % str(self._heap)
    
    def test_heap_status(self):
        self.assertTrue(self._heap.isMinHeap(), 'Heap must be a min heap.')
        self.assertTrue(assert_min_heap_property(self._heap._getHeapAsList()), 'heap property must be satisfied.')
        self.assertTrue([None, 1, 3, 2] == self._heap._getHeapAsList(), 'Heap contents are not same as expected.')
        #Pop
        print 'Removing %s from heap' % str(self._heap.getElement())
        print 'Heap is now %s' % str(self._heap)
        #
        self.assertTrue(assert_min_heap_property(self._heap._getHeapAsList()), 'heap property must be satisfied.')
        self.assertTrue([None, 2, 3] == self._heap._getHeapAsList(), 'Heap contents are not same as expected.')
    
    def tearDown(self):
        unittest.TestCase.tearDown(self)

class MinHeap_TestCase_2_Pops_With_Predictable_SmallSet_Of_Elements(unittest.TestCase):
    """
    Create only. No heap modification. Small predictable set of elements.
    """
    def setUp(self):
        self._heap = Heap()
        self._heap.addElements([3, 1, 2])
        print self.__class__
        print 'Heap in setUp is %s' % str(self._heap)
    
    def test_heap_status(self):
        self.assertTrue(self._heap.isMinHeap(), 'Heap must be a min heap.')
        self.assertTrue(assert_min_heap_property(self._heap._getHeapAsList()), 'heap property must be satisfied.')
        self.assertTrue([None, 1, 3, 2] == self._heap._getHeapAsList(), 'Heap contents are not same as expected.')
        #Pop
        print 'Removing %s from heap' % str(self._heap.getElement())
        print 'Removing %s from heap' % str(self._heap.getElement())
        print 'Heap is now %s' % str(self._heap)
        #
        self.assertTrue(assert_min_heap_property(self._heap._getHeapAsList()), 'heap property must be satisfied.')
        self.assertTrue([None, 3] == self._heap._getHeapAsList(), 'Heap contents are not same as expected.')
    
    def tearDown(self):
        unittest.TestCase.tearDown(self)
 

class MinHeap_TestCase_1000_Pops_With_RandomSet_Of_1000_Elements(unittest.TestCase):
    """
    Create only. No heap modification. Small predictable set of elements.
    """
    def setUp(self):
        import random
        self._heap = Heap(minHeap = True)
        print self.__class__
    
    def test_heap_status_on_push_pop(self):
        self.assertTrue(self._heap.isMinHeap(), 'Heap must be a min heap.')
        
        for i in range(1000):
            self._heap.addElement(randint(0, 1000))
            self.assertTrue(assert_min_heap_property(self._heap._getHeapAsList()), 'heap property must be satisfied.')
            
        print 'Heap has %s elements' % len(self._heap._getHeapAsList())
        
        #pop all
        for i in range(1000):
            self._heap.getElement()
            self.assertTrue(assert_min_heap_property(self._heap._getHeapAsList()), 'heap property must be satisfied.')
        
        print 'Heap has %s elements' % len(self._heap._getHeapAsList())
                
    def tearDown(self):
        unittest.TestCase.tearDown(self)