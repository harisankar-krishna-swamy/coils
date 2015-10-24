'''
Created on Aug 12, 2015
@author: hari
'''
import unittest
from datastructures.lists.singly_linked_list import LinkedList
from random import randint

class LinkedList_Test_Count_With_0_Elements(unittest.TestCase):
    
    def setUp(self):
        self._linkedList = LinkedList()
    
    def test_count_of_empty_list(self):
        self.assertEquals(self._linkedList.length, 0, 'Empty List length must be 0')
    
    def tearDown(self):
        self._linkedList = None

class LinkedList_Test_Head_n_Tail_With_0_Elements(unittest.TestCase):
    
    def setUp(self):
        self._linkedList = LinkedList()
    
    def test_count_of_empty_list(self):
        self.assertEquals(self._linkedList.head, None, 'Head of 0 element list must be None')
        self.assertEquals(self._linkedList.tail, None, 'Tail of 0 element list must be None')
    
    def tearDown(self):
        self._linkedList = None
    
        
class LinkedList_Test_Count_With_4_Predictable_Elements(unittest.TestCase):
    
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

class LinkedList_Test_Remove_Non_Existing_Element_From_0_Element_List(unittest.TestCase):
    
    def setUp(self):
        self._linkedList = LinkedList()
    
    def test_count_of_list(self):
        self._linkedList.remove(-1)
        self.assertEquals(self._linkedList.length, 0, 'Length must be 0 for empty list')
    
    def tearDown(self):
        self._linkedList = None

class LinkedList_Test_Remove_Non_Existing_Element_From_4_Element_List(unittest.TestCase):
    
    def setUp(self):
        self._linkedList = LinkedList()
        self._linkedList.append(1)
        self._linkedList.append(2)
        self._linkedList.append(3)
        self._linkedList.append(4)
    
    def test_count_of_list(self):
        self._linkedList.remove(-1)
        self.assertEquals(self._linkedList.length, 4, 'Length not valid after trying to remove non-existing element')

    def tearDown(self):
        self._linkedList = None

class LinkedList_Test_Remove_Middle_Element_From_4_Element_List(unittest.TestCase):
    
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

class LinkedList_Test_IndexOf_Element_In_Empty_List(unittest.TestCase):
    
    def setUp(self):
        self._linkedList = LinkedList()
    
    def test_index(self):
        index = self._linkedList.index(8)
        self.assertEquals(index, -1, 'Non existing element has index -1')

    def tearDown(self):
        self._linkedList = None

class LinkedList_Test_IndexOf_Elements_In_4_Element_List(unittest.TestCase):
    
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

class LinkedList_Test_Operations_On_List_with_1000_Random_Elements(unittest.TestCase):
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

class LinkedList_Test_extend_With_Predictable_Elements(unittest.TestCase):
    '''
    Test the extend operation of singly_linked_list. 
    a) Create 2 lists. 
    b) Add the second list to the end of the first list. 
    c) Check the indices of the newly added elements.
    '''
    
    def setUp(self):
        self._linkedList = LinkedList()
        self._linkedList.append(1)
        self._linkedList.append(2)
        self._linkedList.append(3)
        self._linkedList.append(4)
        #create a second linkedlist with 5, 6, 7
        self._secondList = LinkedList()
        self._secondList.append(5)
        self._secondList.append(6)
        self._secondList.append(7)
        
    def test_extend_of_list(self):
        self.assertEquals(self._linkedList.length, 4, 'Original list before extend must be 4')
        count_before_extend = self._linkedList.length
        next_index_will_be = count_before_extend
        self._linkedList.extend(self._secondList)
        #check new length
        self.assertEquals(self._linkedList.length, count_before_extend + self._secondList.length, 'New length after extend must add up.')
        #check if the elements of shadow list are present
        for element in self._secondList:
            self.assertEqual(self._linkedList.index(element), next_index_will_be
                             , 'Indices of new elements after extend must add up')
            next_index_will_be += 1
    
    def tearDown(self):
        self._linkedList = None
        self._secondList = None

