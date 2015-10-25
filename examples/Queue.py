'''
Created on Oct 25, 2015
@author: hari
'''
from datastructures.stackNqueues.Queue import Queue
if __name__ == '__main__':
    q = Queue()
    print 'Q size is %s' % str(q.size)
    #enqueue
    print 'Adding 1, 2, 3, 4, 5, 6 elements to queue'
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(6)
    #front
    print 'Q front is %s' % str(q.front)
    
    #iterate and dequeue each element
    print 'Iterating and removing items'
    for item in q:
        print item
