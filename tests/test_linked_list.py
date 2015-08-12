'''
Created on Aug 12, 2015
@author: topcat
'''
import unittest
from datastructures.LinkedList import LinkedList
from random import randint

class LinkedList_TestCase_Count_With_0_Elements(unittest.TestCase):
    
    def setUp(self):
        self._linkedList = LinkedList()
    
    def test_count_of_empty_list(self):
        self.assertEquals(self._linkedList.length, 0, 'Empty List length must be 0')
    
    def tearDown(self):
        self._linkedList = None
        
class LinkedList_TestCase_Count_With_4_Predictable_Elements(unittest.TestCase):
    
    def setUp(self):
        self._linkedList = LinkedList()
        self._linkedList.append(1)
        self._linkedList.append(2)
        self._linkedList.append(3)
        self._linkedList.append(4)
    
    def test_count_of_list(self):
        self.assertEquals(self._linkedList.length, 4, 'Empty List length must be 4')
    
    def tearDown(self):
        self._linkedList = None

class LinkedList_TestCase_Remove_Non_Existing_Element_From_0_Element_List(unittest.TestCase):
    
    def setUp(self):
        self._linkedList = LinkedList()
    
    def test_count_of_list(self):
        self._linkedList.remove(-1)
        self.assertEquals(self._linkedList.length, 0, 'Length must be 0 for empty list')
    
    def tearDown(self):
        self._linkedList = None

class LinkedList_TestCase_Remove_Non_Existing_Element_From_4_Element_List(unittest.TestCase):
    
    def setUp(self):
        self._linkedList = LinkedList()
        self._linkedList.append(1)
        self._linkedList.append(2)
        self._linkedList.append(3)
        self._linkedList.append(4)
    
    def test_count_of_list(self):
        self._linkedList.remove(-1)
        self.assertEquals(self._linkedList.length, 4, 'Length not valid after trying to remove non-existin element')

    def tearDown(self):
        self._linkedList = None

class LinkedList_TestCase_Remove_Middle_Element_From_4_Element_List(unittest.TestCase):
    
    def setUp(self):
        self._linkedList = LinkedList()
        self._linkedList.append(1)
        self._linkedList.append(2)
        self._linkedList.append(3)
        self._linkedList.append(4)
    
    def test_count_of_list(self):
        self._linkedList.remove(3)
        self.assertEquals(self._linkedList.length, 3, 'Length not valid after trying to remove non-existin element')

    def tearDown(self):
        self._linkedList = None

class LinkedList_TestCase_IndexOf_Element_In_Empty_List(unittest.TestCase):
    
    def setUp(self):
        self._linkedList = LinkedList()
    
    def test_index(self):
        index = self._linkedList.index(8)
        self.assertEquals(index, -1, 'Non existing element has index -1')

    def tearDown(self):
        self._linkedList = None

class LinkedList_TestCase_IndexOf_Elements_In_4_Element_List(unittest.TestCase):
    
    def setUp(self):
        self._linkedList = LinkedList()
        self._linkedList.append(1)
        self._linkedList.append(2)
        self._linkedList.append(3)
        self._linkedList.append(4)
    
    def test_index(self):
        for element in range(1, 5):
            index = self._linkedList.index(element)
            self.assertEquals(index + 1, element, 'index failed for element')

    def tearDown(self):
        self._linkedList = None    

class LinkedList_TestCase_Operations_On_List_with_1000_Random_Elements(unittest.TestCase):
    def setUp(self):
        self._linked_list = LinkedList()
        self._shadow_list = []
        for i in range(10):
            random_element = randint(0, 1000)
            self._linked_list.append(random_element)
            self._shadow_list.append(random_element)#will keep track of count and index 
    
    def test_count_index_remove_index_count_on_each_removal(self):
        """
        Check count, index before and after each predictable removal operation 
        """
        for i in self._shadow_list[:]:
            self.assertEquals(self._linked_list.length, len(self._shadow_list))
            
            self.assertEquals(self._linked_list.index(i), self._shadow_list.index(i))
            
            self._shadow_list.remove(i)
            self._linked_list.remove(i)
            
            try:
                self._shadow_list.index(i)
                self.assertEquals(self._linked_list.index(i), self._shadow_list.index(i))
            except ValueError:
                self.assertEquals(self._linked_list.index(i), -1)
            
            self.assertEquals(self._linked_list.length, len(self._shadow_list))