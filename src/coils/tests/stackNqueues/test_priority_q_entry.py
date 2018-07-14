'''
Created on Oct 29, 2015
@author: hari
'''
from __future__ import print_function
import unittest
from coils.stackNqueues.priorityqueue import PriorityQueueEntry

class PriorityQ_Element_Test_Init(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        
    def test_priority_q_init(self):
        with self.assertRaises(ValueError):
            PriorityQueueEntry(item = None, priority = None)
        
    def tearDown(self):
        unittest.TestCase.tearDown(self)

class PriorityQ_Element_Test_Properties_With_None(unittest.TestCase):
    def setUp(self):
        pass 
        
    def test_priority_q_properties_with_none(self):
        with self.assertRaises(ValueError):
            PriorityQueueEntry(item = None, priority = 'Some Priority')
        with self.assertRaises(ValueError):
            PriorityQueueEntry(item = 'Some Item', priority = None)
        
    def tearDown(self):
        self._priority_q_entry = None

class PriorityQ_Element_Test_Properties_With_Known_Item_And_Priority(unittest.TestCase):
    def setUp(self):
        self._item = 'Some Item'
        self._priority = 100
        self._priority_q_entry = PriorityQueueEntry(item = self._item, priority = self._priority) 
        
    def test_priority_q_properties_with_known_properties(self):
        self.assertEqual(self._priority_q_entry.priority, self._priority, 'PriorityQ priority property did not matche expected')
        self.assertEqual(self._priority_q_entry.item, self._item, 'PriorityQ item property did not matche expected')
        
    def tearDown(self):
        self._priority_q_entry = None

class PriorityQ_Element_Test_Equality_of_Two_Entries(unittest.TestCase):
    def setUp(self):
        self._item_1 = 'Some Item'
        self._priority_1 = 100
        
        self._item_2 = 'Some Other Item with same priority'
        self._priority_2 = 100
        
        self._priority_q_entry_1 = PriorityQueueEntry(item = self._item_1, priority = self._priority_1) 
        self._priority_q_entry_2 = PriorityQueueEntry(item = self._item_2, priority = self._priority_2)
        
    def test_priority_q__test_equality_of_entries(self):
        self.assertEqual(self._priority_q_entry_1 == self._priority_q_entry_2, True, 'Priority Q entries with same priority did not pass equality')
        
    def tearDown(self):
        self._priority_q_entry = None


class PriorityQ_Element_Test_Greater_Than_And_Less_Than_Compare_of_Two_Entries(unittest.TestCase):
    def setUp(self):
        self._item_1 = 'Some Item'
        self._priority_1 = 100
        
        self._item_2 = 'Some Other Item with same priority'
        self._priority_2 = 101
        
        self._priority_q_entry_1 = PriorityQueueEntry(item = self._item_1, priority = self._priority_1) 
        self._priority_q_entry_2 = PriorityQueueEntry(item = self._item_2, priority = self._priority_2)
            
    def test_priority_q_test_greater_than_of_entries(self):
        self.assertEqual(self._priority_q_entry_2 > self._priority_q_entry_1, True, 'Priority Q entries did not pass greater than comparison')
    
    def test_priority_q_test_less_than_of_entries(self):
        self.assertEqual(self._priority_q_entry_1 < self._priority_q_entry_2, True, 'Priority Q entries did not pass less than comparison')
        
    def tearDown(self):
        self._priority_q_entry = None
        
if __name__ == '__main__':
    print('Priority Q entry tests')
    unittest.main()