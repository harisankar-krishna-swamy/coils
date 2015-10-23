'''
Created on Oct 23, 2015

@author: hari
'''
import unittest
from datastructures.hashtables.hashbuckets import SplayedHashBucket

class SplayedHashBucket_TestCase_With_0_Elements(unittest.TestCase):
    
    def setUp(self):
        self._hash_bucket = SplayedHashBucket()
    
    def test_count_of_empty_list(self):
        self.assertEquals(len(self._hash_bucket), 0, 'Empty bucket length must be 0')
    
    def tearDown(self):
        self._hash_bucket = None

class SplayedHashBucket_TestCase_Len_With_4_Elements(unittest.TestCase):
    def setUp(self):
        self._hash_bucket = SplayedHashBucket()
        self._hash_bucket[1] = 1
        self._hash_bucket[2] = 2
        self._hash_bucket[3] = 3
        self._hash_bucket[4] = 4
        
    def test_len_of_empty_hash_bucket(self):
        self.assertEquals(len(self._hash_bucket), 4, 'Empty bucket length must be 0')
    
    def tearDown(self):
        self._hash_bucket = None

class SplayedHashBucket_TestCase_Get_Item_With_4_Elements(unittest.TestCase):
    def setUp(self):
        self._hash_bucket = SplayedHashBucket()
        self._hash_bucket[1] = 1
        self._hash_bucket[2] = 2
        self._hash_bucket[3] = 3
        self._hash_bucket[4] = 4
    
    def test_get_item_hash_bucket_with_default_return(self):
        for i in range(1, 5):
            self.assertEquals(self._hash_bucket.get(i), i, 'Hash bucket items did not match on retirieval')
    
    def test_get_item_hash_bucket(self):
        for i in range(1, 5):
            self.assertEquals(self._hash_bucket[i], i, 'Hash bucket items did not match on retirieval')

    def tearDown(self):
        self._hash_bucket = None
    
class SplayedHashBucket_TestCase_Get_Non_Existing_Item_With_4_Elements(unittest.TestCase):
    def setUp(self):
        self._hash_bucket = SplayedHashBucket()
    
    def test_get_non_exiting_item_of_hash_bucket_expect_None_as_default(self):
        self.assertEquals(self._hash_bucket.get(1), None, 
                                        'default value for non existing key was not used')
    
    def test_get_non_exiting_item_of_hash_bucket(self):
        self.assertRaises(KeyError, callableObj = lambda : self._hash_bucket[1])
        
    def test_get_non_exiting_item_of_hash_bucket_expect_Something_as_default(self):
        expected_default_return = "Default"
        self.assertEquals(self._hash_bucket.get(1, default = expected_default_return), expected_default_return, 
                                        'default value for non existing key was not used')
    def tearDown(self):
        self._hash_bucket = None

class SplayedHashBucket_TestCase_Delete_Item_With_4_Elements(unittest.TestCase):
    
    def setUp(self):
        self._hash_bucket = SplayedHashBucket()
        self._hash_bucket[1] = 1
        self._hash_bucket[2] = 2
        self._hash_bucket[3] = 3
        self._hash_bucket[4] = 4
        
    def test_delete_item_hash_bucket(self):
        for i in range(1, 5):
            self.assertEquals(self._hash_bucket[i], i, 'Hash bucket items did not match on retirieval')
            del self._hash_bucket[i]
            self.assertRaises(KeyError, callableObj = lambda : self._hash_bucket[i])
            
    def tearDown(self):
        self._hash_bucket = None

class SplayedHashBucket_TestCase_Set_Item_With_4_Elements(unittest.TestCase):
    
    def setUp(self):
        self._hash_bucket = SplayedHashBucket()
        self._hash_bucket[1] = 1
        self._hash_bucket[2] = 2
        self._hash_bucket[3] = 3
        self._hash_bucket[4] = 4
        
    def test_set_item_hash_bucket(self):
        for i in range(1, 5):
            self.assertEquals(self._hash_bucket[i], i, 'Hash bucket items did not match on retirieval')
            self._hash_bucket[i] = 5 + i
            self.assertEquals(self._hash_bucket[i], 5 + i, 'Hash bucket items did not match on retirieval')
            
    def tearDown(self):
        self._hash_bucket = None

class SplayedHashBucket_TestCase_Iter_Keys_With_4_Elements(unittest.TestCase):
    
    def setUp(self):
        self._hash_bucket = SplayedHashBucket()
        self._hash_bucket[1] = 1
        self._hash_bucket[2] = 2
        self._hash_bucket[3] = 3
        self._hash_bucket[4] = 4
        
    def test_set_item_hash_bucket(self):
        expected_key_list = [1, 2, 3, 4] #underlying ds for bucket is list. we inserted in this order. so we expect in this order.
        actual_key_list = []
        for key in self._hash_bucket:
            actual_key_list.append(key)
        self.assertEquals(expected_key_list, actual_key_list, 'Iterating over bucket keys did not match expected list of keys')
    def tearDown(self):
        self._hash_bucket = None
        
#Allows running as python run.
if __name__ == '__main__':
    unittest.main()