class LinkedList_Test_Check_Tail_On_Remove_In_4_Element_List(unittest.TestCase):
    
    def setUp(self):
        self._linkedList = LinkedList()
        self._linkedList.append(1)
        self._linkedList.append(2)
        self._linkedList.append(3)
        self._linkedList.append(4)
    
    def test_tail_node_on_remove(self):
        self._linkedList.remove(1)#removed head. Tail must be same node 
        self.assertEqual(self._linkedList.tail, 4)
        #Now list is [2, 3, 4]
        self._linkedList.remove(4)#tail should next be 3
        self.assertEqual(self._linkedList.tail, 3, 'Tail must be adjusted on deletion of last node')
        #Now list is [2, 3]
        self._linkedList.remove(2)#tail should next be 3
        self.assertEqual(self._linkedList.tail, 3, 'Tail must be adjusted on deletion of last node')
        #Now list is [3]
        self._linkedList.remove(3)#tail should next be None
        self.assertEqual(self._linkedList.tail, None, 'Tail must be None on empty list')
    def tearDown(self):
        self._linkedList = None    

class LinkedList_Test_Check_Head_On_Remove_In_4_Element_List(unittest.TestCase):

    def setUp(self):
        self._linkedList = LinkedList()
        self._linkedList.append(1)
        self._linkedList.append(2)
        self._linkedList.append(3)
        self._linkedList.append(4)
    
    def test_tail_node_on_remove(self):
        #list is [1, 2, 3, 4]
        self._linkedList.remove(3)#removed head. Head must be same node 
        self.assertEqual(self._linkedList.head, 1)
        #Now list is [1, 2, 4]
        self._linkedList.remove(1)#head should next be 2
        self.assertEqual(self._linkedList.head, 2, 'head must be adjusted on deletion of first node')
        #Now list is [2, 4]
        self._linkedList.remove(2)#head should next be 4
        self.assertEqual(self._linkedList.head, 4, 'head must be adjusted on deletion of first node')
        #Now list is [4]
        self._linkedList.remove(4)#head should next be None
        self.assertEqual(self._linkedList.head, None, 'Head must be None on empty list')
        
    def tearDown(self):
        self._linkedList = None    

class LinkedList_Test_Insert_At_0_With_0_Elements(unittest.TestCase):
    
    def setUp(self):
        self._linkedList = LinkedList()
    
    def test_insert_at_0_of_empty_list(self):
        self._linkedList.insert_at(0, 20)
        self.assertEquals(self._linkedList.length, 1, 'Linked list length must be 1 after inserting to empty list')
        self.assertEquals(self._linkedList.head, self._linkedList.tail, 'Linked list length must be same node after inserting to empty list')
    
    def tearDown(self):
        self._linkedList = None

class LinkedList_Test_Insert_At_Negative_Index_With_0_Elements(unittest.TestCase):
    
    def setUp(self):
        self._linkedList = LinkedList()
    
    def test_insert_at_negative_index_of_empty_list(self):
        self._linkedList.insert_at(-2, 20)
        self.assertEquals(self._linkedList.length, 1, 'Linked list length must be 1 after inserting to empty list at negative index')
        self.assertEquals(self._linkedList.head, self._linkedList.tail, 'Linked list length must be same node after inserting to empty list at negative index')
    
    def tearDown(self):
        self._linkedList = None

class LinkedList_Test_Insert_At_Index_Larger_Than_Length_With_0_Elements(unittest.TestCase):
    
    def setUp(self):
        self._linkedList = LinkedList()
    
    def test_insert_at_negative_index_of_empty_list(self):
        self._linkedList.insert_at(100, 20)
        self.assertEquals(self._linkedList.length, 1, 'Linked list length must be 1 after inserting to empty list at huge index')
        self.assertEquals(self._linkedList.head, self._linkedList.tail, 'Linked list length must be same node after inserting to empty list at huge index')
    
    def tearDown(self):
        self._linkedList = None

