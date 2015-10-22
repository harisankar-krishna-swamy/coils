'''
Created on Oct 22, 2015
@author: hari
'''
from unittest import TestCase
from datastructures.HashTables import SeperateChainHashTable

class SeperateChainHashTable_TestCase_With_0_Elements(TestCase):
    
    def setUp(self):
        self._chained_hash_table = SeperateChainHashTable()
    
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

class SeperateChainHashTable_TestCase_With_1_Elements(TestCase):
    
    def setUp(self):
        self._chained_hash_table = SeperateChainHashTable()
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

class SeperateChainHashTable_TestCase_With_Full_Initial_Capacity_Elements(TestCase):
    
    def setUp(self):
        self._chained_hash_table = SeperateChainHashTable()
        self._default_initial_capacity = 17
        for i in range(1, 18):# 1 to 17 default initial capacity is 17
            self._chained_hash_table[i] = i
             
    def test_get_and_len_on_full_initial_capacity_hash_table(self):
        for i in range(1, 18):
            self.assertEquals(self._chained_hash_table.get(key = i), i, 'get on existing key failed')
            self.assertEquals(self._chained_hash_table[i], i, 'get on existing key failed')
            
        self.assertEquals(len(self._chained_hash_table), self._default_initial_capacity, 'hash table length must be same as full initial capacity')    
    
    def test_del_then_get_and_len__on_full_initial_capacity_hash_table(self):
        rolling_capacity = self._default_initial_capacity
        for i in range(1, 18):
            del self._chained_hash_table[i]
            rolling_capacity = rolling_capacity - 1
            self.assertEquals(self._chained_hash_table.get(key = i), None, 'get on Non existing key must return None')
            self.assertRaises(KeyError, callableObj = lambda : self._chained_hash_table[i])
            self.assertEquals(len(self._chained_hash_table), rolling_capacity, 'hash table length did not add up after delete')
            
    def tearDown(self):
        self._chained_hash_table = None