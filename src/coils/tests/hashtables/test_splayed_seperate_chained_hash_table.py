'''
Created on Oct 23, 2015
@author: hari
'''

#TESTS FOR SeperateChainHashTable with SplayedHashBucket 
from builtins import range
import unittest
from coils.hashtables.HashTables import SeperateChainHashTable
from coils.hashtables.hashbuckets import SplayedHashBucket

#want to use string keys and values. rather than hash (1, 17) 17 is initial capacity
list_of_strings_used_as_keys_and_values = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
                                           'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen']
 
class SeperateChainHashTable_with_SplayedHashBucket_Test_With_0_Elements(unittest.TestCase):
    
    def setUp(self):
        self._chained_hash_table = SeperateChainHashTable(bucket_type_class = SplayedHashBucket)
    
    def test_get_empty_hash_table(self):
        non_existing_key = "SomeKey"
        self.assertEquals(self._chained_hash_table.get(key = non_existing_key), None, 'get on Non existing key must return None')
        self.assertRaises(KeyError, callableObj = lambda : self._chained_hash_table[non_existing_key])
    
    def test_del_empty_hash_table(self):
        non_existing_key = "SomeKey"
        try:
            del self._chained_hash_table[non_existing_key]
        except Exception as e:
            self.assertEquals(e.__class__.__name__, KeyError.__name__, 'deleting non-existing key did not raise key error')
    
    def test_len_empty_hash_table(self):
        self.assertEquals(len(self._chained_hash_table), 0, 'Empty hash table length must be 0')
    
    def test_has_key_empty_hash_table(self):
        non_existing_key = "SomeKey"
        self.assertEquals(self._chained_hash_table.has_key(key = non_existing_key), 0, 'Empty hash table length must be 0')
    
    def tearDown(self):
        self._chained_hash_table = None

class SeperateChainHashTable_with_SplayedHashBucket_Test_With_1_Elements(unittest.TestCase):
    
    def setUp(self):
        self._chained_hash_table = SeperateChainHashTable(bucket_type_class = SplayedHashBucket)
        self._key = 'some_key'
        self._value = 'some_value'
        self._chained_hash_table[self._key] = self._value
         
    def test_get_and_len_on_single_entry_hash_table(self):
        self.assertEquals(self._chained_hash_table.get(key = self._key), self._value, 'get on existing key failed')
        self.assertEquals(self._chained_hash_table[self._key], self._value, 'get on existing key failed')
    
        self.assertEquals(len(self._chained_hash_table), 1, 'single entry hash table length must be 1')
        
    def test_del_single_entry_hash_table(self):
        del self._chained_hash_table[self._key]
        try:
            del self._chained_hash_table[self._key]
        except Exception as e:
            self.assertEquals(e.__class__.__name__, KeyError.__name__, 'deleting non-existing key did not raise key error')
    
    def tearDown(self):
        self._chained_hash_table = None

class SeperateChainHashTable_with_SplayedHashBucket_Test_Capacity_On_Resize(unittest.TestCase):
    def setUp(self):
        self._chained_hash_table = SeperateChainHashTable(bucket_type_class = SplayedHashBucket)
        self._default_initial_capacity = 17
        for i in list_of_strings_used_as_keys_and_values:# 1 to 17 default initial capacity is 17
            self._chained_hash_table[i] = i
             
    def test_capacity_on_resize(self):
        for i in list_of_strings_used_as_keys_and_values:
            self.assertEquals(self._chained_hash_table.get(key = i), i, 'get on existing key failed')
            self.assertEquals(self._chained_hash_table[i], i, 'get on existing key failed')
        #would have resized but number of items would be same
        self.assertEquals(len(self._chained_hash_table), self._default_initial_capacity, 'hash table length does not add up')
        #but table size would have doubled
        self.assertEquals(self._chained_hash_table.current_capacity, self._default_initial_capacity * 2, 'hash table capacity does not add up')    
                
    def tearDown(self):
        self._chained_hash_table = None
        
