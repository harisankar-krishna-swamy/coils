'''
Created on Aug 14, 2015
@author: topcat
'''
from __future__ import print_function
from builtins import range
import unittest
from coils.stackNqueues.queue import Queue

class Test_Len_Of_Empty_Queue(unittest.TestCase):
    
    def setUp(self):
        self._q = Queue()
    
    def test_len_of_empty_queue(self):
        self.assertEqual(len(self._q), 0, 'Empty Q length must be 0')
    
    def tearDown(self):
        del self._q

class Test_Front_Of_Empty_Queue(unittest.TestCase):
    
    def setUp(self):
        self._q = Queue()
    
    def test_front_of_empty_queue(self):
        self.assertEqual(self._q.front, None, 'Empty Q front must be None')
    
    def tearDown(self):
        del self._q

class Test_Dequeue_Of_Empty_Queue(unittest.TestCase):
    
    def setUp(self):
        self._q = Queue()
    
    def test_dequeue_of_empty_queue(self):
        self.assertEqual(self._q.dequeue(), None, 'Empty Q dequeue must be None')
        
    def tearDown(self):
        del self._q
    
class Test_Front_Len_Of_Predictable_Queue_With_1_Elements(unittest.TestCase):
    
    def setUp(self):
        self._q = Queue()
        self._q.enqueue(1)
    
    def test_front_of_queue_with_1_element(self):
        self.assertEqual(self._q.front, 1)
    
    def test_len_of_queue_with_1_element(self):
        self.assertEqual(len(self._q), 1)
    
    def tearDown(self):
        del self._q

class Test_Front_Len_While_Enqueuing_And_Dequeuing_A_Predictable_Queue_With_4_Elements(unittest.TestCase):
    
    def setUp(self):
        self._q = Queue()
        self.a_list = []  # use this to compare len size of queue as we enqueue and dequeue
        
    def test_front_len_with_enqueue_and_dequeue_of_4_element_queue(self):
         
        for i in range(4): # 0,1,2,3
            self.assertEqual(len(self._q), len(self.a_list))            
            self._q.enqueue(i)
            self.a_list.append(i)
            self.assertEqual(len(self._q), len(self.a_list))
            self.assertEqual(self._q.front, self.a_list[0]) #front remains same but we still check
        #DEQUEUE
        for i in range(4): # 0,1,2,3
            self.assertEqual(self._q.front, self.a_list[0])
            self.assertEqual(len(self._q), len(self.a_list))
            self.assertEqual(self._q.dequeue(), self.a_list[0])
            del self.a_list[0]
            self.assertEqual(len(self._q), len(self.a_list))
    
    def tearDown(self):
        del self._q
    
class Test_Iterator_Of_Predictable_Queue_With_4_Elements(unittest.TestCase):
    
    def setUp(self):
        self._q = Queue()
        self.a_list = [1,2,3,4]
        
        for element in self.a_list:
            self._q.enqueue(element)
    
    def test_iterator_of_queue_with_4_elements(self):
        for element in self._q:
            self.assertEqual(element, self.a_list[0], 'Iteration over Q did not give correct element')
            del self.a_list[0]
    def tearDown(self):
        del self._q
#Allows running as python run.
if __name__ == '__main__':
    print('queue tests')
    unittest.main()