class LinkedList_Test_Insert_At_Index_Larger_Than_Length_With_4_Elements(unittest.TestCase):
    
    def setUp(self):
        self._linkedList = LinkedList()
        self._linkedList.append(1)
        self._linkedList.append(2)
        self._linkedList.append(3)
        self._linkedList.append(4)
        
    def test_insert_at_negative_index_of_empty_list(self):
        expected_length = self._linkedList.length + 1
        element_to_insert = 20
        self._linkedList.insert_at(100, element_to_insert)
        self.assertEquals(self._linkedList.length, expected_length, 'Linked list length did not tally after insert at huge index')
        self.assertEquals(self._linkedList.tail, element_to_insert, 'Linked list tail must be same as new element inserted at huge index')
        self.assertEquals(self._linkedList.index(20), expected_length - 1, 'index of new element did not add up')
    
    def tearDown(self):
        self._linkedList = None


class LinkedList_Test_Insert_At_Index_In_Middle_With_4_Elements(unittest.TestCase):
    
    def setUp(self):
        self._linkedList = LinkedList()
        self._linkedList.append(1)
        self._linkedList.append(2)
        self._linkedList.append(4)
        self._linkedList.append(5)
        
    def test_insert_at_negative_index_of_empty_list(self):
        expected_length = self._linkedList.length + 1
        element_to_insert = 3
        insert_at_index = 2
        self._linkedList.insert_at(insert_at_index, element_to_insert)# list will become 1, 2, 3, 4, 5
        self.assertEquals(self._linkedList.length, expected_length, 'Linked list length did not tally after insert in the middle')
        self.assertEquals(self._linkedList.index(3), insert_at_index, 'index of new element is not where we insert it at!')
        
        #iterate and check
        expected_list = []
        for element in self._linkedList:
            expected_list.append(element)
        self.assertEquals(expected_list, [1, 2, 3, 4, 5], 'List was not same as expected after insert At index')
    
    def tearDown(self):
        self._linkedList = None

class LinkedList_Test_Remove_Duplicates_With_0_Elements(unittest.TestCase):
    
    def setUp(self):
        self._linkedList = LinkedList()
    
    def test_remove_duplicate_of_empty_list(self):
        self._linkedList.remove_duplicates()
        
    def tearDown(self):
        self._linkedList = None

class LinkedList_Test_Remove_Duplicates_With_1_Elements(unittest.TestCase):
    
    def setUp(self):
        self._linkedList = LinkedList()
        element_to_append = 1
        self._linkedList.append(element_to_append)
        
    def test_remove_duplicate_of_list_with_1_element(self):
        old_head = self._linkedList.head
        expected_tail = old_head
        
        self._linkedList.remove_duplicates()
        expected_length = 1
        self.assertEqual(self._linkedList.length, expected_length, 'Linked list length did not add up after removing duplicates')
        self.assertEqual(self._linkedList.head, old_head, 'Linked list head did not add up after removing duplicates')
        self.assertEqual(self._linkedList.tail, expected_tail, 'Linked list tail did not add up after removing duplicates')
        
        
    def tearDown(self):
        self._linkedList = None

class LinkedList_Test_Remove_Duplicates_With_2_Identical_Elements(unittest.TestCase):
    
    def setUp(self):
        self._linkedList = LinkedList()
        element_to_append = 1
        self._linkedList.append(element_to_append)
        self._linkedList.append(element_to_append)
        
    def test_remove_duplicates_of_list_with_2_identical_elements(self):
        old_head = self._linkedList.head
        expected_tail = old_head
        
        self._linkedList.remove_duplicates()
        expected_length = 1
        self.assertEqual(self._linkedList.length, expected_length, 'Linked list length did not add up after removing duplicates')
        self.assertEqual(self._linkedList.head, old_head, 'Linked list head did not add up after removing duplicates')
        self.assertEqual(self._linkedList.tail, expected_tail, 'Linked list tail did not add up after removing duplicates')
        
    def tearDown(self):
        self._linkedList = None
        
