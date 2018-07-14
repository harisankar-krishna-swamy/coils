'''
Created on Aug 14, 2015
@author: topcat
'''
from __future__ import print_function
import unittest
from coils.stackNqueues.stack import Stack

class Test_Empty_Stack_Initialization(unittest.TestCase):
    
    def setUp(self):
        self._stack = Stack()
    
    def test_stack_size_is_zero(self):
        self.assertEqual(self._stack.size, 0, 'Empty stack size must be 0')
        
    def tearDown(self):
        del self._stack

class Test_Empty_Stack_Pop(unittest.TestCase):
    
    def setUp(self):
        self._stack = Stack()
    
    def test_empty_stack_pop(self):
        self.assertEqual(self._stack.pop(), None, 'Empty stack must pop None')
                
    def tearDown(self):
        del self._stack

class Test_Empty_Stack_Top(unittest.TestCase):
        
    def setUp(self):
        self._stack = Stack()
    
    def test_empty_stack_top(self):
        self.assertEqual(self._stack.top, None, 'Empty Stact top must be None')
                
    def tearDown(self):
        del self._stack


class Test_Predictable_Stack_Size_With_4_Elements(unittest.TestCase):
    
    def setUp(self):
        self._stack = Stack()
        self._stack.push(1)
        self._stack.push(2)
        self._stack.push(3)
        self._stack.push(4)
    
    def test_stack_size_with_4_elements(self):
        self.assertEqual(self._stack.size, 4, 'NA')
                
    def tearDown(self):
        del self._stack

class Test_Predictable_Stack_Top_With_4_Elements(unittest.TestCase):
    
    def setUp(self):
        self._stack = Stack()
        self._stack.push(1)
        self._stack.push(2)
        self._stack.push(3)
        self._stack.push(4)
    
    def test_stack_top_with_4_elements(self):
        self.assertEqual(self._stack.top, 4, 'NA')
                
    def tearDown(self):
        del self._stack

class Test_Pop_To_Empty_With_Predictable_Stack_Of_4_Elements(unittest.TestCase):
    
    def setUp(self):
        self._stack = Stack()
        self._stack.push(1)
        self._stack.push(2)
        self._stack.push(3)
        self._stack.push(4)
    
    def test_pop_to_empty_stack_with_4_elements(self):
        self.assertEqual(self._stack.size, 4, 'NA')
        
        elements = [4, 3, 2, 1]
        for element in elements:#pop 4 times
            self.assertEqual(self._stack.pop(), element)
        
        self.assertEqual(self._stack.pop(), None, 'Empty stack must return None')
        self.assertEqual(self._stack.size, 0, 'NA')
            
    def tearDown(self):
        del self._stack

class Test_Iterator_With_Stack_Of_4_Elements(unittest.TestCase):
    
    def setUp(self):
        self._stack = Stack()
        self._stack.push(1)
        self._stack.push(2)
        self._stack.push(3)
        self._stack.push(4)
    
    def test_iterator_with_stack_with_4_elements(self):
        elements = [4, 3, 2, 1]
        for stack_element in self._stack:
            self.assertEqual(stack_element, elements[0], 'stack Iterator must match expected elements.')
            del elements[0]
            
    def tearDown(self):
        del self._stack
#Allows running as python run.
if __name__ == '__main__':
    print('stack Tests')
    unittest.main()