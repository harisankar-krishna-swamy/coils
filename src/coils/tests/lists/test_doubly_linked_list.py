'''
Created on Oct 24, 2015
@author: hari
'''
from __future__ import print_function
from builtins import range
import unittest
from coils.lists.doubly_linked_list import DoublyLinkedList
from random import randint

class DoublyDoublyLinkedList_Test_Count_With_0_Elements(unittest.TestCase):
    
    def setUp(self):
        self._doubly_linkedList = DoublyLinkedList()
    
    def test_count_of_empty_list(self):
        self.assertEquals(self._doubly_linkedList.length, 0, 'Empty List length must be 0')
    
    def tearDown(self):
        self._doubly_linkedList = None

class DoublyDoublyLinkedList_Test_Head_n_Tail_With_0_Elements(unittest.TestCase):
    
    def setUp(self):
        self._doubly_linkedList = DoublyLinkedList()
    
    def test_count_of_empty_list(self):
        self.assertEquals(self._doubly_linkedList.head, None, 'Head of 0 element list must be None')
        self.assertEquals(self._doubly_linkedList.tail, None, 'Tail of 0 element list must be None')
    
    def tearDown(self):
        self._doubly_linkedList = None
    
        
class DoublyDoublyLinkedList_Test_Count_With_4_Predictable_Elements(unittest.TestCase):
    
    def setUp(self):
        self._doubly_linkedList = DoublyLinkedList()
        self._doubly_linkedList.append(1)
        self._doubly_linkedList.append(2)
        self._doubly_linkedList.append(3)
        self._doubly_linkedList.append(4)
    
    def test_count_of_list(self):
        self.assertEquals(self._doubly_linkedList.length, 4, 'Empty List length must be 4')
    
    def tearDown(self):
        self._doubly_linkedList = None

class DoublyDoublyLinkedList_Test_Remove_Non_Existing_Element_From_0_Element_List(unittest.TestCase):
    
    def setUp(self):
        self._doubly_linkedList = DoublyLinkedList()
    
    def test_count_of_list(self):
        self._doubly_linkedList.remove(-1)
        self.assertEquals(self._doubly_linkedList.length, 0, 'Length must be 0 for empty list')
    
    def tearDown(self):
        self._doubly_linkedList = None

class DoublyDoublyLinkedList_Test_Remove_Non_Existing_Element_From_4_Element_List(unittest.TestCase):
    
    def setUp(self):
        self._doubly_linkedList = DoublyLinkedList()
        self._doubly_linkedList.append(1)
        self._doubly_linkedList.append(2)
        self._doubly_linkedList.append(3)
        self._doubly_linkedList.append(4)
    
    def test_count_of_list(self):
        self._doubly_linkedList.remove(-1)
        self.assertEquals(self._doubly_linkedList.length, 4, 'Length not valid after trying to remove non-existing element')

    def tearDown(self):
        self._doubly_linkedList = None

class DoublyDoublyLinkedList_Test_Remove_Middle_Element_From_4_Element_List(unittest.TestCase):
    
    def setUp(self):
        self._doubly_linkedList = DoublyLinkedList()
        self._doubly_linkedList.append(1)
        self._doubly_linkedList.append(2)
        self._doubly_linkedList.append(3)
        self._doubly_linkedList.append(4)
    
    def test_count_of_list(self):
        self._doubly_linkedList.remove(3)
        self.assertEquals(self._doubly_linkedList.length, 3, 'Length not valid after trying to remove non-existin element')

    def tearDown(self):
        self._doubly_linkedList = None

class DoublyDoublyLinkedList_Test_IndexOf_Element_In_Empty_List(unittest.TestCase):
    
    def setUp(self):
        self._doubly_linkedList = DoublyLinkedList()
    
    def test_index(self):
        index = self._doubly_linkedList.index(8)
        self.assertEquals(index, -1, 'Non existing element has index -1')

    def tearDown(self):
        self._doubly_linkedList = None

