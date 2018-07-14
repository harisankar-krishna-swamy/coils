'''
Created on Nov 8, 2015
@author: hari
'''
from __future__ import print_function
from builtins import range
import unittest
import gc
from coils.misc.internstore import InternStore
from tests.data.testdata import WrappedString

class Internstore_Test_With_None(unittest.TestCase):
    def setUp(self):
        self._internstore = InternStore()
    
    def test_intern_store_with_none(self):
        
        obj_to_intern = None
        id_of_obj_to_intern = id(obj_to_intern)
        interned_obj = self._internstore.intern(obj = obj_to_intern)
        
        id_of_interned_obj = id(interned_obj)    
        self.assertEqual(id_of_obj_to_intern, id_of_interned_obj, 'Interned object is not same as existing object id')
        
    def tearDown(self):
        pass


class Internstore_Test_With_1_Item_No_GC(unittest.TestCase):
    def setUp(self):
        self._internstore = InternStore()
    
    def test_intern_store_1_item_no_gc(self):
        
        obj_to_intern = WrappedString(string = 'Please intern me')
        id_of_obj_to_intern = id(obj_to_intern)
        interned_obj = self._internstore.intern(obj = obj_to_intern)
        
        id_of_interned_obj = id(interned_obj)    
        self.assertEqual(id_of_obj_to_intern, id_of_interned_obj, 'Interned object is not same as existing object id')
        
    def tearDown(self):
        pass

class Internstore_Test_With_2_Equal_Objects(unittest.TestCase):
    def setUp(self):
        self._internstore = InternStore()
    
    def test_intern_store_2_equal_objects(self):
        
        obj1_to_intern = WrappedString(string = 'Please intern me')
        id_of_obj1_to_intern = id(obj1_to_intern)
        interned_obj1 = self._internstore.intern(obj = obj1_to_intern)
        id_of_interned_obj1 = id(interned_obj1)
        self.assertEqual(id_of_obj1_to_intern, id_of_interned_obj1, 'Interned object is not same as existing object id')
        
        #new interning on a new object which is equal to the one in store.
        obj2_to_intern = WrappedString(string = 'Please intern me')# new object which is equal to the previous one
        id_of_obj2_to_intern = id(obj2_to_intern)
        interned_obj2 = self._internstore.intern(obj = obj2_to_intern)
        id_of_interned_obj2 = id(interned_obj2)    
        self.assertEqual(id_of_obj1_to_intern, id_of_interned_obj2, 'Interned object is not same as existing object id')
        #reference to the new object created will be lost as there is already a reference in the
        #store point to the same/equal object  
        self.assertNotEquals(id_of_obj2_to_intern, id_of_interned_obj2, 'Copy of an interned object was returned instead of original value')
    
    def tearDown(self):
        pass

class Internstore_Test_With_Many_Equal_Objects(unittest.TestCase):
    def setUp(self):
        self._internstore = InternStore()
    
    def test_intern_store_many_equal_objects(self):
        
        original_obj_to_intern = WrappedString(string = 'Please intern me')
        id_of_original_obj_to_intern = id(original_obj_to_intern)
        interned_obj = self._internstore.intern(obj = original_obj_to_intern)
        id_of_interned_obj = id(interned_obj)
        self.assertEqual(id_of_original_obj_to_intern, id_of_interned_obj, 'Interned object is not same as existing object id')
        
        count = 100000
        for i in range (0, count):
            new_obj = WrappedString(string = 'Please intern me')# new object which is equal to the previous one
            id_of_new_obj = id(new_obj)
            # sending this new object for interning will check the store and return an equal object
            # if it exists.
            interned_new_obj = self._internstore.intern(obj = new_obj)
            id_of_interned_new_obj = id(interned_new_obj)    
            self.assertEqual(id_of_original_obj_to_intern, id_of_interned_new_obj, 'Interned object is not same as existing object id')
        
    def tearDown(self):
        pass


if __name__ == '__main__':
    print('Interstore tests')
    unittest.main()