class LinkedList_Test_Remove_Duplicates_With_Duplicates_At_Head(unittest.TestCase):
    
    def setUp(self):
        #build [1, 1, 1, 2]
        self._linkedList = LinkedList()
        element_to_append = 1
        self._linkedList.extend([element_to_append, element_to_append, element_to_append])
        tail_element = 2
        self._linkedList.append(tail_element)
        
    def test_remove_duplicates_of_list_with_2_identical_elements(self):
        expected_head = self._linkedList._head
        expected_tail = self._linkedList._tail
        
        self._linkedList.remove_duplicates()
        expected_length = 2
        self.assertEqual(self._linkedList.length, expected_length, 'Linked list length did not add up after removing duplicates')
        self.assertEqual(self._linkedList._head, expected_head, 'Linked list head did not add up after removing duplicates')
        self.assertEqual(self._linkedList._tail, expected_tail, 'Linked list tail did not add up after removing duplicates')
        
    def tearDown(self):
        self._linkedList = None

class LinkedList_Test_Remove_Duplicates_With_Duplicates_At_Tail(unittest.TestCase):
    
    def setUp(self):
        #build [2, 1, 1, 1]
        self._linkedList = LinkedList()
        self._linkedList.append(2)
        element_to_append = 1
        self._linkedList.extend([element_to_append, element_to_append, element_to_append])
        
    def test_remove_duplicates_of_list_with_2_identical_elements(self):
        expected_head = self._linkedList._head
        expected_tail = self._linkedList._head.nextNode
        
        self._linkedList.remove_duplicates()
        expected_length = 2
        #compare references of head and tail
        self.assertEqual(self._linkedList.length, expected_length, 'Linked list length did not add up after removing duplicates')
        self.assertEqual(self._linkedList._head, expected_head, 'Linked list head did not add up after removing duplicates')
        self.assertEqual(self._linkedList._tail, expected_tail, 'Linked list tail did not add up after removing duplicates')
        
    def tearDown(self):
        self._linkedList = None

class LinkedList_Test_Remove_Duplicates_With_Duplicates_At_Middle(unittest.TestCase):
    
    def setUp(self):
        #build [2, 1, 1, 1, 3]
        self._linkedList = LinkedList()
        self._linkedList.append(2)
        element_to_append = 1
        self._linkedList.extend([element_to_append, element_to_append, element_to_append])
        self._linkedList.append(3)
        
    def test_remove_duplicates_of_list_with_2_duplicates_in_Middle(self):
        expected_head = self._linkedList._head
        expected_tail = self._linkedList._tail
        
        self._linkedList.remove_duplicates()
        expected_length = 3
        self.assertEqual(self._linkedList.length, expected_length, 'Linked list length did not add up after removing duplicates')
        self.assertEqual(self._linkedList._head, expected_head, 'Linked list head did not add up after removing duplicates')
        self.assertEqual(self._linkedList._tail, expected_tail, 'Linked list tail did not add up after removing duplicates')
        
    def tearDown(self):
        self._linkedList = None

class LinkedList_Test_Remove_Duplicates_With_Recurring_Duplicates(unittest.TestCase):
    
    def setUp(self):
        #build [2, 1, 1, 1, 3, 1, 1, 1, 4]
        self._linkedList = LinkedList()
        self._linkedList.append(2)
        element_to_append = 1
        self._linkedList.extend([element_to_append, element_to_append, element_to_append])
        self._linkedList.append(3)
        self._linkedList.extend([element_to_append, element_to_append, element_to_append])
        self._linkedList.append(4)
        
    def test_remove_duplicates_of_list_with_recurring_duplicates(self):
        expected_head = self._linkedList._head
        expected_tail = self._linkedList._tail
        
        self._linkedList.remove_duplicates()
        expected_length = 4
        self.assertEqual(self._linkedList.length, expected_length, 'Linked list length did not add up after removing duplicates')
        self.assertEqual(self._linkedList._head, expected_head, 'Linked list head did not add up after removing duplicates')
        self.assertEqual(self._linkedList._tail, expected_tail, 'Linked list tail did not add up after removing duplicates')
        
    def tearDown(self):
        self._linkedList = None

#Allows running as python run.
if __name__ == '__main__':
    unittest.main()