class DoublyDoublyLinkedList_Test_IndexOf_Elements_In_4_Element_List(unittest.TestCase):
    
    def setUp(self):
        self._doubly_linkedList = DoublyLinkedList()
        self._doubly_linkedList.append(1)
        self._doubly_linkedList.append(2)
        self._doubly_linkedList.append(3)
        self._doubly_linkedList.append(4)
    
    def test_index(self):
        for element in range(1, 5):
            index = self._doubly_linkedList.index(element)
            self.assertEquals(index + 1, element, 'index failed for element')

    def tearDown(self):
        self._doubly_linkedList = None    

class DoublyDoublyLinkedList_Test_Operations_On_List_with_1000_Random_Elements(unittest.TestCase):
    def setUp(self):
        self._linked_list = DoublyLinkedList()
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

class DoublyDoublyLinkedList_Test_extend_With_Predictable_Elements(unittest.TestCase):
    '''
    Test the extend operation of LinkedList. 
    a) Create 2 lists. 
    b) Add the second list to the end of the first list. 
    c) Check the indices of the newly added elements.
    '''
    
    def setUp(self):
        self._doubly_linkedList = DoublyLinkedList()
        self._doubly_linkedList.append(1)
        self._doubly_linkedList.append(2)
        self._doubly_linkedList.append(3)
        self._doubly_linkedList.append(4)
        #create a second linkedlist with 5, 6, 7
        self._secondList = DoublyLinkedList()
        self._secondList.append(5)
        self._secondList.append(6)
        self._secondList.append(7)
        
    def test_extend_of_list(self):
        self.assertEquals(self._doubly_linkedList.length, 4, 'Original list before extend must be 4')
        count_before_extend = self._doubly_linkedList.length
        next_index_will_be = count_before_extend
        self._doubly_linkedList.extend(self._secondList)
        #check new length
        self.assertEquals(self._doubly_linkedList.length, count_before_extend + self._secondList.length, 'New length after extend must add up.')
        #check if the elements of shadow list are present
        for element in self._secondList:
            self.assertEqual(self._doubly_linkedList.index(element), next_index_will_be
                             , 'Indices of new elements after extend must add up')
            next_index_will_be += 1
    
    def tearDown(self):
        self._doubly_linkedList = None
        self._secondList = None

class DoublyDoublyLinkedList_Test_Check_Tail_On_Remove_In_4_Element_List(unittest.TestCase):
    
    def setUp(self):
        self._doubly_linkedList = DoublyLinkedList()
        self._doubly_linkedList.append(1)
        self._doubly_linkedList.append(2)
        self._doubly_linkedList.append(3)
        self._doubly_linkedList.append(4)
    
    def test_tail_node_on_remove(self):
        self._doubly_linkedList.remove(1)#removed head. Tail must be same node 
        self.assertEqual(self._doubly_linkedList.tail, 4)
        #Now list is [2, 3, 4]
        self._doubly_linkedList.remove(4)#tail should next be 3
        self.assertEqual(self._doubly_linkedList.tail, 3, 'Tail must be adjusted on deletion of last node')
        #Now list is [2, 3]
        self._doubly_linkedList.remove(2)#tail should next be 3
        self.assertEqual(self._doubly_linkedList.tail, 3, 'Tail must be adjusted on deletion of last node')
        #Now list is [3]
        self._doubly_linkedList.remove(3)#tail should next be None
        self.assertEqual(self._doubly_linkedList.tail, None, 'Tail must be None on empty list')
    def tearDown(self):
        self._doubly_linkedList = None    

