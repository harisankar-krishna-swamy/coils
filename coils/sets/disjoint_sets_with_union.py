'''
Created on Oct 28, 2015
@author: hari
'''
class DisjointSetForest(object):
    '''
    A disjoint set forest has disjoint sets where each set is represented by an uptree.
    
    A disjoint set DJS has a number of elements from a fixed Universe U. DJS knows all the elements in it.
    The elements in DJS may themselves form subsets. i.e U = { a, b, c, d, r, f, g}. DJS can be
    { {a, g}, {b}, {d}, {c, r, f} }. Disjoint set allows 3 operations.
    
    1) make_set(x) returns a new set {x}
    2) find(x) return R such that x is in set R. for example {c, r, f} be identified by c. then find(r) = c
    3) union(s, t): merges the smaller set into the larger. {c} U {r, f} = {c, r, f}
    for more info please refer Datastructures and their algorithms by Harry Lewis and Larry Denenberg
    
    uptree nodes are used to represent the individual items of the set.
    1) Each item needs to be known just like that in the set.
    2) 
    '''
    
    