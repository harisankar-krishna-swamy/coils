'''
Created on Oct 29, 2015

@author: hari
'''
from __future__ import print_function
from builtins import str
from coils.sets.disjoint_sets_with_union import DisjointSetWithUnion
if __name__ == '__main__':
    integers = [-5, -3, 0, 2, 10]
    disjoint_set = DisjointSetWithUnion()
    
    for integer in integers:
        disjoint_set.make_set(integer)
        
    item_to_find = -3
    set_rep = disjoint_set.find(item_to_find)
    print('Item %d belongs to set represented by %d' % (item_to_find, set_rep))
    
    #join set represented by -5 to the set represented by -3
    print('Joining sets represented by -5 and -3')
    disjoint_set.union(-5, -3)
    
    print('Joining sets represented by 2 and 10')
    disjoint_set.union(2, 10)
    
    
    item_to_find = -3
    set_rep = disjoint_set.find(item_to_find)
    print('Item %d belongs to set represented by %d' % (item_to_find, set_rep))
    
    item_to_find = 10
    set_rep = disjoint_set.find(item_to_find)
    print('Item %d belongs to set represented by %d' % (item_to_find, set_rep))
    
    print('Iterating over the Disjoint set to get (item, set) pairs')
    for item, set_to_which_item_belongs in disjoint_set:
        print('Item %s belongs to set %s' % (str(item), str(set_to_which_item_belongs)))