class DoublyDoublyLinkedList_Test_Check_Head_On_Remove_In_4_Element_List(unittest.TestCase):

    def setUp(self):
        self._doubly_linkedList = DoublyLinkedList()
        self._doubly_linkedList.append(1)
        self._doubly_linkedList.append(2)
        self._doubly_linkedList.append(3)
        self._doubly_linkedList.append(4)
    
    def test_tail_node_on_remove(self):
        #list is [1, 2, 3, 4]
        self._doubly_linkedList.remove(3)#removed head. Head must be same node 
        self.assertEqual(self._doubly_linkedList.head, 1)
        #Now list is [1, 2, 4]
        self._doubly_linkedList.remove(1)#head should next be 2
        self.assertEqual(self._doubly_linkedList.head, 2, 'head must be adjusted on deletion of first node')
        #Now list is [2, 4]
        self._doubly_linkedList.remove(2)#head should next be 4
        self.assertEqual(self._doubly_linkedList.head, 4, 'head must be adjusted on deletion of first node')
        #Now list is [4]
        self._doubly_linkedList.remove(4)#head should next be None
        self.assertEqual(self._doubly_linkedList.head, None, 'Head must be None on empty list')
        
    def tearDown(self):
        self._doubly_linkedList = None    

class DoublyDoublyLinkedList_Test_Insert_At_0_With_0_Elements(unittest.TestCase):
    
    def setUp(self):
        self._doubly_linkedList = DoublyLinkedList()
    
    def test_insert_at_0_of_empty_list(self):
        self._doubly_linkedList.insert_at(0, 20)
        self.assertEquals(self._doubly_linkedList.length, 1, 'list length must be 1 after inserting to empty list')
        self.assertEquals(self._doubly_linkedList.head, self._doubly_linkedList.tail, 'list length must be same node after inserting to empty list')
    
    def tearDown(self):
        self._doubly_linkedList = None

class DoublyDoublyLinkedList_Test_Insert_At_Negative_Index_With_0_Elements(unittest.TestCase):
    
    def setUp(self):
        self._doubly_linkedList = DoublyLinkedList()
    
    def test_insert_at_negative_index_of_empty_list(self):
        self._doubly_linkedList.insert_at(-2, 20)
        self.assertEquals(self._doubly_linkedList.length, 1, 'list length must be 1 after inserting to empty list at negative index')
        self.assertEquals(self._doubly_linkedList._head, self._doubly_linkedList._tail, 'list length must be same node after inserting to empty list at negative index')
    
    def tearDown(self):
        self._doubly_linkedList = None

class DoublyDoublyLinkedList_Test_Insert_At_Index_Larger_Than_Length_With_0_Elements(unittest.TestCase):
    
    def setUp(self):
        self._doubly_linkedList = DoublyLinkedList()
    
    def test_insert_at_negative_index_of_empty_list(self):
        self._doubly_linkedList.insert_at(100, 20)
        self.assertEquals(self._doubly_linkedList.length, 1, 'list length must be 1 after inserting to empty list at huge index')
        self.assertEquals(self._doubly_linkedList.head, self._doubly_linkedList.tail, 'list length must be same node after inserting to empty list at huge index')
    
    def tearDown(self):
        self._doubly_linkedList = None

class DoublyDoublyLinkedList_Test_Insert_At_Index_Larger_Than_Length_With_4_Elements(unittest.TestCase):
    
    def setUp(self):
        self._doubly_linkedList = DoublyLinkedList()
        self._doubly_linkedList.append(1)
        self._doubly_linkedList.append(2)
        self._doubly_linkedList.append(3)
        self._doubly_linkedList.append(4)
        
    def test_insert_at_negative_index_of_empty_list(self):
        expected_length = self._doubly_linkedList.length + 1
        element_to_insert = 20
        self._doubly_linkedList.insert_at(100, element_to_insert)
        self.assertEquals(self._doubly_linkedList.length, expected_length, 'list length did not tally after insert at huge index')
        self.assertEquals(self._doubly_linkedList.tail, element_to_insert, 'list tail must be same as new element inserted at huge index')
        self.assertEquals(self._doubly_linkedList.index(20), expected_length - 1, 'index of new element did not add up')
    
    def tearDown(self):
        self._doubly_linkedList = None


