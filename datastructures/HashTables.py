'''
Created on Oct 21, 2015
@author: hari
This borrows MAD hashing. A hash table takes a key k (you decide for the object) and the object itself. We hash 
the key and get a bucket number B. This is just an index to a table. A bucket can implemented as a list (here) 
or any other ds you like. A Bucket, which is a list masquerading as a python dict, holds multiple objects which 
happened to have keys k1 and k2 that mapped into the same bucket B.    
'''
from datastructures.LinkedList import LinkedList
from datastructures.common import KeyValuePair
from random import randrange
import collections

class ChainedHashBucket(object):
    '''
    A hash bucket is used to hold objects that hash to the same value in a hash table. This is hash bucket
    using a list. This masquerades as a python dict in code where it is used.
    
    Note: HASHBUCKET ITERATION YIELDS KEYS. not the key value pairs in the bucket. 
    '''
    def __init__(self):
        self._list_of_kv_pairs = LinkedList() #we use our linked list!
    
    def __len__(self):
        return self._list_of_kv_pairs.length
    
    def get(self, key, default = None):
        '''
        Get object associated with a key and on key miss return specified default. This is there in Python dict and this class
        masquerades as dict, we implement it.
        '''
        try:
            value = self[key]
            return value
        except KeyError:
            return default            
    
    def __getitem__(self, key):
        for kv_pair in self._list_of_kv_pairs:
            if kv_pair.key == key:
                return kv_pair.value
        raise KeyError('Key Error: %s ' % repr(key))
    
    def __delitem__(self, key):
        for kv_pair in self._list_of_kv_pairs:
            if kv_pair.key == key:
                self._list_of_kv_pairs.remove(kv_pair)
                return    
        raise KeyError('Key Error: %s ' % repr(key))
    
    def __setitem__(self, key, obj):
        for kv_pair in self._list_of_kv_pairs:
            if kv_pair.key == key:
                kv_pair.value = obj
                return    
        self._list_of_kv_pairs.append(KeyValuePair(key = key, value = obj))
  
    def __iter__(self):
        for kvpair in self._list_of_kv_pairs:
            yield kvpair.key
            
class SeperateChainHashTable(collections.MutableMapping):
    '''
    The table uses ListBasedHashBucket (Chain) for its buckets. This uses the MAD compression algorithm. 
    compressed_key = ((scale*key + shift) mod P) mod N. N is the size. P is a
    large prime > N. scale and shift are random integers less than P, scale must be > 0.
    Mutable Mapping? have a look at "cat /usr/lib/python2.7/_abcoll.py" Do not use this directly is advised in the file so we use
    from collections.MutableMapping as advised :-P Basically we dont have to write the methods in Mutable mapping by inheriting.
    '''
    def __init__(self, initial_capacity = 17, large_prime_P = 98764321261, load_factor_limit = 0.75):
        self._large_prime_P = large_prime_P
        self._table_max_size = initial_capacity
        self._scale = 1 + randrange(self._large_prime_P - 1)
        self._shift = randrange(self._large_prime_P)
        self._table = initial_capacity * [None]
        self._hash_table_items_count = 0
        self._load_factor_limit = load_factor_limit
    
    def _find_bucket_for_key(self, key):#which bucket?
        hash_key = hash(key) #Pythons hash
        bucket_index = ((hash_key * self._scale + self._shift) % self._large_prime_P) % self._table_max_size 
        return bucket_index
    
    def _get_item_from_bucket(self, bucket_index, key):
        bucket = self._table[bucket_index]
        if bucket == None:
            raise KeyError('Key Error: %s' % repr(key))
        return bucket[key]
    
    def __getitem__(self, key):
        bucket_index = self._find_bucket_for_key(key)
        return self._get_item_from_bucket(bucket_index, key)
    
    def _delete_item_from_bucket(self, bucket_index, key):
        bucket = self._table[bucket_index]
        if bucket == None:
            raise KeyError('Key Error: %s' % repr(key))
        del bucket[key]
        self._hash_table_items_count = self._hash_table_items_count - 1
        
    def __delitem__(self, key):
        bucket_index = self._find_bucket_for_key(key)
        return self._delete_item_from_bucket(bucket_index, key)
    
    def _set_item_in_bucket(self, bucket_index, key, obj):
        bucket = self._table[bucket_index]
        if bucket == None:
            bucket = ChainedHashBucket()
            self._table[bucket_index] = bucket
        items_count_in_bucket = len(bucket)
        bucket[key] = obj 
        updated_items_count_in_bucket = len(bucket)
        if items_count_in_bucket < updated_items_count_in_bucket:#bucket did not have the item. was not a replace
            self._hash_table_items_count = self._hash_table_items_count + 1
    
    def __setitem__(self, key, obj):
        bucket_index = self._find_bucket_for_key(key)
        self._set_item_in_bucket(bucket_index, key, obj)
        if float(self._hash_table_items_count / len(self._table)) >= self._load_factor_limit:
            self._resize(self._table_max_size * 2)
             
    def __iter__(self):
        for bucket in self._table:
            if bucket != None:
                for key in bucket:
                    yield key
            
    def _resize(self, new_capacity):
        list_of_key_value_pairs = list(self.items())
        self._table = new_capacity * [None]
        self._hash_table_items_count = 0
        
        for key, obj in list_of_key_value_pairs:
            self[key] = obj 