class SeperateChainHashTable_with_SplayedHashBucket_Test_With_Full_Initial_Capacity_Elements_Forces_Resize(unittest.TestCase):
    def setUp(self):
        self._chained_hash_table = SeperateChainHashTable(bucket_type_class = SplayedHashBucket)
        self._default_initial_capacity = 17
        for i in list_of_strings_used_as_keys_and_values:# 1 to 17 default initial capacity is 17
            self._chained_hash_table[i] = i
             
    def test_get_and_len_on_full_initial_capacity_hash_table(self):
        for i in list_of_strings_used_as_keys_and_values:
            self.assertEquals(self._chained_hash_table.get(key = i), i, 'get on existing key failed')
            self.assertEquals(self._chained_hash_table[i], i, 'get on existing key failed')
        #would have resized but number of items would be same
        self.assertEquals(len(self._chained_hash_table), self._default_initial_capacity, 'hash table length does not add up')
        #but table size would have doubled
        self.assertEquals(self._chained_hash_table.current_capacity, self._default_initial_capacity * 2, 'hash table capacity does not add up')    
        
    def test_del_then_get_and_len_on_full_initial_capacity_hash_table(self):
        rolling_capacity = len(self._chained_hash_table)
        for i in list_of_strings_used_as_keys_and_values:
            del self._chained_hash_table[i]
            rolling_capacity = rolling_capacity - 1
            self.assertEquals(self._chained_hash_table.get(key = i), None, 'get on Non existing key must return None')
            self.assertRaises(KeyError, callableObj = lambda : self._chained_hash_table[i])
            self.assertEquals(len(self._chained_hash_table), rolling_capacity, 'hash table length did not add up after delete')
            
    def tearDown(self):
        self._chained_hash_table = None

class SeperateChainHashTable_with_SplayedHashBucket_Test_With_Less_Than_Initial_Capacity_Elements_Cause_No_Resize(unittest.TestCase):
    '''
    By adding 5 elements to an initial capacity of 17 the load factor is just 0.2941 which is < 0.75 loadfactor threshold for resize.
    '''
    def setUp(self):
        self._chained_hash_table = SeperateChainHashTable(bucket_type_class = SplayedHashBucket)
        self._default_initial_capacity = 5
        for i in list_of_strings_used_as_keys_and_values[0:5]:
            self._chained_hash_table[i] = i
             
    def test_get_and_len_on_less_than_initial_capacity_hash_table(self):
        for i in list_of_strings_used_as_keys_and_values[0:5]:
            self.assertEquals(self._chained_hash_table.get(key = i), i, 'get on existing key failed')
            self.assertEquals(self._chained_hash_table[i], i, 'get on existing key failed')
            
        self.assertEquals(len(self._chained_hash_table), self._default_initial_capacity, 'hash table length must be same as full initial capacity')    
    
    def test_del_then_get_and_len_on_less_thaninitial_capacity_hash_table(self):
        rolling_capacity = self._default_initial_capacity
        for i in list_of_strings_used_as_keys_and_values[0:5]:
            del self._chained_hash_table[i]
            rolling_capacity = rolling_capacity - 1
            self.assertEquals(self._chained_hash_table.get(key = i), None, 'get on Non existing key must return None')
            self.assertRaises(KeyError, callableObj = lambda : self._chained_hash_table[i])
            self.assertEquals(len(self._chained_hash_table), rolling_capacity, 'hash table length did not add up after delete')
            
    def tearDown(self):
        self._chained_hash_table = None
        
class SeperateChainHashTable_with_SplayedHashBucket_Test_Multiple_Resizes(unittest.TestCase):
    def setUp(self):
        self._chained_hash_table = SeperateChainHashTable(bucket_type_class = SplayedHashBucket)
        self._default_initial_capacity = 17 
        self._length_upper_limit = 1001 #always choose some multiple of 100 + 1
    def test_get_and_len_with_a_truck_load_of_resizes(self):
        
        for i in range(1, self._length_upper_limit): # will trigger resize 
            self._chained_hash_table[i] = i

        for i in range(1, self._length_upper_limit): # will trigger 
            self.assertEquals(self._chained_hash_table.get(key = i), i, 'get on existing key failed')
            self.assertEquals(self._chained_hash_table[i], i, 'get on existing key failed')
        #would have resized but number of items would be same
        self.assertEquals(len(self._chained_hash_table), self._length_upper_limit - 1, 'hash table length does not add up')
        #but table size would have doubled
        current_capacity_would_be = 2176 #coz 13 is where a default size 17 table resizes at first.
        self.assertEquals(self._chained_hash_table.current_capacity, current_capacity_would_be,'hash table capacity does not add up')    
    
    def test_del_then_get_and_len_with_a_truck_load_of_resizes(self):
        
        for i in range(1, self._length_upper_limit): # will trigger resize 
            self._chained_hash_table[i] = i
            
        rolling_length = len(self._chained_hash_table)
        for i in range(1, self._length_upper_limit): # will trigger
            del self._chained_hash_table[i]
            rolling_length = rolling_length - 1
            self.assertEquals(self._chained_hash_table.get(key = i), None, 'get on Non existing key must return None')
            self.assertRaises(KeyError, callableObj = lambda : self._chained_hash_table[i])
            self.assertEquals(len(self._chained_hash_table), rolling_length, 'hash table length did not add up after delete')
        
    def tearDown(self):
        self._chained_hash_table = None
#Allows running as python run.
if __name__ == '__main__':
    unittest.main()