class DoublyDoublyLinkedList_Test_Insert_At_Index_In_Middle_With_4_Elements(unittest.TestCase):
    
    def setUp(self):
        self._doubly_linkedList = DoublyLinkedList()
        self._doubly_linkedList.append(1)
        self._doubly_linkedList.append(2)
        self._doubly_linkedList.append(4)
        self._doubly_linkedList.append(5)
        
    def test_insert_at_negative_index_of_empty_list(self):
        expected_length = self._doubly_linkedList.length + 1
        element_to_insert = 3
        insert_at_index = 2
        self._doubly_linkedList.insert_at(insert_at_index, element_to_insert)# list will become 1, 2, 3, 4, 5
        self.assertEquals(self._doubly_linkedList.length, expected_length, 'list length did not tally after insert in the middle')
        self.assertEquals(self._doubly_linkedList.index(3), insert_at_index, 'index of new element is not where we insert it at!')
        
        #iterate and check
        expected_list = []
        for element in self._doubly_linkedList:
            expected_list.append(element)
        self.assertEquals(expected_list, [1, 2, 3, 4, 5], 'List was not same as expected after insert At index')
    
    def tearDown(self):
        self._doubly_linkedList = None
#
# Tests for remover duplicates. Need to check head and tail refs directly rather than elements.
#
class DoublyDoublyLinkedList_Test_Remove_Duplicates_With_0_Elements(unittest.TestCase):
    
    def setUp(self):
        self._doubly_linkedList = DoublyLinkedList()
    
    def test_remove_duplicate_of_empty_list(self):
        self._doubly_linkedList.remove_duplicates()
        
    def tearDown(self):
        self._doubly_linkedList = None

class DoublyDoublyLinkedList_Test_Remove_Duplicates_With_1_Elements(unittest.TestCase):
    
    def setUp(self):
        self._doubly_linkedList = DoublyLinkedList()
        element_to_append = 1
        self._doubly_linkedList.append(element_to_append)
        
    def test_remove_duplicate_of_list_with_1_element(self):
        old_head = self._doubly_linkedList._head
        expected_tail = old_head
        
        self._doubly_linkedList.remove_duplicates()
        expected_length = 1
        self.assertEqual(self._doubly_linkedList.length, expected_length, 'list length did not add up after removing duplicates')
        self.assertEqual(self._doubly_linkedList._head, old_head, 'list head did not add up after removing duplicates')
        self.assertEqual(self._doubly_linkedList._tail, expected_tail, 'list tail did not add up after removing duplicates')
        
        
    def tearDown(self):
        self._doubly_linkedList = None

class DoublyDoublyLinkedList_Test_Remove_Duplicates_With_2_Identical_Elements(unittest.TestCase):
    
    def setUp(self):
        self._doubly_linkedList = DoublyLinkedList()
        element_to_append = 1
        self._doubly_linkedList.append(element_to_append)
        self._doubly_linkedList.append(element_to_append)
        
    def test_remove_duplicates_of_list_with_2_identical_elements(self):
        old_head = self._doubly_linkedList._head
        expected_tail = old_head
        
        self._doubly_linkedList.remove_duplicates()
        expected_length = 1
        self.assertEqual(self._doubly_linkedList.length, expected_length, 'list length did not add up after removing duplicates')
        self.assertEqual(self._doubly_linkedList._head, old_head, 'list head did not add up after removing duplicates')
        self.assertEqual(self._doubly_linkedList._tail, expected_tail, 'list tail did not add up after removing duplicates')
        
    def tearDown(self):
        self._doubly_linkedList = None
        
class DoublyDoublyLinkedList_Test_Remove_Duplicates_With_Duplicates_At_Head(unittest.TestCase):
    
    def setUp(self):
        #build [1, 1, 1, 2]
        self._doubly_linkedList = DoublyLinkedList()
        element_to_append = 1
        self._doubly_linkedList.extend([element_to_append, element_to_append, element_to_append])
        tail_element = 2
        self._doubly_linkedList.append(tail_element)
        
    def test_remove_duplicates_of_list_with_2_identical_elements(self):
        expected_head = self._doubly_linkedList._head
        expected_tail = self._doubly_linkedList._tail
        
        self._doubly_linkedList.remove_duplicates()
        expected_length = 2
        self.assertEqual(self._doubly_linkedList._length, expected_length, 'list length did not add up after removing duplicates')
        self.assertEqual(self._doubly_linkedList._head, expected_head, 'list head did not add up after removing duplicates')
        self.assertEqual(self._doubly_linkedList._tail, expected_tail, 'list tail did not add up after removing duplicates')
        
    def tearDown(self):
        self._doubly_linkedList = None

