'''
Created on Oct 28, 2015

@author: hari
'''
from __future__ import print_function
from builtins import range
import unittest
from pycoils.sets.disjoint_sets_with_union import DisjointSetWithUnion

class DisjointSet_With_Union_Test_init(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_init(self):
        self._disjointset = DisjointSetWithUnion()
        
    def tearDown(self):
        self._disjointset = None

class DisjointSet_With_Union_Test_Size_Of_Empty_Set(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_size_of_empty_set(self):
        self._disjointset = DisjointSetWithUnion()
        expected_size = 0
        self.assertEqual(self._disjointset.size, expected_size, 'Empty disjoint set size was not 0')
        
    def tearDown(self):
        self._disjointset = None

class DisjointSet_With_Union_Test_Find_with_Empty_Set(unittest.TestCase):
    def setUp(self):
        self._disjointset = DisjointSetWithUnion()
    
    def test_find_on_empty_set(self):
        self.assertEqual(self._disjointset.find(-1), None, 'Empty disjoint set find must return None')
        
    def tearDown(self):
        self._disjointset = None

class DisjointSet_With_Union_Test_Make_Set_with_None(unittest.TestCase):
    def setUp(self):
        self._disjointset = DisjointSetWithUnion()
    
    def test_make_set_with_none(self):
        self._disjointset.make_set(None)
        
    def tearDown(self):
        self._disjointset = None

class DisjointSet_With_Union_Test_Size_with_Single_Item(unittest.TestCase):
    def setUp(self):
        self._disjointset = DisjointSetWithUnion()
    
    def test_make_set_with_single_item(self):
        item = -1
        self._disjointset.make_set(item)
        expected_size = 1
        self.assertEqual(self._disjointset.size, expected_size, 'Singleton disjoint set size was not 1')
        
    def tearDown(self):
        self._disjointset = None

class DisjointSet_With_Union_Test_Make_Set_with_Single_Item(unittest.TestCase):
    def setUp(self):
        self._disjointset = DisjointSetWithUnion()
    
    def test_make_set_with_single_item(self):
        item = -1
        self._disjointset.make_set(item)
        self.assertEqual(self._disjointset.find(item), item, 'singleton disjoing set find subsequent to make set failed')
        
    def tearDown(self):
        self._disjointset = None

class DisjointSet_With_Union_Test_Make_Set_with_Multiple_Items(unittest.TestCase):
    def setUp(self):
        self._disjointset = DisjointSetWithUnion()
    
    def test_make_set_with_multiple_items(self):
        items = [1, 2, 3, 4, 5, 6, 7]
        for item in items:
            self._disjointset.make_set(item)
        for item in items:
            self.assertEqual(self._disjointset.find(item), item, 'singleton disjoint set find subsequent to make set failed')
        
    def tearDown(self):
        self._disjointset = None        

class DisjointSet_Test_Union_With_None(unittest.TestCase):
    def setUp(self):
        self._disjointset = DisjointSetWithUnion()
    
    def test_union_with_none(self):
        self.assertEqual(self._disjointset.union(item_1 = None, item_2 = None), None,
                                                'disjoint union with none,none failed')
    def test_union_with_none_and_value(self):
        self.assertEqual(self._disjointset.union(item_1 = None, item_2 = 'Some Value'), None,
                                                'disjoint union(None, some value) failed')
    def test_union_with_value_and_none(self):
        self.assertEqual(self._disjointset.union(item_1 = 'Some value', item_2 = None), None,
                                                'disjoint union(some value, None) failed')    
    def tearDown(self):
        self._disjointset = None

class DisjointSet_Test_Union_Towards_Single_Final_Set(unittest.TestCase):
    def setUp(self):
        self._disjointset = DisjointSetWithUnion()
        self._items = [1, 2, 3, 4, 5, 6, 7]
        for item in self._items:
            self._disjointset.make_set(item)
            
    def test_union_towards_single_final_set(self):
        items_count = len(self._items)
        set = None
        for index in range(0 , items_count - 1):
            set = self._disjointset.union(self._items[index], self._items[index + 1])
            self.assertEqual(self._disjointset.find(self._items[index]), set,
                              'Disjoint union-find failed while progressing to a single final set')
            self.assertEqual(self._disjointset.find(self._items[index + 1]), set,
                              'Disjoint union-find failed while progressing to a single final set')
        
    def tearDown(self):
        self._disjointset = None
        
class DisjointSet_Test_Union_Towards_Multiple_Final_Sets(unittest.TestCase):
    def setUp(self):
        self._disjointset = DisjointSetWithUnion()
        self._positive_items_1 = [1, 2, 3, 4, 5, 6, 7, 8]
        self._negative_items_1 = [-1, -2, -3, -4, -5]
        
        self._all_items =  [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
        for item in self._all_items:
            self._disjointset.make_set(item)
            
    def test_union_towards_multiple_final_set(self):
        negative_items_count = len(self._negative_items_1)
        for index in range(0 , negative_items_count - 1):
            set = self._disjointset.union(self._negative_items_1[index], self._negative_items_1[index + 1])
            
        positive_items_count = len(self._positive_items_1)
        for index in range(0 , positive_items_count - 1):
            set = self._disjointset.union(self._positive_items_1[index], self._positive_items_1[index + 1])
        
        #Now there should be 3 sets with representations by -1, 0 and 1
        positive_representative_item = 1
        negative_representative_item = -1
        zero = 0
        
        for item in self._positive_items_1:
            self.assertEqual(self._disjointset.find(item), positive_representative_item,
                                            'Find failed after union towards multiple final sets.')
        
        for item in self._negative_items_1:
            self.assertEqual(self._disjointset.find(item), negative_representative_item,
                                            'Find failed after union towards multiple final sets.')
        
        self.assertEqual(self._disjointset.find(0), zero,
                                            'Find failed after union towards multiple final sets.')
        
    def tearDown(self):
        self._disjointset = None

class DisjointSet_With_Union_Test_Iter_On_Empty_Set(unittest.TestCase):
    def setUp(self):
        self._disjointset = DisjointSetWithUnion()
    
    def test_iter_on_empty_set(self):
        list_of_tuples = []
        for item_and_set in self._disjointset:
            list_of_tuples.append(item_and_set)
        self.assertEqual(len(list_of_tuples), 0, 'Iterating over empty set cannot yield anything')
        
    def tearDown(self):
        self._disjointset = None        

class DisjointSet_With_Union_Test_Iter_On_Singleton_Set(unittest.TestCase):
    def setUp(self):
        self._disjointset = DisjointSetWithUnion()
        self._item = 1
        self._disjointset.make_set(self._item)
        
    def test_iter_on_singleton_set(self):
        list_of_tuples = []
        for item_and_set in self._disjointset:
            list_of_tuples.append(item_and_set)
        self.assertEqual(len(list_of_tuples), 1, 'Iterating over (item, set) pairs in a singleton does not add up')
        
    def tearDown(self):
        self._disjointset = None


class DisjointSet_Test_Iter_After_Union_Towards_Multiple_Final_Sets(unittest.TestCase):
    def setUp(self):
        self._disjointset = DisjointSetWithUnion()
        self._positive_items_1 = [1, 2, 3, 4, 5, 6, 7, 8]
        self._negative_items_1 = [-1, -2, -3, -4, -5]
        
        self._all_items =  [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
        for item in self._all_items:
            self._disjointset.make_set(item)
        
        negative_items_count = len(self._negative_items_1)
        for index in range(0 , negative_items_count - 1):
            set = self._disjointset.union(self._negative_items_1[index], self._negative_items_1[index + 1])
            
        positive_items_count = len(self._positive_items_1)
        for index in range(0 , positive_items_count - 1):
            set = self._disjointset.union(self._positive_items_1[index], self._positive_items_1[index + 1])
        #Now there should be 3 sets with representations by -1, 0 and 1
            
    def test_iter_after_union_towards_multiple_final_set(self):
        
        positive_representative_item = 1
        negative_representative_item = -1
        zero = 0
        
        for item, set_of_item in self._disjointset:
            if item == 0:
                self.assertEqual(set_of_item, zero, 'Iterating over (item, set) yields wrong set membership')
            elif item > 0:
                self.assertEqual(set_of_item, positive_representative_item, 'Iterating over (item, set) yields wrong set membership')
            else:
                self.assertEqual(set_of_item, negative_representative_item, 'Iterating over (item, set) yields wrong set membership')
                
    def tearDown(self):
        self._disjointset = None
        
if __name__ == '__main__':
    print('Disjoint sets with union tests')
    unittest.main()