'''
Created on Oct 29, 2015
@author: hari
'''
from __future__ import print_function
from builtins import range
import unittest
from coils.stackNqueues.priorityqueue import PriorityQueue
import string

class Priority_Q_Min_Heap_Test_Empty_Q_Length(unittest.TestCase):
    def setUp(self):
        self._priorityQ = PriorityQueue(reverse_priority = True)
    
    def test_priority_q_length(self):
        self.assertEqual(len(self._priorityQ), 0, 'Empty priority Q length must be 0')
    
    def tearDown(self):
        self._priorityQ = None

class Priority_Q_Min_Heap_Test_Empty_Q_Iteration(unittest.TestCase):
    def setUp(self):
        self._priorityQ = PriorityQueue(reverse_priority = True)
    
    def test_priority_q_iteration(self):
        list_of_q_entries = []
        for item, priority in self._priorityQ:
            list_of_q_entries.append((item, priority))
            
        self.assertEqual(len(list_of_q_entries), 0, 'Empty priority Q iteration cannot yield anything')

    def tearDown(self):
        self._priorityQ = None

class Priority_Q_Min_Heap_Test_Q_Iteration(unittest.TestCase):
    def setUp(self):
        self._priorityQ = PriorityQueue(reverse_priority = True)
    
    def test_priority_q_iteration(self):
        list_of_q_entries = []
        for item, priority in self._priorityQ:
            list_of_q_entries.append((item, priority))
            
        self.assertEqual(len(list_of_q_entries), 0, 'Empty priority Q iteration cannot yield anything')

    def tearDown(self):
        self._priorityQ = None

class Priority_Q_Min_Heap_Test_Get_With_Empty_Q(unittest.TestCase):
    def setUp(self):
        self._priorityQ = PriorityQueue(reverse_priority = True)
        
    def test_priority_q_test_add_element(self):
        self.assertEqual(self._priorityQ.get(), None, 'Empty Q must return None on get op')
    
    def tearDown(self):
        self._priorityQ = None

class Priority_Q_Min_Heap_Test_Q_Add(unittest.TestCase):
    def setUp(self):
        self._item = 'Some Item'
        self._priority = 2
        self._priorityQ = PriorityQueue(reverse_priority = True)
        
    def test_priority_q_test_add_element(self):
        self._priorityQ.add_item(self._item, self._priority)
        self.assertEqual(len(self._priorityQ), 1, 'Priority Q length must be 1')
    
    def tearDown(self):
        self._priorityQ = None

class Priority_Q_Min_Heap_Test_Q_Add_And_Get_With_Single_Entry(unittest.TestCase):
    def setUp(self):
        self._item = 'Some Item'
        self._priority = 2
        self._priorityQ = PriorityQueue(reverse_priority = True)
        
    def test_priority_q_test_add__and_get(self):
        self._priorityQ.add_item(self._item, self._priority)
        item = self._priorityQ.get()
        self.assertEqual(item, self._item, 'Get op on priority Q did not yield expected item')
    
    def tearDown(self):
        self._priorityQ = None

class Priority_Q_Min_Heap_Test_Q_Iter_With_Single_Entry(unittest.TestCase):
    def setUp(self):
        self._item = 'Some Item'
        self._priority = 2
        self._priorityQ = PriorityQueue(reverse_priority = True)
        
    def test_priority_q_test_iter(self):
        self._priorityQ.add_item(item = self._item, priority = self._priority)
        expected_list_of_entries = [(self._item, self._priority)]
        list_of_q_entries = []
        
        for item, priority in self._priorityQ:
            list_of_q_entries.append((item, priority))
        
        self.assertEqual(list_of_q_entries, expected_list_of_entries, 'Priority Q iteration did not yield expected entries')
        
    def tearDown(self):
        self._priorityQ = None

class Priority_Q_Min_Heap_Test_Add_Get_Multiple_Entries(unittest.TestCase):
    def setUp(self):
        self._item_priority_entries = []
        
        for letter in string.uppercase:#build letter, ord(letter) tuples
            self._item_priority_entries.append((letter, ord(letter)))
             
        self._priorityQ = PriorityQueue(reverse_priority = True)
        
        self._expected_order_of_items_from_get = []
        for letter in string.uppercase:#build Z, Y, X, .....C, B , A because this is a max heap.
            self._expected_order_of_items_from_get.append(letter)
        
    def test_add_get_multiple_entries(self):
        for item, priority in self._item_priority_entries:
            self._priorityQ.add_item(item, priority)
            
        items_from_q = []
        for i in range(len(self._item_priority_entries)):#get this many items from the Q
            items_from_q.append(self._priorityQ.get())
            
        self.assertEqual(items_from_q, self._expected_order_of_items_from_get, 'Items from priority Q did not match expected list.')
    def tearDown(self):
        self._priorityQ = None


class Priority_Q_Min_Heap_Test_Iteration_With_Multiple_Entries(unittest.TestCase):
    def setUp(self):
        self._item_priority_entries = []
        
        for letter in string.uppercase:#build letter, ord(letter) tuples
            self._item_priority_entries.append((letter, ord(letter)))
             
        self._priorityQ = PriorityQueue(reverse_priority = True)
        
        self._expected_item_priority_pairs = []
        for letter in string.uppercase:
            self._expected_item_priority_pairs.append((letter, ord(letter)) )
        
    def test_iteration_with_multiple_entries(self):
        for item, priority in self._item_priority_entries:
            self._priorityQ.add_item(item, priority)
            
        items_and_priorities_pairs_from_q = []
        for item, priority in self._priorityQ:
            items_and_priorities_pairs_from_q.append((item, priority))
        
        self.assertEqual(items_and_priorities_pairs_from_q, self._expected_item_priority_pairs, 'Iteration on priority Q did not yield expected (item, priority) list')
        
    def tearDown(self):
        self._priorityQ = None

if __name__ == '__main__':
    print('Priority Q with Min Heap tests')
    unittest.main()