class DoublyDoublyLinkedList_Test_Remove_Duplicates_With_Duplicates_At_Tail(unittest.TestCase):
    
    def setUp(self):
        #build [2, 1, 1, 1]
        self._doubly_linkedList = DoublyLinkedList()
        self._doubly_linkedList.append(2)
        element_to_append = 1
        self._doubly_linkedList.extend([element_to_append, element_to_append, element_to_append])
        
    def test_remove_duplicates_of_list_with_2_identical_elements(self):
        expected_head = self._doubly_linkedList._head
        expected_tail = self._doubly_linkedList._head.next_node
        
        self._doubly_linkedList.remove_duplicates()
        expected_length = 2
        self.assertEqual(self._doubly_linkedList.length, expected_length, 'list length did not add up after removing duplicates')
        self.assertEqual(self._doubly_linkedList._head, expected_head, 'list head did not add up after removing duplicates')
        self.assertEqual(self._doubly_linkedList._tail, expected_tail, 'list tail did not add up after removing duplicates')
        
    def tearDown(self):
        self._doubly_linkedList = None

class DoublyDoublyLinkedList_Test_Remove_Duplicates_With_Duplicates_At_Middle(unittest.TestCase):
    
    def setUp(self):
        #build [2, 1, 1, 1, 3]
        self._doubly_linkedList = DoublyLinkedList()
        self._doubly_linkedList.append(2)
        element_to_append = 1
        self._doubly_linkedList.extend([element_to_append, element_to_append, element_to_append])
        self._doubly_linkedList.append(3)
        
    def test_remove_duplicates_of_list_with_2_duplicates_in_Middle(self):
        expected_head = self._doubly_linkedList._head
        expected_tail = self._doubly_linkedList._tail
        
        self._doubly_linkedList.remove_duplicates()
        expected_length = 3
        self.assertEqual(self._doubly_linkedList.length, expected_length, 'list length did not add up after removing duplicates')
        self.assertEqual(self._doubly_linkedList._head, expected_head, 'list head did not add up after removing duplicates')
        self.assertEqual(self._doubly_linkedList._tail, expected_tail, 'list tail did not add up after removing duplicates')
        
    def tearDown(self):
        self._doubly_linkedList = None

class DoublyDoublyLinkedList_Test_Remove_Duplicates_With_Recurring_Duplicates(unittest.TestCase):
    
    def setUp(self):
        #build [2, 1, 1, 1, 3, 1, 1, 1, 4]
        self._doubly_linkedList = DoublyLinkedList()
        self._doubly_linkedList.append(2)
        element_to_append = 1
        self._doubly_linkedList.extend([element_to_append, element_to_append, element_to_append])
        self._doubly_linkedList.append(3)
        self._doubly_linkedList.extend([element_to_append, element_to_append, element_to_append])
        self._doubly_linkedList.append(4)
        
    def test_remove_duplicates_of_list_with_recurring_duplicates(self):
        expected_head = self._doubly_linkedList._head
        expected_tail = self._doubly_linkedList._tail
        
        self._doubly_linkedList.remove_duplicates()
        expected_length = 4
        self.assertEqual(self._doubly_linkedList.length, expected_length, 'list length did not add up after removing duplicates')
        self.assertEqual(self._doubly_linkedList._head, expected_head, 'list head did not add up after removing duplicates')
        self.assertEqual(self._doubly_linkedList._tail, expected_tail, 'list tail did not add up after removing duplicates')
        
    def tearDown(self):
        self._doubly_linkedList = None
