'''
Created on Aug 14, 2015
@author: topcat
'''
from unittest import TestCase
from datastructures.Queue import Queue

class TestCase_Size_Len_Of_Empty_Queue(TestCase):
    
    def setUp(self):
        self._q = Queue()
    
    def test_size_len_of_empty_queue(self):
        self.assertEquals(self._q.size, 0, 'Empty Q size must be 0')
        self.assertEquals(len(self._q), 0, 'Empty Q length must be 0')
    
    def tearDown(self):
        del self._q

class TestCase_Front_Of_Empty_Queue(TestCase):
    
    def setUp(self):
        self._q = Queue()
    
    def test_front_of_empty_queue(self):
        self.assertEquals(self._q.front, None, 'Empty Q front must be None')
    
    def tearDown(self):
        del self._q

class TestCase_Dequeue_Of_Empty_Queue(TestCase):
    
    def setUp(self):
        self._q = Queue()
    
    def test_dequeue_of_empty_queue(self):
        self.assertEquals(self._q.dequeue(), None, 'Empty Q dequeue must be None')
        
    def tearDown(self):
        del self._q
    
class TestCase_Front_Size_Len_Of_Predictable_Queue_With_1_Elements(TestCase):
    
    def setUp(self):
        self._q = Queue()
        self._q.enqueue(1)
    
    def test_front_of_queue_with_1_element(self):
        self.assertEquals(self._q.front, 1)
    
    def test_size_of_queue_with_1_element(self):
        self.assertEquals(self._q.size, 1)
    
    def test_len_of_queue_with_1_element(self):
        self.assertEquals(len(self._q), 1)
    
    def tearDown(self):
        del self._q

class TestCase_Front_Size_Len_While_Enqueuing_And_Dequeuing_A_Predictable_Queue_With_4_Elements(TestCase):
    
    def setUp(self):
        self._q = Queue()
        self.a_list = [] # use this to compare len size of queue as we enqueue and dequeue
        
    def test_front_size_len_with_enqueue_and_dequeue_of_4_element_queue(self):
         
        for i in range(4): # 0,1,2,3
            self.assertEqual(self._q.size, len(self.a_list))
            self.assertEqual(len(self._q), len(self.a_list))
            
            self._q.enqueue(i)
            self.a_list.append(i)
            
            self.assertEqual(self._q.size, len(self.a_list))
            self.assertEqual(len(self._q), len(self.a_list))
        #DEQUEUE
        for i in range(4): # 0,1,2,3
            self.assertEqual(self._q.size, len(self.a_list))
            self.assertEqual(len(self._q), len(self.a_list))
            
            self.assertEquals(self._q.dequeue(), self.a_list[0])
            del self.a_list[0]
            
            self.assertEqual(self._q.size, len(self.a_list))
            self.assertEqual(len(self._q), len(self.a_list))
    
    def tearDown(self):
        del self._q