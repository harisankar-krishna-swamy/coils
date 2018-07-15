'''
Created on Oct 25, 2015

@author: hari
'''
from __future__ import print_function
from builtins import str
from pycoils.hashtables.HashTables import SeperateChainHashTable
from pycoils.hashtables.hashbuckets import LinkedListHashBucket,\
    BSTHashBucket, SplayedHashBucket

def print_items_in_hash_table(hash_table):
    print('hash table size is %s' % str(len(hash_table)))
    for key in hash_table:
        print('key %s -> value %s' % (str(key), str(hash_table[key])))

if __name__ == '__main__':
    cht = SeperateChainHashTable()
    #
    # to control bucket data structure type use one of the following
    #
    #cht = SeperateChainHashTable(bucket_type_class = LinkedListHashBucket)
    #cht = SeperateChainHashTable(bucket_type_class = BSTHashBucket)
    #cht = SeperateChainHashTable(bucket_type_class = SplayedHashBucket)
    
    #add key, value pairs
    kvpairs = [(5, 5), (2, 2), (7, 7), (1, 1), (3, 3), (9, 9), (8, 8), (4, 4), (6, 6)]
    for kvpair in kvpairs:
        cht[kvpair[0]] = kvpair[1]
        
    print_items_in_hash_table(cht)
    
    #check if hash table has a key
    key_to_check = 10
    print('Key %s found in hashtable %s' % (str(key_to_check), key_to_check in cht))
    
    #get item with default if not found
    key_to_get = 20
    print('Get value for key %s value is %s' % (str(key_to_get), cht.get(key_to_get)))
    
    #replace
    key_to_replace_at = 1
    new_value = 111
    print('Replacing item at key %s with %s' % (str(key_to_replace_at), str(new_value)))
    cht[1] = 111
    
    #delete
    key_to_delete = 7
    print('Deleting key %s' % str(key_to_delete))
    del cht[7]
    print_items_in_hash_table(cht)