#
# Test Reverse Iteration
#
class DoublyDoublyLinkedList_Test_Reverse_Iteration_With_0_Elements(unittest.TestCase):
    
    def setUp(self):
        self._doubly_linkedList = DoublyLinkedList()
    
    def test_reverse_iteration_of_empty_list(self):
        reverse_iter_of_list = [] 
        for element in reversed(self._doubly_linkedList):
            reverse_iter_of_list.append(element)

        self.assertEquals(len(reverse_iter_of_list), 0, 'Reverse iteration on empty list gives non-empty values!')
        
    def tearDown(self):
        self._doubly_linkedList = None
        
class DoublyLinkedList_Test_Reverse_Iteration_With_1_Elements(unittest.TestCase):
    
    def setUp(self):
        self._doubly_linkedList = DoublyLinkedList()
        self._doubly_linkedList.append(1)
    
    def test_reverse_iteration_of_1_element_list(self):
        expected_reverse_iter_list  = [1] 
        reverse_iter_of_list = [] 
        for element in reversed(self._doubly_linkedList):
            reverse_iter_of_list.append(element)

        self.assertEquals(reverse_iter_of_list, expected_reverse_iter_list, 'reverse iteration did not yield expected list')
        
    def tearDown(self):
        self._doubly_linkedList = None

class DoublyLinkedList_Test_Reverse_Iteration_With_multiple_Elements(unittest.TestCase):
    
    def setUp(self):
        self._doubly_linkedList = DoublyLinkedList()
        extend_elements = [1, 2, 3, 4]
        self._doubly_linkedList.extend(extend_elements)
    
    def test_reverse_iteration_with_multiple_elements(self):
        expected_reverse_iter_list  = [4, 3, 2, 1] 
        reverse_iter_of_list = [] 
        for element in reversed(self._doubly_linkedList):
            reverse_iter_of_list.append(element)

        self.assertEquals(reverse_iter_of_list, expected_reverse_iter_list, 'reverse iteration did not yield expected list')
        
    def tearDown(self):
        self._doubly_linkedList = None
#
# Test __getitem__
#
class DoublyDoublyLinkedList_Test_get_item_With_0_Elements(unittest.TestCase):
    
    def setUp(self):
        self._doubly_linkedList = DoublyLinkedList()
    
    def test_get_item_of_empty_list(self):
        self.assertRaises(IndexError, callableObj = lambda: self._doubly_linkedList[0])
        self.assertRaises(IndexError, callableObj = lambda: self._doubly_linkedList[1])
        self.assertRaises(IndexError, callableObj = lambda: self._doubly_linkedList[-1])
        
    def tearDown(self):
        self._doubly_linkedList = None
    
class DoublyLinkedList_Test_get_item_With_1_Elements(unittest.TestCase):
    
    def setUp(self):
        self._doubly_linkedList = DoublyLinkedList()
        
    def test_reverse_iteration_of_1_element_list(self):
        element_to_add = 1
        self._doubly_linkedList.append(element_to_add)
        self.assertEqual(self._doubly_linkedList[0], element_to_add, 'list get item did not yield expected item')
        self.assertEqual(self._doubly_linkedList[-1], element_to_add, 'list get item did not yield expected item')
        self.assertEqual(self._doubly_linkedList[10], element_to_add, 'list get item did not yield expected item')
        
    def tearDown(self):
        self._doubly_linkedList = None

class DoublyLinkedList_Test_get_item_With_multiple_Elements(unittest.TestCase):
    
    def setUp(self):
        self._doubly_linkedList = DoublyLinkedList()
        self._extend_elements = [1, 2, 3, 4]
        self._doubly_linkedList.extend(self._extend_elements)
    
    def test_get_item_with_multiple_elements(self):
        for i in self._extend_elements:#loop through the items we added. item 1 will be at index 0, 2 at 1 and so on.
            self.assertEquals(self._doubly_linkedList[i - 1], i, 'list get item at index failed')
    
    def tearDown(self):
        self._doubly_linkedList = None
#Allows running as python run.
if __name__ == '__main__':
    print('Doubly Linked List tests')
    unittest.main()
